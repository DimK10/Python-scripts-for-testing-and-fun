import os
for root, dirs, files in os.walk('C:\WINDOWS\system32'):
    for name in files:
            print(os.path.join(root, name))
    for name in dirs:
            print(os.path.join(root, name))
