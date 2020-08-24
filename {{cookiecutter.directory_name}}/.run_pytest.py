import os
import sys

exitCode = os.system("pytest")

if (exitCode > 1):
    exitCode = 1

sys.exit(exitCode)

