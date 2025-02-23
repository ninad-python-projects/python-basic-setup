# python-env-setup:
This repository can be refered to see who you should configure the Python projects.


# Create project structure by running py file
1. go to project directory after cloing on local machine.
2. run command: python project_structure.py.
3. above command will create the standard/basic folder and file strcuture fo your python project.
4. note: once used please delete the file project_structure.py to avoid any issues.


# we have created our own logger
please refer to the module project_logging to use it.
Logs will be appended to the existing log file.
note: if you dont want to use custom logger then remove all imports from main and anywhere you used it.

# Run tests
1. make sure you have pytest in requirements.txt
2. install pytest separately with command: pip install pytest
3. run tests using commnad: pytest -v tests

# Good to know:
1. what is "__init__.py" file? 
    : this file under directory will basically conver the folder into package that you can important in any .py file and use it.
2. 
