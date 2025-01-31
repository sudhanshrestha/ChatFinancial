import subprocess
import sys

# List of required libraries for the project
required_libraries = [
    'python-dotenv',
    'openpyxl',
    'protobuf==3.19.4',
    'numpy==1.24.2',
    'plotly',
    'nbformat',
    'pandas',        
    'numpy',         
    'scikit-learn',  
    'matplotlib',     
    'seaborn',          
    'joblib',
    'ollama',
    'langchain',
    # 'chromadb',
    'langchain-community',
    'streamlit',
    'ipywidgets',
    # 'google-generativeai'     
]

# installs the required libraries if they are not already installed
for library in required_libraries:
    try:
        __import__(library)
    except ImportError:
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', library])

# runs the Ollama model after installing the necessary packages
def run_ollama_model():
    command = "ollama run deepseek-r1:1.5b"
    
    try:
        process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = process.communicate()

        if stdout:
            print(stdout.decode())  # Print the standard output of the model
        if stderr:
            print(stderr.decode())  # Print any error messages
    except Exception as e:
        print(f"An error occurred while running Ollama: {e}")

# Execute the Ollama model
run_ollama_model()
