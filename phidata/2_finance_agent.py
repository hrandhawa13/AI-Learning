from phi.agent import Agent
from phi.model.groq import Groq
from dotenv import load_dotenv
from phi.tools.yfinance import YFinanceTools

load_dotenv()

agent = Agent(
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

agent.print_response("Summarize and compare analyst recommendations and fundamentals for TSLA and NVDIA")