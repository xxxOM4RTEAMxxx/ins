import colorama
from colorama import Fore
import sys
import os
import time
my_message = Fore.GREEN+"""[██████████████████]
succesfully loaded!
starting ........
PRO TIP:INS gives u followers!(but some fillower may unfollow u!)
"""
print(Fore.CYAN+"WELCOME TO INS FOLLOW!!!")
def typewriter(my_message):
    for char in my_message:
        sys.stdout.write(char)
        sys.stdout.flush()

        if char != "\n":
            time.sleep(0.1)

        else:
            time.sleep(1)

os.system("cls") # for linux use clear instead of cls
typewriter(my_message) # call ur funct
while True:
    print("                            Instagram followers")
    print(Fore.RED+"1.15 followers(free)")
    print(Fore.CYAN+"2.50 followers(1$)")
    print(Fore.BLUE+"3.100 followers(2$)")
    print(Fore.GREEN+"4.250 followers(5$)")
    print(Fore.YELLOW+"5.special offer!!300 followers(10>>5$)(expires after 1 years!)")
    print(Fore.GREEN+"6.promocode(promocodes gives u gift example is theres offer is 5$that makes 2$ for promocodes u need dm me:))")
    print(Fore.RED+"0.left")
    choice = input("enter choice!!: ")
    
    choice = choice.strip()
    if (choice == "1"):
        print("dm me at tele@AZERBAYCAN_AZR")
    elif (choice == "2"):
        print("dm me in tele @AZERBAYCAN_AZR")
    elif (choice == "3"):
         print("tm me in tele @AZERBAYCAN_AZR")
    elif (choice == "4"):
         print("tm me in tele @AZERBAYCAN_AZR")
    elif (choice == "5"):
          print("tm me in tele @AZERBAYCAN_AZR")
    elif (choice == "0"):
        break
    