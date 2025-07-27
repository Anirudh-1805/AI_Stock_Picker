# AI Stock Picker

A modular, AI‑driven application that automates the process of discovering trending companies, performing in‑depth financial research, and selecting the best stock for investment—wrapped in an interactive Streamlit dashboard.

## Features

- **Trending Company Discovery**  
  Uses news search (via SerperDevTool) to find 2–3 companies per sector that are “trending” in the news.
- **Deep Financial Research**  
  Runs a multi‑agent pipeline to compile detailed market-position, outlook, and investment-potential analyses.
- **Automated Decision Making**  
  Compares researched companies and picks the best candidate, with rationale delivered via push notification (Pushover) and a Markdown report.
- **Interactive Dashboard**  
  Streamlit UI for selecting sector & date, running the pipeline, and viewing/downloading:
  - Trending companies (JSON)
  - Research report (JSON)
  - Final decision (Markdown)

---

## Detailed Analysis

### 1. **Overall Architecture**

- **CrewAI Orchestration**  
  - Defines a **Crew** (`StockPicker`) that chains three tasks:
    1. **find_trending_companies** (agent: `trending_company_finder`)  
    2. **research_trending_companies** (agent: `financial_researcher`)
    3. **pick_best_company** (agent: `stock_picker`, plus push notification)
  - Configuration is entirely YAML‑driven (`agents.yaml` & `tasks.yaml`), making it easy to tweak roles, goals, and output formats without code changes.

- **Memory & RAG**  
  - **Short‑term & Entity Memory** backed by `RAGStorage` and `LTMSQLiteStorage` for contextual recall across tasks.
  - Enables the agents to “remember” which companies have already been evaluated, preventing duplicates.

- **Search & Tools**  
  - **SerperDevTool** for real‑time web search of news articles.
  - Custom **PushNotificationTool** sending Pushover alerts once a decision is made.

- **UI Layer**  
  - **Streamlit dashboard** (`app.py`) for non‑technical users: sector selection, job kick‑off, and result display/download.

---

### 2. **Key Components**

| Component                   | Purpose                                                       |
|-----------------------------|---------------------------------------------------------------|
| `crew.py`                   | Defines the `StockPicker` Crew, agents, memory layers, tools. |
| `agents.yaml` & `tasks.yaml` | Declarative definitions of each agent’s role & the pipeline.   |
| `push_tool.py`              | Wraps Pushover API for user notifications.                    |
| `app.py`                    | Streamlit front‑end for interactive use.                      |
| `memory/`                   | Local DBs storing long‑term & short‑term memory.              |

---

### 3. **Strengths**

- **Modular & Configurable**  
  - New sectors, agents, or tasks can be added by editing YAML.
- **Persistent Memory**  
  - Prevents redundant research, improves continuity across runs.
- **Multi‑Agent Collaboration**  
  - Clear separation of concerns: discovery vs. research vs. decision.
- **User‑Friendly Interface**  
  - Web UI + downloadable artifacts for easy sharing.

---

