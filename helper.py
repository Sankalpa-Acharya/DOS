import os
import subprocess




def base_temp():
    os.mkdir('templates')
    with open('templates/base.html','w') as f:
        pass



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
    base_temp()
    subprocess.run([f'python','manage.py','startapp',name],shell=True)




