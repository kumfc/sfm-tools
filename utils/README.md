## sfm_runtime_builtins.py
Built-in runtime objects definition for IDE highlighting. Requires return value and argument type clarification.\
Use it as follows during development stage:
```python
try:
    sfm
except NameError:
    from sfm_runtime_builtins import *
```

Also you can add this code at the end of \_\_init__.py of vs module for proper type highlighting:
```
if 1 == 0:
	import appframework
	import datamodel
	import dmeutils
	import dmxedit
	import ipc
	import materialobjects
	import materialsystem
	import mathlib
	import mdlobjects
	import misc
	import movieobjects
	import studio
	import tier1
	import tier3
```