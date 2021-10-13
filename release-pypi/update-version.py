import os
import re
import sys

# ensure version is passed to continue
try:
    path = sys.argv[1]
    version = sys.argv[2]
except IndexError as error:
    raise ValueError("Script requires positional argument 'project_path' and 'version'")

SETUP_PATH = os.path.join(path, 'setup.py')

# open setup.py
with open(SETUP_PATH) as setupfile:
    content = setupfile.read()

# update version in setup content
updated_content = re.sub(
    r'version\s*=\s*"([^"]+)"',
    f'version="{version}"',
    content
)

# overwrite setup.py
with open(SETUP_PATH, 'w') as setupfile:
    setupfile.write(updated_content)
