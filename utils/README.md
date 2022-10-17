## sfm_runtime_builtins.py
\
Built-in runtime objects definition for IDE highlighting. Requires return value and argument type clarification.\
Use it as follows during development stage:
```python
try:
    sfm
except NameError:
    from sfm_runtime_builtins import *
```