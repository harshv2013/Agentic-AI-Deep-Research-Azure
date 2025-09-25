from pydantic import BaseModel, Field
from agents import Agent

INSTRUCTIONS = (
    "You are a senior researcher tasked with writing a cohesive report for a research query. "
    "You will be provided with the original query and some initial research. "
    "Return markdown report (>=1000 words), plus a short summary and follow-up questions."
)

class ReportData(BaseModel):
    short_summary: str = Field(description="Short summary")
    markdown_report: str = Field(description="The report in markdown")
    follow_up_questions: list[str] = Field(description="Suggested follow-ups")

writer_agent = Agent(
    name="WriterAgent",
    instructions=INSTRUCTIONS,
    model="gpt-4o-mini",
    output_type=ReportData,
)
