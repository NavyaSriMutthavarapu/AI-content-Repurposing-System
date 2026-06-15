# 🚀 AI Content Repurposing System

## Overview

The AI Content Repurposing System is an AI-powered application that automatically transforms YouTube videos into multiple content formats.

Users simply provide a YouTube video URL, and the system extracts the transcript, processes it using a Large Language Model (LLM), and generates platform-specific content such as LinkedIn posts, Twitter threads, Instagram captions, and blog articles.

This project demonstrates workflow automation, prompt engineering, API integration, and AI-powered content generation.

---

## Problem Statement

Content creators, educators, marketers, and businesses often spend significant time converting long-form video content into content suitable for different platforms.

The process typically involves:
- Watching the video
- Extracting key points
- Writing platform-specific content
- Repeating the process for multiple platforms

This project automates the entire workflow and significantly reduces manual effort.

---

## Solution

The system performs the following tasks:

1. Accepts a YouTube video URL.
2. Extracts the transcript from the video.
3. Sends the transcript to an LLM.
4. Generates:
   - 📄 LinkedIn Post
   - 🐦 Twitter/X Thread
   - 📸 Instagram Caption
   - 📝 Blog Article
5. Displays the generated content through a Streamlit interface.

---

##  Features

- Automated YouTube Transcript Extraction
- AI-Powered Content Generation
- LinkedIn Post Generation
- Twitter/X Thread Generation
- Instagram Caption Generation
- Blog Article Generation
- Workflow Automation using n8n
- Interactive Streamlit Dashboard

---

## Tech Stack

| Component | Technology |
|------------|------------|
| Frontend | Streamlit |
| Workflow Automation | n8n |
| Programming Language | Python |
| AI Model | Groq LLM |
| Transcript Extraction | YouTube Transcript API |
| Integration | Webhooks |

---

## Architecture

```text
YouTube URL
      ↓
Transcript Extraction
      ↓
Groq LLM
      ↓
LinkedIn Post
Twitter Thread
Instagram Caption
Blog Article
      ↓
Streamlit Dashboard
```

---

## Project Structure

```text
AI-Content-Repurposing-System/
│
├── app.py
├── requirements.txt
├── README.md
│
├── workflow/
│   └── n8n_workflow.json
│
└── screenshots/
    ├── workflow.png
    ├── homepage.png
    └── output.png
```

---

## Installation

Clone the repository:

```bash
git clone https://github.com/yourusername/AI-Content-Repurposing-System.git
```

Navigate to the project folder:

```bash
cd AI-Content-Repurposing-System
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
streamlit run app.py
```

---

## Future Enhancements

- Multi-language Support
- Social Media Auto Posting
- Content Scheduling
- RAG Integration
- Hashtag Recommendation System
---

## License

This project is developed for educational and portfolio purposes.

Author
M.Navya Sri
