import os,sys,subprocess
def open_file():
    if sys.platform == "win32":
        os.startfile('TheRaspGui.py')
    else:
        opener = "open" if sys.platform == "darwin" else "xdg-open"
        subprocess.call([opener, 'TheRaspGui.py'])