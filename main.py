import argparse
import threading
from helper import _project,_app,changePath 


def args_maker():
    parser=argparse.ArgumentParser()
    parser.add_argument('-p',type=str,default=None,help="add app name")
    parser.add_argument('-a',type=str,default=None,help="add project name")
    parser.add_argument('-f',type=str,default=None,help="add file path where you want your work to be done")
    parser.add_argument('-bt',type=str,default=None,help="add base template folder")
    parser.add_argument('-at',type=str,default=None,help="add add template folder")
    args=parser.parse_args()
   
   #adding values 
    project_name=args.p 
    app_name=args.a
    path=args.f
    main(project_name,app_name,path)


def main(project,app,path):
    if path is not None:
        changePath(path)
        return
    if project is None:
        raise Exception('ProjectName cannot be empty')
    else:    
        if app is None:
            _project(project)
        else:
            _project(project)
            _app(app,project)


if __name__=='__main__':
    args_maker()

