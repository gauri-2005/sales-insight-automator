import os
import pandas as pd
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=api_key)

def generate_summary(df, chunk_size=50):
    # Free tier ke liye chhote chunks
    chunks = [df[i:i+chunk_size] for i in range(0, len(df), chunk_size)]
    all_insights = []

    model = genai.GenerativeModel("models/gemini-2.5-flash-lite")  # Free tier friendly

    for idx, chunk in enumerate(chunks):
        data_text = chunk.to_string()
        prompt = f"Analyze this sales data and give business insights.\n\n{data_text}"
        response = model.generate_content(prompt)
        all_insights.append(response.text)

    # Combine all insights
    final_summary = "\n\n".join(all_insights)
    return final_summary

# Example usage
# df = pd.read_csv("sales_data.csv")
# print(generate_summary(df))