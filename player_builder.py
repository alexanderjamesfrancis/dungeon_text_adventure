

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
    name = input("What is you name?")
    print(f'{name} eh? Hopefully it is a name that will be venerable to ones house. How many years have you served your house?')
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
    drink = input("Will you take the Baron's offer? Yes or No")
    while drink.lower() != "yes" or "no"            
#    print('The embers of the fire crackle, the Baron lets out a sigh, "I am sure you are keen to know why I have summoned you at this hour?  ')