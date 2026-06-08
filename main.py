import os
from dotenv import load_dotenv
import litellm
litellm.drop_params = True
from crewai import Agent, Task, Crew, Process
from crewai_tools import SerperDevTool

load_dotenv()

os.environ["GEMINI_API_KEY"] = os.getenv("GEMINI_API_KEY")

llm = "groq/llama-3.3-70b-versatile"

search_tool = SerperDevTool()

researcher = Agent(
    role="Lead Researcher",
    goal="Find comprehensive public information about the target company: {company}",
    backstory=(
        "You are an expert business researcher with a talent for finding "
        "detailed, accurate information about companies using web searches. "
        "You dig deep and surface the most relevant facts."
    ),
    tools=[search_tool],
    llm=llm,
    verbose=True,
    allow_delegation=False,
)

analyst = Agent(
    role="Business Analyst",
    goal="Analyze the research data and extract key business insights about {company}",
    backstory=(
        "You are a sharp business analyst who turns raw research into structured "
        "insights. You identify pain points, opportunities, tech stack, team size, "
        "funding stage, and competitive positioning."
    ),
    llm=llm,
    verbose=True,
    allow_delegation=False,
)

writer = Agent(
    role="Report Writer",
    goal="Write a professional, concise lead report about {company} for a sales team",
    backstory=(
        "You are a professional business writer who crafts clean, compelling reports. "
        "You turn analyst insights into actionable summaries that help sales teams "
        "understand a prospect quickly."
    ),
    llm=llm,
    verbose=True,
    allow_delegation=False,
)

research_task = Task(
    description=(
        "Search the web for detailed information about the company: {company}. "
        "Find: what they do, their product/service, target market, founding year, "
        "team size, location, recent news, funding, tech stack if visible, "
        "and any notable achievements or press mentions."
    ),
    expected_output=(
        "A detailed bullet-point summary of all findings about {company}, "
        "with sources noted where possible."
    ),
    agent=researcher,
)

analysis_task = Task(
    description=(
        "Using the research provided, analyze {company} from a B2B sales perspective. "
        "Identify: their likely pain points, growth stage, decision makers, "
        "budget signals, technology choices, and how a software/AI solution might help them."
    ),
    expected_output=(
        "A structured analysis with sections: Company Overview, Growth Stage, "
        "Pain Points, Tech Stack, Key Decision Makers, and Sales Opportunity Score (1-10)."
    ),
    agent=analyst,
    context=[research_task],
)

writing_task = Task(
    description=(
        "Write a professional lead report for {company} using the research and analysis. "
        "Format it as a clean report a salesperson would use before a call. "
        "Include an executive summary, key facts, opportunities, and a recommended approach."
    ),
    expected_output=(
        "A well-formatted lead report in markdown with sections: "
        "Executive Summary, Company Snapshot, Key Insights, Sales Opportunity, "
        "and Recommended Outreach Angle."
    ),
    agent=writer,
    context=[research_task, analysis_task],
)

crew = Crew(
    agents=[researcher, analyst, writer],
    tasks=[research_task, analysis_task, writing_task],
    process=Process.sequential,
    verbose=True,
)

if __name__ == "__main__":
    company = input("Enter the company name to research: ").strip()
    print(f"\n🚀 Starting CrewAI research on: {company}\n{'='*50}\n")

    result = crew.kickoff(inputs={"company": company})

    print("\n" + "="*50)
    print("📋 FINAL LEAD REPORT")
    print("="*50)
    print(result)

    output_file = f"{company.replace(' ', '_')}_lead_report.md"
    with open(output_file, "w") as f:
        f.write(str(result))
    print(f"\n✅ Report saved to: {output_file}")
