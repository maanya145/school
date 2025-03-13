print("Script Started...")
import os
import openai
from openai import OpenAI
import json
import glob

# Initialize OpenAI client
client = OpenAI(base_url="https://api.groq.com/openai/v1", api_key=os.environ.get("OPENAI_API_KEY"))

# Get all Python files inside 'scripts/'
modified_files = glob.glob("scripts/**/*.py", recursive=True)

if not modified_files:
    print("No Python files found in 'scripts/'. Exiting...")
    exit(0)

# Directory to store AI-generated outputs
OUTPUT_DIR = "output"
os.makedirs(OUTPUT_DIR, exist_ok=True)


def get_script_output(code):
    """Use OpenAI to analyze code and generate the expected output."""
    prompt = f"""
    Analyze the following Python script and predict its expected output **without running it**.
    
    ```
    {code}
    ```

    Only respond with the exact output **as if it were printed by Python**.
    - Do not include any explanations, formatting, or additional text.
    - If the script requires user input, assume reasonable values.
    """
    response = client.chat.completions.create(
        model="llama-3.3-70b-specdec",  # Your preferred model
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content.strip()


for file in modified_files:
    with open(file, "r") as f:
        code = f.read()

    # Get AI-predicted output
    predicted_output = get_script_output(code)

    # Save output
    output_file = os.path.join(OUTPUT_DIR, f"{os.path.basename(file)}.txt")
    with open(output_file, "w") as f:
        f.write(predicted_output)

    print(f"Generated AI output for {file} -> {output_file}")
