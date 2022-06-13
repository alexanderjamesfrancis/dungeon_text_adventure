

from turtle import back

from pkg_resources import find_distributions


class player:
    def __init__(self,name,age,build,background,demeanor,token_tool):
        self.name = name,
        self.age = age,
        self.build = build,
        self.background = background,
        self.demeanor = demeanor,
        self.token_tool = token_tool,
        self.strength = 10,
        self.agility = 10,
        self.charisma = 10

def player_builder():
    strength = 0
    agility = 0
    charisma = 0
    print(
        "The dusk rolls in as you arrive at the Baron's castle. You announce your presence to his footmen, aware of why you have come, they lead you up to the keep and into a dimly lit room. To the left, in front of a dying fire, sits the Baron.",

        'He motions towards the other chair across from him. "Welcome", his voice betraying his lack of sleep. "Apologies, I send word for your presence by title and not name - by what name do you go by?'

    )

    # name input

    name = input("What is you name?")
    print(f'{name} eh? Hopefully it is a name that will be venerable to ones house. How many years have you served your house?')

    # age input

    age = input("How old are you?")
    if age < 28:
        agility += 2
        print("Ah, with such youth comes confidence. Let us hope the agility of your age plays in your favor")
    elif age > 28 and age < 45:
        strength += 2
        print("Good, loyalty and service provide an abundance of experience to draw from. Let us hope you have the strength to persevere.")
    else:
        charisma += 2
        print("Impressive, let us hope the wealth of wisdom and knowledge you possess can be properly utilised with the stength of word as opposed to steel.")    
    print('"You appear to be a promising candidate, come closer into the light to get a better eye of personage.')

    # build input
    build = input('What physical build are you: Skinny, Typical, Muscular?')
    while build.lower() != "skinny" or "typical" or "muscular":
        build = input('What physical build are you: Skinny, Typical, Muscular?')
    if build.lower() == "skinny":
        agility += 2
        strength -= 2
        print('The Baron leans back, "A nimble frame may be better suited to what task I have required of you".')
    elif build.lower() == "Typical":
        print('I see before me someone who is capable of physical work. This is good as you will need the stamina.')
    elif build.lower() == "muscular":
        strength += 2
        agility -= 2
        print('Your personage projects strength, let us pray you do not need it where you are going.')
    print('The Baron leans back in his chair. "Now that I am satisfied that you are physically capable, I would like to know more about your background. First however, can I offer you a drink?')

    # tea offer

    drink = input("Will you take the Baron's offer? Yes or No").lower()
    while drink.lower() != "yes" or "no":
        drink = input("Will you take the Baron's offer? Yes or No")
    print('The Baron makes a motion off into the darkness and a hasty shuffling is heard. A minute passes and a servant appear carrying a tray of tea.')    
    if drink.lower() == 'yes':
        print('The beverage is dispensed and you are handed a cup. The baron takes likewise and take a long swig from the cup.\n "Lovely stuff", the Baron comments')
    elif drink.lower() == 'no':
        print('The servant pours a cup for the Baron and passes it to him. He takes a long swig from the cup.\n "Shame, the local tea is excellent", the Baron comments')

    # background input

    print('"Now, I would like to know more about you. My intended contract is of a sensetive nature so I need to know you are of positive character. Tell me, what lies in you background?') 
    background = input('What is your background? Street Urchin, Tradesman or Guild-Member').lower()
    if background == 'street urchin':
        agility += 1
        print('The Baron raises an eyebrow. "Interesting, your apprance does not betray such a....rustic upbringing. Nonetheless, you may find these skills useful')
    elif background == 'tradesman':
        strength += 1
        print('"A person who values a hard days work wrought with the tool they have. Good. This will serve you well."')
    elif background == 'guild-member':
        charisma += 1
        print('"Surrounded by investments and questionable decisions, Ha. I have seen many from this path and know their tongue is often sharper than any blade."')        

    # demenor input

    print('"Your background interests me". The Baron readjusts himself on his chair before the dying fire. "I pose this question: A man has just been robbed and has sustained a life threatening injury at the hand of his assailant. He is asking for those around him for help but it falls on deaf ears. What do you do?"')
    demeanor = ""
    print('A: Help the man, bind his wounds and find suitable assistance even if you are ultimately out of pocket')
    print('B: Approach the man and only offer assistance in return for financial incentives.')
    print('C: Do nothing, leave the man to his fate')
    demeanor = input('Pick: A,B or C.').lower()
    if demeanor == 'a':
        pass
    elif demeanor == 'b':
        pass
    if demeanor == 'c':
        pass

    # tool input

    print('The Baron re-focuses towards your hip. "I see you have brought tools for the job, what do have that you believe will aid you in this matter?')
    print('A: Knife')
    print('B: Rope')
    print('C: Hammer')
    token_tool = input('Pick: A,B or C.').lower()
    if token_tool == 'a':
        pass
    elif token_tool == 'b':
        pass
    if token_tool == 'c':
        pass

    # player creation conclusion
    print('The Baron reclines further. "I have learnt much in these moments and I believe you are the person I require to undertake my task. I ask you now, reflect on yourself and consider if you are also right for the task.\n\n')

    finish = input('End character creation? Y or N').lower

    if finish ==  'y':
        return player(name=name,age=age,build=build,background=background,demeanor=demeanor,token_tool=token_tool)
    elif finish == 'n':
        player_builder()     

#    print('The embers of the fire crackle, the Baron lets out a sigh, "I am sure you are keen to know why I have summoned you at this hour?  ')