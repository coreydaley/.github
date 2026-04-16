# AI/ML Learning Roadmap

## Goal

A deliberate 12-month learning plan for software engineers looking to expand into AI/ML engineering — building the depth needed to design, build, and operate reliable, scalable AI systems in production.

> **Disclaimer:** This roadmap is provided for educational purposes only. Course availability, pricing, and platform features may change over time. Any cloud computing, software, or hardware costs incurred while following this curriculum are solely the responsibility of the individual. The author makes no guarantees about outcomes, job placement, or the accuracy of third-party pricing or availability information referenced herein.

---

## Mindset: Learning as an Investment

In a perfect world, everything in this roadmap would be free. Much of it actually is — the Anthropic Academy courses, Google Colab, Kaggle, Ollama, and most of the software tools cost nothing. But some of it — the course subscriptions, an AI coding assistant subscription, cloud compute, and eventually an API key or two — will cost money.

The right way to think about this is as an investment in your career, not an expense. A few hundred dollars in subscriptions, spread over a year, is a rounding error compared to the salary trajectory it can unlock. Engineers with real, demonstrable AI/ML skills are among the highest-compensated in the industry right now. The ROI on this roadmap, if you follow through, is exceptional.

That said, there's no reason to spend more than you have to:

**Check your employer's learning budget first.** Many companies offer annual learning and development stipends — often $1,000–$5,000 per year — specifically for courses, certifications, and conferences. This money frequently goes unused. Before spending a dollar of your own, ask your manager or HR team whether you have a learning budget and whether it covers online course subscriptions and professional certifications. In many cases this roadmap can be funded entirely by your employer.

**Time your purchases.** Coursera Plus and deeplearning.ai Pro both run significant promotional discounts at predictable times of year — Black Friday, New Year, and back-to-school. If you're not in a rush to start, waiting for a sale can save $100–150 on subscriptions alone.

**Use free tiers first.** Several courses on this roadmap are available for free audit (without certificates). Start there to validate the content is right for you before paying for access.

**Get an AI assistant — your personal tutor and coding partner.** This is as close to a requirement as anything on this list. As a coding partner, it accelerates course exercises, portfolio project work, and debugging. As a personal tutor, it's an always-available resource for deepening your understanding — confused by a concept in a paper, want to talk through an architecture decision, or need something explained three different ways until it clicks? A conversational AI meets you exactly where you are, with no office hours and no judgment. Pick one (or more!) and use it (or them!) throughout the entire program.

| Tool | Subscription | Best For |
|------|-------------|----------|
| [Claude Pro](https://claude.ai) + [Claude Code](https://claude.ai/code) | ~$20/mo + usage | Architecture discussions, long context, complex reasoning |
| [ChatGPT Plus](https://chat.openai.com) + [Codex](https://platform.openai.com) | ~$20/mo | Largest community, most Stack Overflow-style help available |
| [Google AI Pro](https://gemini.google/subscriptions/) + [Gemini CLI](https://github.com/google-gemini/gemini-cli) | ~$20/mo | Best for image generation (Imagen) and video generation (Veo) — recommended if you want flat-rate creative media without per-use API charges |

Depending on usage, you may eventually hit limits on the standard $20/month plans — Claude, ChatGPT, and Google AI all offer higher-tier plans (~$100/month) with significantly more capacity. Start low and upgrade/downgrade month-to-month as needed. If you regularly use image or video generation, Google AI Pro is worth adding alongside your primary AI subscription — it's significantly stronger than ChatGPT Plus for creative media and eliminates the need for pay-as-you-go API charges.

---

## Pre-Roadmap

**Anthropic Academy** ([anthropic.skilljar.com](https://anthropic.skilljar.com) — all free)
- [x] Claude 101
- [x] Claude Code 101
- [x] Claude Code in Action
- [x] Introduction to Claude Cowork
- [x] AI Fluency: Framework & Foundations
- [x] Building with the Claude API
- [x] Introduction to Model Context Protocol
- [x] Model Context Protocol: Advanced Topics
- [x] Introduction to Agent Skills
- [x] Introduction to Subagents
- [x] AI Capabilities and Limitations
- [x] AI Fluency for educators
- [x] AI Fluency for students
- [x] AI Fluency for nonprofits
- [x] Teaching AI Fluency
- [ ] Claude with Amazon Bedrock
- [ ] Claude with Google Cloud's Vertex AI

**Other Certificates**
- [x] Real-World AI for Everyone — Advancing Women in Tech ([Coursera](https://www.coursera.org/specializations/real-world-ai-for-everyone), sponsored by Anthropic)
- [x] IBM AI Developer Professional Certificate — [Coursera](https://www.coursera.org/professional-certificates/applied-artifical-intelligence-ibm-watson-ai)
- [ ] IBM Generative AI Engineering Professional Certificate — [Coursera](https://www.coursera.org/professional-certificates/ibm-generative-ai-engineering)

---

## Phase 1 — ML Foundations (Months 1–4)

**Month 1**
- [ ] [Deep Learning Specialization](https://www.deeplearning.ai/courses/deep-learning-specialization/) (part 1) — deeplearning.ai Pro
- [ ] Blog post: Implement backprop from scratch
- [ ] Portfolio project: Define architecture and start building — apply course concepts to a real project
- [ ] Update LinkedIn headline and about section to reflect AI engineering pivot

**Month 2**
- [ ] [Deep Learning Specialization](https://www.deeplearning.ai/courses/deep-learning-specialization/) (part 2) — deeplearning.ai Pro
- [ ] Blog post: CNNs + RNNs explained for engineers
- [ ] Portfolio project: Implement a neural network component from scratch

**Month 3**
- [ ] [NLP Specialization](https://www.deeplearning.ai/courses/natural-language-processing-specialization/) (part 1) — deeplearning.ai Pro
- [ ] Blog post: Attention mechanism deep dive
- [ ] Portfolio project: Add NLP or text processing capability to your project
- [ ] Blog post: Write about a design decision or architecture choice in your project

**Month 4**
- [ ] [NLP Specialization](https://www.deeplearning.ai/courses/natural-language-processing-specialization/) (part 2) + transformer architecture — deeplearning.ai Pro
- [ ] Blog post: Building a toy transformer
- [ ] Portfolio project: Integrate a transformer or LLM into your project in a meaningful way
- [ ] Publish portfolio project publicly if not already — clean README, docs, examples
- [ ] Find and enter first AI hackathon — check [lablab.ai](https://lablab.ai), [Hugging Face](https://huggingface.co/events), [Devpost](https://devpost.com), [MLH](https://mlh.io)

**Milestone:**
- Understand how LLMs actually work under the hood
- Portfolio project has a working LLM integration

---

## Phase 2 — LLMs + Generative AI (Months 5–7)

**Month 5**
- [ ] [Generative AI with LLMs](https://www.coursera.org/learn/generative-ai-with-llms) — deeplearning.ai Pro + AWS (Coursera)
- [ ] Blog post: RLHF + fine-tuning tradeoffs
- [ ] Portfolio project: Implement or experiment with fine-tuning on a small model
- [ ] Enter first AI hackathon
- [ ] Take Claude Certified Architect exam ($99 or free via partner org)
- [ ] Add Claude Certified Architect credential to LinkedIn and resume

**Month 6**
- [ ] [LLMOps](https://www.deeplearning.ai/short-courses/llmops/) — deeplearning.ai Pro
- [ ] Blog post: Deploying LLMs — what nobody tells you
- [ ] Portfolio project: Add a deployment pipeline or serving layer to your project
- [ ] Update LinkedIn skills to include ML/LLM engineering keywords

**Month 7**
- [ ] [AI Agents in LangGraph](https://www.deeplearning.ai/short-courses/ai-agents-in-langgraph/) — deeplearning.ai Pro
- [ ] Blog post: Comparing agent frameworks — what you learned from building your own
- [ ] Portfolio project: Implement a multi-agent workflow or agentic feature
- [ ] Update portfolio project README and docs to reflect current capabilities

**Milestone:**
- Build and deploy a production LLM-backed system end to end
- Portfolio project is publicly demonstrable

---

## Phase 3 — ML Engineering at Scale (Months 8–10)

**Month 8**
- [ ] [ML Engineering for Production / MLOps](https://www.coursera.org/specializations/machine-learning-engineering-for-production-mlops) — Coursera (Google)
- [ ] Blog post: CI/CD for ML — a Staff engineer's take
- [ ] Portfolio project: Add observability, monitoring, or a CI/CD pipeline to your project
- [ ] Reassess hardware upgrade based on cloud compute usage
- [ ] Start building referral network — engage with AI company engineers on GitHub and LinkedIn

**Month 9**
- [ ] [MLOps Specialization](https://www.coursera.org/specializations/machine-learning-engineering-for-production-mlops) (cont.) — Coursera (Google)
- [ ] Blog post: Model monitoring + drift detection patterns
- [ ] Portfolio project: Implement model monitoring or evaluation tooling
- [ ] Enter second AI hackathon if opportunity arises

**Month 10**
- [ ] Cloud ML specialty — Coursera ([AWS](https://www.coursera.org/specializations/aws-machine-learning) or [GCP](https://www.coursera.org/specializations/preparing-for-google-cloud-machine-learning-engineer-professional-certificate) track)
- [ ] Blog post: LLM infra cost optimization on AWS vs GCP
- [ ] Portfolio project: Deploy your project to cloud with proper ML infrastructure
- [ ] Do a full LinkedIn profile review and refresh
- [ ] Review target company job boards — note language and keywords used in target roles

**Milestone:**
- Architect and operate ML systems at scale — the Staff-level bar

---

## Phase 4 — Capstone (Months 11–12)

> **Choose your path:** If you are targeting a promotion or expanded role at your current company, follow **Phase 4a**. If you are targeting a new role at an AI company, follow **Phase 4b**. You can also combine elements of both.

---

## Phase 4a — Internal Growth + Promotion Prep (Months 11–12)

**Month 11**
- [ ] Identify an AI/ML initiative at your current company you can lead or contribute to
- [ ] Present your AI/ML learnings internally — lunch and learn, tech talk, or internal blog post
- [ ] Blog post: Your take on a research paper or concept relevant to your company's domain
- [ ] Portfolio project: Add a feature or capability directly relevant to your current work
- [ ] Polish portfolio project — docs, README, demo video or screenshots
- [ ] Polish personal blog — ensure all blog posts are published and well-presented
- [ ] Document your AI/ML contributions and impact for performance review

**Month 12**
- [ ] Lead or ship an AI-related project or improvement at work
- [ ] Blog post: Year-in-review + what you built
- [ ] Final LinkedIn polish — reflect your new AI/ML engineering depth
- [ ] Prepare promotion case — tie AI/ML skills to business impact
- [ ] Schedule promotion or role expansion conversation with your manager

**Milestone:**
- Demonstrable AI/ML impact at your current company
- Clear promotion case built on real delivered work

---

## Phase 4b — Target Company Deep Dive + Application Prep (Months 11–12)

> **Note:** This phase is specifically for those targeting a new role at an AI company. If that is not your goal, follow Phase 4a above instead.

**Month 11**
- [ ] Identify 2-3 target AI companies and research their published work deeply
- [ ] Read key research papers from your target companies (see reading list below for Anthropic examples)
- [ ] Bookmark and regularly read your target companies' engineering and research blogs
- [ ] Blog post: Your take on a research paper or technical concept from your target company
- [ ] Portfolio project: Add a safety, evaluation, or alignment-relevant feature
- [ ] Polish portfolio project — docs, README, demo video or screenshots
- [ ] Polish personal blog — ensure all blog posts are published and well-presented
- [ ] Investigate fellowship or residency programs at target companies

**Month 12**
- [ ] Portfolio project: Final polish and any remaining features
- [ ] Blog post: Year-in-review + what you built
- [ ] Final LinkedIn polish — ensure your profile speaks your target companies' language
- [ ] Identify specific remote-friendly roles at target companies
- [ ] Reach out to referrals at target companies
- [ ] Begin applying

**Milestone:**
- Portfolio, blog, and projects speak the language of top AI companies

---

## Research Reading List (Month 11)

> **Note:** This reading list is primarily relevant for those following **Phase 4b**, but the approach of deeply studying your target company's published research applies to any path. The list below uses Anthropic as an example — substitute or supplement with papers from your own target company or employer.

### Anthropic — Example Reading List

#### Core — Read First
- [ ] **[Constitutional AI: Harmlessness from AI Feedback](https://arxiv.org/abs/2212.08073)** (Bai et al., 2022)
  - The foundational paper behind how Claude is trained. Introduces RLAIF.
- [ ] **[Measuring Progress on Scalable Oversight for Large Language Models](https://www.anthropic.com/research/measuring-progress-on-scalable-oversight-for-large-language-models)**
  - Core safety problem: supervising AI systems that outperform us on the task.
- [ ] **[Collective Constitutional AI](https://www.anthropic.com/research/collective-constitutional-ai-aligning-a-language-model-with-public-input)**
  - Extends CAI with democratic/public input into the constitution.

#### Interpretability — Relevant to Infra/Tooling Roles
- [ ] **[Towards Monosemanticity: Decomposing Language Models With Dictionary Learning](https://www.anthropic.com/news/decomposing-language-models-into-understandable-components)**
  - Foundational mechanistic interpretability paper from Anthropic.
- [ ] **[The Engineering Challenges of Scaling Interpretability](https://www.anthropic.com/research/engineering-challenges-interpretability)**
  - Directly relevant: Anthropic explicitly states the next obstacle is engineering, not science.

#### Ongoing Reading
- [ ] **[Anthropic Alignment Science Blog](https://alignment.anthropic.com)**
  - Active research: scalable oversight, sleeper agents, alignment faking, sabotage evals.
- [ ] **[Anthropic Fellows Program](https://alignment.anthropic.com/2025/anthropic-fellows-program-2026/)**
  - No PhD required, 40%+ of fellows join Anthropic full-time.

---

## Portfolio Strategy

### Project
Build or choose one meaningful open source project and evolve it throughout the 12 months. The best portfolio projects are ones you actually use or care about — not toy examples. As you progress through the curriculum, apply what you're learning directly to the project. Frame architecture decisions around LLM inference, context management, multi-agent orchestration, and production reliability. See each phase for specific project milestones.

### Blog
One post per month **minimum**, timed to learning milestones. 
_See each phase for specific post topics._

**Goals**
- Demonstrate genuine depth, not just course completion
- Use vocabulary aligned with top AI companies (constitutional AI, RLHF, scalable oversight, evals)
- Document real implementations, not just summaries

### Hackathons
- Target first hackathon around Month 4–5
- Platforms
	- [lablab.ai](https://lablab.ai)
	- [Hugging Face Events](https://huggingface.co/events)
	- [Devpost](https://devpost.com)
	- [MLH](https://mlh.io)

---

## Claude Certified Architect — Foundations

**Official Anthropic certification launched March 12, 2026.**

- Exam registration: [anthropic.skilljar.com](https://anthropic.skilljar.com/claude-certified-architect-foundations-access-request)
- Free prep courses (13 total): [anthropic.skilljar.com](https://anthropic.skilljar.com)
- Cost: $99 (free for first 5,000 employees of Claude Partner Network member orgs)

### Exam Domains
| Domain | Weight |
|--------|--------|
| Agentic Architecture & Orchestration | 27% |
| Claude Code Configuration & Workflows | 20% |
| Prompt Engineering & Structured Output | 20% |
| Tool Design & MCP Integration | 18% |
| Context Management & Reliability | 15% |

Passing score: **720 / 1000**

### Action Items
- [ ] Check if current employer joins the [Claude Partner Network](https://www.anthropic.com/news/claude-partner-network) (free access for employees)
- [x] Complete the 13 free prep courses at [anthropic.skilljar.com](https://anthropic.skilljar.com)
- [x] Key prep courses: Claude 101, Building Applications with Claude API, Introduction to MCP, Claude Code developer training
- [ ] Take exam — free via partner org access, or $99 out of pocket
- [ ] Add credential to LinkedIn and resume

### Why This Matters
This is an official Anthropic credential that validates production-level Claude implementation skills — directly relevant to the target role. The exam is architecture-focused (how you design and deploy Claude-powered systems), which plays to Staff SWE strengths. As the first major AI lab to offer formal certifications, this credential will carry increasing weight with AI company recruiters.

---

## Subscriptions

- **[deeplearning.ai Pro](https://www.deeplearning.ai/courses/)** — primary for ML fundamentals and LLMs
- **[Coursera Plus](https://www.coursera.org/courseraplus)** — MLOps and production ML engineering

**Cost tips:**
- Both are annual subscriptions — check for promotional pricing before committing
- Coursera Plus frequently offers significant discounts ($100–150 off) around Black Friday, New Year, and back-to-school periods
- deeplearning.ai Pro often runs holiday and new year deals — worth waiting for if you're not in a rush to start
- Coursera Plus gives access to the full catalog including IBM, Google, and DeepLearning.AI specializations — check if courses you need are included before paying separately
- Some employers offer learning stipends that cover these subscriptions — worth asking before paying out of pocket

---

## Hardware Recommendations

Hardware is split into two tiers: **Get Started** (sufficient for Phases 1–2) and **Go Deeper** (recommended for Phases 3–4 and serious local inference/fine-tuning).

**Cost tips:**
- The Get Started tier is sufficient for all coursework — don't over-invest in hardware early
- Black Friday and back-to-school are the best times to buy GPUs and workstation components
- For Windows/Linux builds, refurbished or open-box components from reputable sellers can save 20–40%
- Apple Silicon Macs hold their value well — consider refurbished models from Apple's official refurb store for meaningful savings
- Cloud compute (Colab, spot instances) is almost always more cost-effective than buying high-end local hardware for occasional training runs — reassess the Go Deeper tier at Month 8–9 based on actual usage

### macOS

| | CPU | RAM | Storage | GPU |
|---|---|---|---|---|
| Get Started | Apple M2 or later | 16GB unified | 512GB SSD | Integrated (MPS) |
| Go Deeper | Apple M4 Max or later | 64GB+ unified | 1TB+ SSD | Integrated (MPS, 40-core GPU+) |

**Note:** MPS (Metal Performance Shaders) gives Apple Silicon meaningful GPU acceleration for PyTorch. 64GB+ unified memory allows running 30B+ parameter models locally.

### Windows

| | CPU | RAM | Storage | GPU |
|---|---|---|---|---|
| Get Started | Intel Core i7 / AMD Ryzen 7 (8+ cores) | 16GB DDR4 | 512GB SSD | NVIDIA RTX 3060 (12GB VRAM) |
| Go Deeper | Intel Core i9 / AMD Ryzen 9 (16+ cores) | 64GB DDR5 | 2TB NVMe SSD | NVIDIA RTX 4080/4090 (16–24GB VRAM) |

**Note:** NVIDIA CUDA is the most widely supported GPU acceleration for ML frameworks. VRAM is the critical constraint — 12GB minimum, 24GB for comfortable local fine-tuning.

### Linux

| | CPU | RAM | Storage | GPU |
|---|---|---|---|---|
| Get Started | Intel Core i7 / AMD Ryzen 7 (8+ cores) | 16GB DDR4 | 512GB SSD | NVIDIA RTX 3060 (12GB VRAM) |
| Go Deeper | AMD Threadripper / Intel Core i9 (16+ cores) | 64GB+ DDR5 | 2TB+ NVMe SSD | NVIDIA RTX 4090 or A-series (24GB+ VRAM) |

**Note:** Linux is the most flexible platform for ML work — native CUDA support, best tooling compatibility, and preferred in production environments. AMD GPUs are increasingly supported via ROCm but NVIDIA remains the safer choice.

---

## Cloud Resources

Cloud is essential for this roadmap — use it for training runs, MLOps deployments, and anything that exceeds local hardware limits.

### Free Tiers and Learning Credits (Start Here)
- **[Google Colab](https://colab.research.google.com)** — free tier includes GPU access (T4), sufficient for most course exercises. Colab Pro adds more runtime and better GPUs.
- **[AWS Free Tier](https://aws.amazon.com/free/)** — 12 months of limited EC2, S3, and SageMaker Studio Lab (free, no credit card for Studio Lab)
- **[GCP Free Tier](https://cloud.google.com/free)** — $300 in credits for new accounts, plus always-free tier for small compute
- **[Azure Free Tier](https://azure.microsoft.com/free)** — $200 in credits for new accounts, plus free tier for select services
- **[Kaggle Notebooks](https://www.kaggle.com/code)** — free GPU/TPU access (30 hrs/week), no setup required

### AWS — Key Services for This Roadmap
| Service | Use Case |
|---------|----------|
| EC2 (p3/p4/g4/g5 instances) | GPU training and inference |
| SageMaker | Managed ML training, deployment, and pipelines |
| SageMaker Studio | Jupyter-based ML IDE in the cloud |
| S3 | Dataset and model artifact storage |
| ECR + ECS/EKS | Containerized model serving |
| Lambda | Serverless LLM inference endpoints |
| Bedrock | Managed access to foundation models including Claude |

> **Cost tip:** Use spot instances for training (up to 90% cheaper). Set billing alerts. Shut down instances when not in use.

### GCP — Key Services for This Roadmap
| Service | Use Case |
|---------|----------|
| Vertex AI | Managed ML platform — training, pipelines, and model registry |
| Compute Engine (A2/G2 instances) | GPU training and inference |
| Cloud Storage | Dataset and artifact storage |
| Cloud Run | Serverless containerized model serving |
| GKE | Kubernetes-based model serving at scale |
| Vertex AI Model Garden | Access to foundation models including Claude via Anthropic |

> **Cost tip:** Committed use discounts and preemptible VMs significantly reduce training costs.

### Azure — Key Services for This Roadmap
| Service | Use Case |
|---------|----------|
| Azure Machine Learning | Managed ML platform — training, pipelines, and deployment |
| NC/ND-series VMs | GPU training and inference |
| Azure Blob Storage | Dataset and artifact storage |
| Azure Container Apps | Serverless containerized model serving |
| AKS | Kubernetes-based model serving at scale |
| Azure OpenAI Service | Managed access to foundation models |

> **Cost tip:** Azure Hybrid Benefit and reserved instances reduce long-term costs significantly.

### Cost-Saving Tips (All Platforms)
- Always set **billing alerts** before experimenting — runaway GPU instances are expensive
- Use **spot/preemptible/interruptible instances** for training jobs — save 60–90%
- Store data in cloud storage, not on compute instances
- Use **free notebook environments** (Colab, Kaggle) for course exercises — save paid cloud for MLOps and deployment work
- Tear down resources immediately after use — idle GPU instances still incur charges
- For LLM inference experiments, use **API endpoints** (Anthropic, OpenAI) rather than self-hosting — far cheaper at low volume

---

## Software and Tools

### Core Languages and Runtimes
| Tool | Purpose | When Needed | Install |
|------|---------|-------------|---------|
| Python 3.11+ | Primary ML language | Phase 1 — start here | [python.org](https://python.org) or via package manager |
| Node.js LTS | JS tooling, some LLM SDKs | As needed | [nodejs.org](https://nodejs.org) or [nvm](https://github.com/nvm-sh/nvm) |
| Git | Version control | Day 1 | [git-scm.com](https://git-scm.com) |

### ML Frameworks and Libraries
| Package | Purpose | When Needed | Install |
|---------|---------|-------------|---------|
| PyTorch | Primary deep learning framework | Phase 1 | `pip install torch torchvision torchaudio` |
| NumPy | Numerical computing | Phase 1 | `pip install numpy` |
| Pandas | Data manipulation | Phase 1 | `pip install pandas` |
| Matplotlib | Data visualization | Phase 1 | `pip install matplotlib` |
| scikit-learn | Classical ML algorithms | Phase 1 | `pip install scikit-learn` |
| SciPy | Scientific computing | Phase 1 | `pip install scipy` |
| Transformers | Hugging Face model library | Phase 2 | `pip install transformers` |
| Datasets | Hugging Face datasets | Phase 2 | `pip install datasets` |
| LangChain | LLM application framework | Phase 2 | `pip install langchain` |
| LangGraph | Agent workflow framework | Phase 2 | `pip install langgraph` |
| Hugging Face Hub | Model and dataset hub CLI | Phase 2 | `pip install huggingface_hub` |
| Accelerate | Distributed training | Phase 3 | `pip install accelerate` |
| PEFT | Parameter-efficient fine-tuning | Phase 3 | `pip install peft` |
| MLflow | Experiment tracking | Phase 3 | `pip install mlflow` |
| Weights & Biases | Experiment tracking (alternative) | Phase 3 | `pip install wandb` |

> **Tip:** Use a virtual environment (`python -m venv .venv`) or conda to keep project dependencies isolated.

### LLM API Access

Your portfolio project will need access to LLM models. There are several options depending on your budget and hardware — you don't need to spend money to get started.

#### Paid APIs (best quality, pay per token)
| Provider | API Console | Notes |
|----------|-------------|-------|
| Anthropic (Claude) | [console.anthropic.com](https://console.anthropic.com) | Best for instruction following and long context |
| OpenAI (GPT) | [platform.openai.com](https://platform.openai.com) | Largest ecosystem and community |
| Google (Gemini) | [aistudio.google.com](https://aistudio.google.com) | Free tier available, cheap at scale |
| Mistral | [console.mistral.ai](https://console.mistral.ai) | Cheapest major provider, EU-based |

> All of the above have free tiers or trial credits to get started — you don't need to spend money immediately.

#### Free / Low-Cost Alternatives
| Option | How | Notes |
|--------|-----|-------|
| [Ollama](https://ollama.com) | Run models locally | Free, no API key needed, works on Mac/Windows/Linux. Limited by local hardware. |
| [LM Studio](https://lmstudio.ai) | Run models locally (GUI) | Same as Ollama but with a user interface. Good for beginners. |
| [LocalAI](https://localai.io) | Run models locally (OpenAI-compatible API) | Drop-in OpenAI API replacement, no GPU required |
| [Google Gemini Free Tier](https://aistudio.google.com) | Cloud API | Generous free tier via Google AI Studio — good for experimentation |
| [Groq](https://groq.com) | Cloud API | Free tier, extremely fast inference on open-source models (Llama, Mixtral) |
| [Together AI](https://together.ai) | Cloud API | Free trial credits, cheap pay-as-you-go for open-source models |
| [OpenRouter](https://openrouter.ai) | Cloud API | Single API for 100+ models, free tier available, pay only for what you use |

**Recommendation for getting started:** Use Ollama locally for free experimentation during Phases 1–2. Add a paid API key when you're ready to build something in Phase 2–3.

### LLM Tooling

| Tool | Purpose | When Needed | Install |
|------|---------|-------------|---------|
| Ollama | Run LLMs locally | Phase 1 | [ollama.com](https://ollama.com) |
| Anthropic SDK | Claude API client | Phase 2 | `pip install anthropic` |
| OpenAI SDK | OpenAI API client | Phase 2 | `pip install openai` |
| Hugging Face CLI | Download and manage models | Phase 2 | `pip install huggingface_hub` |
| LM Studio | GUI for local model inference | Optional | [lmstudio.ai](https://lmstudio.ai) |
| vLLM | High-performance LLM serving | Phase 3 | `pip install vllm` (Linux/GPU only) |

### Development Tools
| Tool | Purpose | When Needed | Install |
|------|---------|-------------|---------|
| JupyterLab | Interactive notebooks for coursework | Phase 1 | `pip install jupyterlab` |
| VS Code | Code editor | Day 1 | [code.visualstudio.com](https://code.visualstudio.com) |
| Docker | Containerization for ML deployments | Phase 3 | [docker.com](https://docker.com) |
| Postman | API testing | Phase 2 | [postman.com](https://postman.com) |

### Cloud CLIs
| Tool | Purpose | When Needed | Install |
|------|---------|-------------|---------|
| AWS CLI | AWS resource management | Phase 3 | [aws.amazon.com/cli](https://aws.amazon.com/cli) |
| gcloud CLI | GCP resource management | Phase 3 | [cloud.google.com/sdk](https://cloud.google.com/sdk) |
| Azure CLI | Azure resource management | Phase 3 | [aka.ms/installazurecli](https://aka.ms/installazurecli) |
| kubectl | Kubernetes cluster management | Phase 3 | [kubernetes.io/docs/tasks/tools](https://kubernetes.io/docs/tasks/tools) |
