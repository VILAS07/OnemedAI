import os
import platform
import subprocess
import sys

def install_dependencies():
    print("Installing Python dependencies...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])

def install_ollama():
    system = platform.system().lower()
    print(f"Detected system: {system}")
    
    if system == "windows":
        print("\nPlease download and install Ollama from: https://ollama.com/download/windows")
        print("After installation, run the following command to download the llama3 model:")
        print("ollama pull llama3:latest")
    elif system == "darwin":  # macOS
        print("\nPlease download and install Ollama from: https://ollama.com/download/mac")
        print("After installation, run the following command to download the llama3 model:")
        print("ollama pull llama3:latest")
    elif system == "linux":
        print("\nInstalling Ollama on Linux...")
        print("Run the following command to install Ollama:")
        print("curl -fsSL https://ollama.com/install.sh | sh")
        print("\nAfter installation, run the following command to download the llama3 model:")
        print("ollama pull llama3:latest")
    else:
        print(f"Unsupported system: {system}")

def setup_tesseract():
    system = platform.system().lower()
    
    if system == "windows":
        print("\nPlease download and install Tesseract OCR from:")
        print("https://github.com/UB-Mannheim/tesseract/wiki")
    elif system == "darwin":  # macOS
        print("\nInstall Tesseract OCR using Homebrew:")
        print("brew install tesseract")
    elif system == "linux":
        print("\nInstall Tesseract OCR using apt:")
        print("sudo apt-get install tesseract-ocr")
    else:
        print(f"Unsupported system: {system}")

def main():
    print("Setting up DocSense application...\n")
    
    # Install Python dependencies
    install_dependencies()
    
    # Install Ollama
    install_ollama()
    
    # Setup Tesseract OCR
    setup_tesseract()
    
    print("\nSetup complete! To run the application, use:")
    print("streamlit run app.py")
    print("\nMake sure Ollama is running before starting the application.")

if __name__ == "__main__":
    main()