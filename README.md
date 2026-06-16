# 🚀 AI Content Repurposing System

## Overview

The AI Content Repurposing System is an AI-powered automation workflow that transforms YouTube videos into multiple content formats.

Users provide a YouTube video URL, and the system automatically extracts the video transcript, processes it using a Large Language Model (LLM), and generates platform-specific content for social media and content marketing.

This project demonstrates workflow automation, API integration, prompt engineering, and AI-powered content generation using n8n and Groq LLM.

---

## Problem Statement

Content creators, educators, marketers, and businesses often spend significant time repurposing long-form video content into content suitable for different platforms.

The traditional process involves:

* Watching the video
* Extracting key insights
* Writing platform-specific content
* Repeating the process for multiple platforms

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
 │ Instagram Caption│
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
5. The AI generates platform-specific content.
6. The generated content is returned as a structured API response.

---

## Project Structure

```text

AI-Content-Repurposing-System/
│
├── README.md
|
│
├── workflow/
│   └── n8n_workflow.json
│
└── screenshots/
    ├── workflow.png
    ├── postman_request.png
    └── output.png
```

---

## Usage

1. Start the n8n workflow.
2. Expose the local webhook using ngrok.
3. Copy the generated ngrok URL.
4. Send a POST request from Postman containing the YouTube video URL.
5. Receive AI-generated content in the API response.

---

## Screenshots

### Workflow Automation

Screenshot of the n8n workflow showing the complete automation pipeline.

### API Request

Screenshot of the Postman request containing the YouTube video URL.

### Generated Output

Screenshot of the generated LinkedIn post, Twitter/X thread, Instagram caption, and blog article.

---

## Future Enhancements

* Multi-Language Content Generation
* Social Media Auto Posting
* Content Scheduling
* RAG Integration
* SEO Optimization
* Hashtag Recommendation System
* Additional Content Formats

---

## License

This project is developed for educational and portfolio purposes.

---

## Author

**M. Navya Sri**



