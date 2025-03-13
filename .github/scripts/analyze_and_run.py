print("Script Started...")
import os
import openai
import subprocess
import json

# Set API key

openai = openai.OpenAI(
    base_url="https://api.groq.com/openai/v1",
    api_key=os.environ.get("OPENAI_API_KEY")
)

# Directory to store outputs
OUTPUT_DIR = "output"
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Get modified Python files
# Get modified Python files inside 'scripts/' only
result = subprocess.run(
    ["git", "diff", "--name-only", "HEAD~1", "--", "scripts/"],
    capture_output=True,
    text=True
)
modified_files = [f.strip() for f in result.stdout.split("\n") if f.endswith(".py") and f.startswith("scripts/")]

def get_test_input(code):
    """Use OpenAI to analyze code and generate appropriate input."""
    prompt = f"""
    Analyze the following Python script and provide user inputs that are most relevant to its functionality.
    
    ```
    {code}
    ```
    
    Respond with a JSON array of inputs, like: ["42", "hello", "10 20"]
    """
    response = openai.ChatCompletion.create(
        model="mixtral-8x7b-32768",
        messages=[{"role": "user", "content": prompt}]
    )
    try:
        inputs = json.loads(response["choices"][0]["message"]["content"])
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
