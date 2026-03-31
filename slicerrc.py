import os
import sys
from glob import glob
from pathlib import Path
import numpy as np

# Hot keys
restart_hotkey = "Ctrl+Shift+R" # Restart 3D Slicer
rectum_seg_hotkey = "Ctrl+Shift+A" # Run rectum segmentation
toggle_select_hotkey = "T" # Toggle select segment and its visibility
review_segment_hotkey = "Ctrl+Shift+Q"
export_hotkey = "Ctrl+Shift+S"

# Restart
shortcut = qt.QShortcut(qt.QKeySequence(restart_hotkey), slicer.util.mainWindow())
shortcut.connect('activated()', slicer.util.restart)

anatomy = 'rectum'

reviewDir = input('Path to segmentation folder: ')

hot_key = "Ctrl+Shift+Q"

print(f'Press {hot_key} to continue')

rootDir = '/home/promaxo/Downloads/Slicer-5.4.0-linux-amd64/'
sys.path.append(os.path.abspath(rootDir))


# Rectum segmentation review

# from prostate_seg import edit_prostate_segmentation
from rectum_seg import edit_rectum_segmentation
# from brain_seg import edit_brain_segmentation
func = eval(f'edit_{anatomy}_segmentation')

shortcut3 = qt.QShortcut(qt.QKeySequence(review_segment_hotkey), slicer.util.mainWindow())
shortcut3.connect('activated()', lambda: func(reviewDir))

# Toggle select segment and its visibility
from utils import toggleSelectSegment
shortcut2 = qt.QShortcut(qt.QKeySequence(toggle_select_hotkey), slicer.util.mainWindow())
shortcut2.connect('activated()', lambda: toggleSelectSegment())


# Toggle select segment and its visibility
from utils import exportLabelmap
shortcut4 = qt.QShortcut(qt.QKeySequence(export_hotkey), slicer.util.mainWindow())
shortcut4.connect('activated()', lambda: exportLabelmap(expDir))

# Set maximum panel size, prevent autoscaling panel too big with long filename
mainWindow = slicer.util.mainWindow()
modulePanelDockWidget = mainWindow.findChildren('QDockWidget','PanelDockWidget')[0]
modulePanelDockWidget.setMaximumWidth(700)
modulePanelDockWidget.setMinimumWidth(0)

# Note to install new python package: pip.main(['install', 'scipy'])