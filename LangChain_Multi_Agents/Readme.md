# 🔬 AI Research Agent

Multi-agent research pipeline built with **LangChain + Groq + Streamlit**.

Input a topic → 4 agents collaborate → get a polished research report.

----------------------------------------------------------------------------

## 🎯 What It Does

| Step | Agent | Job |
|------|-------|-----|
| 1️⃣ | 🔍 Search Agent | Finds reliable sources from the web |
| 2️⃣ | 📄 Reader Agent | Scrapes the most relevant URL |
| 3️⃣ | ✍️ Writer Agent | Drafts a research report |
| 4️⃣ | 🧐 Critic Agent | Reviews and provides feedback |

----------------------------------------------------------------------------


## ⚙️ Tech Stack

- **LangChain** — Agent orchestration
- **Groq** — LLM (gpt-oss-120b)
- **Streamlit** — Web UI
- **Tavily** — Search API
- **trafilatura + BeautifulSoup** — Web scraping
- **Python 3.11**

----------------------------------------------------------------------------


```bash
# Create and activate conda environment
conda create -n langagent python=3.11 -y
conda activate langagent

# Install dependencies
pip install -r requirements.txt