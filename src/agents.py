from agents import Agent
from .tools import send_email

# Specialist 1: The Corporate Professional
prof_agent = Agent(
    name="Professional_SDR",
    instructions="Write a formal, data-driven sales email focused on ROI and compliance.",
    model="gpt-4o-mini",
)

# Specialist 2: The Creative Connector
creative_agent = Agent(
    name="Creative_SDR",
    instructions="Write a witty, engaging email that uses humor to build a connection.",
    model="gpt-4o-mini",
)

# Specialist 3: The Direct/Busy Agent
busy_agent = Agent(
    name="Concise_SDR",
    instructions="Write an extremely short, 3-sentence email for a very busy executive.",
    model="gpt-4o-mini",
)

# The Sales Manager (Orchestrator)
# It sees the sub-agents as tools and has the power to send the email
sales_manager = Agent(
    name="Sales_Manager",
    instructions="Review the user's lead info. Use your sub-agents to generate 3 options. "
    "Then, pick the best one and present it for approval.",
    tools=[
        prof_agent.as_tool(
            tool_name="get_professional_draft",
            tool_description="Generate a formal, data-driven sales email",
        ),
        creative_agent.as_tool(
            tool_name="get_creative_draft",
            tool_description="Generate a witty, engaging sales email",
        ),
        busy_agent.as_tool(
            tool_name="get_concise_draft",
            tool_description="Generate a short, 3-sentence sales email",
        ),
        send_email,
    ],
    model="gpt-4o",
)
