# # 🚀 AI Content Repurposing System

## Overview

The AI Content Repurposing System is an AI-powered automation solution that transforms YouTube videos into multiple content formats.

Users provide a YouTube video URL, and the system automatically extracts the video transcript, processes it using a Large Language Model (LLM), and generates platform-specific content suitable for social media and content marketing.

This project demonstrates workflow automation, API integration, prompt engineering, and AI-powered content generation using n8n and Groq LLM.

---

## Problem Statement

Content creators, educators, marketers, and businesses often spend significant time repurposing long-form video content for multiple platforms.

The traditional process involves:

* Watching the entire video
* Extracting key insights
* Writing platform-specific content
* Repeating the process for different social media platforms

This manual workflow is time-consuming and inefficient.

---

## Solution

The system automates the entire content repurposing process by:

1. Accepting a YouTube video URL.
2. Extracting the transcript from the video.
3. Processing the transcript using a Large Language Model (LLM).
4. Generating:

   * 📄 LinkedIn Post
   * 🐦 Twitter/X Thread
   * 📸 Instagram Caption
   * 📝 Blog Article
5. Returning AI-generated content through an automated workflow.

---

## Features

* Automated YouTube Transcript Extraction
* AI-Powered Content Generation
* LinkedIn Post Generation
* Twitter/X Thread Generation
* Instagram Caption Generation
* Blog Article Generation
* Workflow Automation using n8n
* Webhook-Based Integration
* API Testing using Postman
* Secure Local Development using ngrok
* Real-Time Content Processing

---

## Tech Stack

| Component             | Technology             |
| --------------------- | ---------------------- |
| Workflow Automation   | n8n                    |
| Programming Language  | Python                 |
| AI Model              | Groq LLM               |
| Transcript Extraction | YouTube Transcript API |
| API Testing           | Postman                |
| Tunnel Service        | ngrok                  |
| Integration           | Webhooks               |

---

## Architecture

```text
YouTube URL (Postman)
          ↓
      ngrok Tunnel
          ↓
      n8n Webhook
          ↓
 Transcript Extraction
          ↓
       Groq LLM
          ↓
 ┌─────────────────┐
 │ LinkedIn Post   │
 │ Twitter Thread  │
 │ Instagram Post  │
 │ Blog Article    │
 └─────────────────┘
          ↓
   Generated Output
```

---

## Workflow

1. User sends a YouTube video URL through Postman.
2. The request is forwarded to the n8n webhook using ngrok.
3. The workflow extracts the transcript from the YouTube video.
4. The transcript is processed by Groq LLM.
5. The AI generates content optimized for different platforms.
6. The generated content is returned as a structured API response.

---

## Project Structure

```text
AI-Content-Repurposing-System/
│
├── app.py
├── README.md
│
├── workflow/
│   └── n8n_workflow.json
│
└── screenshots/
    ├── workflow.png
    ├── postman_request.png
    ├── output.png
```

---

## Installation

### Clone the Repository

```bash
git clone https://github.com/yourusername/AI-Content-Repurposing-System.git
```

### Navigate to the Project Directory

```bash
cd AI-Content-Repurposing-System
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Configure Environment Variables

Create a `.env` file and add your API credentials:

```env
GROQ_API_KEY=your_api_key
```

### Start n8n

```bash
n8n start
```

### Expose Local Webhook using ngrok

```bash
ngrok http 5678
```

### Send Requests using Postman

Use the generated ngrok URL to test the webhook endpoint and generate content.

---

## Screenshots

### Workflow Automation

* n8n workflow showing the complete automation pipeline.

### API Request

* Postman request containing the YouTube video URL.

### Generated Output

* AI-generated LinkedIn post, Twitter thread, Instagram caption, and blog article.

---

## Future Enhancements

* Multi-Language Content Generation
* Social Media Auto Posting
* Content Scheduling
* RAG-Based Knowledge Enhancement
* SEO Optimization
* Hashtag Recommendation System
* Content Performance Analytics
* Support for Additional Platforms

---

## Author

**M. Navya Sri**


