import os
import openai
from openai import OpenAI
import subprocess

print("📢 Script Started...")

# Initialize OpenAI client
client = OpenAI(base_url="https://api.groq.com/openai/v1", api_key=os.environ.get("OPENAI_API_KEY"))

# Get modified or newly added files in the OTHER directory
try:
    git_command = "git diff --name-only --diff-filter=AM HEAD^ HEAD"
    modified_files = subprocess.check_output(git_command, shell=True, text=True).splitlines()
except subprocess.CalledProcessError as e:
    print(f"❌ Git error: {e}")
    exit(1)

modified_files = [f for f in modified_files if f.startswith("OTHER/")]

if not modified_files:
    print("✅ No modified files found in 'OTHER/'. Exiting...")
    exit(0)

def generate_filename(file_path):
    """Use OpenAI to generate a meaningful name based on the file type and content."""
    file_extension = os.path.splitext(file_path)[1].lower()

    # Try to extract readable content
    try:
        if file_extension in [".txt", ".md", ".json", ".csv"]:
            with open(file_path, "r", encoding="utf-8") as f:
                content = f.read(500)  # Read first 500 characters
        else:
            content = f"[{file_extension.upper()} file] (binary content not readable)"
    except Exception as e:
        print(f"⚠️ Error reading {file_path}: {e}")
        content = "[Unreadable content]"

    prompt = f"""
    Here is a file from a project directory. It contains the following content:
    
    ```
    {content}
    ```

    Suggest a **concise and meaningful name** that describes the file's content **without the extension**.
    
    Only return the suggested name **without any additional text**.
    """

    try:
        response = client.chat.completions.create(
            model="llama-3.3-70b-specdec",
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        print(f"⚠️ OpenAI API error: {e}")
        return None

def get_unique_filename(directory, base_name, extension):
    """Ensure the filename is unique by appending a number if necessary."""
    new_name = f"{base_name}{extension}"
    counter = 1

    while os.path.exists(os.path.join(directory, new_name)):
        new_name = f"{base_name}_{counter}{extension}"
        counter += 1

    return new_name

for file in modified_files:
    if not os.path.isfile(file):
        print(f"⏭️ Skipping {file} (not a regular file)")
        continue

    directory, old_filename = os.path.split(file)
    old_name, extension = os.path.splitext(old_filename)

    # Get AI-generated name
    new_base_name = generate_filename(file)
    if not new_base_name:
        print(f"⏭️ Skipping {file} (AI name generation failed)")
        continue

    # Generate a unique filename
    new_filename = get_unique_filename(directory, new_base_name, extension)

    # Skip renaming if the new name is the same
    if new_filename == old_filename:
        print(f"✅ {file} already has a meaningful name. Skipping...")
        continue

    # Rename the file
    new_path = os.path.join(directory, new_filename)
    os.rename(file, new_path)
    print(f"📝 Renamed {file} -> {new_path}")

print("🎉 Renaming process completed successfully!")
