import os, platform
try:
    import requests
except:
    os.system('pip install requests')
os.system('git pull')
bit = platform.architecture()[0]
if bit == '64bit':
    import bigsec
elif bit == '32bit':
    print("\x1b[1;91mOpps Sorry Brother Your Mobile Not Support This Tools")
