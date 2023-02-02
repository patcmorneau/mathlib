# mathlib

mathlib is wrapping some powerful librairies into simple function that take pure python class as input


### unittest
```
python unittest/test_lib.py
```

### How to add mathlib to your github project
```
pip install -r requirements.txt
```
in the root of your project repo
```
git submodule add https://github.com/patcmorneau/mathlib.git
```
then add these line to your python file to import the module
```
import os, sys
mathlibDir = os.path.abspath(os.path.join(os.path.dirname(__file__), "mathlib"))
sys.path.append(mathlibDir)
from mathlib import mathlib
```
