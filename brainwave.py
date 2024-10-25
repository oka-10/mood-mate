import subprocess
import sys

def install_huggingface():
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "transformers"])
        print("Hugging Face Transformers library installed successfully.")
    except subprocess.CalledProcessError:
        print("Failed to install Hugging Face Transformers library.")
        sys.exit(1)

# Install Hugging Face Transformers library
install_huggingface()
