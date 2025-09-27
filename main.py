import gradio as gr
from dotenv import load_dotenv
from deep_research.research_manager import ResearchManager

load_dotenv(override=True)

async def run(query: str):
    async for chunk in ResearchManager().run(query):
        yield chunk

def main():
    with gr.Blocks(theme=gr.themes.Default(primary_hue="sky")) as ui:
        gr.Markdown("# Deep Research with Agentic AI + Azure OpenAI")
        query_textbox = gr.Textbox(label="What topic would you like to research?")
        run_button = gr.Button("Run", variant="primary")
        report = gr.Markdown(label="Report")
        
        run_button.click(fn=run, inputs=query_textbox, outputs=report, queue=True)
        query_textbox.submit(fn=run, inputs=query_textbox, outputs=report, queue=True)

    # ui.launch(inbrowser=True)
    ui.launch(server_name="0.0.0.0", server_port=7860)


if __name__ == "__main__":
    main()
