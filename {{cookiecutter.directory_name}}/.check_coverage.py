import os
import sys

os.system("coverage run -m pytest")
errCode = os.system("coverage report -m --fail-under=75")
print(errCode)
if errCode > 1:
    errCode = 1
sys.exit(errCode)
