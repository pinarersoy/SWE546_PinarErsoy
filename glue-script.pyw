#!C:/Users/pinar/Anaconda3\pythonw.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'glueviz==0.9.1','gui_scripts','glue'
__requires__ = 'glueviz==0.9.1'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('glueviz==0.9.1', 'gui_scripts', 'glue')()
    )
