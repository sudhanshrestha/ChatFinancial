# requirements.py
import subprocess
import sys

# List of required libraries for the project
required_libraries = [
    'python-dotenv',
    'openpyxl',
    'protobuf==3.19.4',
    'numpy == 1.24.2',
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
    'chromadb',
    'langchain-community',
    # 'tensorflow ==2.10.0',
    # 'torch',
    # 'keras',
    # 'transformers',
    # 'accelerate>=0.26.0'   
    'ipywidgets',
    # 'google-generativeai'     
]

for library in required_libraries:
    try:
        __import__(library)
    except ImportError:
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', library])