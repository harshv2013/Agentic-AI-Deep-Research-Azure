import asyncio
from agents import trace, gen_trace_id
# from planner_agent import planner_agent, WebSearchItem, WebSearchPlan
# from writer_module import writer_agent, ReportData
# from email_agent import email_agent, send_email
# from search_agent import search_agent, mock_web_search
# from azure_client import azure_chat

from deep_research.planner_agent import planner_agent, WebSearchItem, WebSearchPlan
from deep_research.writer_module import writer_agent, ReportData
from deep_research.email_agent import email_agent, send_email
from deep_research.search_agent import search_agent, mock_web_search
from deep_research.azure_client import azure_chat

from contextlib import contextmanager

@contextmanager
def trace(name, trace_id=None):
    # No-op trace: does nothing
    print(f"[Research TRACE] {name} (trace_id={trace_id})")
    yield

class ResearchManager:

    async def run(self, query: str):
        """ Run the deep research process, yielding status updates + final report """
        trace_id = gen_trace_id()
        with trace("Research trace", trace_id=trace_id):
            print(f"Trace: https://platform.openai.com/traces/trace?trace_id={trace_id}")
            yield f"Trace: https://platform.openai.com/traces/trace?trace_id={trace_id}"

            search_plan = await self.plan_searches(query)
            yield "Searches planned, starting to search..."     

            search_results = await self.perform_searches(search_plan)
            yield "Searches complete, writing report..."

            report = await self.write_report(query, search_results)
            yield "Report written, sending email..."

            await self.send_email(report)
            yield "Email sent, research complete"
            yield report.markdown_report

    async def plan_searches(self, query: str) -> WebSearchPlan:
        print("Planning searches...")
        response = azure_chat(planner_agent.instructions, f"Query: {query}")
        # fallback: 3 mock searches
        items = [
            WebSearchItem(query=f"{query} overview", reason="high-level view"),
            WebSearchItem(query=f"{query} trends 2025", reason="recent developments"),
            WebSearchItem(query=f"{query} comparison", reason="compare frameworks"),
        ]
        return WebSearchPlan(searches=items)

    async def perform_searches(self, search_plan: WebSearchPlan) -> list[str]:
        print("Searching...")
        tasks = [asyncio.create_task(self.search(item)) for item in search_plan.searches]
        results = await asyncio.gather(*tasks)
        print("Finished searching")
        return results

    async def search(self, item: WebSearchItem) -> str:
        return mock_web_search(item.query)

    async def write_report(self, query: str, search_results: list[str]) -> ReportData:
        print("Writing report...")
        input_text = f"Query: {query}\nResults: {search_results}"
        content = azure_chat(writer_agent.instructions, input_text)
        return ReportData(
            short_summary="This is a short summary (mock).",
            markdown_report=content,
            follow_up_questions=["What companies are leading?", "What risks exist?"]
        )

    async def send_email(self, report: ReportData):
        subject = "Research Results"
        html_body = "<html><body><pre>" + report.markdown_report[:500] + "</pre></body></html>"
        send_email(subject, html_body)
