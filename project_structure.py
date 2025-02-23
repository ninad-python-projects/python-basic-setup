import os
from pathlib import Path

project_dir_name = "ninadPythonProjectStructure"

list_of_files = [
    f".github/workflow/develop.yml",
    f".github/workflow/master.yml",
    f"{project_dir_name}/src/__init__.py",
    f"{project_dir_name}/src/components/data_integration_1.py",
    f"{project_dir_name}/src/components/data_validation_2.py",
    f"{project_dir_name}/src/components/data_transformation_3.py",
    f"{project_dir_name}/src/components/model_trainer_4.py",
    f"{project_dir_name}/logging/__init_.py",
    f"{project_dir_name}/logging/project_logger.py",
    f"{project_dir_name}/exception/__init__.py",
    f"{project_dir_name}/exception/project_exception.py",
    f"{project_dir_name}/utils/__init__.py",
    f"{project_dir_name}/utils/project_utils.py",
    f"{project_dir_name}/docs/__init__.py",
    f"{project_dir_name}/docs/project_docs.py",
    f"{project_dir_name}/tests/__init__.py",
    f"{project_dir_name}/requirements.txt",
]

for path in list_of_files:
    filepath=Path(path)
    
    filedir,filename=os.path.split(path)

    if filedir != "":
        os.makedirs(filedir,exist_ok=True)

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath)==0):
        with open(filepath, "w") as f:
            pass     