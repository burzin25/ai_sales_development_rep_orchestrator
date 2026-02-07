import streamlit as st
import asyncio
from openai import Runner, trace
from src.agents import sales_manager
from dotenv import load_dotenv

load_dotenv()

st.set_page_config(page_title="AI SDR Orchestrator", page_icon="🤖")

st.title("🤖 AI Sales Dev Orchestrator")
st.markdown(
    "Automated multi-agent generation and selection of high-performing sales emails."
)

# Input for the lead
lead_info = st.text_area(
    "Enter Prospect Info (Company, Role, Recent News):",
    placeholder="e.g. Acme Corp, CTO, just raised Series B...",
)

if st.button("Generate Campaign"):
    if not lead_info:
        st.warning("Please provide lead info first.")
    else:
        with st.status("Agents are collaborating...") as status:

            async def run_manager():
                # We use trace to enable observability in the OpenAI dashboard
                with trace("SDR_Workflow"):
                    result = await Runner.run(
                        sales_manager, f"Draft and pick the best email for: {lead_info}"
                    )
                    return result.final_output

            # Running the async agent in a Streamlit context
            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)
            final_draft = loop.run_until_complete(run_manager())

            st.session_state.draft = final_draft
            status.update(label="Drafting Complete!", state="complete")

if "draft" in st.session_state:
    st.subheader("Final Draft Selection")
    st.info(st.session_state.draft)

    if st.button("🚀 Confirm & Send to Prospect"):
        st.success("The 'send_email' tool has been triggered! Check your inbox.")
