# Global External Architecture Corpus — v0.1

**Status:** SPECIFIED / SEEDED  
**Purpose:** Connect real public GitHub repositories and research sources to the WANGA Institute architecture by institutional/technical function.

## Boundary

This registry records **publicly discoverable repositories as external architecture sources**. A repository connection does not imply ownership, endorsement, membership, control, government authority, regulatory authority, diplomatic representation, or contractual relationship.

Each source is routed by function:

`External Source → Architecture Family → Institute Office → Vitruvius Node → Vitruvius Global Root → WANGA Main Bridge`

A source may map to multiple offices. No ancestry or institutional relationship is inferred without evidence.

## Core routing model

| Layer | Meaning |
|---|---|
| Source | Public GitHub repository / public technical artifact |
| Institution | Organization named by repository owner or source metadata |
| Domain | Government / finance / insurance / AI / academia / infrastructure / etc. |
| Office | One of the Institute functional offices |
| Family | Architecture family assigned by the corpus taxonomy |
| Vitruvius | Architecture/dependency/lineage mapping layer |
| Evidence | Provenance, hashes, timestamps, replay/verification where available |
| Status | DISCOVERED / CLASSIFIED / MAPPED / VERIFIED |

## Government and public-sector seed corpus

### Foreign Affairs / International Cooperation

- `Udenrigsministeriet/iati-api` — branch `v2` — international-development data/API architecture.
- `Udenrigsministeriet/IATI-to-SQL-Database` — branch `master` — structured international-aid data infrastructure.
- `alphagov/whitehall` — branch `main` — UK government publishing/service architecture.

### Finance / Treasury / Public Data

- `GSA/data` — `master`
- `GSA/data.gov` — `main`
- `GSA/api.data.gov` — `main`
- `GSA/catalog.data.gov` — `main`
- `GSA/data-strategy` — `main`
- `GSA/datagov-harvester` — `main`
- `GSA/us-data-federation` — `main`
- `worldbank/debt-data` — `master1`
- `worldbank/WDI-Production` — `master`

### Justice

- `ministryofjustice/justice` — `main`
- `ministryofjustice/justice-gov-uk` — `main`
- `ministryofjustice/cloud-platform-cli` — `main`
- `ministryofjustice/cloud-platform-user-guide` — `main`
- `ministryofjustice/digital-prison-reporting-jobs` — `main`
- `ministryofjustice/moj-design-system` — `main`
- `ministryofjustice/technical-guidance` — `main`

### Digital Government / Public Infrastructure

- `alphagov/govuk-frontend` — `main`
- `alphagov/govuk-design-system` — `main`
- `alphagov/govuk-infrastructure` — `main`
- `alphagov/notifications-api` — `main`
- `alphagov/notifications-admin` — `main`
- `alphagov/publisher` — `main`
- `GSA/code-gov-web` — `master`
- `GSA/federal-website-index` — `main`
- `GSA/federal-open-source-repos` — `gh-pages`
- `GSA/federal-apis` — `master`
- `GSA/idmanagement.gov` — `staging`
- `GovTechSG/sgds` — `v3`
- `GovTechSG/developer.gov.sg-nm` — `master`
- `datagovhr/data.gov.hr` — `master`

## International development / global economy

- `worldbank/Python-for-Data-Science` — `master`
- `worldbank/dime-data-handbook` — `main`
- `worldbank/data360-mcp` — `dev`
- `worldbank/llm4data` — `main`
- `worldbank/ai4data` — `main`
- `worldbank/ai4coding` — `main`
- `worldbank/GOST_AIS` — `master`
- `worldbank/impactAI` — `main`
- `worldbank/AI4StatsDemo` — `main`
- `worldbank/MANAGE-WB` — `main`

## Central-bank / monetary-system discovery seed

- `ecb/data-loader` — `master`

This is a **discovery seed**, not a claim that the registry currently exhausts all central-bank repositories.

## AI companies / AI infrastructure

### OpenAI

- `openai/openai-agents-python` — `main`
- `openai/mle-bench` — `main`
- `openai/ai-and-efficiency` — `master`
- `openai/universe` — `master`
- `openai/openai-reflect` — `main`

### Hugging Face

- `huggingface/transformers` — `main`
- `huggingface/sentence-transformers` — `main`
- `huggingface/transformers.js` — `main`
- `huggingface/optimum` — `main`
- `huggingface/trl` — `main`
- `huggingface/alignment-handbook` — `main`
- `huggingface/swift-transformers` — `main`

### Google DeepMind

- `google-deepmind/lab` — `master`
- `google-deepmind/ai-foundations` — `main`
- `google-deepmind/ai-safety-gridworlds` — `master`
- `google-deepmind/disco_rl` — `main`
- `google-deepmind/agent_debugger` — `main`

### NVIDIA

- `NVIDIA/GenerativeAIExamples` — `main`
- `NVIDIA/garak` — `main`
- `NVIDIA/OpenShell` — `main`
- `NVIDIA/Trustworthy-AI` — `main`
- `NVIDIA/NeMo-Agent-Toolkit` — `develop`
- `NVIDIA/aistore` — `main`

### Microsoft

- `microsoft/ML-For-Beginners` — `main`
- `microsoft/SynapseML` — `master`
- `microsoft/onnxruntime-inference-examples` — `main`
- `microsoft/InnerEye-DeepLearning` — `main`
- `microsoft/nni` — `master`
- `microsoft/Purview-Machine-Learning-Lineage-Solution-Accelerator` — `main`

### Meta / Facebook Research

- `facebookresearch/CodeGen` — `main`
- `facebookresearch/CrypTen` — `main`
- `facebookresearch/fairchem` — `main`
- `facebookresearch/certified-removal` — `main`
- `facebookresearch/recipes` — `main`

### Core AI frameworks

- `pytorch/pytorch` — `main`
- `pytorch/serve` — `master`
- `pytorch/torchtitan` — `main`
- `pytorch/executorch` — `main`
- `pytorch/elastic` — `master`
- `tensorflow/tensorflow` — `master`
- `tensorflow/models` — `master`
- `tensorflow/tensorboard` — `master`
- `tensorflow/probability` — `main`

## Academic / research corpus

Academic and research sources are a **cross-cutting corpus**, routed into Architecture, Models, Evidence, Standards, Infrastructure, Organizations and Policy rather than being treated as a separate governmental office.

### Stanford NLP

- `stanfordnlp/CoreNLP` — `main`
- `stanfordnlp/stanza` — `main`
- `stanfordnlp/dspy` — `main`
- `stanfordnlp/pyreft` — `main`
- `stanfordnlp/pyvene` — `main`
- `stanfordnlp/GloVe` — `master`
- `stanfordnlp/axbench` — `main`

### Allen Institute for AI

- `allenai/ai2thor` — `main`
- `allenai/ai2-scholarqa-lib` — `main`
- `allenai/ai2thor-rearrangement` — `main`
- `allenai/Holodeck` — `main`
- `allenai/procthor` — `main`
- `allenai/tango` — `main`
- `allenai/allenact` — `main`
- `allenai/prior` — `main`
- `allenai/hybrid-preferences` — `main`

### Oxford Machine Learning

- `OxfordML/GPz` — `master`
- `OxfordML/bayesquad` — `master`
- `OxfordML/GaussianProcess.jl` — `master`
- `OxfordML/BayesianOptimisation.jl` — `master`
- `OxfordML/Fair_Regression` — `master`

### University / engineering research

- `UCL/mlbd-lectures` — `main`
- `UCL/InnerEye-DeepLearning` — `main`
- `CambridgeEngineering/PartIA-Computing-Michaelmas` — `main`
- `CambridgeEngineering/PartI-Computing` — `master`
- `CambridgeEngineering/PartIA-Flood-Warning-System` — `main`
- `ethz-asl/kalibr` — `master`
- `ethz-asl/maplab` — `master`
- `ethz-asl/voxblox` — `master`
- `ethz-asl/rotors_simulator` — `master`
- `ethz-asl/okvis` — `master`
- `ethz-asl/rovio` — `master`

### Research infrastructure

- `CERN/awesome-cern` — `main`
- `apache/spark` — `master`
- `apache/datafusion` — `main`
- `apache/flink-cdc` — `master`
- `apache/avro` — `main`
- `apache/hudi` — `master`

## Functional routing into the 14 Institute Offices

| Institute Office | Primary external sources |
|---|---|
| Evidence & Provenance | public-data platforms, AI lineage, metadata, reproducibility |
| Verification & Audit | testing, trustworthy-AI, certified-removal, audit tooling |
| AI Drift Forensics | model evaluation, benchmarks, lineage, monitoring |
| Architecture Intelligence / Vitruvius | all software architecture repositories |
| Model Fabric & Models | OpenAI, Hugging Face, DeepMind, PyTorch, TensorFlow |
| Digital Agents | OpenAI Agents, NVIDIA NeMo-Agent-Toolkit, agent research |
| Compute & Infrastructure | cloud/platform repos, PyTorch, TensorFlow, Apache |
| Industrial Execution | robotics, simulation, engineering, industrial software |
| Finance, Banking & Insurance | World Bank, central-bank sources, finance/insurance repositories |
| Organizations & Operations | enterprise/public-service platforms |
| Policy, Authorization & Risk | government policy systems, AI safety, risk tooling |
| Integration & Deployment | APIs, platform infrastructure, GovTech, adapters |
| Standards & Interoperability | GOV.UK design systems, IATI, Apache data formats, APIs |
| Global Branch Managers | aggregate routing/status across every corpus branch |

## Academic overlay

`Academic Institution / Research Organization → Research Artifact → Architecture Family → Institute Office → Vitruvius`

The academic layer is deliberately **cross-cutting**. It is not claimed that any university or research organization participates in the Institute unless a real relationship is established.

## Scale target

The architecture supports:

- multiple repositories per institution;
- thousands of repositories per Office;
- many-to-many repository-to-Office mapping;
- deduplication by canonical `owner/repository`;
- default-branch capture;
- architecture-tree extraction;
- dependency and lineage mapping;
- periodic refresh;
- evidence-state tracking.

**Target ≠ achieved count.** Actual corpus size must be calculated from live discovery results.

## Expansion protocol

1. Discover public repositories using institution, ministry, agency, domain and architecture queries.
2. Record `owner/repository`, default branch, source query and discovery timestamp.
3. Deduplicate.
4. Classify into architecture family and subfamily.
5. Route to one or more Institute Offices.
6. Pass the repository through Vitruvius architecture extraction.
7. Preserve provenance and evidence state.
8. Mark unresolved institutional identity or ancestry as `UNKNOWN`.
9. Never convert a repository match into a claim of institutional relationship.
10. Refresh periodically because public repositories and branches change.

## Current measured seed

The registry contains a substantial multi-domain seed from connected GitHub discovery, including public-sector, World Bank, AI-company, AI-framework and academic/research repositories.

This file is intentionally **not labeled exhaustive**. Exhaustiveness requires a reproducible global discovery run and evidence for the resulting corpus.
