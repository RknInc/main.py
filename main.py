#import moduals
import time 
import random 
import sys
import os
import colorama

#Type effect
def typewriter(text, speed=0.05):
    """Print text one character at a time like a Pokémon-style text box."""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()  # Ensures the character is printed immediately
        time.sleep(speed)   # Adjust speed for slower/faster text
    print()  # Move to a new line after the text is done

#Minigame Segments:
def mayor_orchard():
  os.system('clear')
  global total_apples
  total_apples = (0)
  total_achivement_apples = (5)
  typewriter("---------Mini Game---------")
  print(colorama.Fore.GREEN + """
              .        +          .      .          .
     .            _        .                    .
  ,              /;-._,-.____        ,-----.__
 ((        .    (_:#::_.:::. `-._   /:, /-._, `._,
  `                 \   _|`"=:_::.`.);  \ __/ /
                      ,    `./  \:. `.   )==-'  .
    .      ., ,-=-.  ,\, +#./`   \:.  / /           .
.           \/:/`-' , ,\ '` ` `   ): , /_  -o
       .    /:+- - + +- : :- + + -:'  /(o-) \)     .
  .      ,=':  \    ` `/` ' , , ,:' `'--".--"---._/`7
   `.   (    \: \,-._` ` + '\, ,"   _,--._,---":.__/
              \:  `  X` _| _,\/'   .-'
.               ":._:`\____  /:'  /      .           .
                    \::.  :\/:'  /              +
   .                 `.:.  /:'  }      .
           .           ):_(:;   \           .
                      /:. _/ ,  |
                   . (|::.     ,`                  .
     .                |::.    {\
                      |::.\  \ `.
                      |:::(\    |
              O       |:::/{ }  |                  (o
               )  ___/#\::`/ (O "==._____   O, (O  /`
          ~~~w/w~"~~,\` `:/,-(~`"~~~~~~~~"~o~\~/~w|/~
dew   ~~~~~~~~~~~~~~~~~~~~~~~\\W~~~~~~~~~~~~\|/~~

------------------------------------------------
""")
  time.sleep(0.5)
  typewriter("Sign: Welcome to the Mayor's Orchard!")
  time.sleep(0.5)
  typewriter("Sign: You Will Need to Choose 3 Trees To Shake")
  time.sleep(0.5)
  typewriter("Sign: If You Shake Them All Correctly, You Will Recieve a apple")
  time.sleep(0.5)
  typewriter("Sign: If You Shake Them Incorrectly, You Will Drop a apple")
  time.sleep(0.5)
  typewriter("Sign: You Need A Total Of 5 Apples To Win Bring Back To The Mayor")
  time.sleep(0.5)
  typewriter("Sign: Good Luck!")
  time.sleep(0.5)
  for x in range(total_achivement_apples):
    treenum = random.randint(1,3)
    treeawns = input(typewriter("Sign: Which Tree Do You Want To Shake? (1, 2, or 3):"))
    treeawns = int(treeawns)

    typewriter("You Shake The Tree...")
    if treeawns == treenum:
      typewriter("You Recieve An Apple!")
      total_apples += 1
  else:
      typewriter("You Drop An Apple!")
      total_apples -= 1
  typewriter("Well Done! You Have Recieved " + str(total_apples) + " Apples!")
  time.sleep(0.5)
  typewriter("Sign: Here You Go! Have " + str(total_achivement_apples - total_apples) + " Apples!")
  total_apples = (5)
  time.sleep(0.5)
  typewriter("Sign: Now, Go Back To The Mayor!")
  time.sleep(0.5)
  typewriter("Sign: *You Head Back To The TownHall*")
  time.sleep(0.5)
  TownHallGuiFinMayorOrchard()
  

def TownHallGuiFinMayorOrchard():
  os.system('clear')
  typewriter("---------TownHall---------")
  typewriter("Mayor: Welcome Back! I Hope You Didn't Forget About The Orchard")
  time.sleep(0.5)
  typewriter(name + ": I Didn't Forget About The Orchard")
  time.sleep(0.5)
  typewriter("Mayor: Well, Give Me The Apples Then")
  time.sleep(0.5)
  typewriter("*You Give The Apples To The Mayor*")
  time.sleep(0.5)
  typewriter("Mayor: Thank You! Now For Your Reward")
  time.sleep(0.5)
  typewriter("**You Have Recived 10 Gold And 1 Room Key For TownHall Bedroom**")
  global gold
  gold = (gold + 10)
  save()
  time.sleep(0.5)
  typewriter("*You Head Back To The Town Center Where*")
  segment2()
  
  
  

  
             
    
    
    
  

#Game Segments For SAVE AND LOAD

def segment1():
  global segment
  segment = (1)
  print("*Autosaving*")
  os.system('clear')
  save()
  header()
  time.sleep(0.5)
  print("Begining Game...")
  time.sleep(1)
  typewriter("Dialogue: You have awaken in a land.. Unlike home but weirdly similar..", 0.08)
  time.sleep(0.5)
  typewriter(f"{name}: Woah.. Where am I, this isnt home..", 0.08)
  time.sleep(0.5)
  typewriter("Dialogue: You look around and see a small village in the distance..", 0.08)
  time.sleep(0.5)
  gotovillage = input(typewriter("**Enter 'W' to walk to the village**"))
  if gotovillage == "W":
    typewriter("** walking to the village.. **")
    time.sleep(0.5)
    os.system('clear')
    segment2()


def segment2():
  global segment
  global buildinggo
  segment = (2)
  print("*Autosaving*")
  os.system('clear')
  save()
  header()
  time.sleep(1)
  print("*Village murmours*")
  time.sleep(0.5)
  typewriter(name + ": Woah.. This is like a stone aged town.. Everyone looks so different to home.." , 0.08)
  time.sleep(0.5)
  print("** You see a couple buildings.. What one do you want to go to?**")
  print("-----------------------------------------------------------")
  print("Building list: Town Hall [TH], Blacksmith [B], Old Pub [OP]")
  buildinggo = input("-----------------------------------------------------------")
  if buildinggo == "TH":
    os.system('clear')
    Town_Hall()
    
  if buildinggo == "B":
    os.system('clear')
    Blacksmith()
    
  if buildinggo == "OP":
    os.system('clear')
    Old_Pub()
  
def Town_Hall():
  global townhalldialog
  global townhalldialog2
  townhalldialog2 = ("0")
  townhalldialog = ("0")
  typewriter("--New Achivement Unlocked (Enter The Town Hall!)--")
  typewriter("** You walk to the Town Hall **,")
  time.sleep(0.5)
  typewriter("*Mayor Gets Spooked By " + name + "*", 0.08)
  time.sleep(0.5)
  typewriter("Mayor: Hey! What are you doing here?!", 0.08)
  time.sleep(0.5)
  townhalldialog = input(typewriter(name + """:
  1)*Im just passing by*
  2)*Can you Help Me?*""", 0.08))
  if townhalldialog == ("1"):
      typewriter("Mayor: Oh.. Thats fine..", 0.08)
      time.sleep(0.5)
      typewriter("Mayor: What Brings You Here Anyways?", 0.08)
      time.sleep(0.5)
      typewriter(name + ": Im Not Too Sure I Woke Up Here?", 0.08)
      time.sleep(0.5)
      typewriter("Mayor: Well.. I cant remember hearing anything last night?", 0.08)
      time.sleep(0.5)
      typewriter("Mayor: Perhaps I Had A Bit Too Much Orange Juice", 0.08)
      time.sleep(0.5)
      typewriter("""Mayor: Anyways.. Whilst Your Here If You Do Me A Favour
      I will make it worth your while
      how does 10 Gold and a place to sleep for the remainding time your here   sound?""", 0.08) 
      townhalldialog2 = input(typewriter(name + """:
      1) Okay Hit Me!
      2) Im Going To Explore For A While"""))
  if townhalldialog2 == ("1"):
      typewriter("Mayor: Okay So Tommorow Is The Towns national Apple Day")
      time.sleep(0.5)
      typewriter("Mayor: So I Need You To Go To The Apple Orchard And Pick Some   Apples For Me")
      time.sleep(0.5)
      typewriter("Sound Good?")
      typewriter(name + ": Yeah Sounds Good" , 0.08)
      time.sleep(0.5)
      typewriter("Mayor: Okay Ill See You Tommorow")
      time.sleep(0.5)
      typewriter("Mayor: Good Luck")
      mayor_orchard()
  if townhalldialog2 == ("2"):
      typewriter("Mayor: Okay See you later")
      time.sleep(0.5)
      typewriter("*You Return To The Town Center*")
      time.sleep(0.5)
      os.system('clear')
      segment2()
   
  else:
    typewriter("""Mayor: Well The Only Information I Can Give You Right Now Is That The Town Has A Apple Day Tommorrow 
    (*Mumbles I Love Apples*)""")
    time.sleep(0.5)
    typewriter(name + ": Okay ThankYou")
    time.sleep(0.5)
    typewriter("Mayor: Good Luck")
    os.system('clear')
    typewriter("You Return To The City Center")
    segment2()

def Blacksmith():
  global blacksmithdialog
  global blacksmithdialog2
  blacksmithdialog2 = ("0")
  blacksmithdialog = ("0")
  typewriter("--New Achivement Unlocked (Enter The Blacksmiths!)--")
  typewriter("** You Walk To The Blacksmith **")
  time.sleep(0.5)
  typewriter("Blacksmith: Welcome, what can I do for you?" , 0.08)
  time.sleep(0.5)
  blacksmithdialog = input(typewriter(name + """:
  1)*Im just passing by*
  2)*Whats this your doing?*""", 0.08))
  if blacksmithdialog == ("1"):
    typewriter("Blacksmith: Ah.. I see..", 0.08)
    time.sleep(0.5)
    typewriter("Blacksmith: Do I know you? Never seen you around before ay.", 0.08)
    time.sleep(0.5)
    typewriter(name + ": Funny you mention.. I sort off woke up here?", 0.08)
    time.sleep(0.5)
    typewriter("Blacksmith: Woke up here? Never heard anything like it! ", 0.08)
    time.sleep(0.5)
    typewriter("Blacksmith: I Blame the old pub down the rode, me mate forgets who is down there.. poor bloke.", 0.08)
    time.sleep(0.5)
    typewriter("""Blacksmith: Anyways, if your 'ave woken up here you ought to need some proction. This is no easy place...'?""", 0.08) 
    time.sleep(0.5)
    typewriter(name + ": Protection?.. What is this place?", 0.08)
    time.sleep(0.5)
    typewriter("Blacksmith: Ay forget I said anything, Its lovely here.. Just take this will yah.", 0.08)
    time.sleep(0.5)
    typewriter("--New Achivement Unlocked (What protection?)--", 0.08)
    typewriter("--The Blacksmith has given you a pocket knife--", 0.08)
    time.sleep(0.5)
    typewriter(name + ": Uhmm thank you sir, be sure to see you soon..", 0.08)
    time.sleep(0.5)
    typewriter("Blacksmith: Good luck out there..", 0.08)
    time.sleep(0.5)
    typewriter(name + ": Pardon?..",0.08)
    typewriter("Blacksmith: Uhm sorry, I said Good bye have fun out there..", 0.08)
    time.sleep(0.5)
    typewriter(name +": Uhm okay.. thank you..", 0.08)
    segment(2)
  else:
    typewriter(name + ": Whats this your doing?", 0.08)
    time.sleep(0.5)
    typewriter("Blacksmith: Normally people say hello first.. Anyway Im the Town Blacksmith, I've been here for a while..", 0.08)  
    time.sleep(0.5)
    typewriter(name +"Sorry, this is all to knew to me.. Are you selling anything?", 0.08)
    time.sleep(0.5)
    typewriter("Blacksmith: New here ay? Well I've never seen you before to be fair. ",0.08)
    time.sleep(0.5)
    typewriter("Blacksmith: And I am selling. Its weapons though.. You got ID?", 0.08)
    time.sleep(0.5)
    typewriter(name +": ID you ask... Uhm no?", 0.08)
    time.sleep(0.25)
    typewriter("Blacksmith: No ID cant sell sorry however you will need something out here.", 0.08)
    time.sleep(0.5)
    typewriter(name +": Uhmm.. What do you mean?", 0.08)
    time.sleep(0.5)
    typewriter("Blacksmith: Ay forget I said anything.. Just Take this its on the house.. ", 0.08)
    typewriter("--New Achivement Unlocked (You'll need this..)--", 0.08)
    typewriter("--The Blacksmith has given you a pocket knife--", 0.08)
    time.sleep(0.5)
    typewriter(name + ": Well thank you.. I ought to be off now. See you soon", 0.08)
    time.sleep(0.5)
    typewriter("Blacksmith: See yah soon nipper...", 0.08)
    segment(2)

def Old_Pub():
  global oldpubdialog
  global oldpubdialog2
  oldpubdialog2 = ("0")
  oldpubdialog = ("0")
  typewriter("--New Achivement Unlocked (Enter The Old Pub!)--")
  typewriter("** You Walk To The Old Pub **")
  time.sleep(0.5)
  print("** Pub Murmours **")
  time.sleep(0.5)
  goovertomystery = input(typewriter("""???: Whos that new nipper over there..
  1)*Walk up to  him*
  2)*Ignore him and go up to the bar*""", 0.08))
  if goovertomystery == ("1"):
    typewriter("** Walking to the mysterious person **", 0.08)
    time.sleep(0.5)
    typewriter("???: Hey! Who are you.. Your no local.", 0.08)
    time.sleep(0.5)
    typewriter(name + ": I'm" + name + ", Who are you?", 0.08)
    time.sleep(0.5)
    typewriter("???: I'm the Mayors Butler.. Whats gotten you here?", 0.08)
    time.sleep(0.5)
    typewriter(name + ": I seemed to have woken up here..", 0.08)
    time.sleep(0.5)
    typewriter("Mayors Butler: Woken up here!! You must be off your rocker! Never heard such a thing..", 0.08)
    time.sleep(0.5)
    typewriter(name + ": I know.. It sounds like I've lost it but i promise its true..", 0.08)
    time.sleep(0.5)
    typewriter("Mayors Butler: Well.. If you say so.. You must be thursty, Take some gold and get a drink.", 0.08)
    time.sleep(0.5)
    typewriter("--New Achivement Unlocked (Put it on my tab!)--")
    typewriter("** The Mayors Butler gives you '2 Gold'! **")
    gold = (gold + 2)
    time.sleep(0.5)
    typewriter(name + ": Thank you.. I ought to get my drink now.", 0.08)
    typewriter("** You walk up the the bar **")
    time.sleep(0.5)
    typewriter("Barista: Hello, What can I get you?", 0.08)
    print("----------------------------------------------------------------------------")
    print("Drinks menu: Water [W] (1 Gold), Apple Juice [AJ] (2 Gold), Orange Juice [OJ] (2 Gold), The Mayors Magic Mix [MM] (5 Gold)")
    print("----------------------------------------------------------------------------")
    drinkchoice = input(typewriter("** What do you fancy? **", 0.08))
    if drinkchoice == ("W"):
      typewriter(name +": I'll take a water please.", 0.08)
      time.sleep(0.5)
      typewriter("Barista: No problem, coming right up..", 0.08)
      time.sleep(0.5)
      typewriter("Barista: Here you are.. 1 Gold Please.", 0.08)
      time.sleep(0.5)
      typewriter(name +": Thank you, and here you go.", 0.08)
      gold = (gold - 1)
      typewriter("Barista: Thank you enjoy!", 0.08)
      time.sleep(0.5)
      typewriter(name + ": I will thank you, see you later!", 0.08)
      time.sleep(0.5)
      typewriter("** You Have your drink **")
    if drinkchoice == ("AJ"):
      typewriter(name +": I'll take an Apple juice please.", 0.08)
      time.sleep(0.5)
      typewriter("Barista: No problem, coming right up..", 0.08)
      time.sleep(0.5)
      typewriter("Barista: Here you are.. 1 Gold Please.", 0.08)
      time.sleep(0.5)
      typewriter(name +": Thank you, and here you go.", 0.08)
      gold = (gold - 2)
      typewriter("Barista: Thank you enjoy!", 0.08)
      time.sleep(0.5)
      typewriter(name + ": I will thank you, see you later!", 0.08)
      time.sleep(0.5)
      typewriter("** You Have your drink **")
    if drinkchoice == ("OJ"):
      typewriter(name +": I'll take an Orange juice please.", 0.08)
      time.sleep(0.5)
      typewriter("Barista: No problem, coming right up..", 0.08)
      time.sleep(0.5)
      typewriter("Barista: Here you are.. 2 Gold Please.", 0.08)
      time.sleep(0.5)
      typewriter(name +": Thank you, and here you go.", 0.08)
      gold = (gold - 2)
      typewriter("Barista: Thank you enjoy!", 0.08)
      time.sleep(0.5)
      typewriter(name + ": I will thank you, see you later!", 0.08)
      time.sleep(0.5)
      typewriter("** You Have your drink **")
    if drinkchoice == ("MM"):
      typewriter(name +": I'll take a Mayors Magic Mix please.", 0.08)
      time.sleep(0.5)
      typewriter("Barista: No problem, coming right up..", 0.08)
      time.sleep(0.5)
      typewriter("Barista: Here you are.. 5 Gold Please.", 0.08)
      time.sleep(0.5)
      typewriter(name +": Thank you, and here you go.", 0.08)
      gold = (gold - 1)
      typewriter("Barista: Thank you enjoy!", 0.08)
      time.sleep(0.5)
      typewriter(name + ": I will thank you, see you later!", 0.08)
      time.sleep(0.5)
      typewriter("** You have your drink **")
      typewriter("** The Magic effect has healed you completely!**")
      if health > 100:
        typewriter("** You Have full health **")
      if health < 100:
        health = (health + (100 - health))
        typewriter("** You now have full health **")
  if goovertomystery == ("2"):
    typewriter("** You ignore the man and walk up to the bar **", 0.08)
    typewriter("Barista: Hello, What can I get you?", 0.08)
    print("----------------------------------------------------------------------------")
    print("Drinks menu: Water [W] (1 Gold), Apple Juice [AJ] (2 Gold), Orange Juice [OJ] (2 Gold), The Mayors Magic Mix [MM] (5 Gold)")
    print("----------------------------------------------------------------------------")
    drinkchoice = input(typewriter("** What do you fancy? **", 0.08))
    if drinkchoice == ("W"):
      typewriter(name +": I'll take a water please.", 0.08)
      time.sleep(0.5)
      typewriter("Barista: No problem, coming right up..", 0.08)
      time.sleep(0.5)
      typewriter("Barista: Here you are.. 1 Gold Please.", 0.08)
      time.sleep(0.5)
      typewriter(name +": Thank you, and here you go.", 0.08)
      gold = (gold - 1)
      typewriter("Barista: Thank you enjoy!", 0.08)
      time.sleep(0.5)
      typewriter(name + ": I will thank you, see you later!", 0.08)
      time.sleep(0.5)
      typewriter("** You Have your drink **")
    if drinkchoice == ("AJ"):
      typewriter(name +": I'll take an Apple juice please.", 0.08)
      time.sleep(0.5)
      typewriter("Barista: No problem, coming right up..", 0.08)
      time.sleep(0.5)
      typewriter("Barista: Here you are.. 1 Gold Please.", 0.08)
      time.sleep(0.5)
      typewriter(name +": Thank you, and here you go.", 0.08)
      gold = (gold - 2)
      typewriter("Barista: Thank you enjoy!", 0.08)
      time.sleep(0.5)
      typewriter(name + ": I will thank you, see you later!", 0.08)
      time.sleep(0.5)
      typewriter("** You Have your drink **")
    if drinkchoice == ("OJ"):
      typewriter(name +": I'll take an Orange juice please.", 0.08)
      time.sleep(0.5)
      typewriter("Barista: No problem, coming right up..", 0.08)
      time.sleep(0.5)
      typewriter("Barista: Here you are.. 2 Gold Please.", 0.08)
      time.sleep(0.5)
      typewriter(name +": Thank you, and here you go.", 0.08)
      gold = (gold - 2)
      typewriter("Barista: Thank you enjoy!", 0.08)
      time.sleep(0.5)
      typewriter(name + ": I will thank you, see you later!", 0.08)
      time.sleep(0.5)
      typewriter("** You Have your drink **")
    if drinkchoice == ("MM"):
      typewriter(name +": I'll take a Mayors Magic Mix please.", 0.08)
      time.sleep(0.5)
      typewriter("Barista: No problem, coming right up..", 0.08)
      time.sleep(0.5)
      typewriter("Barista: Here you are.. 5 Gold Please.", 0.08)
      time.sleep(0.5)
      typewriter(name +": Thank you, and here you go.", 0.08)
      gold = (gold - 1)
      typewriter("Barista: Thank you enjoy!", 0.08)
      time.sleep(0.5)
      typewriter(name + ": I will thank you, see you later!", 0.08)
      time.sleep(0.5)
      typewriter("** You have your drink **")
      typewriter("** The Magic effect has healed you completely!**")
      if health > 100:
        typewriter("** You Have full health **")
      if health < 100:
        health = (health + (100 - health))
        typewriter("** You now have full health **")
        
def segment(3):
goforest = input(typewriter("Dialogue: You walk down this narrow foot path and come across a dark gloomy forest cutting the path in to ways.. You can either go left or right.. [L/R] ", 0.08)
if goforest == ("L"):
  typewriter("** You take the left turn.. **", 0.08)
  time.sleep(0.5)
  typewriter("** You see smoke coming from behind a bush.. Your curiostity gets the better of you and you walk towards it.. **", 0.08)
  time.sleep(0.5)
  typewriter("** You push your way through the brambles (-2 heath) **", 0.08)
  time.sleep(0.5)
  health = (health - 2)
  typewriter(name +": Woahh.. Its an Old Cottage! I wonder whats in there..", 0.08)
  time.sleep(0.5)
  typewriter("** You walk up to the cottage door and start knocking.. **", 0.08)
  time.sleep(0.5)
  typewriter("** Knock **")
  time.sleep(0.5)
  typewriter("** Knock **")
  time.sleep(0.5)
  typewriter("** Knock **")
  time.sleep(0.5)
  typewriter(name +" Hmm.. It seems to be empty..", 0.08)
  time.sleep(0.5)
  typewriter("** You check to see if its locked.. **", 0.08)
  time.sleep(0.5)
  typewriter(name +": Crumbs!.. Its locked.. There must be another way in..")
  time.sleep(0.5)
  typewriter("** You see an open window..")
  ctw = input(typewriter("** climb through the window [CW]"))
  if ctw == ("CW"):
    typewriter("** You climb through the Cottage window **", 0.08)
    import random.randint(0 , 1)
    if random.randint == (0):
      typewriter("** AHH you fall through the window and land on your back.. (-5 health)", 0.08)
      health = (health - 5)
      typewriter(name +": OUCH.. Thats a bit off a fall hey..", 0.08)
      time.sleep(0.5)
      typewriter("** You look around the Cottage **", 0.08)
      time.sleep(0.5)
      cil = input(typewriter("** You see: A chest [C], An old door [OD], A Cauldron [CA] **", 0.08))
      if cil == ("C"):
        typewriter("** You walk over to the chest **", 0.08)
        time.sleep(0.5)
        OPC = input(typewriter("** Open the Chest [OC] **", 0.08))
        if OPC == ("OC"):
          import random.randint(0, 1)
          if random.randint == (0):
            typewriter("** You tried opening the chest but failed.. **", 0.08)
            OPCA = input(typewriter("** Try opening the chest again [OCA] **", 0.08))
            if OPCA == ("OCA"):
              typewriter("** You succesfully opened the chest! **", 0.08)
              time.sleep(0.5)
              typewriter("** You found an old bag, a strange key, and an old book **", 0.08)
              time.sleep(0.5)
              typewriter(name +": *cough *cough*.. This chest couldnt have been opened for years!..", 0.08)
              time.sleep(0.5)
              typewriter("** You put the key in your pocket **", 0.08)
              time.sleep(0.5)
              typewriter(name +": Hmm.. Whats in this bag..?", 0.08)
              time.sleep(0.5)
              typewriter("** You open the back and  Gold scatters out! **", 0.08)
              tume.sleep(0.5)
              typewriter(name +": Gold! Sweet! I wonder how much there is?..", 0.08)
              time.sleep(0.5)
              typewriter("** You count up all the gold! **", 0.08)
              typewriter("--New Achivement Unlocked (Gold Gold Gold!)--")
              time.sleep(0.5)
              typewriter(name +": Wow! Twenty Gold!! Thats loads!..", 0.08)
              gold = (gold + 20)
              time.sleep(0.5)
              typewriter(name +": Now lets see where this key leads to..", 0.08)
              whatdoor = input(typewriter("** You see two doors, one on the left side [LD], and one on the right side [RD] but what one does the key fit in? **", 0.08))
              if whatdoor == ("LD"):
                typewriter(name +": Its got the be the left door!..", 0.08)
                time.sleep(0.5)
                typewriter("** You walk up to the door and try the key in the lock **", 0.08)
                time.sleep(0.5)
                typewriter(name +": Hmm.. Its not working.. Must be the other door!", 0.08)
                time.sleep(0.5)
                typewriter("** You walk up to the door and try the key in the lock **", 0.08)
                time.sleep(0.5)
                typewriter(name +": Yes!! It worked!..",0.08)

              
              
          if random.randint == (1):
            typewriter("** You succesfully opened the chest! **", 0.08)
            time.sleep(0.5)
            typewriter("** You found an old bag, a strange key, and an old book **", 0.08)
            time.sleep(0.5)
            typewriter(name +": *cough *cough*.. This chest couldnt have been opened for years!..", 0.08)
            time.sleep(0.5)
            typewriter("** You put the key in your pocket **", 0.08)
            time.sleep(0.5)
            typewriter(name +": Hmm.. Whats in this bag..?", 0.08)
            time.sleep(0.5)
            typewriter("** You open the back and  Gold scatters out! **", 0.08)
            tume.sleep(0.5)
            typewriter(name +": Gold! Sweet! I wonder how much there is?..", 0.08)
            time.sleep(0.5)
            typewriter("** You count up all the gold! **", 0.08)
            typewriter("--New Achivement Unlocked (Gold Gold Gold!)--")
            time.sleep(0.5)
            typewriter(name +": Wow! Twenty Gold!! Thats loads!..", 0.08)
            gold = (gold + 20)
            time.sleep(0.5)
            typewriter(name +": Now lets see where this key leads to..", 0.08)
            whatdoor = input(typewriter("** You see two doors, one on the left side [LD], and one on the right side [RD] but what one does the key fit in? **", 0.08))
            if whatdoor == ("LD"):
              typewriter(name +": Its got the be the left door!..", 0.08)
              time.sleep(0.5)
              typewriter("** You walk up to the door and try the key in the lock **", 0.08)
              time.sleep(0.5)
              typewriter(name +": Hmm.. Its not working.. Must be the other door!", 0.08)
              time.sleep(0.5)
              typewriter("** You walk up to the door and try the key in the lock **", 0.08)
              time.sleep(0.5)
              typewriter(name +": Yes!! It worked!..",0.08)
            
    if random.randint == (1):
      typewriter("** You safely climbed into the Cottage! **", 0.08)
      typewriter(name +": Woah.. This is nice..", 0.08)
      time.sleep(0.5)
      typewriter("** You look around the Cottage **", 0.08)
      time.sleep(0.5)
      cil = input(typewriter("** You see: A chest [C], An old door [OD], A Cauldron [CA] **", 0.08))
      if cil == ("C"):
        typewriter("** You walk over to the chest **", 0.08)
        time.sleep(0.5)
        OPC = input(typewriter("** Open the Chest [OC] **", 0.08))
        if OPC == ("OC"):
          import random.randint(0, 1)
          if random.randint == (0):
            typewriter("** You tried opening the chest but failed.. **", 0.08)
            OPCA = input(typewriter("** Try opening the chest again [OCA] **", 0.08))
            if OPCA == ("OCA"):
              typewriter("** You succesfully opened the chest! **", 0.08)
              time.sleep(0.5)
              typewriter("** You found an old bag, a strange key, and an old book **", 0.08)
              time.sleep(0.5)
              typewriter(name +": *cough *cough*.. This chest couldnt have been opened for years!..", 0.08)
              time.sleep(0.5)
              typewriter("** You put the key in your pocket **", 0.08)
              time.sleep(0.5)
              typewriter(name +": Hmm.. Whats in this bag..?", 0.08)
              time.sleep(0.5)
              typewriter("** You open the back and  Gold scatters out! **", 0.08)
              tume.sleep(0.5)
              typewriter(name +": Gold! Sweet! I wonder how much there is?..", 0.08)
              time.sleep(0.5)
              typewriter("** You count up all the gold! **", 0.08)
              typewriter("--New Achivement Unlocked (Gold Gold Gold!)--")
              time.sleep(0.5)
              typewriter(name +": Wow! Twenty Gold!! Thats loads!..", 0.08)
              gold = (gold + 20)
              time.sleep(0.5)
              typewriter(name +": Now lets see where this key leads to..", 0.08)
              whatdoor = input(typewriter("** You see two doors, one on the left side [LD], and one on the right side [RD] but what one does the key fit in? **", 0.08))
              if whatdoor == ("LD"):
                typewriter(name +": Its got the be the left door!..", 0.08)
                time.sleep(0.5)
                typewriter("** You walk up to the door and try the key in the lock **", 0.08)
                time.sleep(0.5)
                typewriter(name +": Hmm.. Its not working.. Must be the other door!", 0.08)
                time.sleep(0.5)
                typewriter("** You walk up to the door and try the key in the lock **", 0.08)
                time.sleep(0.5)
                typewriter(name +": Yes!! It worked!..",0.08)
          

                   
        
      
      
    
      


  
    

# Hi mate jsut letting you know to clear any text in the console it is os.system('Clear')
    #thank you didint know how to dothat


    
  


      
    
def invetorysortsys():
  if inv1 == ("Empty"):
    inv1 = (shoppuchase)
    print(shoppuchase , "Has Been saved to slot 1")
    shoppuchase = ("Empty")
  else:
    if inv2 =="Empty":
      inv2 = (shoppuchase)
      print(shoppuchase , "Has Been saved to slot 2")
      shoppuchase = ("Empty")
    else:
      if inv3 == ("Empty"):
        inv3 = (shoppuchase)
        print(shoppuchase , "Has Been saved to slot 3")
        shoppuchase = ("Empty")
        
def segment_loader():
  global segment
  if segment == (1):
    segment1()
  if segment == (2):
    segment2()
    
#save script + includes autosave just call for function
def save():
  #open text document and saves all variables for later use 
  a = open('savestate.txt', 'w')
  a.write(name)
  a.write('\n')
  a.write(str(health))
  a.write('\n')
  a.write(str(gold))
  a.write('\n')
  a.write(str(day))
  a.write('\n')
  a.write(inv1)
  a.write('\n')
  a.write(inv2)
  a.write('\n')
  a.write(inv3)
  a.write('\n')
  a.write(str(armourC))
  a.write('\n')
  a.write(str(armourH))
  a.write('\n')
  a.write(str(armourL))
  a.write('\n')
  a.write(str(armourB))
  a.write('\n')
  a.write(str(swordW))
  a.write('\n')
  a.write(str(swordS))
  a.write('\n')
  a.write(str(swordI))
  a.write('\n')
  a.write(str(shield))
  a.write('\n')
  a.write(str(crossbow))
  a.write('\n')
  a.write(str(bow))
  a.write('\n')
  a.write(str(arrow))
  a.write('\n')
  a.write(str(optt))
  a.write('\n')
  a.write(str(segment))
  a.close()
  print('Game Saved Succesfully')

#loadscript + includes load just call for function
def load():
  global name, health, gold, day, inv1, inv2, inv3, armourC, armourH, armourL, armourB
  global swordW, swordS, swordI, shield, crossbow, bow, arrow, optt, segment

  with open('savestate.txt', 'r') as a:
      print('Save state Opened')
      print('------Console Activated------')

      name = a.readline().strip()
      time.sleep(0.1)
      print('name.stip.Read')
      health = int(a.readline().strip())
      time.sleep(0.1)
      print('health.stip.Read')
      gold = int(a.readline().strip())
      time.sleep(0.1)
      print('gold.stip.Read')
      day = int(a.readline().strip())
      time.sleep(0.1)
      print('day.stip.Read')
      inv1 = a.readline().strip()
      time.sleep(0.1)
      print('inv1.stip.Read')
      inv2 = a.readline().strip()
      time.sleep(0.1)
      print('inv2.stip.Read')
      inv3 = a.readline().strip()
      time.sleep(0.1)
      print('inv3.stip.Read')
      armourC = int(a.readline().strip())
      time.sleep(0.1)
      print('armourC.stip.Read')
      armourH = int(a.readline().strip())
      time.sleep(0.1)
      armourL = int(a.readline().strip())
      time.sleep(0.1)
      armourB = int(a.readline().strip())
      time.sleep(0.1)
      print("armourB.stip.Read")
      swordW = int(a.readline().strip())
      time.sleep(0.1)
      print("swordW.stip.Read")
      swordS = int(a.readline().strip())
      time.sleep(0.1)
      print("swordS.stip.Read")
      swordI = int(a.readline().strip())
      time.sleep(0.1)
      print("swordI.stip.Read")
      shield = int(a.readline().strip())
      time.sleep(0.1)
      print("shield.stip.Read")
      crossbow = int(a.readline().strip())
      time.sleep(0.1)
      print("crossbow.stip.Read")
      bow = int(a.readline().strip())
      time.sleep(0.1)
      print("bow.stip.Read")
      arrow = int(a.readline().strip())
      time.sleep(0.1)
      print("arrow.stip.Read")
      optt = int(a.readline().strip())
      time.sleep(0.1)
      print("optt.strip.Read")
      time.sleep(0.1)
      segment = int(a.readline().strip())
      time.sleep(0.1)
      print("segment.stip.Read")
      time.sleep(0.1)
      print("All Stip.Read" + "\33[33m" + "{OK}")
      time.sleep(0.1)
      print("Deactivating Console")
      time.sleep(1.5)
      print("------Console Deactivated------")
  time.sleep(1)
  os.system('clear')
  print("-----Loaded Save Data:-----")
  typewriter(f"Name: {name}, Health: {health}, Gold: {gold}, Day: {day}, Segment: {segment}")
  print("---------------------------")
  os.system('clear')
#this calls for all segments to be read from registory and loaded into the game
  segment_loader()

#this is called headder TEXT add for all segment dialog beginging
def header():

  print("---------", name , "---------")
  typewriter(f"Health: {health}, Gold: {gold}, Day: {day} | Segment: {segment}")
  print("-------------------------")

#tutortial subprogramme
def Tutorial():
  os.system('clear')
  print("---------", name , "---------")
  typewriter(f"Health: {health}, Gold: {gold}, Day: {day}")
  print("---------------------------")
  print("")
  print("")
  print("")
  typewriter(f"Welcome to the tutorial {name}!")
  time.sleep(1)
  typewriter(f"In this game you will be playing as {name}!")
  time.sleep(1)
  typewriter("When propted with a choice, you will be given a list of options to choose from.")
  time.sleep(1)
  typewriter("Prompts Will Typicly Look Like This:")
  print("")
  print("---------------------------")
  typewriter("1)Save")
  typewriter("2)Contiue")
  print("---------------------------")
  time.sleep(1)
  typewriter("To Select A Option Simply Input the number that is beside it")
  time.sleep(1)
  typewriter("At Every Prompt There Will Be A Option That says Save and Quit")
  time.sleep(1)
  typewriter("When This Option Is Selected There is no way of going back if accidently entered")
  time.sleep(1)
  typewriter("Along Side This, The Game Works In Segments Meaning When Saved It Will Load The Segment")
  time.sleep(1)
  typewriter("Apon Entering a New Segment A Line Of Text Will Appear At The Top of the screen")
  time.sleep(1)
  typewriter('This Will Be Beside the Statistics GUI at the top')
  time.sleep(1)
  typewriter("This Will Tell You What Segment You Are In For Example")
  time.sleep(1)
  print("---------", name , "---------")
  typewriter(f"Health: {health}, Gold: {gold}, Day: {day} | Segment: Tutorial")
  print("---------------------------")
  time.sleep(1)
  typewriter("Now that you know how to play, lets get started!")
  
  time.sleep(1)
  os.system('clear')
  segment1()
  
def menu():
  opt = input("""
  1. Inventory
  2. Shop
  3. Interact With Characters
  4: Continue
  6: Quit""")

  if opt == ("1"):
    inventory()

  if opt == ("2"):
    shop()

  if opt == ("5"):
    save()
    print("Game Saved")
    print("Please Download The Save File , savestate.txt")

def inventory():
  
  print("You have" , inv1)
  print("You have" , inv2)
  print("You have" , inv3)
  optt = input("Please enter the number of the item you would like to use")
  if optt == ("1"):
    inventoryselecton()

  if optt == ("2"):
    inventoryselecton()

  if optt == ("3"):
    inventoryselection()

  print("*Travelling to shop*")
  time.sleep(1)
  print("Shop Clerk: Welcome, its lovely to see a new face around!")
  time.sleep(1)

def shop():
  shopopt = input("""Shop Clerk: What can I interest you in today?
  1. Health potion
  2. Weapons
  3. Armour
  4: Leave""") 
  if shopopt == ("1"):
    conbuy1 = input("Shop Clerk: I see your interested in a health potion, drinking one will heal your health by 20, would you like one? It costs 10 Gold. [Y/N]")
  if conbuy1 == ("Y"):
      print("*ITEM PURCHASED*")
      time.sleep(0.5)
      print("------------------------")
      print("Inventory: +1 Health potion")
      shoppurchases = ("Health potion")
    
      print("Currency",gold - 10)
      print("------------------------")
      print("Shop Clerk: Thank you for your purchase!")
      time.sleep(1)
      print("Shop Clerk: Come again soon!")
      time.sleep(1)
      print(name,": Thank you!")
  if shopopt == ("2"):
    print("Shop Clerk: I see weapons are you interest, check my stock and come back when you have made your decision.")
    print("------------------------------------------------------------------------")
    print("Weapon Stock: Wooden Sword  [WS](5 Gold), Stone Sword [SS](10 Gold), Iron Sword [IS](20 Gold), Bow [B](20 Gold), CrossBow [CB](25 Gold), Arrows [AR](2 Gold for 3) ")
    print("------------------------------------------------------------------------")
  
    wshopchoice = str(input("Shop Clerk: Any you like? [Y/N]"))
  if wshopchoice == ("Y"):
      weaponsbuy = input("Shop Clerk: What one do you want?")
  if weaponsbuy == ("WS"):
      if gold < 5:
        print("Shop Clerk: Sorry, you havent got enough gold to buy this item.")
      print("------------------------")
      print("Inventory: Wooden Sword")
      print("Currency:",gold - 5)
      print("------------------------")
      print("Shop Clerk: Thank you for your perchase! See you soon!")
      print(name,": Thank you, see you soon!")
      if weaponsbuy == ("SS"):
        if gold < 10:
          print("Shop Clerk: Sorry, you havent got enough gold to buy this item.")
      print("------------------------")
      print("Inventory: Stone Sword")
      print("Currency:",gold - 10)
      print("------------------------")
      print("Shop Clerk: Thank you for your perchase! See you soon!")
      print(name,": Thank you, see you soon!")
      if weaponsbuy == ("IS"):
        if gold < 20:
          print("Shop Clerk: Sorry, you havent got enough gold to buy this item.")
      print("------------------------")
      print("Inventory: Iron Sword")
      print("Currency:",gold - 20)
      print("------------------------")
      print("Shop Clerk: Thank you for your perchase! See you soon!")
      print(name,": Thank you, see you soon!")
      if weaponsbuy == ("B"):
        if gold < 20:
          print("Shop Clerk: Sorry, you havent got enough gold to buy this item.")
      print("------------------------")
      print("Inventory: Bow")
      print("Currency:",gold - 20)
      print("------------------------")
      print("Shop Clerk: Thank you for your perchase! See you soon!")
      print(name,": Thank you, see you soon!")
      if weaponsbuy == ("CB"):
        if gold < 25:
          print("Shop Clerk: Sorry, you havent got enough gold to buy this item.")
      print("------------------------")
      print("Inventory: CrossBow")
      print("Currency:",gold - 25)
      print("------------------------")
      print("Shop Clerk: Thank you for your perchase! See you soon!")
      print(name,": Thank you, see you soon!")
      if weaponsbuy == ("AR"):
        if gold < 2:
          print("Shop Clerk: Sorry, you havent got enough gold to buy this item.")
      print("------------------------")
      print("Inventory: 3x Arrows")
      print("Currency:",gold - 2)
      print("------------------------")
      print("Shop Clerk: Thank you for your perchase! See you soon!")
      print(name,": Thank you, see you soon!")
  if shopopt == ("3"):
    print("Shop Clerk: I see armour is your interest, check my stock and come back when you have made your decision.")
    print("-------------------------------------------------------------------------")
    print("Armour Stock: Chestplate [CP](15 Gold), Helmet [HT](10 Gold), Leggings [LG](15 Gold), Boots [BT](10 Gold)")
    print("-------------------------------------------------------------------------")
    ashopchoice = input("Shop Clerk: Any that interes you? [Y/N]")
    if ashopchoice == ("Y"):
      armourbuy = input("Shop Clerk: Great! What one interests you?")
      if armourbuy == ("CP"):
        print("------------------------")
        print("Inventory: Chestplate")
        print("Currency:",gold - 15)
        print("------------------------")
        print("Shop Clerk: Thank you for your perchase! See you soon!")
        print(name,": Thank you, see you soon!")
      if armourbuy == ("HT"):
        print("------------------------")
        print("Inventory: helmet")
        print("Currency:",gold - 10)
        print("------------------------")
        print("Shop Clerk: Thank you for your perchase! See you soon!")
        print(name,": Thank you, see you soon!")
      if armourbuy == ("LG"):
        print("------------------------")
        print("Inventory: Leggings")
        print("Currency:",gold - 15)
        print("------------------------")
        print("Shop Clerk: Thank you for your perchase! See you soon!")
        print(name,": Thank you, see you soon!")
      if armourbuy == ("BT"):
        print("------------------------")
        print("Inventory: Boots")
        print("Currency:",gold - 10)
        print("------------------------")
        print("Shop Clerk: Thank you for your perchase! See you soon!")
        print(name,": Thank you, see you soon!")
  if shopopt == ("4"):
    print(name,": Im okay for items now thank you!")
    time.sleep(1)
    print("Shop Clerk: Okay, come again soon!")
    
        
def inventoryselecton():
    if optt == ("1"):
      if inv1 == ("Empty"):
        print("You have no items in your inventory slot")
    else:
      if inv1 == ("Health potion"):
        print("You drink the health potion")
        health = (health + 10)
#def start  
def main_game():
  
  time.sleep(1)
  typewriter("Welcome to the game, " + name)
  time.sleep(1)
  Menu1 = input("Do You Have A Load File? [Y/N]")
  if Menu1 == ("N") or Menu1 == ("n"):
    #will call all variables to be used for all across all subprogrammes
    global health
    global gold
    global day
    global inv1
    global inv2
    global inv3
    global armourC
    global armourH
    global armourL
    global armourB
    global swordW
    global swordS
    global swordI
    global shield
    global crossbow
    global bow
    global arrow
    global optt
    global savestate
    global shoppurchase
    global wshopchoice
    global Game_option
    global segment
    
    health = (100)
    gold = (20)
    day = (0)
    inv1 = ('Empty')
    inv2 = ('Empty')
    inv3 = ('Empty')
    armourC = (10)
    armourH = (10)
    armourL = (10)
    armourB = (10)
    swordW = (3)
    swordS = (5)
    swordI = (10)
    shield = (10)
    crossbow = (10)
    bow = (10)
    arrow = (10)
    optt = (0)
    savestate = (0)
    shoppuchase = ("Empty")
    wshopchoice = ("Empty")
    Game_option = (0)
    segment = (0)
    
    print("\033[33m" + "Welcome to the game")
    Game_option = int(input("""
    1) Take the tutourial of the game?
    2) Skip the tutorial?"""))
    if Game_option == (1):
      Tutorial()
    if Game_option == (2):
      segment1()
  if Menu1 == ("Y") or Menu1 == ("y"):
    os.system('clear')
    print("-----Loading Save Data:-----")
    time.sleep(1)
    load()

 
#End of define subprocesses

#Start Defining the game Properties
typewriter("Please Enter Your Name Below")
name = input()
main_game()