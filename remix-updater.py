# remix-updater
# Remix-updater is for updating existing installations of a remix-modpack
# Place it in the modpack folder and run it, the script will take care of the rest.

# Needed functions:
# Grab latest changes from a github release, e.g. download and unpack the zip to a temporary directory
# E.g. from https://github.com/GreatestFool/ATM6-remix/releases/latest
# NOTE probably going to have to make the repo public for that to work
# Copy over the unique configs to the modpack config folder
# Either change the non-unique configs through code, or simply copy over and overwrite- that's probably easier
# Download specified modfile from project page on curseforge and move to mods folder.
# Update manifest and modlist