# 🧠 Excel Column Description Generator using LM Studio API

This Python script automates the generation of one-line descriptions for columns in an Excel sheet by leveraging a locally hosted **LM Studio** (Large Language Model) API. It is designed to improve data documentation and metadata quality, especially in large data systems.

---

## 📋 Features

- ✅ Reads table and column names from an Excel sheet
- ✅ Sends prompts to a local LM Studio API
- ✅ Receives AI-generated descriptions for each column
- ✅ Automatically writes back the updated descriptions to a new Excel file

---

## 🛠️ Requirements

- Python 3.7+
- LM Studio running locally (API endpoint)
- Dependencies (install using the command below)

```bash
pip install -r requirements.txt
