import os

def install_requirements():
    os.system('pip install -r ' + os.path.join('requirements.txt'))

if __name__ == '__main__':
    install_requirements()