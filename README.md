# websitescreenshotscript
Python Script to screenshot a list of Web Pages from a text file. This script was written to be run on windows 10. Other operating systems may also work doing some modifications.

screenshooter is a simple Python script that lets you make screenshots given a list of urls. These are being saved as .png inside the folder named "screenshots".

This script makes use of the selenium web driver. <b>In order to run it, you must download an appropriate chromedriver for your system and version of Chrome and copy it into the directory of this script!</b>

input.txt is the file where you place the complete urls (includig protocol, e.g. https://... or http://...).

usage:
needs Python3 to be installed

simply run:
python shooter.py

Use is at your own risk.

I wrote this script for visual reconnaissance while doing bug bounties. Since I run ubuntu on a windows subsystem for linux I needed a solution having no problems with headless drivers etc.
