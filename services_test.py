# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import os

class system:
    def __init__(self, name, vhdx):
        self.name = name
        self.vhdx = vhdx
        self.services = []
        self.drive_used = ""
        
    def mount_vhdx():
        os.system('powershell.exe Mount-DiskImage -ImagePath '+self.vhdx)
        
        #mount vhdx to system
    def umount_vhdx():
        os.system('powershell.exe Dismount-DiskImage -ImagePath '+self.vhdx)
        
    def services_get(self):
        reg_location = 'D:\C\windows\system32\config\SYSTEM.reg'
        os.system('reg load HKLM\Meme '+reg_location)
        test = os.popen('reg query HKLM\Meme\CurrentControlSet\Services /se #').read()
        service_quest=[]
        gnarly = test.split("\n")
        for i in gnarly:
            new_i = i.split("\\")
            if new_i[-1] != "":
                number = 1
                if new_i[-1] in self.services:
                    new_number = self.services.get(new_i[-1])
                    number = int(new_number) + 1
                self.services.append({new_i[-1]: number})
        os.system('reg unload HKLM\Meme')
    

def find_system(workingD):
    Files =[]
    os.chdir(workingD)
    for root, dirs, files in os.walk(workingD, topdown = True):
        for name in files:
            filepath = os.path.join(root, name)
            if name[-5:] == ".vhdx":
                system_name = filepath.split("\\")[-2][-15:]
                Files.append({"system_name": system_name, "file_path": filepath})
    return Files
	

Hostname = os.popen('hostname').read()  #find hostname

CurrentWorkingSet = system(Hostname)    #name system class after homename

CurrentWorkingSet.services_get()    #Get services of current system

#print(CurrentWorkingSet.services)


#for i in CurrentWorkingSet.services:
#    if i.get('gupdate') == True:
#        print(i.get('gupdate'))


for i in find_system("C:\\Users\\Phillippe\\Desktop\\Test"):    #enter Kape collection location
    Hostname = i['system_name']
    Vhdx = i['file_path']
    CurrentWorkingSet = system(Hostname, Vhdx)
    print(CurrentWorkingSet.name)

#Capture on multiple Kape's then -> mount and parse kape vhdx
#get hostname and registry file
#add to class data structure