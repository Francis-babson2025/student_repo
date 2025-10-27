from fpdf import FPDF
import os

pdf = FPDF()
pdf.set_auto_page_break(auto=True, margin=15)
pdf.add_page()

# Font setup: DejaVu if available, otherwise Arial
font_path = "DejaVuSans.ttf"
if os.path.exists(font_path):
    pdf.add_font('DejaVu', '', font_path, uni=True)
    pdf.add_font('DejaVu', 'B', font_path, uni=True)
    font_name = 'Arial'
else:
    font_name = 'Arial'

# Title
pdf.set_font(font_name, 'B', 16)
pdf.cell(0, 10, "Babson Coding Environment Setup", ln=True, align="C")
pdf.ln(5)

# Intro
pdf.set_font(font_name, '', 12)
intro = (
    "Welcome to your Babson Python coding environment!\n\n"
    "This guide walks you through setting up GitHub and Codespaces - your cloud-based coding workspace. "
    "By the end, you'll have your own repository, a working Python IDE, and the tools needed to write and submit assignments.\n\n"
    "Follow each step carefully. If something doesn't look right, ask for help!"
)
pdf.multi_cell(0, 8, intro)
pdf.ln(5)

# Steps
steps = [
    "Log into your GitHub account. This is where your code will live.",
    "Open the Canvas assignment link and click 'Accept'.\n\nThis creates your own personal copy of the class repository - like getting your own digital notebook.",
    "Your new repo will be named:\n    python-YOUR_GITHUB_USER_NAME\n\nThis is your private workspace for the course.",
    "Go back to github.com, refresh, and click on your new repo.",
    "Click Code -> Codespaces -> Create codespace on main.\n\nThis launches a cloud-based coding environment with your files already loaded.",
    "Open Settings: hamburger menu -> File -> Preferences -> Settings.",
    "Search for 'git.untrack', change MIXED to HIDDEN, then close settings.\n\nThis hides unnecessary Git files so you can focus on your code.",
    ("Visual reference for Settings panel:", "vs_code_LHS.png"),
    "Click Extensions in the left sidebar, search 'Live Server', and install the one by Ritwick Dey.\n\nThis lets you preview HTML files in your browser.",
    "In the terminal (just once for the course), enter:\n git remote add upstream https://github.com/babson-org/classroom-week00-python_class.git\n\nThis connects your repo to the teacher's master copy so you can pull updates.",
    ("Git Source Control view in Codespaces shows a commit icon on the upper left. "
     "Clicking it adds a suggested commit message:", "commit.png")
]

for i, step in enumerate(steps, 1):
    if isinstance(step, tuple):
        caption, img_file = step
        pdf.set_font(font_name, 'B', 12)
        pdf.multi_cell(0, 8, f"{caption}")
        pdf.set_font(font_name, '', 12)
        pdf.image(img_file, w=100)
        pdf.ln(5)
    else:
        pdf.set_font(font_name, 'B', 12)
        step_prefix = f"Step {i}: "
        pdf.set_font(font_name, '', 12)
        pdf.multi_cell(0, 8, step_prefix + step)
        pdf.ln(2)

# What's Going On
pdf.set_font(font_name, 'B', 14)
pdf.cell(0, 10, "What's Going On?", ln=True)
pdf.set_font(font_name, '', 12)
explanation = (
    "GitHub is your code's home base. When you accept the assignment, GitHub creates a private copy "
    "of the teacher's repository just for you.\n\n"
    "Codespaces is your coding workspace - like a virtual computer in the cloud. It opens your repo "
    "in a full-featured Python editor.\n\n"
    "Git tracks changes to your files. When you 'commit', you're saving a snapshot of your work. "
    "You'll write a short message each time to describe what you changed.\n\n"
    "To keep your repo up to date with the teacher's version, you'll use:\n"
    "    git pull --no-edit upstream main\n\n"
    "This command does three things:\n"
    "  * Connects to the teacher's repo (called 'upstream')\n"
    "  * Pulls in the latest changes from the main branch\n"
    "  * Merges them into your repo without asking for a commit message\n\n"
    "  ** Before running this command, you must commit your changes and sync. If you haven't committed and synced, Git won't let you pull - "
    "and you risk losing unsaved work.\n\n"
    "  ** You'll use this command often:\n"  
    "  * After your instructor announces updates\n\n"    
    "Make it a habit:\n"
    "    Commit -> Sync -> Pull -> Code"
)
pdf.multi_cell(0, 8, explanation)
pdf.ln(5)


# Important Note
pdf.set_font(font_name, 'B', 12)
pdf.set_text_color(255, 0, 0)
pdf.multi_cell(0, 8, "IMPORTANT: Always commit and sync your work BEFORE updating from the master repository.")
pdf.set_text_color(0, 0, 0)
pdf.ln(5)

# Checklist
checklist = [
    "# Accepted the GitHub Classroom assignment",
    "# Created a Codespace on main",
    "# Installed Live Server extension",
    "# Set git.untrack to HIDDEN",
    "# Added upstream remote",
    "# Committed at least once"
]
pdf.set_font(font_name, 'B', 12)
pdf.cell(0, 10, "Setup Checklist", ln=True)
pdf.set_font(font_name, '', 12)
for item in checklist:
    pdf.cell(0, 8, item, ln=True)

# Save PDF
pdf_file = "Babson_Coding_Environment_Setup.pdf"
pdf.output(pdf_file)
print(f"PDF created: {pdf_file}")


