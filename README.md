# AI Content Repurposing System 🚀


The AI Content Repurposing System is an AI-powered application that automatically converts YouTube videos into multiple content formats.

Instead of manually creating content for different platforms, users only need to provide a YouTube video URL. The system extracts the transcript, processes it using a Large Language Model (LLM), and generates platform-specific content within seconds.

# Problem Statement

Content creators, educators, and marketers often spend significant time converting long-form video content into social media posts and blog articles. This process is repetitive and time-consuming.

The goal of this project is to automate content creation and reduce manual effort by generating multiple content formats from a single YouTube video.

# Solution

The system performs the following steps:

Accepts a YouTube video URL.
Extracts the video transcript.
Sends the transcript to an LLM.
Generates:
📄 LinkedIn Post
🐦 Twitter/X Thread
📸 Instagram Caption
📝 Blog Article
Displays the generated content through a Streamlit interface.
Features
Automated Transcript Extraction
AI-Powered Content Generation
LinkedIn Post Creation
Twitter Thread Generation
Instagram Caption Generation
Blog Article Generation
Workflow Automation using n8n
Interactive Streamlit Dashboard
# Tech Stack
Python
Streamlit
n8n
Groq LLM
YouTube Transcript API
Webhooks
Architecture
YouTube URL
      ↓
Transcript Extraction
      ↓
Groq LLM
      ↓
LinkedIn | Twitter | Instagram | Blog
      ↓
Streamlit Dashboard
Installation
git clone https://github.com/yourusername/AI-Content-Repurposing-System.git

cd AI-Content-Repurposing-System

pip install -r requirements.txt

streamlit run app.py
Future Enhancements
Multi-language Support
Social Media Auto Posting
Content Scheduling
RAG Integration

Author
M.Navya Sri
