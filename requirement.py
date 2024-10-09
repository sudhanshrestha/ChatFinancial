# requirements.py
import subprocess
import sys

# List of required libraries for the project
required_libraries = [
    'openpyxl',
    'pandas',        
    'numpy',         
    'scikit-learn',  
    'matplotlib',     
    'seaborn',          
    'joblib'         
]

for library in required_libraries:
    try:
        __import__(library)
    except ImportError:
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', library])