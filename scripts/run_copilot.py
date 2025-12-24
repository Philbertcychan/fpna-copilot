from data_prep import prepare_data, format_for_llm
from llm_interface import generate_summary

# Step 1: prepare data
df = prepare_data("../data/fake_fpna.csv")
data_text = format_for_llm(df)

# Step 2: build prompt
prompt = f"""
You are a financial analyst generating executive-ready insights.
Here is the monthly FP&A data:

{data_text}

Please provide a concise summary highlighting:
1. Revenue vs Budget (with key variances)
2. Expenses vs Budget (with key variances)
3. Any significant trends or risks
4. Recommendations for management

Write in a professional executive tone, suitable for directors and VPs.
"""

# Step 3: generate AI summary
summary_text = generate_summary(prompt)
print(summary_text)

# Optional: save output
with open("../outputs/fpna_ai_summary.txt", "w") as f:
    f.write(summary_text)
