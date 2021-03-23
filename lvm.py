import os
import getpass
os.system("tput setaf 7")
print("..................................Hola User..................................")
os.system("tput setaf 12")
def PVCREATE():
    disk=input("Enter the Disk name")
    os.system('pvcreate {}'.format(disk))
def PVDISPLAY():
    disk=input("Enter disk name which you want to see")
    os.system('pvdisplay {}'.format(disk))
def VGCREATE():
    name=input("enter the name of vg")
    disk=input("enter the name of disk and if more thn 1 disk thn use space between names")
    os.system('vgcreate {} {}'.format(name,disk))
def VGDISPLAY():
    name=input("Enter the name of VG: ")
    os.system('vgdisplay {}'.format(name))
def LVCREATE():
    name=input("Enter the name of LV")
    size=int(input("Enter the size of LV"))
    vgn=input("Enter the name of VG")
    os.system('lvcreate --size {}G --name {} {}'.format(size,name,vgn))
def LVDISPLAY():
    name=input("Enter the name of LV")
    os.system('lvdisplay {}'.format(name))
def FORMAT():
    exe=input("Enter the extension")
    name=input("Enter the LV name")
    os.system('mkfs.{} {}'.format(exe,name))
def MOUNT():
    name=input("Enter the LV name")
    loc=input("Enter the location")
    os.system('mount {} {}'.format(name,loc))
def UNMOUNT():
    name=input("Enter the disk to unmount")
    os.system('umount {}'.format(name))
def EXTEND():
    size=input("Enter the size to extend")
    name=input("Enter the name of LV")
    os.system('lvextend --size +{}G {}'.format(size,name))
def RESIZE():
    name=input("Enter the LV name")
    os.system('resize2fs {}'.format(name))
def REDUCE():
    name=input("Enter the LV name")
    size=input("Enter the size to reduce")
    os.system('lvreduce -L {}G {}'.format(size,name))
def LVM():
    i=0
    number=int(input("Enter the number of disks"))
    for i in range(number):
        PVCREATE()
        PVDISPLAY()
        i=i+1
    VGCREATE()
    VGDISPLAY()
    LVCREATE()
    LVDISPLAY()
    FORMAT()
    MOUNT()
def RePVCREATE():
    disk=input("Enter the Disk name")
    ip=input("Enter the ip")
    os.system('ssh {} pvcreate {}'.format(ip,disk))
def RePVDISPLAY():
    ip=input("Enter the ip")
    disk=input("Enter disk name which you want to see")
    os.system('ssh {} pvdisplay {}'.format(ip,disk))
def ReVGCREATE():
    ip=input("Enter the ip")
    name=input("enter the name of vg")
    disk=input("enter the name of disk and if more thn 1 disk thn use space between names")
    os.system('ssh {} vgcreate {} {}'.format(ip,name,disk))
def ReVGDISPLAY():
    ip=input("Enter the ip")
    name=input("Enter the name of VG: ")
    os.system('ssh {} vgdisplay {}'.format(ip,name))
def ReLVCREATE():
    ip=input("Enter the ip")
    name=input("Enter the name of LV")
    size=input("Enter the size of LV")
    vgn=input("Enter the name of VG")
    os.system('ssh {} lvcreate --size {}G --name {} {}'.format(ip,size,name,vgn))
def ReLVDISPLAY():
    ip=input("Enter the ip")
    name=input("Enter the name of LV")
    os.system('ssh {} lvdisplay {}'.format(ip,name))
def ReFORMAT():
    ip=input("Enter the ip")
    exe=input("Enter the extension")
    name=input("Enter the LV name")
    os.system('ssh {} mkfs.{} {}'.format(ip,exe,name))
def ReMOUNT():
    ip=input("Enter the ip")
    name=input("Enter the LV name")
    loc=input("Enter the location")
    os.system('ssh {} mount {} {}'.format(ip,name,loc))
def ReUNMOUNT():
    ip=input("Enter the ip")
    name=input("Enter the disk to unmount")
    os.system('ssh {} umount {}'.format(ip,name))
def ReEXTEND():
    ip=input("Enter the ip")
    size=input("Enter the size to extend")
    name=input("Enter the name of LV")
    os.system('ssh {} lvextend --size +{}G {}'.format(ip,size,name))
def ReRESIZE():
    ip=input("Enter the ip")
    name=input("Enter the LV name")
    os.system('ssh {} resize2fs {}'.format(ip,name))
def ReREDUCE():
    ip=input("Enter the ip")
    name=input("Enter the LV name")
    size=input("Enter the size to reduce")
    os.system('ssh {} lvreduce -L {}G {}'.format(ip,size,name))
def ReLVM():
    i=0
    number=input("Enter the number of disks")
    for i in range(number):
        RePVCREATE()
        RePVDISPLAY()
        i=i+1
    ReVGCREATE()
    ReVGDISPLAY()
    ReLVCREATE()
    ReLVDISPLAY()
    ReFORMAT()
    ReMOUNT()
login=input("What do you want LOCAL or REMOTE login:")
print("Your Choice",login)
while True:
    print('''
    Press 1: To use LVM
    Press 2: To create PV
    Press 3: To display PV
    Press 4: To create vg
    Press 5: To display vg
    Press 6: To create lv
    Press 7: To display lv
    Press 8: To format
    Press 9: To mount
    Press 10: TO extend
    Press 11: To resize
    Press 12: To reduce
    Press 13: To unmount
    Press 0: To Exit
    ''')
    if login == "local":
        i=int(input("enter your choice"))
        if i==1:
            LVM()
        elif i==2:
            PVCREATE()
        elif i==3:
            PVDISPLAY()
        elif i==4:
            VGCREATE()
        elif i==5:
            VGDISPLAY()
        elif i==6:
            LVCREATE()
        elif i==7:
            LVDISPLAY()
        elif i==8:
            FORMAT()
        elif i==9:
            MOUNT()
        elif i==10:
            EXTEND()
        elif i==11:
            RESIZE()
        elif i==12:
            REDUCE()
        elif i==13:
            UNMOUNT()
	elif i==0:
            exit()
    else:
        i=input("enter your choice for remote")
        if i==1:
            ReLVM()
        if i==2:
            RePVCREATE()
        if i==3:
            RePVDISPLAY()
        if i==4:
            ReVGCREATE()
        if i==5:
            ReVGDISPLAY()
        if i==6:
            ReVGCREATE()
        if i==7:
            ReLVDISPLAY()
        if i==8:
            ReFORMAT()
        if i==9:
            ReMOUNT()
        if i==10:
            ReEXTEND()
        if i==11:
            ReRESIZE()
        if i==12:
            ReREDUCE()
        if i==13:
            ReUNMOUNT()

