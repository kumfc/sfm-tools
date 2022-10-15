# SFM Flex Unlocker

This script removes default flex limitations [0.0, 0.1] from Source Filmmaker and allows you to make GMod-like ugly faces.

![](preview.png)

Credits: 
- **Me** for investigating rendering limitations and making the patcher
- @0TheSpy for investigating interface limitations and two-way flexes

Steam Workshop: https://steamcommunity.com/sharedfiles/filedetails/?id=2873014451

**Important - you should run this script from embedded python interpreter!\
Not compatible with Source 2 Filmmaker.**

## Installation
You can do it in two ways:
- *Execute manually every animation session*\
Put file inside /game/platform/scripts/sfm/mainmenu/ and run via program navbar
- *Execute on startup so it will never bother you again*\
Replace sfm_init.py with this file

## Usage
You can move slider in a range of 1.0 for each direction per 1 click. Release the slider and hold it again to escape the limits.\
*or*\
Double-click on the flex slider and set any value you want.

## Known issues
- Sometimes SFM stops viewport rendering few frames before fully applying new coefficients if you set exact values by double-clicking the slider. Just move a camera or something else for a second to force rendering.
- Render preview differs from the viewport, but rendered file will look as you expect. 

## TODO
- Make it possible to "Remap Slider Range"
- Offset independence (not really todo because SFM has no updates)
