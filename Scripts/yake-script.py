#!c:\progettipython\plagiarismdetection\plagiarism\scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'yake==0.4.8','console_scripts','yake'
__requires__ = 'yake==0.4.8'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('yake==0.4.8', 'console_scripts', 'yake')()
    )