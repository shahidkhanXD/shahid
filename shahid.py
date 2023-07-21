import os, platform, time, sys
 
try:
 
    import requests
 
except:
 
    os.system('pip install requests')
 
os.system('git pull --quiet 2>/dev/null')
 
bit = platform.architecture()[0]
 
if bit == '64bit':
    from shahid import menu
 
    menu()