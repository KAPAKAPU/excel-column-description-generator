import pandas as pd
import requests
import os

# Load environment variables or fallback to default
API_URL = os.getenv("LM_API_URL", "http://localhost:1234/v1/chat/completions")
MODEL_NAME = os.getenv("LM_MODEL_NAME", "mistral-7b-instruct-v0.3")

# Path to Excel file (change if needed)
excel_path = "table_metadata.xlsx"

# Read Excel
df = pd.read_excel(excel_path)

# Ensure Description column is string type
df["Description"] = df["Description"].astype(str)

# Loop through rows and generate descriptions
for idx, row in df.iterrows():
    table_name = row.get("Table Name", "")
    column_name = row.get("Column Name", "")
    
    if not table_name or not column_name:
        print(f"Skipping row {idx}: missing table or column name")
        continue

    prompt = f"Generate a one-line description for the column '{column_name}' in table '{table_name}'."

    payload = {
        "model": MODEL_NAME,
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0.7,
        "max_tokens": 50
    }

    try:
        response = requests.post(API_URL, json=payload)
        response.raise_for_status()
        data = response.json()
        description = data["choices"][0]["message"]["content"].strip()
    except Exception as e:
        print(f"Error for row {idx}: {e}")
        description = "ERROR"

    df.at[idx, "Description"] = description

# Save updated Excel
output_path = "updated_table_metadata.xlsx"
df.to_excel(output_path, index=False)
print(f"✅ Descriptions updated and saved to {output_path}")
