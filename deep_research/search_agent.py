from agents import Agent

INSTRUCTIONS = (
    "You are a research assistant. Given a search term, you return a concise summary "
    "with the key points. No fluff."
)

# --- Mock search instead of real WebSearchTool ---
def mock_web_search(query: str) -> str:
    return f"[MOCK SEARCH] Results for '{query}':\n- Key insight 1\n- Key insight 2\n- Key insight 3"

search_agent = Agent(
    name="Search agent",
    instructions=INSTRUCTIONS,
    tools=[mock_web_search],   # mocked instead of WebSearchTool
    model="gpt-4o-mini",
)
