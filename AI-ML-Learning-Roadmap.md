# AI Practice Roadmap

> **This roadmap changed course in November 2026.** It started as a 12-month
> curriculum for learning to *train* models: backprop from scratch, CNNs and
> RNNs, fine-tuning, MLOps. For an experienced engineer who builds *with*
> models, that was the wrong map. This version is about the usage side:
> building with models and around them, and learning by shipping. Why it
> changed: [I planned to learn AI by training models. I'm building with them instead.](https://coreydaley.dev/posts/2026/11/learning-ai-by-building-not-training/)
> The original curriculum is in this file's git history.

## Goal

Get good at the engineering around AI models: the harnesses, tools, evals,
orchestration and security that make a model useful and safe in real work.
Not training models, and not a certificate collection. Every step ends in
something public: code, a write-up, or both.

> **Disclaimer:** This roadmap is provided for educational purposes only.
> Course availability, pricing, and platform features may change over time.
> Any software, API, or hardware costs incurred while following it are solely
> the responsibility of the individual. The author makes no guarantees about
> outcomes or the accuracy of third-party pricing or availability information
> referenced here.

---

## Why the usage side

- **Most AI engineering work is around the model, not inside it.** Deciding
  what context a model gets, which tools it can call, how its output is
  checked, what it may touch, and what it costs. That's platform and
  systems engineering, and experienced engineers already have most of it.
- **You don't need ML theory to start.** It helps to understand what a model
  is doing (tokens, context windows, why it makes things up), and the free
  courses below cover that. Backprop from scratch doesn't change how you
  build an agent harness.
- **Shipping teaches faster than coursework.** A real project hits real
  problems (a prompt injection in a fetched page, an eval that passes for the
  wrong reason, a context window that fills up) that no course exercise
  does.

## How to use this roadmap

Work in a loop, not a 12-month schedule:

1. **Pick one skill** from the list below, ideally one your current project
   needs.
2. **Build it into something you actually use.** Not a toy example.
3. **Write it up** (what you tried, what broke, what you'd do again) and
   publish the code if you can.
4. **Repeat** with the next skill.

Keep one project going for a long time rather than starting a new one for
each skill. A project that accumulates evals, security and orchestration
over months shows far more than six demos.

---

## Skills to deepen

Each skill has a practice suggestion: the kind of thing to build so the
learning leaves something behind.

### 1. Evals and model testing

Knowing whether a change to a prompt, tool or model made things better or
worse. Without evals, every change is a guess.

- **Practice:** write a small eval suite for something you've built: a set
  of real inputs, what a good answer looks like, and a script that scores
  them. Run it before and after every prompt or model change.
- **Read:** [Your AI product needs evals](https://hamel.dev/blog/posts/evals/)
  (Hamel Husain); Anthropic's [Define success criteria and build evaluations](https://docs.claude.com/en/docs/test-and-evaluate/develop-tests).

### 2. Agent security

Prompt injection, tool permissions, sandboxing, and what an agent can reach.
Any agent that reads untrusted content (web pages, email, issues, files) can
be steered by it.

- **Practice:** threat-model your own agent. List what it reads, what it can
  do, and what someone who controls one input could make it do. Then
  constrain it: least-privilege tools, sandboxed execution, a human approval
  step for anything irreversible.
- **Read:** [OWASP Top 10 for LLM Applications](https://genai.owasp.org/llm-top-10/);
  Simon Willison on [prompt injection](https://simonwillison.net/tags/prompt-injection/);
  the [MCP security best practices](https://modelcontextprotocol.io/docs/tutorials/security/security_best_practices).

### 3. Context engineering

Deciding what goes into the model's context, when, and in what form:
instructions, retrieved documents, tool results, memory. Most agent failures
are context failures.

- **Practice:** take a long-running agent task and measure what fills its
  context. Cut it down: summarize, load on demand, split work across
  sub-agents with their own context.
- **Read:** [Effective context engineering for AI agents](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents) (Anthropic).

### 4. Model routing and cost

Using the smallest model that does the job, caching what repeats, and
knowing what a task actually costs.

- **Practice:** log tokens and cost per task in something you run. Route the
  easy steps to a smaller model and check (with your evals) that quality
  holds.
- **Read:** the model comparison and [prompt caching](https://docs.claude.com/en/docs/build-with-claude/prompt-caching)
  docs for whichever provider you use.

### 5. Multi-agent orchestration

Splitting work across agents that plan, do and review, and keeping the flow
explicit and testable instead of hidden in one giant prompt.

- **Practice:** turn a multi-step workflow you do by hand into an explicit
  graph or state machine that agents walk, with a check at each step.
- **Read:** [Building effective agents](https://www.anthropic.com/engineering/building-effective-agents)
  and [How we built our multi-agent research system](https://www.anthropic.com/engineering/multi-agent-research-system) (Anthropic).

### 6. On-device models

Small models running locally: private by default, free per call, and
available offline. Good for classification, extraction and short summaries.

- **Practice:** move one small task from a cloud API to a local model and
  compare quality, speed and cost.
- **Read:** Apple's [Foundation Models framework](https://developer.apple.com/documentation/foundationmodels)
  (on-device models on Apple platforms); [Ollama](https://ollama.com) or
  [LM Studio](https://lmstudio.ai) for local models anywhere.

### 7. Teaching others to use AI well

Explaining AI to people who aren't engineers: why it makes things up, how to
check its answers, what not to paste into it, and when not to trust it.
Teaching is also the best test of whether you understand something.

- **Practice:** write plain-language explainers for friends, family or
  colleagues. Run a short session at work or in your community.
- **Read:** Anthropic's free AI Fluency courses (below), including *Teaching
  AI Fluency*.

---

## Public work

- **Make your harness public.** If you've built prompts, skills, agents or
  workflow tooling for your own use, publishing it (with secrets and personal
  details stripped) is the clearest proof of what you can do. Mine is
  [agent-config](https://github.com/coreydaley/agent-config).
- **Write regularly.** One post a month at minimum, about real work: what you
  built, what failed, what you measured. Specific beats general.
- **Contribute upstream.** The tools you use (MCP servers, agent CLIs, SDKs)
  take issues, docs fixes and pull requests. Small, real contributions count.

---

## Foundations (free)

Enough understanding of how models work to build with them well. All free.

**Anthropic Academy** ([anthropic.skilljar.com](https://anthropic.skilljar.com))
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
- [x] Claude Platform 101
- [ ] Claude with Amazon Bedrock
- [ ] Claude with Google Cloud's Vertex AI
- [ ] AI Fluency for Small Businesses
- [ ] AI Fluency for Builders

**Other certificates I've completed**
- [x] Real-World AI for Everyone — Advancing Women in Tech ([Coursera](https://www.coursera.org/specializations/real-world-ai-for-everyone), sponsored by Anthropic)
- [x] IBM AI Developer Professional Certificate — [Coursera](https://www.coursera.org/professional-certificates/applied-artifical-intelligence-ibm-watson-ai)

---

## Claude Certified Architect — Foundations

Anthropic's certification for designing and deploying Claude-based systems.
It's architecture-focused, which suits the usage side. The 13 free prep
courses are on [anthropic.skilljar.com](https://anthropic.skilljar.com);
check there for the current exam price and registration.

| Domain | Weight |
|--------|--------|
| Agentic Architecture & Orchestration | 27% |
| Claude Code Configuration & Workflows | 20% |
| Prompt Engineering & Structured Output | 20% |
| Tool Design & MCP Integration | 18% |
| Context Management & Reliability | 15% |

Passing score: **720 / 1000**

- [x] Complete the 13 free prep courses
- [ ] Take the exam

---

## Tools

### An AI assistant

As close to a requirement as anything here: as a coding partner for the
projects, and as a tutor that will explain a concept three different ways
until it clicks. Start on a standard plan and move up only if you hit the
limits.

| Tool | Subscription | Best For |
|------|-------------|----------|
| [Claude Pro](https://claude.ai) + [Claude Code](https://claude.ai/code) | ~$20/mo + usage | Architecture discussions, long context, complex reasoning |
| [ChatGPT Plus](https://chat.openai.com) + [Codex](https://platform.openai.com) | ~$20/mo | Largest community, most Stack Overflow-style help available |
| [Google AI Pro](https://gemini.google/subscriptions/) + [Gemini CLI](https://github.com/google-gemini/gemini-cli) | ~$20/mo | Image and video generation alongside a general assistant |

### LLM API access

Building your own tools means calling a model directly. You don't need to
spend money to get started.

#### Paid APIs (pay per token)
| Provider | API Console | Notes |
|----------|-------------|-------|
| Anthropic (Claude) | [console.anthropic.com](https://console.anthropic.com) | Strong instruction following and long context |
| OpenAI (GPT) | [platform.openai.com](https://platform.openai.com) | Largest ecosystem and community |
| Google (Gemini) | [aistudio.google.com](https://aistudio.google.com) | Free tier available, cheap at scale |
| Mistral | [console.mistral.ai](https://console.mistral.ai) | Low-cost major provider, EU-based |

> All of the above have free tiers or trial credits to get started.

#### Free / low-cost alternatives
| Option | How | Notes |
|--------|-----|-------|
| [Ollama](https://ollama.com) | Run models locally | Free, no API key needed, works on Mac/Windows/Linux. Limited by local hardware. |
| [LM Studio](https://lmstudio.ai) | Run models locally (GUI) | Same as Ollama but with a user interface. |
| [Google Gemini Free Tier](https://aistudio.google.com) | Cloud API | Generous free tier via Google AI Studio |
| [Groq](https://groq.com) | Cloud API | Free tier, very fast inference on open models |
| [OpenRouter](https://openrouter.ai) | Cloud API | One API for many models, pay only for what you use |

### SDKs and protocols
| Tool | Purpose | Install |
|------|---------|---------|
| Anthropic SDK | Claude API client | `pip install anthropic` / `npm install @anthropic-ai/sdk` |
| OpenAI SDK | OpenAI API client | `pip install openai` / `npm install openai` |
| Model Context Protocol | Standard way to give agents tools and data | [modelcontextprotocol.io](https://modelcontextprotocol.io/specification/latest) |
| Docker | Sandboxed execution for agents and tools | [docker.com](https://docker.com) |

### Hardware

You don't need special hardware for the usage side: models run in the cloud,
and a normal laptop is enough. Local models are the exception: more memory
lets you run bigger ones. On a Mac, unified memory is shared with the GPU, so
32GB or more goes a long way; on Windows or Linux, GPU VRAM is the limit.

---

## Saving money

Most of this is free: the courses, local models, and free API tiers. What
costs money is an AI assistant subscription and, eventually, some API usage.

- **Ask about a learning budget.** Many employers have an annual learning
  and development budget that covers subscriptions, API credits and
  certification exams. It often goes unused.
- **Use free tiers first,** and move up a plan only when you hit a limit.
- **Set spending limits** on every API key before you experiment.
