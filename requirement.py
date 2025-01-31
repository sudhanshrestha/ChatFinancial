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