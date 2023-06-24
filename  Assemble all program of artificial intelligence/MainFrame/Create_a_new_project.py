import os
from Body.Speak import Say

def New_project(project_name):
    try:
        os.mkdir(f"../Project/{project_name}")
        Say(f"Successfully created the '{project_name}' project directory.")
    except FileExistsError:
        Say(f"The '{project_name}' project directory already exists.")
    except Exception as e:
        Say(f"An error occurred while creating the '{project_name}' project directory: {str(e)}")


# New_project("fgdfg")