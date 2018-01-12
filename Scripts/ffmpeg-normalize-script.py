#!c:\python27\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'ffmpeg-normalize==0.2.4','console_scripts','ffmpeg-normalize'
__requires__ = 'ffmpeg-normalize==0.2.4'
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.exit(
        load_entry_point('ffmpeg-normalize==0.2.4', 'console_scripts', 'ffmpeg-normalize')()
    )
