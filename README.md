# Bias Detection Explanation AI

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Flask](https://img.shields.io/badge/Flask-Backend-green)
![Groq](https://img.shields.io/badge/Groq-Llama_3.1-orange)

## Project Abstract
[cite_start]This project focuses on building a Generative AI-powered media analysis system that helps users understand bias in news articles[cite: 9]. [cite_start]The Bias Detection Explanation AI analyzes written content and provides clear, structured explanations of potential bias, framing techniques, and missing perspectives[cite: 10]. [cite_start]Using large language models and critical reasoning prompts, the system evaluates how information is presented, what viewpoints are emphasized or omitted, and how language influences reader perception[cite: 11]. [cite_start]The goal is to promote media literacy by making bias more transparent and understandable[cite: 12].

## Problem Statement
[cite_start]In today's information-rich environment, readers often consume news without recognizing subtle biases in tone, framing, or perspective[cite: 14]. [cite_start]This can lead to misinformation, skewed opinions, and lack of critical thinking[cite: 15]. [cite_start]The Bias Detection Explanation AI addresses this challenge by allowing users to input a news article or text[cite: 16]. [cite_start]The system analyzes the content and highlights indicators of bias—such as selective wording, one-sided arguments, or missing viewpoints[cite: 17].

## Key Features & Modules
* **Article Input & Processing Module:** Accepts news articles or text content and prepares it for analysis[cite: 22, 23].
* **Bias Detection Engine:** Uses LLMs to identify linguistic bias, tone, framing, and selective emphasis[cite: 24, 26].
* **Perspective Analysis Tool:** Detects missing viewpoints or underrepresented angles in the content[cite: 27, 28].
* **Explanation Generator Module:** Produces clear, human-readable explanations of identified biases and their impact[cite: 29, 30].

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
