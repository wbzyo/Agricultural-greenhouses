#!E:\new\bigpeng\venv\Scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'PyInstaller==3.5','console_scripts','pyi-set_version'
__requires__ = 'PyInstaller==3.5'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('PyInstaller==3.5', 'console_scripts', 'pyi-set_version')()
    )
