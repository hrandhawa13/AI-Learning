from phi.agent import Agent
from phi.model.groq import Groq
from dotenv import load_dotenv
from phi.tools.duckduckgo import DuckDuckGo
from phi.tools.yfinance import YFinanceTools

load_dotenv()

web_agent = Agent(
    model=Groq(id="llama-3.3-70b-versatile"),
    markdown=True,
    tools=[DuckDuckGo()],
    show_tool_calls=True,
    instructions=["Always include Sources"]
)


finance_agent = Agent(
    model=Groq(id="llama-3.3-70b-versatile"),
    markdown=True,
    tools=[YFinanceTools(
            stock_price=True,
            analyst_recommendations=True,
            company_info=True,
            company_news=True,
    )],
    show_tool_calls=True,
    instructions=["Use tables to display data"]
)

agent_team = Agent(
    model=Groq(id="llama-3.3-70b-versatile"),
    team=[web_agent, finance_agent],
    instructions=["Always include sources", "Use tables to display data"],
    show_tool_calls=True,
    markdown=True
)

agent_team.print_response("Summarize analyst recommendations and share latest news for NVIDIA", stream=True)