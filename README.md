**AI Sales Dev Orchestrator**

Automated multi-agent system that drafts, reviews, and selects high-performing sales outreach emails.

**Live Demo:** https://aisalesdevelopmentreporchestrator-5zjx6ekhymecwnddbkho7q.streamlit.app/

**Quick Description:**
- **What it does:** Generates three email drafts using specialist agents (professional, creative, concise), then the Sales Manager agent selects the best draft for review and optionally sends it via the Resend API.
- **Built with:** Streamlit frontend plus the `openai-agents` multi-agent framework.

**Files of interest:**
- `app.py`: Streamlit application entrypoint.
- `requirements.txt`: Python dependencies used for deployment.
- `src/agents.py`: Agent definitions and orchestrator setup.
- `src/tools.py`: External tool integrations (Resend email function).

**Local setup (development)**
1. Create and activate a virtual environment (Windows):

```powershell
python -m venv venv
venv\Scripts\Activate.ps1
```

2. Install dependencies:

```powershell
python -m pip install -r requirements.txt
```

3. Set required environment variables (example using PowerShell):

```powershell
$env:RESEND_API_KEY = "your_resend_api_key"
$env:OPENAI_API_KEY = "your_openai_api_key"
```

4. Run the app:

```powershell
streamlit run app.py
```

**Deploying to Streamlit Cloud**
- Ensure `requirements.txt` contains the needed packages and all env vars are set in the Streamlit app settings.
- Push to the repository's `main` (or `master`) branch — Streamlit Cloud will auto-deploy from the default branch.

**Notes & Tips**
- `sendgrid` is present in `requirements.txt` but unused by default — you may remove it if not needed.
- Verify `RESEND_API_KEY` and sender verification for Resend before enabling sending in production.

**Contact / Next steps**
- If you want, I can add a `README` section with screenshots, or a `Procfile` and `streamlit` config for Cloud-specific settings.
