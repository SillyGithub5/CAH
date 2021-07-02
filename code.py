
import random
EliOSAPI = "www.zincosconfigapi.eliosdconnect.vnc.net/hdivbdjfjejwebfjhbvfn "
# Computer Functions
def users():
    user = input("Who is using the computer?")
    print ("Welcome,", user)
    print ("If you are on settings, please wait for your computer to boot up")
    setset()
def spacelist():
    spacelist = ["A Rocket", "A Spacesuit", "A Oxgen tank", "Some Space shoes"]
    print ("Wer'e going to space!")
    whatNeed = input("What do you think we need?")
    spacelist.append (whatNeed)
    whatNeed = input("What do you think we need?")
    spacelist.append (whatNeed)
    print ("Let's see what we need...")
    for item in spacelist:
        print (item)
    print ("Wee! Off I go to space!")
def bootup():
    print ("EliOS Terminal2 booting up...")
    for bu in range (0,8):
        print ("64 BYTES OF DATA FROM ELIOS API")
    print ("Downloads Complete")
    print ("Welcome to EliOS")
    users()
def bootup2():
    print ("EliOS Treminal2 booting up...")
    for bu in range (0,8):
        print ("64 BYTES OF DATA FROM ELIOS API")
    print ("Downloads Complete")
    print ("Welcome to EliOS")
    whattodo()  
def castle():
    exitChoice = "Nothing"
    while exitChoice != "EXIT": 
        print ("You are in a dark room in a mysterious castle.")
        print ("In front of you are four doors. You must choose one.")
        playerChoice = input("Choose 1, 2,3 or 4...")
        if playerChoice == "1":
            print ("You finda room full of treasure. You're rich!")
            print ("GAME OVER, YOU WIN.")
        elif playerChoice == "2":
            print ("The door opens and an angry ogre hits you with his club.")
            print ("GAME OVER, YOU LOSE.")
        elif playerChoice == "3":
            print ("You go into the room and find a sleeping dragon.")
            print ("You can either:")
            print ("1) Try to steal some of the dragon's gold.")
            print ("2) Try to sneak around the dragon to the exit.")
        dragonChoice = input("Type 1 or 2...")
        if dragonChoice == "1":
            print ("The dragon wakes up and eats you. You are delicous.")
            print ("GAME OVER, YOU LOSE")
        elif dragonChoice == "2":
             print ("You sneak around the dragon and escape the castle, blinking in the sunlight.")
             print ("GAME OVER! YOU WIN!")
        else:
             print ("Sorry, you didn't enter 1 or 2!")
        if playerChoice == "4":
             print ("You enter a room with a sphinx.")
             print ("It asks you to guess what number it is thinking of, between 1 and 10")
             number = int(input("What number do you choose?"))
        if number == random.randint(1,10):
             print ("The sphinx hisses in dissapointment. You geussed correctly.")
             print ("She must let you go free")
             print ("GAME OVER. YOU WIN")
        else:
             print ("The sphinx tells you that your geuss is incorrect.")
             print ("You are now her prisoner forever.")
             print ("GAME OVER, YOU LOSE")

    else:
        print("Sorry, You didn't enter 1, 2, 3 or 4!")
        exitChoice = input("Press return to play again, or type EXIT to leave.")
        whattodo()
def wifi():
    wifis = ["School Network", "GuestWifi", "MySpectrumNetwork1f-2G", ]
    print ("There are currently 3 wifi networks online. Please select one")
    print ("(1) Cafe Network")
    print ("(2) Guest Network")
    print ("(3) MySpectrumNetwork1f-2g")
    connected = input("Wich one do you want to connect? (Enter the number)")
    print ("Connected to", wifis[int(connected)] )
def setthetime():
    global time
    time = input("What is the time?")
    print ("The time is", time)
    setset()
def showthetime():
    print ("The time is", time)
def error():
    
    bootup()
def setset():
    print ("Welcome to EliOS setings")
    print ("You can change these:")
    print ("(1) Change the the wifi connection")
    print ("(2) Set the user name")
    print ("(3) Set the time")
    print ("(4) fdhdbdvd")
    print ("(5) Activate your computer")
    print ("(6) About...")
    settings = input("What settings would you like to change (Enter the number or text)")
    if settings == "1":
        wifi()
    elif settings == "2":
        users()
    elif settings == "Change the the wifi connection":
        wifi()
    elif settings == "Set the user name":
        users()
    elif settings == "3":
        setthetime()
    elif settings == "Set the time":
        setthetime()
    elif settings == "Exit":
        whattodo()
    elif settings == "4":
        error()
    elif settings == "5":
        activate()
    elif settings == "6":
        about()                           
def whattodo():
    whatdo = input("What would you like to do?")
    if whatdo == "Email":
        print ("EZincSOt Currlyas no emails.")
        whattodo()
    elif whatdo == "Play a game":
        print ("Two games avlible")
        gamedo = input("Enetr 1 or 2")
        if gamedo == "1":
            castle()
        elif gamedo == "2":
            spacelist() 
    elif whatdo == "Exit":
      print ("Goodbye....")
    elif whatdo == "Settings":
        setset()
    elif whatdo == "ShowTime":
        showthetime()                                                                             
    else:
        print ("EliOS Couldn't find the command '", whatdo, "'")
        whattodo()
def activate():
    print ("EliOS requires your prouduct code. To find it, look at About in EliOS settings")
    ent = input("Enter your product code...")
    if ent == "1637329":
        print ("EliOS API", ELIOSAPI, "Recongnized this product code.")
        print ("Succsefully activated.")
        bootup2()
    else:
        print ("This code is not valid.")
        activate()
def about():
    print ("-------------------------------------ABOUT CAH--------------------------------------------")
    print ("Version: 1.8")
    print ("Storage: 17.7Mb")
    print ("Product code: 1637329")
    print ("CAHOS API:", ELIOSAPI)
    exit = input("Would you like to exit?")
    if exit == "Yes":
        setset()
    else:
        about()
    print ("------------------------------------------------------------------------------------------------------")
# Program running sequence
bootup
choose=random.choice
import time
wait=time.sleep
from Quotes import WHITE
from Quotes import BLACK 
def rpn():
  white=choose(WHITE)
  black=choose(BLACK)
  wait(1)
  print(black,white,"\n","\n")

EliOSAPI = "www.zincosconfigapi.eliosdconnect.vnc.net/hdivbdjfjejwebfjhbvfn fnvnnkjvrjghjrthgrhgrtghjrgnjrgjbgj1114556776554"
# Computer Functions
def users():
    user = input("Who is using the computer?")
    print ("Welcome,", user)
    print ("If you are on settings, please wait for your computer to boot up")
    setset()
def spacelist():
    spacelist = ["A Rocket", "A Spacesuit", "A Oxgen tank", "Some Space shoes"]
    print ("Wer'e going to space!")
    whatNeed = input("What do you think we need?")
    spacelist.append (whatNeed)
    whatNeed = input("What do you think we need?")
    spacelist.append (whatNeed)
    print ("Let's see what we need...")
    for item in spacelist:
        print (item)
    print ("Wee! Off I go to space!")
def bootup():
    print ("EliOS Terminal2 booting up...")
    for bu in range (0,8):
        print ("64 BYTES OF DATA FROM ELIOS API")
    print ("Downloads Complete")
    print ("Welcome to EliOS")
    users()
def bootup2():
    print ("EliOS Treminal2 booting up...")
    for bu in range (0,8):
        print ("64 BYTES OF DATA FROM ELIOS API")
    print ("Downloads Complete")
    print ("Welcome to EliOS")
    whattodo()  
def castle():
    exitChoice = "Nothing"
    while exitChoice != "EXIT": 
        print ("You are in a dark room in a mysterious castle.")
        print ("In front of you are four doors. You must choose one.")
        playerChoice = input("Choose 1, 2,3 or 4...")
        if playerChoice == "1":
            print ("You finda room full of treasure. You're rich!")
            print ("GAME OVER, YOU WIN.")
        elif playerChoice == "2":
            print ("The door opens and an angry ogre hits you with his club.")
            print ("GAME OVER, YOU LOSE.")
        elif playerChoice == "3":
            print ("You go into the room and find a sleeping dragon.")
            print ("You can either:")
            print ("1) Try to steal some of the dragon's gold.")
            print ("2) Try to sneak around the dragon to the exit.")
        dragonChoice = input("Type 1 or 2...")
        if dragonChoice == "1":
            print ("The dragon wakes up and eats you. You are delicous.")
            print ("GAME OVER, YOU LOSE")
        elif dragonChoice == "2":
             print ("You sneak around the dragon and escape the castle, blinking in the sunlight.")
             print ("GAME OVER! YOU WIN!")
        else:
             print ("Sorry, you didn't enter 1 or 2!")
        if playerChoice == "4":
             print ("You enter a room with a sphinx.")
             print ("It asks you to guess what number it is thinking of, between 1 and 10")
             number = int(input("What number do you choose?"))
        if number == random.randint(1,10):
             print ("The sphinx hisses in dissapointment. You geussed correctly.")
             print ("She must let you go free")
             print ("GAME OVER. YOU WIN")
        else:
             print ("The sphinx tells you that your geuss is incorrect.")
             print ("You are now her prisoner forever.")
             print ("GAME OVER, YOU LOSE")

    else:
        print("Sorry, You didn't enter 1, 2, 3 or 4!")
        exitChoice = input("Press return to play again, or type EXIT to leave.")
        whattodo()
def wifi():
    wifis = ["Cafe Network", "GuestWifi", "MySpectrumNetwork1f-2G", ]
    print ("There are currently 3 wifi networks online. Please select one")
    print ("(1) Cafe Network")
    print ("(2) Guest Network")
    print ("(3) MySpectrumNetwork1f-2g")
    connected = input("Wich one do you want to connect? (Enter the number)")
    print ("Connected to", wifis[int(connected)] )
    whattodo()
def setthetime():
    global time
    time = input("What is the time?")
    print ("The time is", time)
    setset()
def showthetime():
    print ("The time is", time)
def error():
    
    bootup()
def setset():
    print ("Welcome to EliOS setings")
    print ("You can change these:")
    print ("(1) Change the the wifi connection")
    print ("(2) Set the user name")
    print ("(3) Set the time")
    print ("(4) fdhdbdvd")
    print ("(5) Activate your computer")
    print ("(6) About...")
    settings = input("What settings would you like to change (Enter the number or text)")
    if settings == "1":
        wifi()
    elif settings == "2":
        users()
    elif settings == "Change the the wifi connection":
        wifi()
    elif settings == "Set the user name":
        users()
    elif settings == "3":
        setthetime()
    elif settings == "Set the time":
        setthetime()
    elif settings == "Exit":
        whattodo()
    elif settings == "4":
        error()
    elif settings == "5":
        activate()
    elif settings == "6":
        about()                           
def whattodo():
    whatdo = input("What would you like to do?")
    if whatdo == "Email":
        print ("EZincSOt Currlyas no emails.")
        whattodo()
    elif whatdo == "Play a game":
        print ("Two games avlible")
        gamedo = input("Enetr 1 or 2")
        if gamedo == "1":
            castle()
        elif gamedo == "2":
            spacelist() 
    elif whatdo == "Exit":
      print ("Goodbye....")
    elif whatdo == "Settings":
        setset()
    elif whatdo == "ShowTime":
        showthetime()                                                                             
    else:
        print ("EliOS Couldn't find the command '", whatdo, "'")
        whattodo()
def activate():
    print ("EliOS requires your prouduct code. To find it, look at About in EliOS settings")
    ent = input("Enter your product code...")
    if ent == "1637329":
        print ("EliOS API", ELIOSAPI, "Recongnized this product code.")
        print ("Succsefully activated.")
        bootup2()
    else:
        print ("This code is not valid.")
        activate()
def about():
    print ("-------------------------------------ABOUT ELIOS TERMINAL2--------------------------------------------")
    print ("Version: 20.17")
    print ("Storage: 123 GB")
    print ("Product code: 1637329")
    print ("EliOS API:", ELIOSAPI)
    exit = input("Would you like to exit?")
    if exit == "Yes":
        setset()
    else:
        about()
    print ("------------------------------------------------------------------------------------------------------")
# Program running sequence
bootup
import random
EliOSAPI = "www.zincosconfigapi.eliosdconnect.vnc.net/hdivbdjfjejwebfjhbvfn fnvnnkjvrjghjrthgrhgrtghjrgnjrgjbgj1114556776554"
# Computer Functions
def users():
    user = input("Who is using the computer?")
    print ("Welcome,", user)
    print ("If you are on settings, please wait for your computer to boot up")
    setset()
def spacelist():
    spacelist = ["A Rocket", "A Spacesuit", "A Oxgen tank", "Some Space shoes"]
    print ("Wer'e going to space!")
    whatNeed = input("What do you think we need?")
    spacelist.append (whatNeed)
    whatNeed = input("What do you think we need?")
    spacelist.append (whatNeed)
    print ("Let's see what we need...")
    for item in spacelist:
        print (item)
    print ("Wee! Off I go to space!")
def bootup():
    print ("EliOS Terminal2 booting up...")
    for bu in range (0,8):
        print ("64 BYTES OF DATA FROM ELIOS API")
    print ("Downloads Complete")
    print ("Welcome to EliOS")
    users()
def bootup2():
    print ("EliOS Treminal2 booting up...")
    for bu in range (0,8):
        print ("64 BYTES OF DATA FROM ELIOS API")
    print ("Downloads Complete")
    print ("Welcome to EliOS")
    whattodo()  
def castle():
    exitChoice = "Nothing"
    while exitChoice != "EXIT": 
        print ("You are in a dark room in a mysterious castle.")
        print ("In front of you are four doors. You must choose one.")
        playerChoice = input("Choose 1, 2,3 or 4...")
        if playerChoice == "1":
            print ("You finda room full of treasure. You're rich!")
            print ("GAME OVER, YOU WIN.")
        elif playerChoice == "2":
            print ("The door opens and an angry ogre hits you with his club.")
            print ("GAME OVER, YOU LOSE.")
        elif playerChoice == "3":
            print ("You go into the room and find a sleeping dragon.")
            print ("You can either:")
            print ("1) Try to steal some of the dragon's gold.")
            print ("2) Try to sneak around the dragon to the exit.")
        dragonChoice = input("Type 1 or 2...")
        if dragonChoice == "1":
            print ("The dragon wakes up and eats you. You are delicous.")
            print ("GAME OVER, YOU LOSE")
        elif dragonChoice == "2":
             print ("You sneak around the dragon and escape the castle, blinking in the sunlight.")
             print ("GAME OVER! YOU WIN!")
        else:
             print ("Sorry, you didn't enter 1 or 2!")
        if playerChoice == "4":
             print ("You enter a room with a sphinx.")
             print ("It asks you to guess what number it is thinking of, between 1 and 10")
             number = int(input("What number do you choose?"))
        if number == random.randint(1,10):
             print ("The sphinx hisses in dissapointment. You geussed correctly.")
             print ("She must let you go free")
             print ("GAME OVER. YOU WIN")
        else:
             print ("The sphinx tells you that your geuss is incorrect.")
             print ("You are now her prisoner forever.")
             print ("GAME OVER, YOU LOSE")

    else:
        print("Sorry, You didn't enter 1, 2, 3 or 4!")
        exitChoice = input("Press return to play again, or type EXIT to leave.")
        whattodo()
def wifi():
    wifis = ["Cafe Network", "GuestWifi", "MySpectrumNetwork1f-2G", ]
    print ("There are currently 3 wifi networks online. Please select one")
    print ("(1) Cafe Network")
    print ("(2) Guest Network")
    print ("(3) MySpectrumNetwork1f-2g")
    connected = input("Wich one do you want to connect? (Enter the number)")
    print ("Connected to", wifis[int(connected)] )
    whattodo()
def setthetime():
    global time
    time = input("What is the time?")
    print ("The time is", time)
    setset()
def showthetime():
    print ("The time is", time)
def error():
    
    bootup()
def setset():
    print ("Welcome to EliOS setings")
    print ("You can change these:")
    print ("(1) Change the the wifi connection")
    print ("(2) Set the user name")
    print ("(3) Set the time")
    print ("(4) fdhdbdvd")
    print ("(5) Activate your computer")
    print ("(6) About...")
    settings = input("What settings would you like to change (Enter the number or text)")
    if settings == "1":
        wifi()
    elif settings == "2":
        users()
    elif settings == "Change the the wifi connection":
        wifi()
    elif settings == "Set the user name":
        users()
    elif settings == "3":
        setthetime()
    elif settings == "Set the time":
        setthetime()
    elif settings == "Exit":
        whattodo()
    elif settings == "4":
        error()
    elif settings == "5":
        activate()
    elif settings == "6":
        about()                           
def whattodo():
    whatdo = input("What would you like to do?")
    if whatdo == "Email":
        print ("EZincSOt Currlyas no emails.")
        whattodo()
    elif whatdo == "Play a game":
        print ("Two games avlible")
        gamedo = input("Enetr 1 or 2")
        if gamedo == "1":
            castle()
        elif gamedo == "2":
            spacelist() 
    elif whatdo == "Exit":
      print ("Goodbye....")
    elif whatdo == "Settings":
        setset()
    elif whatdo == "ShowTime":
        showthetime()                                                                             
    else:
        print ("EliOS Couldn't find the command '", whatdo, "'")
        whattodo()
def activate():
    print ("EliOS requires your prouduct code. To find it, look at About in EliOS settings")
    ent = input("Enter your product code...")
    if ent == "1637329":
        print ("EliOS API", ELIOSAPI, "Recongnized this product code.")
        print ("Succsefully activated.")
        bootup2()
    else:
        print ("This code is not valid.")
        activate()
def about():
    print ("-------------------------------------ABOUT ELIOS TERMINAL2--------------------------------------------")
    print ("Version: 20.17")
    print ("Storage: 123 GB")
    print ("Product code: 1637329")
    print ("EliOS API:", ELIOSAPI)
    exit = input("Would you like to exit?")
    if exit == "Yes":
        setset()
    else:
        about()
    print ("------------------------------------------------------------------------------------------------------")
# Program running sequence
bootup

import random
EliOSAPI = "www.zincosconfigapi.eliosdconnect.vnc.net/hdivbdjfjejwebfjhbvfn fnvnnkjvrjghjrthgrhgrtghjrgnjrgjbgj1114556776554"
# Computer Functions
def users():
    user = input("Who is using the computer?")
    print ("Welcome,", user)
    print ("If you are on settings, please wait for your computer to boot up")
    setset()
def spacelist():
    spacelist = ["A Rocket", "A Spacesuit", "A Oxgen tank", "Some Space shoes"]
    print ("Wer'e going to space!")
    whatNeed = input("What do you think we need?")
    spacelist.append (whatNeed)
    whatNeed = input("What do you think we need?")
    spacelist.append (whatNeed)
    print ("Let's see what we need...")
    for item in spacelist:
        print (item)
    print ("Wee! Off I go to space!")
def bootup():
    print ("EliOS Terminal2 booting up...")
    for bu in range (0,8):
        print ("64 BYTES OF DATA FROM ELIOS API")
    print ("Downloads Complete")
    print ("Welcome to EliOS")
    users()
def bootup2():
    print ("EliOS Treminal2 booting up...")
    for bu in range (0,8):
        print ("64 BYTES OF DATA FROM ELIOS API")
    print ("Downloads Complete")
    print ("Welcome to EliOS")
    whattodo()  
def castle():
    exitChoice = "Nothing"
    while exitChoice != "EXIT": 
        print ("You are in a dark room in a mysterious castle.")
        print ("In front of you are four doors. You must choose one.")
        playerChoice = input("Choose 1, 2,3 or 4...")
        if playerChoice == "1":
            print ("You finda room full of treasure. You're rich!")
            print ("GAME OVER, YOU WIN.")
        elif playerChoice == "2":
            print ("The door opens and an angry ogre hits you with his club.")
            print ("GAME OVER, YOU LOSE.")
        elif playerChoice == "3":
            print ("You go into the room and find a sleeping dragon.")
            print ("You can either:")
            print ("1) Try to steal some of the dragon's gold.")
            print ("2) Try to sneak around the dragon to the exit.")
        dragonChoice = input("Type 1 or 2...")
        if dragonChoice == "1":
            print ("The dragon wakes up and eats you. You are delicous.")
            print ("GAME OVER, YOU LOSE")
        elif dragonChoice == "2":
             print ("You sneak around the dragon and escape the castle, blinking in the sunlight.")
             print ("GAME OVER! YOU WIN!")
        else:
             print ("Sorry, you didn't enter 1 or 2!")
        if playerChoice == "4":
             print ("You enter a room with a sphinx.")
             print ("It asks you to guess what number it is thinking of, between 1 and 10")
             number = int(input("What number do you choose?"))
        if number == random.randint(1,10):
             print ("The sphinx hisses in dissapointment. You geussed correctly.")
             print ("She must let you go free")
             print ("GAME OVER. YOU WIN")
        else:
             print ("The sphinx tells you that your geuss is incorrect.")
             print ("You are now her prisoner forever.")
             print ("GAME OVER, YOU LOSE")

    else:
        print("Sorry, You didn't enter 1, 2, 3 or 4!")
        exitChoice = input("Press return to play again, or type EXIT to leave.")
        whattodo()
def wifi():
    wifis = ["Cafe Network", "GuestWifi", "MySpectrumNetwork1f-2G", ]
    print ("There are currently 3 wifi networks online. Please select one")
    print ("(1) Cafe Network")
    print ("(2) Guest Network")
    print ("(3) MySpectrumNetwork1f-2g")
    connected = input("Wich one do you want to connect? (Enter the number)")
    print ("Connected to", wifis[int(connected)] )
    whattodo()
def setthetime():
    global time
    time = input("What is the time?")
    print ("The time is", time)
    setset()
def showthetime():
    print ("The time is", time)
def error():
    
    bootup()
def setset():
    print ("Welcome to EliOS setings")
    print ("You can change these:")
    print ("(1) Change the the wifi connection")
    print ("(2) Set the user name")
    print ("(3) Set the time")
    print ("(4) fdhdbdvd")
    print ("(5) Activate your computer")
    print ("(6) About...")
    settings = input("What settings would you like to change (Enter the number or text)")
    if settings == "1":
        wifi()
    elif settings == "2":
        users()
    elif settings == "Change the the wifi connection":
        wifi()
    elif settings == "Set the user name":
        users()
    elif settings == "3":
        setthetime()
    elif settings == "Set the time":
        setthetime()
    elif settings == "Exit":
        whattodo()
    elif settings == "4":
        error()
    elif settings == "5":
        activate()
    elif settings == "6":
        about()                           
def whattodo():
    whatdo = input("What would you like to do?")
    if whatdo == "Email":
        print ("EZincSOt Currlyas no emails.")
        whattodo()
    elif whatdo == "Play a game":
        print ("Two games avlible")
        gamedo = input("Enetr 1 or 2")
        if gamedo == "1":
            castle()
        elif gamedo == "2":
            spacelist() 
    elif whatdo == "Exit":
      print ("Goodbye....")
    elif whatdo == "Settings":
        setset()
    elif whatdo == "ShowTime":
        showthetime()                                                                             
    else:
        print ("EliOS Couldn't find the command '", whatdo, "'")
        whattodo()
def activate():
    print ("EliOS requires your prouduct code. To find it, look at About in EliOS settings")
    ent = input("Enter your product code...")
    if ent == "1637329":
        print ("EliOS API", ELIOSAPI, "Recongnized this product code.")
        print ("Succsefully activated.")
        bootup2()
    else:
        print ("This code is not valid.")
        activate()
def about():
    print ("-------------------------------------ABOUT ELIOS TERMINAL2--------------------------------------------")
    print ("Version: 20.17")
    print ("Storage: 123 GB")
    print ("Product code: 1637329")
    print ("EliOS API:", ELIOSAPI)
    exit = input("Would you like to exit?")
    if exit == "Yes":
        setset()
    else:
        about()
    print ("------------------------------------------------------------------------------------------------------")
# Program running sequence
bootup

import random
EliOSAPI = "www.zincosconfigapi.eliosdconnect.vnc.net/hdivbdjfjejwebfjhbvfn fnvnnkjvrjghjrthgrhgrtghjrgnjrgjbgj1114556776554"
# Computer Functions
def users():
    user = input("Who is using the computer?")
    print ("Welcome,", user)
    print ("If you are on settings, please wait for your computer to boot up")
    setset()
def spacelist():
    spacelist = ["A Rocket", "A Spacesuit", "A Oxgen tank", "Some Space shoes"]
    print ("Wer'e going to space!")
    whatNeed = input("What do you think we need?")
    spacelist.append (whatNeed)
    whatNeed = input("What do you think we need?")
    spacelist.append (whatNeed)
    print ("Let's see what we need...")
    for item in spacelist:
        print (item)
    print ("Wee! Off I go to space!")
def bootup():
    print ("EliOS Terminal2 booting up...")
    for bu in range (0,8):
        print ("64 BYTES OF DATA FROM ELIOS API")
    print ("Downloads Complete")
    print ("Welcome to EliOS")
    users()
def bootup2():
    print ("EliOS Treminal2 booting up...")
    for bu in range (0,8):
        print ("64 BYTES OF DATA FROM ELIOS API")
    print ("Downloads Complete")
    print ("Welcome to EliOS")
    whattodo()  
def castle():
    exitChoice = "Nothing"
    while exitChoice != "EXIT": 
        print ("You are in a dark room in a mysterious castle.")
        print ("In front of you are four doors. You must choose one.")
        playerChoice = input("Choose 1, 2,3 or 4...")
        if playerChoice == "1":
            print ("You finda room full of treasure. You're rich!")
            print ("GAME OVER, YOU WIN.")
        elif playerChoice == "2":
            print ("The door opens and an angry ogre hits you with his club.")
            print ("GAME OVER, YOU LOSE.")
        elif playerChoice == "3":
            print ("You go into the room and find a sleeping dragon.")
            print ("You can either:")
            print ("1) Try to steal some of the dragon's gold.")
            print ("2) Try to sneak around the dragon to the exit.")
        dragonChoice = input("Type 1 or 2...")
        if dragonChoice == "1":
            print ("The dragon wakes up and eats you. You are delicous.")
            print ("GAME OVER, YOU LOSE")
        elif dragonChoice == "2":
             print ("You sneak around the dragon and escape the castle, blinking in the sunlight.")
             print ("GAME OVER! YOU WIN!")
        else:
             print ("Sorry, you didn't enter 1 or 2!")
        if playerChoice == "4":
             print ("You enter a room with a sphinx.")
             print ("It asks you to guess what number it is thinking of, between 1 and 10")
             number = int(input("What number do you choose?"))
        if number == random.randint(1,10):
             print ("The sphinx hisses in dissapointment. You geussed correctly.")
             print ("She must let you go free")
             print ("GAME OVER. YOU WIN")
        else:
             print ("The sphinx tells you that your geuss is incorrect.")
             print ("You are now her prisoner forever.")
             print ("GAME OVER, YOU LOSE")

    else:
        print("Sorry, You didn't enter 1, 2, 3 or 4!")
        exitChoice = input("Press return to play again, or type EXIT to leave.")
        whattodo()
def wifi():
    wifis = ["Cafe Network", "GuestWifi", "MySpectrumNetwork1f-2G", ]
    print ("There are currently 3 wifi networks online. Please select one")
    print ("(1) Cafe Network")
    print ("(2) Guest Network")
    print ("(3) MySpectrumNetwork1f-2g")
    connected = input("Wich one do you want to connect? (Enter the number)")
    print ("Connected to", wifis[int(connected)] )
    whattodo()
def setthetime():
    global time
    time = input("What is the time?")
    print ("The time is", time)
    setset()
def showthetime():
    print ("The time is", time)
def error():
    
    bootup()
def setset():
    print ("Welcome to EliOS setings")
    print ("You can change these:")
    print ("(1) Change the the wifi connection")
    print ("(2) Set the user name")
    print ("(3) Set the time")
    print ("(4) fdhdbdvd")
    print ("(5) Activate your computer")
    print ("(6) About...")
    settings = input("What settings would you like to change (Enter the number or text)")
    if settings == "1":
        wifi()
    elif settings == "2":
        users()
    elif settings == "Change the the wifi connection":
        wifi()
    elif settings == "Set the user name":
        users()
    elif settings == "3":
        setthetime()
    elif settings == "Set the time":
        setthetime()
    elif settings == "Exit":
        whattodo()
    elif settings == "4":
        error()
    elif settings == "5":
        activate()
    elif settings == "6":
        about()                           
def whattodo():
    whatdo = input("What would you like to do?")
    if whatdo == "Email":
        print ("EZincSOt Currlyas no emails.")
        whattodo()
    elif whatdo == "Play a game":
        print ("Two games avlible")
        gamedo = input("Enetr 1 or 2")
        if gamedo == "1":
            castle()
        elif gamedo == "2":
            spacelist() 
    elif whatdo == "Exit":
      print ("Goodbye....")
    elif whatdo == "Settings":
        setset()
    elif whatdo == "ShowTime":
        showthetime()                                                                             
    else:
        print ("EliOS Couldn't find the command '", whatdo, "'")
        whattodo()
def activate():
    print ("EliOS requires your prouduct code. To find it, look at About in EliOS settings")
    ent = input("Enter your product code...")
    if ent == "1637329":
        print ("EliOS API", ELIOSAPI, "Recongnized this product code.")
        print ("Succsefully activated.")
        bootup2()
    else:
        print ("This code is not valid.")
        activate()
def about():
    print ("-------------------------------------ABOUT ELIOS TERMINAL2--------------------------------------------")
    print ("Version: 20.17")
    print ("Storage: 123 GB")
    print ("Product code: 1637329")
    print ("EliOS API:", ELIOSAPI)
    exit = input("Would you like to exit?")
    if exit == "Yes":
        setset()
    else:
        about()
    print ("------------------------------------------------------------------------------------------------------")
# Program running sequence
bootup
EliOSAPI = "www.zincosconfigapi.eliosdconnect.vnc.net/hdivbdjfjejwebfjhbvfn fnvnnkjvrjghjrthgrhgrtghjrgnjrgjbgj1114556776554"
# Computer Functions
def users():
    user = input("Who is using the computer?")
    print ("Welcome,", user)
    print ("If you are on settings, please wait for your computer to boot up")
    setset()
def spacelist():
    spacelist = ["A Rocket", "A Spacesuit", "A Oxgen tank", "Some Space shoes"]
    print ("Wer'e going to space!")
    whatNeed = input("What do you think we need?")
    spacelist.append (whatNeed)
    whatNeed = input("What do you think we need?")
    spacelist.append (whatNeed)
    print ("Let's see what we need...")
    for item in spacelist:
        print (item)
    print ("Wee! Off I go to space!")
def bootup():
    print ("EliOS Terminal2 booting up...")
    for bu in range (0,8):
        print ("64 BYTES OF DATA FROM ELIOS API")
    print ("Downloads Complete")
    print ("Welcome to EliOS")
    users()
def bootup2():
    print ("EliOS Treminal2 booting up...")
    for bu in range (0,8):
        print ("64 BYTES OF DATA FROM ELIOS API")
    print ("Downloads Complete")
    print ("Welcome to EliOS")
    whattodo()  
def castle():
    exitChoice = "Nothing"
    while exitChoice != "EXIT": 
        print ("You are in a dark room in a mysterious castle.")
        print ("In front of you are four doors. You must choose one.")
        playerChoice = input("Choose 1, 2,3 or 4...")
        if playerChoice == "1":
            print ("You finda room full of treasure. You're rich!")
            print ("GAME OVER, YOU WIN.")
        elif playerChoice == "2":
            print ("The door opens and an angry ogre hits you with his club.")
            print ("GAME OVER, YOU LOSE.")
        elif playerChoice == "3":
            print ("You go into the room and find a sleeping dragon.")
            print ("You can either:")
            print ("1) Try to steal some of the dragon's gold.")
            print ("2) Try to sneak around the dragon to the exit.")
        dragonChoice = input("Type 1 or 2...")
        if dragonChoice == "1":
            print ("The dragon wakes up and eats you. You are delicous.")
            print ("GAME OVER, YOU LOSE")
        elif dragonChoice == "2":
             print ("You sneak around the dragon and escape the castle, blinking in the sunlight.")
             print ("GAME OVER! YOU WIN!")
        else:
             print ("Sorry, you didn't enter 1 or 2!")
        if playerChoice == "4":
             print ("You enter a room with a sphinx.")
             print ("It asks you to guess what number it is thinking of, between 1 and 10")
             number = int(input("What number do you choose?"))
        if number == random.randint(1,10):
             print ("The sphinx hisses in dissapointment. You geussed correctly.")
             print ("She must let you go free")
             print ("GAME OVER. YOU WIN")
        else:
             print ("The sphinx tells you that your geuss is incorrect.")
             print ("You are now her prisoner forever.")
             print ("GAME OVER, YOU LOSE")

    else:
        print("Sorry, You didn't enter 1, 2, 3 or 4!")
        exitChoice = input("Press return to play again, or type EXIT to leave.")
        whattodo()
def wifi():
    wifis = ["Cafe Network", "GuestWifi", "MySpectrumNetwork1f-2G", ]
    print ("There are currently 3 wifi networks online. Please select one")
    print ("(1) Cafe Network")
    print ("(2) Guest Network")
    print ("(3) MySpectrumNetwork1f-2g")
    connected = input("Wich one do you want to connect? (Enter the number)")
    print ("Connected to", wifis[int(connected)] )
    whattodo()
def setthetime():
    global time
    time = input("What is the time?")
    print ("The time is", time)
    setset()
def showthetime():
    print ("The time is", time)
def error():
    
    bootup()
def setset():
    print ("Welcome to EliOS setings")
    print ("You can change these:")
    print ("(1) Change the the wifi connection")
    print ("(2) Set the user name")
    print ("(3) Set the time")
    print ("(4) fdhdbdvd")
    print ("(5) Activate your computer")
    print ("(6) About...")
    settings = input("What settings would you like to change (Enter the number or text)")
    if settings == "1":
        wifi()
    elif settings == "2":
        users()
    elif settings == "Change the the wifi connection":
        wifi()
    elif settings == "Set the user name":
        users()
    elif settings == "3":
        setthetime()
    elif settings == "Set the time":
        setthetime()
    elif settings == "Exit":
        whattodo()
    elif settings == "4":
        error()
    elif settings == "5":
        activate()
    elif settings == "6":
        about()                           
def whattodo():
    whatdo = input("What would you like to do?")
    if whatdo == "Email":
        print ("EZincSOt Currlyas no emails.")
        whattodo()
    elif whatdo == "Play a game":
        print ("Two games avlible")
        gamedo = input("Enetr 1 or 2")
        if gamedo == "1":
            castle()
        elif gamedo == "2":
            spacelist() 
    elif whatdo == "Exit":
      print ("Goodbye....")
    elif whatdo == "Settings":
        setset()
    elif whatdo == "ShowTime":
        showthetime()                                                                             
    else:
        print ("EliOS Couldn't find the command '", whatdo, "'")
        whattodo()
def activate():
    print ("EliOS requires your prouduct code. To find it, look at About in EliOS settings")
    ent = input("Enter your product code...")
    if ent == "1637329":
        print ("EliOS API", ELIOSAPI, "Recongnized this product code.")
        print ("Succsefully activated.")
        bootup2()
    else:
        print ("This code is not valid.")
        activate()
def about():
    print ("-------------------------------------ABOUT ELIOS TERMINAL2--------------------------------------------")
    print ("Version: 20.17")
    print ("Storage: 123 GB")
    print ("Product code: 1637329")
    print ("EliOS API:", ELIOSAPI)
    exit = input("Would you like to exit?")
    if exit == "Yes":
        setset()
    else:
        about()
    print ("------------------------------------------------------------------------------------------------------")
# Program running sequence
bootup
EliOSAPI = "www.zincosconfigapi.eliosdconnect.vnc.net/hdivbdjfjejwebfjhbvfn fnvnnkjvrjghjrthgrhgrtghjrgnjrgjbgj1114556776554"
# Computer Functions
def users():
    user = input("Who is using the computer?")
    print ("Welcome,", user)
    print ("If you are on settings, please wait for your computer to boot up")
    setset()
def spacelist():
    spacelist = ["A Rocket", "A Spacesuit", "A Oxgen tank", "Some Space shoes"]
    print ("Wer'e going to space!")
    whatNeed = input("What do you think we need?")
    spacelist.append (whatNeed)
    whatNeed = input("What do you think we need?")
    spacelist.append (whatNeed)
    print ("Let's see what we need...")
    for item in spacelist:
        print (item)
    print ("Wee! Off I go to space!")
def bootup():
    print ("EliOS Terminal2 booting up...")
    for bu in range (0,8):
        print ("64 BYTES OF DATA FROM ELIOS API")
    print ("Downloads Complete")
    print ("Welcome to EliOS")
    users()
def bootup2():
    print ("EliOS Treminal2 booting up...")
    for bu in range (0,8):
        print ("64 BYTES OF DATA FROM ELIOS API")
    print ("Downloads Complete")
    print ("Welcome to EliOS")
    whattodo()  
def castle():
    exitChoice = "Nothing"
    while exitChoice != "EXIT": 
        print ("You are in a dark room in a mysterious castle.")
        print ("In front of you are four doors. You must choose one.")
        playerChoice = input("Choose 1, 2,3 or 4...")
        if playerChoice == "1":
            print ("You finda room full of treasure. You're rich!")
            print ("GAME OVER, YOU WIN.")
        elif playerChoice == "2":
            print ("The door opens and an angry ogre hits you with his club.")
            print ("GAME OVER, YOU LOSE.")
        elif playerChoice == "3":
            print ("You go into the room and find a sleeping dragon.")
            print ("You can either:")
            print ("1) Try to steal some of the dragon's gold.")
            print ("2) Try to sneak around the dragon to the exit.")
        dragonChoice = input("Type 1 or 2...")
        if dragonChoice == "1":
            print ("The dragon wakes up and eats you. You are delicous.")
            print ("GAME OVER, YOU LOSE")
        elif dragonChoice == "2":
             print ("You sneak around the dragon and escape the castle, blinking in the sunlight.")
             print ("GAME OVER! YOU WIN!")
        else:
             print ("Sorry, you didn't enter 1 or 2!")
        if playerChoice == "4":
             print ("You enter a room with a sphinx.")
             print ("It asks you to guess what number it is thinking of, between 1 and 10")
             number = int(input("What number do you choose?"))
        if number == random.randint(1,10):
             print ("The sphinx hisses in dissapointment. You geussed correctly.")
             print ("She must let you go free")
             print ("GAME OVER. YOU WIN")
        else:
             print ("The sphinx tells you that your geuss is incorrect.")
             print ("You are now her prisoner forever.")
             print ("GAME OVER, YOU LOSE")

    else:
        print("Sorry, You didn't enter 1, 2, 3 or 4!")
        exitChoice = input("Press return to play again, or type EXIT to leave.")
        whattodo()
def wifi():
    wifis = ["Cafe Network", "GuestWifi", "MySpectrumNetwork1f-2G", ]
    print ("There are currently 3 wifi networks online. Please select one")
    print ("(1) Cafe Network")
    print ("(2) Guest Network")
    print ("(3) MySpectrumNetwork1f-2g")
    connected = input("Wich one do you want to connect? (Enter the number)")
    print ("Connected to", wifis[int(connected)] )
    whattodo()
def setthetime():
    global time
    time = input("What is the time?")
    print ("The time is", time)
    setset()
def showthetime():
    print ("The time is", time)
def error():
    
    bootup()
def setset():
    print ("Welcome to EliOS setings")
    print ("You can change these:")
    print ("(1) Change the the wifi connection")
    print ("(2) Set the user name")
    print ("(3) Set the time")
    print ("(4) fdhdbdvd")
    print ("(5) Activate your computer")
    print ("(6) About...")
    settings = input("What settings would you like to change (Enter the number or text)")
    if settings == "1":
        wifi()
    elif settings == "2":
        users()
    elif settings == "Change the the wifi connection":
        wifi()
    elif settings == "Set the user name":
        users()
    elif settings == "3":
        setthetime()
    elif settings == "Set the time":
        setthetime()
    elif settings == "Exit":
        whattodo()
    elif settings == "4":
        error()
    elif settings == "5":
        activate()
    elif settings == "6":
        about()                           
def whattodo():
    whatdo = input("What would you like to do?")
    if whatdo == "Email":
        print ("EZincSOt Currlyas no emails.")
        whattodo()
    elif whatdo == "Play a game":
        print ("Two games avlible")
        gamedo = input("Enetr 1 or 2")
        if gamedo == "1":
            castle()
        elif gamedo == "2":
            spacelist() 
    elif whatdo == "Exit":
      print ("Goodbye....")
    elif whatdo == "Settings":
        setset()
    elif whatdo == "ShowTime":
        showthetime()                                                                             
    else:
        print ("EliOS Couldn't find the command '", whatdo, "'")
        whattodo()
def activate():
    print ("EliOS requires your prouduct code. To find it, look at About in EliOS settings")
    ent = input("Enter your product code...")
    if ent == "1637329":
        print ("EliOS API", ELIOSAPI, "Recongnized this product code.")
        print ("Succsefully activated.")
        bootup2()
    else:
        print ("This code is not valid.")
        activate()
def about():
    print ("-------------------------------------ABOUT ELIOS TERMINAL2--------------------------------------------")
    print ("Version: 20.17")
    print ("Storage: 123 GB")
    print ("Product code: 1637329")
    print ("EliOS API:", ELIOSAPI)
    exit = input("Would you like to exit?")
    if exit == "Yes":
        setset()
    else:
        about()
    print ("------------------------------------------------------------------------------------------------------")
# Program running sequence
bootup

EliOSAPI = "www.zincosconfigapi.eliosdconnect.vnc.net/hdivbdjfjejwebfjhbvfn fnvnnkjvrjghjrthgrhgrtghjrgnjrgjbgj1114556776554"
# Computer Functions
def users():
    user = input("Who is using the computer?")
    print ("Welcome,", user)
    print ("If you are on settings, please wait for your computer to boot up")
    setset()
def spacelist():
    spacelist = ["A Rocket", "A Spacesuit", "A Oxgen tank", "Some Space shoes"]
    print ("Wer'e going to space!")
    whatNeed = input("What do you think we need?")
    spacelist.append (whatNeed)
    whatNeed = input("What do you think we need?")
    spacelist.append (whatNeed)
    print ("Let's see what we need...")
    for item in spacelist:
        print (item)
    print ("Wee! Off I go to space!")
def bootup():
    print ("EliOS Terminal2 booting up...")
    for bu in range (0,8):
        print ("64 BYTES OF DATA FROM ELIOS API")
    print ("Downloads Complete")
    print ("Welcome to EliOS")
    users()
def bootup2():
    print ("EliOS Treminal2 booting up...")
    for bu in range (0,8):
        print ("64 BYTES OF DATA FROM ELIOS API")
    print ("Downloads Complete")
    print ("Welcome to EliOS")
    whattodo()  
def castle():
    exitChoice = "Nothing"
    while exitChoice != "EXIT": 
        print ("You are in a dark room in a mysterious castle.")
        print ("In front of you are four doors. You must choose one.")
        playerChoice = input("Choose 1, 2,3 or 4...")
        if playerChoice == "1":
            print ("You finda room full of treasure. You're rich!")
            print ("GAME OVER, YOU WIN.")
        elif playerChoice == "2":
            print ("The door opens and an angry ogre hits you with his club.")
            print ("GAME OVER, YOU LOSE.")
        elif playerChoice == "3":
            print ("You go into the room and find a sleeping dragon.")
            print ("You can either:")
            print ("1) Try to steal some of the dragon's gold.")
            print ("2) Try to sneak around the dragon to the exit.")
        dragonChoice = input("Type 1 or 2...")
        if dragonChoice == "1":
            print ("The dragon wakes up and eats you. You are delicous.")
            print ("GAME OVER, YOU LOSE")
        elif dragonChoice == "2":
             print ("You sneak around the dragon and escape the castle, blinking in the sunlight.")
             print ("GAME OVER! YOU WIN!")
        else:
             print ("Sorry, you didn't enter 1 or 2!")
        if playerChoice == "4":
             print ("You enter a room with a sphinx.")
             print ("It asks you to guess what number it is thinking of, between 1 and 10")
             number = int(input("What number do you choose?"))
        if number == random.randint(1,10):
             print ("The sphinx hisses in dissapointment. You geussed correctly.")
             print ("She must let you go free")
             print ("GAME OVER. YOU WIN")
        else:
             print ("The sphinx tells you that your geuss is incorrect.")
             print ("You are now her prisoner forever.")
             print ("GAME OVER, YOU LOSE")

    else:
        print("Sorry, You didn't enter 1, 2, 3 or 4!")
        exitChoice = input("Press return to play again, or type EXIT to leave.")
        whattodo()
def wifi():
    wifis = ["Cafe Network", "GuestWifi", "MySpectrumNetwork1f-2G", ]
    print ("There are currently 3 wifi networks online. Please select one")
    print ("(1) Cafe Network")
    print ("(2) Guest Network")
    print ("(3) MySpectrumNetwork1f-2g")
    connected = input("Wich one do you want to connect? (Enter the number)")
    print ("Connected to", wifis[int(connected)] )
    whattodo()
def setthetime():
    global time
    time = input("What is the time?")
    print ("The time is", time)
    setset()
def showthetime():
    print ("The time is", time)
def error():
    
    bootup()
def setset():
    print ("Welcome to EliOS setings")
    print ("You can change these:")
    print ("(1) Change the the wifi connection")
    print ("(2) Set the user name")
    print ("(3) Set the time")
    print ("(4) fdhdbdvd")
    print ("(5) Activate your computer")
    print ("(6) About...")
    settings = input("What settings would you like to change (Enter the number or text)")
    if settings == "1":
        wifi()
    elif settings == "2":
        users()
    elif settings == "Change the the wifi connection":
        wifi()
    elif settings == "Set the user name":
        users()
    elif settings == "3":
        setthetime()
    elif settings == "Set the time":
        setthetime()
    elif settings == "Exit":
        whattodo()
    elif settings == "4":
        error()
    elif settings == "5":
        activate()
    elif settings == "6":
        about()                           
def whattodo():
    whatdo = input("What would you like to do?")
    if whatdo == "Email":
        print ("EZincSOt Currlyas no emails.")
        whattodo()
    elif whatdo == "Play a game":
        print ("Two games avlible")
        gamedo = input("Enetr 1 or 2")
        if gamedo == "1":
            castle()
        elif gamedo == "2":
            spacelist() 
    elif whatdo == "Exit":
      print ("Goodbye....")
    elif whatdo == "Settings":
        setset()
    elif whatdo == "ShowTime":
        showthetime()                                                                             
    else:
        print ("EliOS Couldn't find the command '", whatdo, "'")
        whattodo()
def activate():
    print ("EliOS requires your prouduct code. To find it, look at About in EliOS settings")
    ent = input("Enter your product code...")
    if ent == "1637329":
        print ("EliOS API", ELIOSAPI, "Recongnized this product code.")
        print ("Succsefully activated.")
        bootup2()
    else:
        print ("This code is not valid.")
        activate()
def about():
    print ("-------------------------------------ABOUT ELIOS TERMINAL2--------------------------------------------")
    print ("Version: 20.17")
    print ("Storage: 123 GB")
    print ("Product code: 1637329")
    print ("EliOS API:", ELIOSAPI)
    exit = input("Would you like to exit?")
    if exit == "Yes":
        setset()
    else:
        about()
    print ("------------------------------------------------------------------------------------------------------")
# Program running sequence
bootup

EliOSAPI = "www.zincosconfigapi.eliosdconnect.vnc.net/hdivbdjfjejwebfjhbvfn fnvnnkjvrjghjrthgrhgrtghjrgnjrgjbgj1114556776554"
# Computer Functions
def users():
    user = input("Who is using the computer?")
    print ("Welcome,", user)
    print ("If you are on settings, please wait for your computer to boot up")
    setset()
def spacelist():
    spacelist = ["A Rocket", "A Spacesuit", "A Oxgen tank", "Some Space shoes"]
    print ("Wer'e going to space!")
    whatNeed = input("What do you think we need?")
    spacelist.append (whatNeed)
    whatNeed = input("What do you think we need?")
    spacelist.append (whatNeed)
    print ("Let's see what we need...")
    for item in spacelist:
        print (item)
    print ("Wee! Off I go to space!")
def bootup():
    print ("EliOS Terminal2 booting up...")
    for bu in range (0,8):
        print ("64 BYTES OF DATA FROM ELIOS API")
    print ("Downloads Complete")
    print ("Welcome to EliOS")
    users()
def bootup2():
    print ("EliOS Treminal2 booting up...")
    for bu in range (0,8):
        print ("64 BYTES OF DATA FROM ELIOS API")
    print ("Downloads Complete")
    print ("Welcome to EliOS")
    whattodo()  
def castle():
    exitChoice = "Nothing"
    while exitChoice != "EXIT": 
        print ("You are in a dark room in a mysterious castle.")
        print ("In front of you are four doors. You must choose one.")
        playerChoice = input("Choose 1, 2,3 or 4...")
        if playerChoice == "1":
            print ("You finda room full of treasure. You're rich!")
            print ("GAME OVER, YOU WIN.")
        elif playerChoice == "2":
            print ("The door opens and an angry ogre hits you with his club.")
            print ("GAME OVER, YOU LOSE.")
        elif playerChoice == "3":
            print ("You go into the room and find a sleeping dragon.")
            print ("You can either:")
            print ("1) Try to steal some of the dragon's gold.")
            print ("2) Try to sneak around the dragon to the exit.")
        dragonChoice = input("Type 1 or 2...")
        if dragonChoice == "1":
            print ("The dragon wakes up and eats you. You are delicous.")
            print ("GAME OVER, YOU LOSE")
        elif dragonChoice == "2":
             print ("You sneak around the dragon and escape the castle, blinking in the sunlight.")
             print ("GAME OVER! YOU WIN!")
        else:
             print ("Sorry, you didn't enter 1 or 2!")
        if playerChoice == "4":
             print ("You enter a room with a sphinx.")
             print ("It asks you to guess what number it is thinking of, between 1 and 10")
             number = int(input("What number do you choose?"))
        if number == random.randint(1,10):
             print ("The sphinx hisses in dissapointment. You geussed correctly.")
             print ("She must let you go free")
             print ("GAME OVER. YOU WIN")
        else:
             print ("The sphinx tells you that your geuss is incorrect.")
             print ("You are now her prisoner forever.")
             print ("GAME OVER, YOU LOSE")

    else:
        print("Sorry, You didn't enter 1, 2, 3 or 4!")
        exitChoice = input("Press return to play again, or type EXIT to leave.")
        whattodo()
def wifi():
    wifis = ["Cafe Network", "GuestWifi", "MySpectrumNetwork1f-2G", ]
    print ("There are currently 3 wifi networks online. Please select one")
    print ("(1) Cafe Network")
    print ("(2) Guest Network")
    print ("(3) MySpectrumNetwork1f-2g")
    connected = input("Wich one do you want to connect? (Enter the number)")
    print ("Connected to", wifis[int(connected)] )
    whattodo()
def setthetime():
    global time
    time = input("What is the time?")
    print ("The time is", time)
    setset()
def showthetime():
    print ("The time is", time)
def error():
    
    bootup()
def setset():
    print ("Welcome to EliOS setings")
    print ("You can change these:")
    print ("(1) Change the the wifi connection")
    print ("(2) Set the user name")
    print ("(3) Set the time")
    print ("(4) fdhdbdvd")
    print ("(5) Activate your computer")
    print ("(6) About...")
    settings = input("What settings would you like to change (Enter the number or text)")
    if settings == "1":
        wifi()
    elif settings == "2":
        users()
    elif settings == "Change the the wifi connection":
        wifi()
    elif settings == "Set the user name":
        users()
    elif settings == "3":
        setthetime()
    elif settings == "Set the time":
        setthetime()
    elif settings == "Exit":
        whattodo()
    elif settings == "4":
        error()
    elif settings == "5":
        activate()
    elif settings == "6":
        about()                           
def whattodo():
    whatdo = input("What would you like to do?")
    if whatdo == "Email":
        print ("EZincSOt Currlyas no emails.")
        whattodo()
    elif whatdo == "Play a game":
        print ("Two games avlible")
        gamedo = input("Enetr 1 or 2")
        if gamedo == "1":
            castle()
        elif gamedo == "2":
            spacelist() 
    elif whatdo == "Exit":
      print ("Goodbye....")
    elif whatdo == "Settings":
        setset()
    elif whatdo == "ShowTime":
        showthetime()                                                                             
    else:
        print ("EliOS Couldn't find the command '", whatdo, "'")
        whattodo()
def activate():
    print ("EliOS requires your prouduct code. To find it, look at About in EliOS settings")
    ent = input("Enter your product code...")
    if ent == "1637329":
        print ("EliOS API", ELIOSAPI, "Recongnized this product code.")
        print ("Succsefully activated.")
        bootup2()
    else:
        print ("This code is not valid.")
        activate()
def about():
    print ("-------------------------------------ABOUT ELIOS TERMINAL2--------------------------------------------")
    print ("Version: 20.17")
    print ("Storage: 123 GB")
    print ("Product code: 1637329")
    print ("EliOS API:", ELIOSAPI)
    exit = input("Would you like to exit?")
    if exit == "Yes":
        setset()
    else:
        about()
    print ("------------------------------------------------------------------------------------------------------")
# Program running sequence
bootup

EliOSAPI = "www.zincosconfigapi.eliosdconnect.vnc.net/hdivbdjfjejwebfjhbvfn fnvnnkjvrjghjrthgrhgrtghjrgnjrgjbgj1114556776554"
# Computer Functions
def users():
    user = input("Who is using the computer?")
    print ("Welcome,", user)
    print ("If you are on settings, please wait for your computer to boot up")
    setset()
    return 69
def spacelist():
    spacelist = ["A Rocket", "A Spacesuit", "A Oxgen tank", "Some Space shoes"]
    print ("Wer'e going to space!")
    whatNeed = input("What do you think we need?")
    spacelist.append (whatNeed)
    whatNeed = input("What do you think we need?")
    spacelist.append (whatNeed)
    print ("Let's see what we need...")
    print ("The End. Oh were you expecting a game, maybe press one next time")
    for item in spacelist:
        print (item)
    print ("Wee! Off I go to space!")
def bootup():
    print ("CahOS Terminal2 booting up...")
    for bu in range (0,8):
        print ("64 BYTES OF DATA FROM CahOS API")
    print ("Downloads Complete")
    print ("Welcome to CahOS")
    users()
def bootup2():
    print ("CahOS Treminal2 booting up...")
    for bu in range (0,8):
        print ("64 BYTES OF DATA FROM CagOS API")
    print ("Downloads Complete")
    print ("Welcome to CahOS")
    whattodo()  
def castle():
    exitChoice = "Nothing"
    while exitChoice != "EXIT": 
        print ("You are in a dark room in a mysterious castle.")
        print ("In front of you are four doors. You must choose one.")
        playerChoice = input("Choose 1, 2,3 or 4...")
        if playerChoice == "1":
            print ("You finda room full of treasure. You're rich!")
            print ("GAME OVER, YOU WIN.")
        elif playerChoice == "2":
            print ("The door opens and an angry ogre hits you with his club.")
            print ("GAME OVER, YOU LOSE.")
        elif playerChoice == "3":
            print ("You go into the room and find a sleeping dragon.")
            print ("You can either:")
            print ("1) Try to steal some of the dragon's gold.")
            print ("2) Try to sneak around the dragon to the exit.")
        dragonChoice = input("Type 1 or 2...")
        if dragonChoice == "1":
            print ("The dragon wakes up and eats you. You are delicous.")
            print ("GAME OVER, YOU LOSE")
        elif dragonChoice == "2":
             print ("You sneak around the dragon and escape the castle, blinking in the sunlight.")
             print ("GAME OVER! YOU WIN!")
        else:
             print ("Sorry, you didn't enter 1 or 2!")
        if playerChoice == "4":
             print ("You enter a room with a sphinx.")
             print ("It asks you to guess what number it is thinking of, between 1 and 10")
             number = int(input("What number do you choose?"))
        if number == random.randint(1,10):
             print ("The sphinx hisses in dissapointment. You geussed correctly.")
             print ("She must let you go free")
             print ("GAME OVER. YOU WIN")
        else:
             print ("The sphinx tells you that your geuss is incorrect.")
             print ("You are now her prisoner forever.")
             print ("GAME OVER, YOU LOSE")

    else:
        print("Sorry, You didn't enter 1, 2, 3 or 4!")
        exitChoice = input("Press return to play again, or type EXIT to leave.")
        whattodo()
def wifi():
    wifis = ["School Network", "BT-Hub87 Network", "MyVodafone-4G", ]
    print ("There are currently 3 wifi networks online. Please select one")
    print ("(1) School Network")
    print ("(2) BT-Hub87 Network")
    print ("(3) MyVodafone-4G")
    connected = input("Wich one do you want to connect? (Enter the number)")
    print ("Connected to", wifis[int(connected)] )
    whattodo()
def setthetime():
    global time
    time = input("What is the time?")
    print ("The time is", time)
    setset()
def showthetime():
    print ("The time is", time)
def error():
    
    bootup()
def setset():
    print ("Welcome to CahOS setings")
    print ("You can change these:")
    print ("(1) Change the the wifi connection")
    print ("(2) Set the user name")
    print ("(3) Set the time")
    print ("(4) fdhdbdvd")
    print ("(5) Activate your computer")
    print ("(6) About...")
    settings = input("What settings would you like to change (Enter the number or text)")
    if settings == "1":
        wifi()
    elif settings == "2":
        users()
    elif settings == "Change the the wifi connection":
        wifi()
    elif settings == "Set the user name":
        users()
    elif settings == "3":
        setthetime()
    elif settings == "Set the time":
        setthetime()
    elif settings == "Exit":
        whattodo()
    elif settings == "4":
        error()
    elif settings == "5":
        activate()
    elif settings == "6":
        about()                           
def whattodo():
    whatdo = input("What would you like to do?")
    if whatdo == "Email":
        print ("EZincSOt Currlyas no emails.")
        return 69
        whattodo()
    elif whatdo == "Play a game":
        print ("Two games avlible")
        gamedo = input("Enetr 1 or 2")
        if gamedo == "1":
            castle()
        elif gamedo == "2":
            spacelist() 
        return 69
    elif whatdo == "Commands":
      print("Play a game")
      print("Exit")
      print("Settings")
      print("ShowTime")
      print("Email")
      return 69
    elif whatdo == "Exit":
      print ("Goodbye....")
      return 2
    elif whatdo == "Settings":
        setset()
        return 69
    elif whatdo == "ShowTime":
        showthetime()         
        return 69
    else:
        print ("CahOS Couldn't find the command '", whatdo, "'")
        whattodo()
def activate():
    print ("CahOS requires your prouduct code. To find it, look at About in CahOS settings")
    ent = input("Enter your product code...")
    if ent == "1637329" or ent == "255":
        print ("CahOS API", EliOSAPI, "Recongnized this product code.")
        print ("Succsefully activated.")
        bootup2()
    else:
        print ("This code is not valid.")
        activate()
def about():
    print ("-------------------------------------ABOUT CAH--------------------------------------------")
    print ("Version: 1.8")
    print ("Storage: 17.7Mb")
    print ("Product code: 1637329")
    print ("CahOS API:", EliOSAPI)
    exit = input("Would you like to exit?")
    if exit == "Yes":
        setset()
    else:
        about()
    print ("------------------------------------------------------------------------------------------------------")
# Program running sequence
bootup

