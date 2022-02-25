import os
import subprocess

def changePath(path):
    if path is not None:
        try:
            os.chdir(path)
        except FileNotFoundError as e:
            print(e)


def _project(name):
    subprocess.run([f'django-admin','startproject',name],shell=True)

def _app(name,project):
    changePath(project)
    subprocess.run([f'python','manage.py','startapp',name],shell=True)