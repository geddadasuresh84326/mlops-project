import os
from pathlib import Path

list_of_files = [
    ".github/workflows/.gitkeep",
    "src/__init__.py",
    "src/components/__init__.py",
    "src/components/data_ingestion.py",
    "src/components/data_transformation.py",
    "src/components/model_trainer.py",
    "src/components/model_evaluation.py",
    "src/pipeline/__init__.py",
    "src/pipeline/training_pipeline.py",
    "src/pipeline/prediction_pipeline.py",
    "src/utils/__init__.py",
    "src/utils/utils.py",
    "src/logging.py",
    "src/exception.py",
    "tests/unit/__init__.py",
    "tests/integration/__init__.py",
    "init_setup.sh",
    "requirements.txt",
    "requirements_dev.txt",
    'setup.py',
    "setup.config",
    "pyproject.toml",
    "tox.ini",
    "experiment/experiments.ipynb"
]

for file_path in list_of_files:
    file_path = Path(file_path)
    filedir,filename = os.path.split(file_path)
    if filedir != "":
        os.makedirs(filedir,exist_ok=True)
        # logging.info(f"Creating directory:{filedir} for file: {filename}")

    if (not os.path.exists(file_path)) or (os.path.getsize(file_path)==0):
            with open(file_path,'w') as f:
                 pass
