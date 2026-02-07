# Updated tools.py for Resend
import os
import resend
from openai import function_tool

resend.api_key = os.environ.get("RESEND_API_KEY")


@function_tool
def send_email(body: str):
    """Sends the approved email using the Resend API."""
    try:
        resend.Emails.send(
            {
                "from": "onboarding@resend.dev",  # Or your verified domain
                "to": "your-test-email@gmail.com",
                "subject": "AI Sales Outreach",
                "text": body,
            }
        )
        return {"status": "success"}
    except Exception as e:
        return {"status": "error", "message": str(e)}
