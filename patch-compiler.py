# General layout idea:
# The ATM6 modpack itself is in a folder called 'modpack'
# The patches is in 'remix-patch'
#
# What the script needs to do:
# Copy the 'modpack' directory content
# Paste it into a temporary .dot-dir, perhaps '.processing'?
# Copy contents of 'remix-patch' and paste in '.processing'
## NOTE for content that require editing of a file, e.g. configs, have a special function to edit them
# Once copied and patched, update pack data and then package to a .zip file and place in '.exports'
# Once exported, delete '.processing'

import shutil
import zipfile
import os

# If '.processing' does not exist, it creates the folder
# If '.processing' exists, it deletes the folder... I don't remember why I added that last part
if not os.path.exists('.processing'):
    os.makedirs('.processing')
else:
    shutil.rmtree('.processing')

# Extract modpack zip file to '.processing'
# TODO currently hardcoded, fix later
with zipfile.ZipFile('.imports/All+the+Mods+6-1.6.4.zip', 'r') as zip_ref:
    zip_ref.extractall('.processing/')

# Copy mod addition configs to '.processing/overrides/config/'
shutil.copytree('.remix-patch/config', '.processing/overrides/config', symlinks=False, ignore=shutil.ignore_patterns('.ignore'), dirs_exist_ok=True)

# TODO Modify configuration files for already existing files using hardcoded values
# TODO Modify manifest.json and modlist.toml

# Package '.processing' into a zip file
# TODO Make the export name variable
shutil.make_archive('.exports/test', 'zip', '.processing')

# Deletes '.processing'
shutil.rmtree('.processing')