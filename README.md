# MvC2_MusicHandler
 Python app with tkinter GUI library to help rename ADX files for MvC2
## Requirements  
 Requires the following python libraries:  
```Py
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import os
import shutil
```
## ADXs  
 App assumes you already have music converted to ADX (.adx), put them in ADXs folder and they should appear as an option in dropdowns.

## Playlists  
 Offers 4 options of playlists: `2 Track, 4 Track, 8 Track, and 32 Shuffle`  
 Select a playlist then select a stage. Choose a ADX for your track listing and save.  
 It will output a .txt in the `Playlists` folder for the respective playlist you are saving.  

## Exporting  
 Will copy and rename .adx file to appropriate filename for selected playlist.  
 The newly created file will be in `Output` folder and a subfolder for playlist.  
 Example: `Output\2Track\ADX1S000.BIN`
