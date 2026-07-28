import os
import json
import pandas as pd
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def clean_row_with_openai(dirty_data_string):
    """
    Sends a dirty row of data to OpenAI to be cleaned and formatted
    """
    prompt = f"""
    You are an expert in data cleaning assistant. I will give you a row of students mark sheet. 
    Add salutations to the student_name if not already present and capitalize the first letter of the word. 
    If any *_mark is not present, make it 0.

    Dirty Data: {dirty_data_string}
    """

    try:
        response = client.chat.completions.create(
            model='gpt-4o-mini',
            messages=[
                {"role":"system", "content":"You are precise data cleaning tool. Respond only raw JSON. Do not explain or markdown"},
                {"role":"user","content":prompt}
            ],
            response_format={"type":"json_object"}
        )
        cleaned_json = json.loads(response.choices[0].message.content)
        return cleaned_json
    except Exception as e:
        print(f"Error cleaning data {e}")
        return None

def run_etl(input_file, output_file):
    print(f"Loading {input_file}...")
    df = pd.read_csv(input_file)

    cleaned_rows = []

    print("Cleaning data with OpenAI (this might take a moment)...")
    for index, row in df.iterrows():
        dirty_string = row.to_dict()

        print(f"Processing row {index+1}/{len(df)}...")
        cleaned_data = clean_row_with_openai(dirty_string)

        if cleaned_data:
            cleaned_rows.append(cleaned_data)
        else:
            cleaned_rows.append(dirty_string)

    print(f"Saving cleaned data to {output_file}...")
    cleaned_df = pd.DataFrame(cleaned_rows)
    cleaned_df.to_csv(output_file, index=False)

    print("ETL Pipeline completed Successfully")

if __name__ == "__main__":
    INPUT_CSV = "G:/D Drive/Data/Simple 100 Student Marks.csv"
    OUTPUT_CSV = "G:/D Drive/Data/Simple 100 Student Marks_Output.csv"
    run_etl(INPUT_CSV, OUTPUT_CSV)