from __future__ import annotations
from dataclasses import asdict, dataclass
from itertools import combinations
import hashlib, json
from typing import Dict, List, Tuple

NODES = tuple("אבגדהוזחטיכלמנסעפצקרשת")
PARTITIONS = {
    "mothers": tuple("אמש"),
    "doubles": tuple("בגדהכפרת"),
    "simples": tuple("הוזחטיכלנסעצק"),
}

@dataclass(frozen=True)
class Gate:
    id: int
    a: int
    b: int
    @property
    def pair(self) -> Tuple[str, str]: return NODES[self.a], NODES[self.b]
    @property
    def forward(self) -> str: return "".join(self.pair)
    @property
    def backward(self) -> str: return "".join(reversed(self.pair))

@dataclass(frozen=True)
class RunMetrics:
    nodes: int
    gates: int
    edges: int
    propagation_steps: int
    state_sha256: str

class SYNeuroKernel:
    """Small deterministic graph/neural sandbox.
    The canonical computational space is the relation graph, not the glyphs.
    """
    def __init__(self) -> None:
        self.nodes = NODES
        self.gates: List[Gate] = [Gate(i,a,b) for i,(a,b) in enumerate(combinations(range(22),2))]
        self.adjacency = self._build_shared_node_graph()

    def _build_shared_node_graph(self) -> List[List[int]]:
        adjacency=[[] for _ in self.gates]
        for i,left in enumerate(self.gates):
            for j in range(i+1,len(self.gates)):
                right=self.gates[j]
                if {left.a,left.b} & {right.a,right.b}:
                    adjacency[i].append(j); adjacency[j].append(i)
        return adjacency

    def gate_id(self,a:str,b:str)->int:
        if a==b: raise ValueError("Self-pairs are outside the canonical 231 gate space")
        ia,ib=self.nodes.index(a),self.nodes.index(b); x,y=sorted((ia,ib))
        return next(g.id for g in self.gates if (g.a,g.b)==(x,y))

    def partitions(self)->Dict[str,Tuple[str,...]]: return PARTITIONS

    def directed_view(self,gate_id:int)->Dict[str,str]:
        g=self.gates[gate_id]; return {"forward":g.forward,"backward":g.backward}

    def propagate(self,steps:int=3)->List[float]:
        if steps<0: raise ValueError("steps must be >= 0")
        state=[1.0]*len(self.gates)
        for _ in range(steps):
            nxt=[]
            for i,neighbors in enumerate(self.adjacency):
                mean=sum(state[j] for j in neighbors)/len(neighbors) if neighbors else state[i]
                nxt.append((state[i]+mean)/2.0)
            state=nxt
        return state

    def metrics(self,steps:int=3)->RunMetrics:
        state=self.propagate(steps)
        payload=json.dumps(state,separators=(",",":"),ensure_ascii=False).encode()
        digest=hashlib.sha256(payload).hexdigest()
        edges=sum(map(len,self.adjacency))//2
        return RunMetrics(22,231,edges,steps,digest)

    def snapshot(self,steps:int=3)->Dict:
        return {"nodes":list(self.nodes),"gate_count":231,"partitions":{k:list(v) for k,v in PARTITIONS.items()},"metrics":asdict(self.metrics(steps)),"status":"COMPUTATIONAL_HYPOTHESIS"}
