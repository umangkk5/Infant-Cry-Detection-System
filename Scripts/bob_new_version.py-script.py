#!c:\python27\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'bob.extension==2.2.1','console_scripts','bob_new_version.py'
__requires__ = 'bob.extension==2.2.1'
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.exit(
        load_entry_point('bob.extension==2.2.1', 'console_scripts', 'bob_new_version.py')()
    )
