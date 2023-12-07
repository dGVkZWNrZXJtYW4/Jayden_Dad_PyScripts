A virtual environment can give you a place to work on each project and install various python packages without messing up your main Python environment. 
You can setup a python virtual environment for this project like this:

1. Open a fresh terminal session
2. Type: python3 -m venv catfacts 
3. Type: cd catfacts/bin (cd = change directory)
4. Type: source activate (this will activate your virtual environment)
5. Copy the contents of this script to your clipboard: https://github.com/dGVkZWNrZXJtYW4/Jayden_Dad_PyTurtle/blob/main/cat_info.py
6. Inside catfacts/bin type: pbpaste > cat_info.py 
7. You need to install the requests library before running the script. Type: pip install requests
8. To run your script type: python cat_info.py
9. To deactivate any time and leave your venv just type: deactivate
10. To reactivate the venv at any time you can type this from any directory: source ~/catfacts/bin/activate
