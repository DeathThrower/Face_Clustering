import sys
import subprocess

# implement pip as a subprocess:
subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'numpy'])
subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'sklearn'])
subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'keras-facenet'])
subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'clusteval'])