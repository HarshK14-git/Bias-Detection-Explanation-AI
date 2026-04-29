# Bias Detection Explanation AI

## Project Abstract
This project focuses on building a Generative AI-powered media analysis system that helps users understand bias in news articles. The Bias Detection Explanation AI analyzes written content and provides clear, structured explanations of potential bias, framing techniques, and missing perspectives. Using large language models and critical reasoning prompts, the system evaluates how information is presented, what viewpoints are emphasized or omitted, and how language influences reader perception. The goal is to promote media literacy by making bias more transparent and understandable.

## Problem Statement
In today's information-rich environment, readers often consume news without recognizing subtle biases in tone, framing, or perspective. This can lead to misinformation, skewed opinions, and lack of critical thinking. The Bias Detection Explanation AI addresses this challenge by allowing users to input a news article or text. The system analyzes the content and highlights indicators of bias—such as selective wording, one-sided arguments, or missing viewpoints. 

## Key Features & Modules
* **Article Input & Processing Module:** Accepts news articles or text content and prepares it for analysis.
* **Bias Detection Engine:** Uses LLMs to identify linguistic bias, tone, framing, and selective emphasis.
* **Perspective Analysis Tool:** Detects missing viewpoints or underrepresented angles in the content.
* **Explanation Generator Module:** Produces clear, human-readable explanations of identified biases and their impact.

## Tech Stack
* **Backend Framework:** Python / Flask
* **Cross-Origin Resource Sharing:** Flask-CORS
* **LLM Engine:** Groq API (`llama-3.1-8b-instant`)
* **Prompt Engineering:** Zero-shot constrained JSON prompting

## Project Structure
```text
Bias_Detection_Project/
│
├── backend/
│   ├── app.py               # Flask application and API routing
│   ├── bias_engine.py       # Groq API integration and Regex/JSON parsing fallback
│   ├── prompts.py           # Structured constraints and critical reasoning prompts
│   └── test.py              # Initial LLM connection test script
│
├── .env                     # Environment variables (API Keys - DO NOT UPLOAD)
├── .gitignore               # Specifies intentionally untracked files to ignore
└── README.md                # Project documentation
