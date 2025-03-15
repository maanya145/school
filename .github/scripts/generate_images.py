import os
import time
import base64
import urllib.parse
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

# Directories
CODE_DIR = "code_snippets"
OUTPUT_DIR = "generated_images"

# Ensure output directory exists
if not os.path.exists(OUTPUT_DIR):
    os.makedirs(OUTPUT_DIR)

# Set up Chrome options for GitHub Actions
chrome_options = Options()
chrome_options.add_argument("--headless")  # No GUI
chrome_options.add_argument("--no-sandbox")  # Required for GitHub Actions
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--window-size=1920,1080")

# Configure Chrome to automatically download PNG files
prefs = {
    "download.default_directory": os.path.abspath(OUTPUT_DIR),  # Download PNGs to `generated_images/`
    "download.prompt_for_download": False,  # No download prompt
    "download.directory_upgrade": True,
    "safebrowsing.enabled": True  # Allow safe downloads
}
chrome_options.add_experimental_option("prefs", prefs)

# Set up WebDriver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

# Function to encode code snippet for Ray.so URL
def encode_code_for_ray(code):
    base64_code = base64.b64encode(code.encode()).decode()
    return urllib.parse.quote(base64_code)

# Process each Python file in `code_snippets/`
for filename in os.listdir(CODE_DIR):
    if filename.endswith(".py"):
        file_path = os.path.join(CODE_DIR, filename)

        # Read the code from the file
        with open(file_path, "r", encoding="utf-8") as f:
            code_content = f.read()

        # Generate the Ray.so URL
        encoded_code = encode_code_for_ray(code_content)
        url = f"https://ray.so/#padding=64&theme=vercel&code={encoded_code}&language=python"

        # Open Ray.so and trigger the image generation
        driver.get(url)
        time.sleep(3)  # Allow time for page to load
        driver.find_element(By.XPATH, "(.//*[normalize-space(text()) and normalize-space(.)='Format Code'])[1]/following::span[2]").click()

        # Wait for the file to be downloaded
        time.sleep(5)  # Adjust as needed

        # Find the downloaded PNG file
        downloaded_files = [f for f in os.listdir(OUTPUT_DIR) if f.endswith(".png")]
        if downloaded_files:
            old_path = os.path.join(OUTPUT_DIR, downloaded_files[0])  # Get first downloaded file
            new_path = os.path.join(OUTPUT_DIR, filename.replace(".py", ".png"))  # Rename it
            os.rename(old_path, new_path)
            print(f"Saved image: {new_path}")
        else:
            print(f"Download failed for {filename}")

# Close the browser
driver.quit()
