from typing import Dict
from agents import Agent

# --- Mocked email function ---
def send_email(subject: str, html_body: str) -> Dict[str, str]:
    print("\n[MOCK EMAIL] Pretending to send email...")
    print("From: ed@edwarddonner.com")
    print("To:   ed.donner@gmail.com")
    print("Subject:", subject)
    print("HTML Body (preview):\n", html_body[:400])
    print("[MOCK EMAIL] Success\n")
    return {"status": "success"}

INSTRUCTIONS = """You are able to send a nicely formatted HTML email based on a detailed report.
You will be provided with a detailed report. You should use your tool to send one email, providing the 
report converted into clean, well presented HTML with an appropriate subject line."""

email_agent = Agent(
    name="Email agent",
    instructions=INSTRUCTIONS,
    tools=[send_email],  # keep as callable function
    model="gpt-4o-mini",
)
