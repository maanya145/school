print("Script Started...")
import os
import openai
from openai import OpenAI

client = OpenAI(base_url="https://api.groq.com/openai/v1", api_key=os.environ.get("OPENAI_API_KEY"))
import subprocess
import json
import glob

# Get all Python files inside 'scripts/'
modified_files = glob.glob("scripts/**/*.py", recursive=True)

if not modified_files:
    print("No Python files found in 'scripts/'. Exiting...")
    exit(0)
# Set API key


# TODO: The 'openai.api_base' option isn't read in the client API. You will need to pass it when you instantiate the client, e.g. 'OpenAI(base_url="https://api.groq.com/openai/v1")'
# openai.api_base = "https://api.groq.com/openai/v1"

# Directory to store outputs
OUTPUT_DIR = "output"
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Get modified Python files
# Get modified Python files inside 'scripts/' only


def get_test_input(code):
    """Use OpenAI to analyze code and generate appropriate input."""
    prompt = f"""
    Analyze the following Python script and provide user inputs that are most relevant to its functionality.
    
    ```
    {code}
    ```
    
    Respond with a JSON array of inputs, like: ["42", "hello", "10 20"]
    """
    response = client.chat.completions.create(model="mixtral-8x7b-32768",
    messages=[{"role": "user", "content": prompt}])
    print(response)
    try:
        inputs = json.loads(response.choices[0].message.content)
        print(input)
        return inputs if isinstance(inputs, list) else []
    except json.JSONDecodeError:
        return []

for file in modified_files:
    with open(file, "r") as f:
        code = f.read()

    # Get test inputs
    test_inputs = get_test_input(code)

    # Run the script with simulated inputs
    process = subprocess.run(
        ["python3", file],
        input="\n".join(test_inputs),
        text=True,
        capture_output=True
    )

    # Save output
    output_file = os.path.join(OUTPUT_DIR, f"{os.path.basename(file)}.txt")
    with open(output_file, "w") as f:
        f.write(process.stdout + "\n" + process.stderr)

    print(f"Generated output for {file} -> {output_file}")
