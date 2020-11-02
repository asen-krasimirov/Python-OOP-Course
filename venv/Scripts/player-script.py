#!C:\Users\Game\Desktop\Python-OOP\venv\Scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'player==0.6.1','console_scripts','player'
__requires__ = 'player==0.6.1'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('player==0.6.1', 'console_scripts', 'player')()
    )
