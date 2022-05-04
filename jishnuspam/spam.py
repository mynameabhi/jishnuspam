a='\033[31m'
lgreen = '\033[92m'

bold = '\033[01m'
print(a+bold+"""

                          ....................../´¯/) 
                         ....................,/¯../ 
                         .................../..../ 
                         ............./´¯/'...'/´¯¯`·¸ 
                         ........../'/.../..../......./¨¯\ 
                         ........('(...´...´.... ¯~/'...') 
                         .........\.................'...../  
                         ..........''...\.......... _.·´ 
                         ............\..............( 
                         ..............\.............\..     
                                                               
      ███   ███          █████                           
     ░░░   ░░░          ░░███                            
     █████ ████   █████  ░███████   ████████   █████ ████
    ░░███ ░░███  ███░░   ░███░░███ ░░███░░███ ░░███ ░███ 
     ░███  ░███ ░░█████  ░███ ░███  ░███ ░███  ░███ ░███ 
     ░███  ░███  ░░░░███ ░███ ░███  ░███ ░███  ░███ ░███ 
     ░███  █████ ██████  ████ █████ ████ █████ ░░████████
     ░███ ░░░░░ ░░░░░░  ░░░░ ░░░░░ ░░░░ ░░░░░   ░░░░░░░░ 
 ███ ░███                                                
░░██████                                                 
 ░░░░░░    
  """)
print("                                    ")


print(lgreen+bold+"                    this is created by jishnu       ")


print("  ")






####_____________________________________________________________________________-

import webbrowser
import time





import pyautogui

green='\033[92m'
pink='\033[95m'
blue='\033[94m'
skyblue='\033[96m'
yellow='\033[93m'
red='\033[91m'
bod='\033[1m'
white='\033[0m'
underline='\033[4m'
purple='\033[35m'

print(green+"   press 1 for normol spam")
print(red+"   press 2 for abuse spam")
typeofspam = str(input("press 1 or 2 for spam : "+blue))



if typeofspam == '1':

    print(pink+"""
           NOW YOU ARE IN NORMAL SPAM
    """)

    print(pink+"press",pink+"1","for",red+"instagram",)
    print(pink+"press",pink+"2", "for", blue+"facebook")
    site=str(input(green+bod+"open website by writing : "))    

    if site == '1':
        webbrowser.open("https://www.instagram.com/direct/inbox/")
    if site == '2':
        webbrowser.open("https://www.facebook.com/")



    spm=int(input(yellow+"enter spam range : "))


    text1=str(input(skyblue+"enter the text : "))
    text2=str(input("enter the text : "))

#### input abuse




    ### time statements



    tim=int(input(purple+"enter time to left  "))
    # for i in range(tim):
    print(tim-1)
    time.sleep(1)
    print(tim-2)
    time.sleep(tim)
    ####---------------------------------------
    ##input abuse here




    ##________________________
    ##spam starts here          | 
    ##------------------------

    pyautogui.write("jai shree ram")
    pyautogui.press("enter")
    for i in range(spm):

        pyautogui.write(text1)
        pyautogui.press("enter")
    
        pyautogui.write(text2)
        pyautogui.press("enter")


####                  first spam end xxxxx
####__________________________________________________________________________________
########------------------------------------------------------------------------------------
####______________________________________________________________________________________

########================================================================================



if typeofspam == '2':
    print(pink+"""
           NOW YOU ARE IN ABUSE SPAM
    """)


    print(pink+"press",pink+"1","for",red+"instagram",)
    print(pink+"press",pink+"2", "for", blue+"facebook")
    site=str(input(green+"open website by writing : 1 or 2  "))    

    if site == '1':
        webbrowser.open("https://www.instagram.com/direct/inbox/")
    if site == '2':
        webbrowser.open("https://www.facebook.com/")


    print("remeber spam must be less then 5")
    rg=int(input(yellow+"enter the range : "))
    
    tx=str(input(blue+"enter ur 1 enemy name : "))
    tx2=str(input(blue+"enter ur 2 enemy name 'if no 2 the put the same ': "))


    ###=====================================================================
    file=open('abuse.txt','r').read()
    file=file.splitlines()

    timm=int(input(purple+"enter time to left  "))
    # for i in range(tim):
    print(timm-1)
    time.sleep(1)
    print(timm-2)
    time.sleep(timm)



    for i in range (rg):
        for i in file:
            pyautogui.write(tx +' '+i)
            pyautogui.press('enter')
            pyautogui.write(tx2+' '+i)
            pyautogui.press('enter')




