import os, sys
os.environ.pop("PYSIDE_DESIGNER_PLUGINS", None)
if getattr(sys, "frozen", False):
    if hasattr(sys, "_MEIPASS"):
        os.chdir(sys._MEIPASS)  # onefile일 때
    else:
        os.chdir(os.path.dirname(sys.executable))  # onedir일 때
