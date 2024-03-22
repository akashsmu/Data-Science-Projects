import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

project_name = "textSummarizer"
list_files = [
    "ML/NLP/.github/workflows/.gitkeep",
    f"ML/NLP/src/{project_name}/__init__.py",
    f"ML/NLP/src/{project_name}/components/__init__.py",
    f"ML/NLP/src/{project_name}/utils/__init__.py",
    f"ML/NLP/src/{project_name}/utils/common.py",
    f"ML/NLP/src/{project_name}/logging/__init__.py",
    f"ML/NLP/src/{project_name}/config/__init__.py",
    f"ML/NLP/src/{project_name}/config/configuration.py",
    f"ML/NLP/src/{project_name}/pipeline/__init__.py",
    f"ML/NLP/src/{project_name}/entity/__init__.py",
    f"ML/NLP/src/{project_name}/constants/__init__.py",
    "ML/NLP/config/config.yaml",
    "ML/NLP/params.yaml",
    'ML/NLP/app.yaml',
    "ML/NLP/main.py",
    "ML/NLP/Dockerfile",
    "ML/NLP/requirements.txt",
    'ML/NLP/setup.py',
    "ML/NLP/research/trials.ipynb",
]

for filepath in list_files:
    file = Path(filepath)
    filedir, filename = os.path.split(file)
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory: {filedir} for the file: {filename}")

    if (not os.path.exists(file)) or (os.path.getsize(file) == 0):
        with open(file, "w") as f:
            pass
            logging.info(f"Creating file: {file} for the file: {filename}")
    else:
        logging.info(f"Skipping file: {file} for the file: {filename}")
    
