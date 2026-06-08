# AI Lead Research Crew 🤖

A multi-agent AI system built with CrewAI that autonomously researches any company and generates a full B2B lead report — in seconds.

## How It Works

Three specialized AI agents collaborate in sequence:

**Agent 1 — Lead Researcher** searches the web multiple times, refining its queries until it has enough data about the target company.

![Researcher Agent thinking and searching](Lead%20Researcher-1.png)
![Researcher refining search queries](Lead%20Researcher-2.png)
![Researcher final answer with sources](Lead%20Researcher-3.png)

**Agent 2 — Business Analyst** takes the raw research and extracts structured insights: growth stage, pain points, tech stack, key decision makers, and a sales opportunity score.

![Analyst Agent output](Business%20Analyst.png)

**Agent 3 — Report Writer** turns the analysis into a clean, professional lead report a salesperson would use before a call.

![Writer Agent output](Report%20Writer.png)

## Final Output

A full markdown lead report saved automatically to a `.md` file.

![Final lead report output](FInal%20Report.png)

## Stack

- **CrewAI** — multi-agent orchestration framework
- **Groq (LLaMA 3.3 70B)** — fast, free LLM
- **Serper API** — real-time Google search tool
- **Python** — runs in terminal

## Agent Architecture

```
Input: Company Name
       ↓
Agent 1: Lead Researcher
  - Tools: Serper web search
  - Searches multiple times autonomously
  - Returns: detailed bullet-point research with sources
       ↓
Agent 2: Business Analyst
  - Context: research from Agent 1
  - Returns: Company Overview, Growth Stage, Pain Points,
             Tech Stack, Key Decision Makers, Lead Score (1-10)
       ↓
Agent 3: Report Writer
  - Context: research + analysis from Agents 1 & 2
  - Returns: Full markdown lead report
       ↓
Output: Saved as {company}_lead_report.md
```

## Setup

**1. Clone the repo**
```bash
git clone https://github.com/MarkJosephAlfred/ai-lead-crew.git
cd ai-lead-crew
```

**2. Install dependencies**
```bash
pip install crewai crewai-tools python-dotenv litellm
```

**3. Create a `.env` file**
```
GROQ_API_KEY=your_groq_key_here
SERPER_API_KEY=your_serper_key_here
```

Get your free keys:
- Groq: https://console.groq.com
- Serper: https://serper.dev

**4. Run it**
```bash
python main.py
```

**5. Enter a company name when prompted**

```
Enter the company name to research: Peak Nine

🚀 Starting CrewAI research on: Peak Nine
==================================================
# Agent: Lead Researcher thinking...
# Agent: Business Analyst thinking...
# Agent: Report Writer thinking...

✅ Report saved to: Peak_Nine_lead_report.md
```

## Why This Is Useful

Sales teams waste hours manually researching leads before calls. This system does it in under 2 minutes, for any company in the world, and outputs a structured report ready to use.

Built in one day as a proof of concept for automating B2B sales research workflows.
