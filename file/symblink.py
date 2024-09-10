import os
from os import path


def main():
    # setup utils folder
    source = 'E:\\Dropbox\\Dev\\Repo\\pod_projects\\utils'
    project = 'pod_organize'
    destination = f"E:\\Dropbox\\Dev\\Repo\\pod_projects\\{project}\\utils"
    create_symb_link(source, destination)

    # setup db folder
    source = 'E:\\Dropbox\\Dev\\Repo\\pod_projects\\db'
    project = 'pod_organize'
    destination = f"E:\\Dropbox\\Dev\\Repo\\pod_projects\\{project}\\db"
    create_symb_link(source, destination)



def create_symb_link(source, dest):
    if path.exists(source) and path.isdir(source):
        if not path.exists(dest):
            os.symlink(source, dest)
        else:
            print(f"Dest Dir is bad: {dest}")
    else:
        print(f"Source Dir is bad: {source}")

    
if __name__ == "__main__":
    main()
