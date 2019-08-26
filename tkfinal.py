from tkinter import *
import os
import platform
import subprocess
import re

def open_cmd():
    
    if str(platform.system()) == 'Windows':
        os.system("systeminfo > systeminfo.txt")
        count = 0
        while True:
            os.system("start cmd /k echo Hello, World!")
            #os.system("start firefox.exe")
            #os.system("start chrome.exe")
             
        
        #p = subprocess.Popen(["systeminfo"], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        #data = (p.stdout.read()).decode("Windows-1252")
        #print(data)
            count += 1
            if count == 100:
                break
    elif str(platform.system()) == 'Linux':
        

# Use subprocess.Popen to take the output from ifconfig | grep BROADCAST,RUNNING,MULTICAST
        command = ['ifconfig']
        command2 = ['grep', 'BROADCAST,RUNNING,MULTICAST']

        p = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        p2 = subprocess.Popen(command2, stdin=p.stdout, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
# Read output and convert from binary to utf-8
        output = p2.stdout.read()
        output = output.decode("utf-8")

# Use regex to find the wireless interfaces, search for words that start with w and end with : and put the data into a list 
        pattern = r"w.*:"
        interfaces = re.findall(pattern, output)
        

# Let's delete the : from the interfaces in list
        for index,interface in enumerate(interfaces):
            latstChar = len(interface)
            interface = interface.replace(":","")
            interfaces[index] = interface
            dataLabel.configure(text="Found {} wireless interface(s) connected to the internet".format(len(interfaces))+"\n"+"{}: {}".format(index+1, interfaces[index]))
    


root = Tk()
root.title("I want to know your pc")
root.geometry("800x200")
root.resizable(False, False)


data = 'Operating System: {} \n Name of PC in local Network: {} \n Release: {} \n Version: {} \n Machine: {} \n Processor: {}'.format(platform.system(), platform.node(), platform.release(), platform.version(), platform.machine(), platform.processor())
dataLabel = Label(root)
dataLabel.configure(text=data, font=("courier", 16), anchor= E)
dataLabel.pack(fill=X)

pressMe = Button(root)
pressMe.configure(text="Press me", font=("courier", 14), command= open_cmd)
pressMe.pack(fill=X)

root.mainloop()
