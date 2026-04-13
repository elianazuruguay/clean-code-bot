# 📘 Clean Code Bot

A CLI tool that analyzes “dirty” code, refactors it using AI, and outputs clean, documented, SOLID-compliant code with automatic file generation and syntax highlighting.

---

# 🚀 Features

- 🧠 AI-powered code refactoring (OpenAI)
- 📊 Step-by-step pipeline: Analyze → Plan → Generate
- 🎨 Beautiful CLI output (Rich UI)
- 🔐 Input validation & security sanitization
- 🌐 Multi-language support (Python, PHP, JS, TS, Java)
- 💾 Automatic output file generation
- 🧱 SOLID-based architecture

---

# 📦 Supported Languages

- Python (`.py`, `.pyw`)
- PHP (`.php`)
- JavaScript (`.js`)
- TypeScript (`.ts`)
- Java (`.java`)

---

# 🛠️ Installation

## 1. Clone repository

```bash
git clone https://github.com/your-username/clean-code-bot.git
cd clean-code-bot
```

## 2. Create virtual environment (Mac / Linux)
```
python3 -m venv venv
source venv/bin/activate
```
## 3. Install dependencies
pip install -r requirements.txt

# 🔑 OpenAI API Key Setup
### 1. Create OpenAI account

Go to:
https://platform.openai.com/

### 2. Generate API Key
Go to API Keys section
Click Create new secret key
Copy your key (you won’t see it again)
### 3. Set environment variable (Mac/Linux)
```
export OPENAI_API_KEY="your-api-key-here"
```

To persist it:

```
echo 'export OPENAI_API_KEY="your-api-key-here"' >> ~/.zshrc
source ~/.zshrc
```

# ▶️ How to Run
Basic usage
```
python cli.py examples/before.py
```

With custom output file
```
python cli.py examples/before.py -o output/result.py
```
📁 Output Naming Convention

By default, generated files follow a configurable naming convention.
```
<prefix>_<original_filename>
```
Example

Input file:
```
examples/before.php
```

Output file:
```
output/after_before.php
```
⚙️ Configuration

The prefix can be customized in config/settings.py:
```
OUTPUT_PREFIX = "after"
```

You can change it to:

```
OUTPUT_PREFIX = "refactored"
```
Result:

output/refactored_before.php

📁 Project Structure
```
clean-code-bot/
│
├── cli.py
├── core/
│   ├── processor.py
│   ├── prompt_engine.py
│   ├── language_detector.py
│   └── formatter.py
│
├── security/
│   ├── sanitizer.py
│   └── file_validator.py
│
├── ui/
│   └── console.py
│
├── config/
│   └── settings.py
│
├── examples/
│   └── before.py
│
├── output/
│   └── (generated files)
│
├── requirements.txt
└── README.md
```
## 🧪 Example Workflow
### Input
```
def calc(a,b):
    return a+b
```

### Output
- 🔍 Code Analysis
- 🛠 Improvement Plan
- 💻 Refactored Code (colored CLI output)
- 💾 Saved automatically in /output
---
### ⚙️ Requirements
- click
- openai
- rich
- black
- python-dotenv

### 🔐 Security Features
- File validation (allowed extensions only)
- Input sanitization
- Prompt injection detection
- Safe LLM interaction layer
---
### 🧠 Architecture Flow
```
Input Code
   ↓
Validation & Sanitization
   ↓
Language Detection
   ↓
AI Analysis (CoT Step 1)
   ↓
AI Planning (CoT Step 2)
   ↓
Code Generation (CoT Step 3)
   ↓
Formatting (Black / fallback)
   ↓
Output File
```
