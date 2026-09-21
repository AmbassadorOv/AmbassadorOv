from sy_neurokernel import SYNeuroKernel

def test_22_nodes_and_231_gates():
    k=SYNeuroKernel(); assert len(k.nodes)==22; assert len(k.gates)==231; assert len({g.pair for g in k.gates})==231

def test_direction_is_a_view_not_a_second_gate():
    k=SYNeuroKernel(); gid=k.gate_id("א","ב")
    assert k.directed_view(gid)=={"forward":"אב","backward":"בא"}; assert k.gate_id("ב","א")==gid

def test_partition_sizes():
    p=SYNeuroKernel().partitions(); assert len(p["mothers"])==3; assert len(p["doubles"])==7; assert len(p["simples"])==12

def test_metrics_reproducible():
    k=SYNeuroKernel(); assert k.metrics(3).state_sha256==k.metrics(3).state_sha256
