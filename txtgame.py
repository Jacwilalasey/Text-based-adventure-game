from sys import exit

def frog_fate():
    print("You wake up in a room, all you see is blackness with short, sharp strobes of bright green lights.")
    print("You have an overly deep sense that you are being watched.")
    print("In the distance you see moving shapes.")
    print("What are you going to do?")
    print("""
    1. Reach for the green strobes of light, hoping to catch one.\n
    2. Search the room, hoping to find an exit.\n
    3. Head over to the moving shapes in the distance, maybe they can help.""" )

    choice1 = input("> ")

    if choice1 == "1":
        dead("""
        You put up your hand to catch and strobe of light, suprisingly enough you grab a hold of something. 
        When you look down you realise the flashing strobes light were actually radioactive frogs!
        The scared frog takes one look at you and vomits acid all over your face, melting your skin away from the bone.""")
    elif choice1 == "2":
        print("Well, aren't you a smart cookie! Just a little looking around and you managed to dodge the acid frogs and find a secret door out.")
        print("The green bricked road ahead seems to lead on to a big city.")
        frog_fate2()

    elif choice1 == "3":
        print(""" 
        As you slowly approach the shapes in the distance you can begin to make our what you couldn't see before.
        These are not humans as you first believed, these are.... GIANT RADIOACTIVE FROGS!!! """)
        print("\n\tDo you want to run, or stay?\n")

        frogchoice = input("> ")

        if frogchoice == "run":
            dead("Ha! You can't outrun giant frogs! they hunt you down and vomit acid all over your butt, you scream for help while you watch you butt fade away into existence.")
        elif frogchoice == "stay":
            print("It turns out the frog people are quite kind unless provoked, they offer you a warm meal of bugs and give you directions to the next room.")
            frog_fate2()


guards = []

for i in range(0, 26):
    guards.append(i)

def frog_fate2():
    print("\nWell look who made it to frog city!")
    print("The frog guards demand you pick a number between 1 and 23 to determine whether you can enter, or wheter you die.")


    for i in guards:
        print(f"option {i}.")

    while True:         
        numberchoice = int(input("\nInput your choice> "))

        if numberchoice == 22:
            print("Excellent selection, you may enter Frog City!")
            frog_city()
        elif numberchoice <= 20:
            print("Terrible choice, you are an amateur in random number selection games and must die!")
            dead("The frog guards take you to the guillotine, and the frog king chops off your head in front of a crowd of frog people.")
        elif numberchoice == 23 or 21:
            print("So, so close! I tell you what have one more guess on the house.")
        else:
            print("That was not a selectable number, you will now die for this disrespect!")
            dead("The frog guards chopped of your head, oh well.")


def frog_city():
    complete("""\n 
    Welcome to Frog City, it's a beautiful city, with cascading waterfalls, lots of bugs to eat and lots of single frogs to settle down with.
    You will be happy here. Good adventuring, hope we see you again!
    """)


def moonstone_fate():
        print("You awaken on your planets nearest moon, for a minute you are still, taking in the vast, bare landscape...")
        dead("A few seconds pass and you realise you are becoming short of breath. You have no space suit, you are sucked into the deep, dark vacuum of space forever.")

weapons = ['sword', 'axe', 'mace']

def sword_fate():
    print("You see a brave warrior standing in front of you, he proclaims 'Welcome to Warrior World! Pick your weapon.'")
    print("In front you there are several weapons laid out")
    
    print(f"The weapons are spread out in front of you, there is {weapons}, what do you choose?")

    weaponchoice = input("\n> ")

    if weaponchoice == 'sword':
        print("So you stuck with your original weapon, wise move, the sword is a weapon of honour and will grant you many blessing in warrior world")
        print("The brave warrior leads you away, mentioning something about an impending battle.")
        battle()

    elif weaponchoice == 'axe':
        complete("""
        You select the axe, you feel an affinity with the power of the weapon.
        You look at the warrior and back at the axe, turning around and walking away.
        You have decided to become a lumber jack. Good luck?
        """)

    elif weaponchoice == 'mace':
        print("Ahhh the mace, I see you are a person of lesser morals.")
        print("You should head over to the flying wombat public house, you can meet your kind there.")
        print("""
        Do you want to;
        a - Head over to the flying wombat for a drink, or
        b - Follow the warrior anyway, who cares what he says. 
        """)

        dirchoice = input("> ")

        if dirchoice == 'a':
            print("You take the warriors advice and head over to the pub, sounds like the best idea to you.")
            flying_wombat()

        if dirchoice == 'b':
            print("The brave warrior leads you away, mentioning something about an impending battle.")
            battle()

    else:
        print("That is not one of your options, are you daft?")
        dead("The warrior had enough of your shit and stabbed you in the belly.")

def battle():
    print("""
    \"Into battle we go\" yells the warrior, you are following closely as you pick up pace towards the fight.
    You ready your weapon, grasping it tightly with you hands, making eye contact with the man ahead of you.
    He yells and charges towards you. Do you swing your weapon left or right?    
    """)

    swing = input("\n> ")

    if swing == 'left':
        dead(f"""The warrior swings his sword at your head, slightly grazing your cheek.
        You ready your sword, as the attacker comes back at you again you dodge {swing} 
        Unluckily for you, he was also slashing to the left, your head now has his sword firmly 
        placed between both of your eyes, you are dead.        
        """)
    elif swing == 'right':
        print(f"""
        The warrior swings his sword at your head, slightly grazing your cheek.
        You ready your sword, as the attacker comes back at you again you dodge {swing} 
        Smartly avoiding his attack you are able to riposte and come back with your own deadly swing.
        The battle continues for some hours, and you defeat enemy after enemy.
        """)
        print("You are lauded for your skill in battle and are presented with a knighthood by the king.")
        complete("You are now free to take whomever you choose as a partner, a spend the rest of your days drinking wine and sleeping around.")


def flying_wombat():
    print("\n The moment you enter the pub, someone's head rolls on by your feet.")
    print("Seems like a lovely place. You sit at the bar and ask for an ale, but you can feel everyone's eyes upon you.")
    print("A drawf with a bloody big axes approaches you and asks, 'heads or tails' as he plays with a golden coin in his hand.")
    print("You take a deep breath, knowing that this decision could be your last, and you choose...")

    coinflip = input("\n> ")

    if coinflip == 'heads':
        print("The dwarf looks at you with a big grin across his face.")
        dead("He swiftly unsheathes his axe and in one foul swoop, he topples your head, you are now looking up at your headless body from the ground.")
    elif coinflip == 'tails':
        print("The dwarf murmers something about being lucky under his breath and walks away.")
        print("You finish you ale and head out, thinking that this place is too dangerous.")
        complete("""
        As your first step lands on the pavement outside, 
        you look around warrior world and see nothing but opportunity.
        Maybe you will open and patisserie for all of the warriors seeing as you are too scared to go into battle.
        Good luck on the rest of your journey "warrior"!
        """)


def dead(why):
    print(why, "Good job!")
    exit(0)

def complete(why):
    print(why, "See you next time!")
    exit(0)

def start():
    print("Your adventure begins here, I hope you are ready.")
    print("A grand decision lies ahead of you.")
    print("A wizard offers you three items, all with varying fates behind them.")
    print("He holds a frog, a moonstone and a sword.")
    print("Which do you choose?")

    while True:
        choice = input("\n> ")

        if choice == 'frog':
            frog_fate()
        elif choice == 'moonstone':
            moonstone_fate()
        elif choice == 'sword':
            sword_fate()
        else:
            print("I don't understand your selection, please choose again.")

start()
