📘 Jarvis – Python Voice Assistant
✅ About the Project

Jarvis is a voice-controlled personal assistant built using Python. It listens to your commands, opens websites like Google and YouTube, plays music from a predefined library, fetches the latest news, and provides answers using OpenAI's language model.

This project demonstrates how to combine voice recognition, text-to-speech, API integration, and environment variable management in Python.

🚀 Features

✔ Voice recognition using speech_recognition
✔ Text-to-speech using pyttsx3
✔ Open websites (Google, YouTube, LinkedIn)
✔ Play music from a preset list
✔ Fetch news headlines using NewsAPI
✔ Provide AI-powered responses using OpenAI's API
✔ Secure API keys management using .env file

⚙ Setup Instructions

Clone the repository

git clone your_repo_url
cd your_project_directory


Create and activate the virtual environment

python -m venv .venv
.\.venv\Scripts\Activate.ps1   # For PowerShell


Install required packages

pip install -r requirements.txt


Create a .env file in the project directory and add:

OPENAI_API_KEY=your_openai_api_key
NEWSAPI_KEY=your_newsapi_key


Run the assistant

python main.py

📂 File Structure
Jarvis/
├── .venv/                # Virtual environment (excluded from GitHub)
├── .env                 # Stores your API keys (excluded from GitHub)
├── .gitignore           # To ignore sensitive files
├── main.py              # Main script file
├── requirements.txt    # List of Python packages
├── musicLib.py          # Music library links
└── README.md            # This file

📦 .gitignore

Make sure .venv/ and .env are listed in .gitignore to keep your environment and API keys private.

📢 Usage Notes

Always activate the virtual environment before running the script.

Do not share your .env file as it contains your API keys.

Keep pip updated for best performance.
