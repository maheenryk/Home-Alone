#last left on 1124

import random
from random import randint as dice
import datetime #To print in the time/date
from collections import defaultdict
gamerun = datetime.datetime.now() #assigning gamerun to a date

#---------------- Player Stats ------------------------------
player_max = 600 #Maximum value the player can reach or obtain through heals and items
player_hp = 100 
defense_hp = 100 #"Shield" health. if below 0, shield hp = 0, you essentially can't use it.
defense_max = 100 #Shield Value you get after a fight

#------------------------------------------------------------
#--------------- Player Attack Options -----------------
player_attacks = ['punch', 'kick', 'scratch', 'defend'] #You can change this around or create an entirely new system!    
#------------------------------------------------------
kick_dmg = dice(20, 30)
punch_dmg = dice(10,20)
scratch_dmg = dice(5, 10)


#-------------------------  Enemy  ----------------------------------
enemy_hp = 100 #enemy set hp
enemy_max = 150
enemy_choice = ['Slash', 'Strike', 'Shriek', 'Shield'] #Choice.list that the enemy can choose from
slash_dmg = dice(20, 30)
strike_dmg = dice(10, 20)
shriek_dmg = dice(5, 10)                                                       
shield_hp = 70                                                     
#---------------------------------------------------------------------

#----------- Boss (Reflection of Yourself) ----------------
boss_hp = 300
boss_max = 600
boss_shield_hp = 300
boss_shield_max = 350
boss_slash_dmg = dice(40, 50)
boss_strike_dmg = dice(30, 40)
boss_shriek_dmg = dice(20, 30)

blankdamage = 30 #This is just to show a set attack damage in the game, you can delete this or change if you will

def showInstructions():
  #print a main menu and the commands
  print('''
RPG Game
========
You wake up in the living room of an abandoned house.
Everything is scattered and out of place, as if a storm tore through it.
There is no one around.
“What is happening, what…  what is this… where am i…”.
You try to recall any memory of your life,
but your mind is as mysterious and unknown as the story of this house.
There is a map in front of your feet,
carefully drawn by hand and laid out in the manner of a gift.

Commands:
  go [north, south, east, west, up, down]
  get [item]
  examine [Items, rooms (e.g. "examine living-room")]
  help [for help with commands]
''')

def showStatus():
  #print the player's current status
  print('---------------------------')
  print('You are in the', currentRoom)
  #print the current inventory
  print('Inventory : ', str(inventory))
  print('You have :', player_hp, 'hp left')
  #print an item if there is one
  if "item" in rooms[currentRoom]:
      print('You see a', rooms[currentRoom]['item'])
  print("---------------------------")
  
#an inventory, which is initially empty
inventory = []


#a dictionary linking a room to other rooms
rooms = {
    
#============FIRST FLOOR AND BASEMENT=====================    

            'Living Room' : {
                'east'  : 'Front Entryway',
                'south' : 'Drawing Room',
                'home' : 'Living Room at Home',
                'item'  : 'map'
                },
            
            'Living Room at Home' : {
                },
            
            'Front Entryway' : {
                'west'  : 'Living Room',
                'south' : 'Foyer',
                'east'  : 'Stairs'
                },
            
            'Stairs' : {
                'west'  : 'Front Entryway',
                'east'  : 'Garage',
                'down'  : 'Basement',
                'up'    : 'Upper Stairs'
                },
            
            'Basement' : {
                'up'    : 'Stairs',
                'item' : 'rope'
                },
            
            'Garage' : {
                'west'  : 'Stairs',
                'item' : 'hook'
                },
            
            'Drawing Room' : {
                'north' : 'Living Room',
                'east'  : 'Foyer'
                },
            
            'Foyer' : {
                'north' : 'Front Entryway',
                'west'  : 'Drawing Room',
                'south' : 'Kitchen',
                'east'  : 'Toilet'
                },
            
            'Toilet' : {
                'west'  : 'Foyer'
                },
            
            'Dining Room' : {
                'east'  : 'Kitchen'
                },
            
            'Kitchen' : {
                'west'  : 'Dining Room',
                'north' : 'Foyer',
                'east'  : 'Storage',
                'south' : 'Garden',
                'item' : 'plate-of-food'
                },
            
            'Storage' : {
                'west'  : 'Kitchen',
                'out' : 'False Freedom'
                },
            
            'False Freedom' : {
                },
            
            'Garden' : {
                'north' : 'Kitchen',
                'down' : 'Secret Basement',
                'climb' : 'Wall Crack'
                },
            
            'Wall Crack' : {
                'climb' : 'Garden',
                'item' : 'letter'
                },
            
            'Secret Basement' : {
                'up' : 'Garden',
                'item' : 'device'
                },
            
#===============SECOND FLOOR PLUS ATTIC===================            
            
            'Upper Stairs' : {
                'down'  : 'Stairs',
                'west'  : 'Hall Entry'
                },
            
            'Hall Entry' : {
                'east'  : 'Upper Stairs',
                'west'  : 'Bedroom',
                'south' : 'Lower Hall',
                'item'  : 'map2'
                },
            
            'Bedroom' : {
                'east'  : 'Hall Entry'
                },
            
            'Lower Hall' : {
                'north' : 'Hall Entry',
                'south' : 'Hall',
                'east'  : 'Playroom',
                'west'  : 'Kids Bedroom'
                },
            
            'Bathroom' : {
                'east': 'Hall'
                },
            
            'Kids Bedroom' : {
                'east'  : 'Lower Hall'
                },
            
            'Playroom' : {
                'west'  : 'Lower Hall'
                },
            
            'Hall' : {
                'north' : 'Lower Hall',
                'south' : 'Upper Hall',
                'east'  : 'Balcony',
                'west'  : 'Bathroom'
                },
            
            'Bathroom' : {
                'east': 'Hall'
                },
            
            'Balcony' : {
                'west' : 'Hall',
                'jump' : 'air, freefalling'
                },
            
            'air, freefalling' : {
                },
            
            'Upper Hall' : {
                'north' : 'Hall',
                'south' : 'Master Bedroom',
                'east'  : 'Attic Entry',
                'west'  : 'Library'
                },
            
            'Library' : { 
                'east'  : 'Upper Hall',
                'item' : 'note'
                },
            
            'Attic Entry' : {
                'up'    : 'Attic',
                'west' : 'Upper Hall',
                'south' : 'Sunroom'
                },
            
            'Attic' : {
                'down'  : 'Attic Entry' 
                },
            
            'Sunroom' : {
                'north' : 'Attic Entry'
                },
            
            'Master Bedroom' : {
                'north' : 'Upper Hall'
                }
            
            
            

         }

room_visits = defaultdict(int) #Used to track if you've been to a room before
examine_times = defaultdict(int) #for tracking how many times you examine something
healing_usage = defaultdict(int) #Used to track how many times you've healed
healing_usage = 0
player_wins =  0
bedroom_hint = 0

#start the player in the Living Room
currentRoom = 'Living Room'

showInstructions()

#loop forever
while True:

  showStatus()

  #get the player's next 'move'
  #.split() breaks it up into an list array
  #eg typing 'go east' would give the list:
  #['go','east']
  move = ''
  while move == '':  
    move = input('>')
    
  move = move.lower().split()
  
  if move[0] == 'help':
      print('''
---------------------------------------------GO COMMAND---------------------------------------------------
You move by typing "go" and then the direction you want to go in.
For example, to go from the living room to the front entryway, you'll have to type "go east".
To use stairs, you can type "go up" or "go down".

There will be times where you will be able to move in directions other than the usual, so keep an eye out for "go"!

You can check the directions and your location always in the map.

---------------------------------------------GET COMMAND--------------------------------------------------
You can get or obtain an item by typing "get" followed by the item you want, that is also in the current room you are in.
Type it exactly as you see it under your hp text, or you won't be able to get it.

For example, to get the map in the living room, you can type "get map" and you'll have it in your inventory.
To obtain things with two words, like tissue box, you will need a dash in the middle.

So to get a tissue box, you will have to type "get tissue-box". But you should see that under your hp bar anyway!

-------------------------------------------EXAMINE COMMAND------------------------------------------------
You can use this command to examine rooms, and items. This will tell you about the room or item, and might even give you a hint.

For example, to look at your map, you will have to type "examine map", and you will be able to look at the map.

To examine things with more than one word, you will need to add a dash again.
So to examine the living room, you can either type, "examine room" or "examine living-room".

You also don't need capital letters in examine commands! So don't type "examine Map", just "map" is fine.

Sometimes in examine statements, you might be introduced to something else you can examine, so keep examining as you go!

----------------------------------------------GOOD LUCK---------------------------------------------------
''')

  #if they type 'go' first
  if move[0] == 'go':
    
    if currentRoom == 'Balcony' and move[1] == 'jump':
        leaveorgo = str(input("You can feel your heart thumping. This is a way out, you're tired of this... Do you want to jump? Y/N"))
        if leaveorgo == 'Y':
            print("You decide to jump, be free, get away from whatever this is... by any means possible.")
            currentRoom = rooms[currentRoom][move[1]]
        else:
            print("No... You can't leave like this... You decide to not go just yet.")
            
    elif currentRoom == 'Storage' and move[1] == 'out':
        if 'back-door-key' in inventory:
            leaveorgo = str(input('''
You open the back door and a gust of wind hits you in the face.
You take in your first breath of fresh air in so long. Too long.

You look outside and your heart starts racing in excitement. This is it...

But...

It's only an inkling at the back of your mind but... But something feels wrong.

Your foot is half out the door. Will you go?

Y/N:
'''))
            if leaveorgo == 'Y':
                print("You decide to leave, be free, get away from whatever this is...")
                currentRoom = rooms[currentRoom][move[1]]
            else:
                print("No... You can't leave like this... You decide to not go just yet.")
                
        else:
            print("You need a key to unlock the door.")
            
    elif currentRoom == 'Upper Hall' and move[1] == 'west':
        if 'library-key' in inventory:
            currentRoom = rooms[currentRoom][move[1]]
        else:
            print('Hmm, the library is locked. Seems like you need a key.')
            
    elif currentRoom == 'Garden' and move[1] == 'climb':
        if 'grappling-hook' in inventory:
            currentRoom = rooms[currentRoom][move[1]]
        else:
            print('You need something strong and sturdy to climb.')
  
    elif currentRoom == 'Garden' and move[1] == 'down': #trapdoor 
        if 'key' in inventory:
            currentRoom = rooms[currentRoom][move[1]]
        else:
            print('Hmm, seems like you need a key.')
    
    elif currentRoom == 'Living Room' and move[1] == 'home': #ending 5
        if 'peace' in inventory:
            currentRoom = rooms[currentRoom][move[1]]
        else:
            print('You can\'t go that way!') 
            
    #check that they are allowed wherever they want to go
    elif move[1] in rooms[currentRoom]:
      #set the current room to the new room
        currentRoom = rooms[currentRoom][move[1]]
      #there is no door (link) to the new room
    else:
        print('You can\'t go that way!')

  #if they type 'get' first
  if move[0] == 'get' :
    #if the room contains an item, and the item is the one they want to get
    if "item" in rooms[currentRoom] and move[1] in rooms[currentRoom]['item']:
      #add the item to their inventory
      inventory += [move[1]]
      #display a helpful message
      print(move[1] + ' got!')
      #delete the item from the room
      del rooms[currentRoom]['item']
    #otherwise, if the item isn't there to get
    else:
      #tell them they can't get it
      print('Can\'t get ' + move[1] + '!')
      
  if currentRoom == 'Living Room at Home':
      print('''
You open your eyes slowly, the ceiling light almost blinding. You’re hungry. Extremely hungry.
How long were you asleep? Where are you? You blink a few times to make the blurriness go away.
Someone’s talking. No. A lot of someones are talking.
There are people gathered all around you, talking excitedly, some with tears in their eyes.

You’re so confused.

You can’t hear anything properly due to just waking up but as the milliseconds tick by, you regain further clarity.
Suddenly understanding dawns on you. You remember what happened.

Everyone had gathered at the house to celebrate… something important you did.
It doesn’t matter what it was. It’s not that important anymore.
Your friends were there, your mentor, your family,
and even your crush, who you remember nervously texting at 4 am to invite.

Everyone was so happy, but you.
You’d been so annoyed with everything that day.

Your friends had been going out without inviting you, and you felt so angry and hurt.

Your mentor had told you that you could do better, that you weren’t giving it your all, you’d felt disappointed in yourself.
But you channeled that into resentment for your mentor.

Your family had been constantly on your back for little things.
You felt trapped. Angry. Frustrated.

You even felt negatively about your crush, why couldn’t they just like you back? What were you missing?
It was the wrong place and the wrong time.

You blew up at all of them, insulting them and calling them every harsh thing on the planet just to feel better.

But you didn’t. You just felt worse.
So you ran.

You ran up to the balcony and you just felt this suffocating anger.
At yourself.

You didn’t think. You didn’t wait. You just acted.

The next thing you know there’s people screaming your name, some on the brink of crying.
Somebody had wrapped their arms around you… who was it… one of your friends you think.
They’d gone outside for a stroll and had jumped under you to break your fall… you start tearing up.

They’re standing right in front you softly smiling with their arm in a sling.
You open your mouth to say something but before you can, everyone tackles you and you are overwhelmed with love.
There will be time for it all, you think. Take this moment in, for now. Just rest.

You’re home. (Ending 5/5)








... where's the sound of static coming from?
''')
      break
    
  if currentRoom == 'False Freedom':
      print('''
You did it. You’re out of this hellscape! You step outside.
You run out into the street and you feel joy bubbling up inside you… You look around expecting to see… what?
What were you expecting to find out here?

Your momentary bout of happiness starts to fade away and all you see is the grey land you could see from the windows.
You escaped… but why doesn’t it feel like it? Endless emptiness everywhere you look.
More lifeless than inside.

You figured out how to get out, how to leave forever.

Where will you go now? You’re out of the house but still trapped within this barren land.

Why are you here?
What got you here?
Who even are you?
What are you so afraid of?
What’s in the house that you can’t deal with?

Will you go back? (Ending 4/5)
''')
      break

  if currentRoom == 'air, freefalling':
      print('''
You jumped off the balcony.
Maybe it got too stressful for you, or maybe you were too fed up.
Maybe neither. Maybe both. Maybe both and more.
Maybe you thought this was the only way. It isn’t.

In this game, you have the choice of starting all over again.
After all, this is only one of five endings, a weak comparison to the real thing.
Are you satisfied with this end? Are you asking yourself why you did it?

Will you try again? (Ending 1/5)
''')
      break
      
     #If they type examine first   
  if move[0] == "examine":
     if 'map' in inventory and move[1] == 'map': #If the entire command is "examine map", it prints all of this
         print('''
 ________   ____________________________________
|        | |        |                    |      |
|Basement| | Living |   Front             Garage|      
|        | | Room •     Door      Stairs |      |      N
|________| |___  ___|            ________|      |      |
           |        |           |        |      |  W --•-- E
           | Drawing|   Foyer   | Toilet |______|      |
           |  Room                       |             S
           |________|____   ____|________|
           |        |           |        |
           | Dining |  Kitchen  |Storage |  • = You got the map here
           |  Room                       |
           |________|___________|________|       
                |                   |            
                |      Garden       |      
                |___________________|       
''')

         
     elif 'map2' in inventory and move[1] == 'map2': #If the entire command is "examine map", it prints all of this
         print('''
 ________________________________
|          |                     | 
| Bedroom  |  Hall •     Stairs  |   • = You got the map here
|              Entry             |
|__________|           __________|        N
|          |          |          |        |
|   Kids'  |   Lower  | Playroom |    W --•-- E
|  Bedroom     Hall              |        |
|__________|          |__________|        S
|          |          |          :
| Bathroom |   Hall     Balcony  :
|                                :   ___________________
|__________|          |__________:  |                   |
|          |             Attic   |  |                   |
|          |   Upper     Entry   |  |       Attic       |
| Library      Hall    ___   ____|  |                   |
|                     |          |  |___________________|
|          |____  ____| Sunroom  |
|          |          |          |
|          |  Master  |          |
|          | Bedroom  |          |
|__________|__________|__________|

''')
         
#-------------------------------------------------------------------------------------------
      #I'd say keep this in the game, its a healing item that has limited uses.       
      #You can make any other item like this too!. But honestly learn to code better because elif and ifs and a p a i n    
     elif 'leaves' in inventory and move[1] == 'leaves':
         print("Leaves from one of these barely alive plants, they seem to restore some of your health when you chew on them. Would you like to use them?")
         yorno = str(input("Y / N: "))
         if yorno == "Y": #Using healing 
             player_hp = player_hp + 50
             healing_usage += 1
             print("")
             print("You sit down and chew the leaves to restore your vitality and mind. Soon, you're back onto your feet.")
             print("")
             examine_times['leaves'] += 1
             if healing_usage == 4: #if you want more uses, change that 2 to anything higher
                 inventory.remove("leaves")
                 print("You've used all your leaves.")
                 print("")
             if player_hp > player_max: #This caps out your hp, remove if you want m o r e 
                 player_hp = player_max
                 print ("You've reached the fullest vitality. Go and fight!")                 
         elif yorno == "N": #Canceling your use of healing
             print("Seems as if you're already healthy enough, time to continue.")
             
#===============================FOOD===============================================
             
     elif 'plate-of-food' in inventory and move[1] == 'plate-of-food' or 'plate-of-food' in inventory and move[1] == 'food':
         print("Some food from the kitchen. It seems nutritious and will restore your health to full. Would you like to eat?")
         yorno = str(input("Y / N: "))
         if yorno == "Y": #Using healing 
             player_hp = player_max
             healing_usage += 1
             print("")
             print("You sit down and slowly eat the food, enjoying each bite. Soon, you're back onto your feet.")
             print("You've reached the fullest vitality. Your arms feel strong. As do your legs.")
             print("You feel ready for whatever you must face next.")
             print("")
             examine_times['plate-of-food'] += 1
             if healing_usage == 1: #if you want more uses, change that 2 to anything higher
                 inventory.remove("plate-of-food")
                 print("You've eaten all your food.")
                 print("")              
         elif yorno == "N": #Canceling your use of healing
             print("Seems as if you're already healthy enough, time to continue.")        
         
#================================KEY===============================================
             
     elif 'key' in inventory and move[1] == 'key':
         print('''
A rusty, old looking key. It seems it hasn't been used in a while.
''')

#=========================MAKING GRAPPLING HOOK====================================
             
     elif 'rope' in inventory and 'hook' in inventory and move[1] == 'rope' or 'rope' in inventory and 'hook' in inventory and move[1] == 'hook':
         print('Hmm, seems as though you can make a grappling hook. You get to work.')
         inventory.remove('rope')
         inventory.remove('hook')
         inventory.append('grappling-hook')
         
     elif 'rope' in inventory and 'hook' not in inventory and move[1] == 'rope':
         print('You could make something with this rope. It seems sturdy and strong.')
         
     elif 'hook' in inventory and 'rope' not in inventory and move[1] == 'hook':
         print('This hook is sharp, you could even use it to climb something. If something was attached to it.')

#============================LETTER===============================================
         
     elif 'letter' in inventory and move[1] == 'letter':
         print('''
Hi, to whoever's reading this.

If you managed to get up here, you must be desperate to get out. I'll tell you how.

You might have noticed that the library is locked. There is a key. But you need to enter a code.
You will have to decipher it yourself but I will tell you where to enter it.
Static.
The lock safe gives out strong static. It is somewhere in the house, but the static should be loud.
Loud enough to lead you to it. Keep checking rooms to hear for it. Oh also.

When you do hear it, don't listen for more than a minute. It's going to make your ears bleed.
Literally.

The code is "jmzi rmri xlvii xas".
Key: 4

Good luck :)

P.S. there's a decryption device in the house somewhere. You might need a key to get there.
''')
         
#==============================NOTE==================================================
     
     elif 'note' in inventory and move[1] == 'note':
         print('''
Hello again.

I see you made it to the library. Well done.

You have a few more steps to go now. There is another code for another safe.
This safe contains the key to the storage room's back door. The back door is your way out.

You'll have to look for the safe again somewhere in this house.

The code is "vul lpnoa zlclu mvby".
Key: 7
 
Good luck. 
''')
         
#=========================DECRYPTION DEVICE==========================================
         
     elif 'device' in inventory and move[1] == 'device':
         alphabet = "abcdefghijklmnopqrstuvwxyz"

         key = input("Enter decryption key (NUMBER):")
         key = int(key)
         newMessage = ""

         message = input("Please enter encrypted message:")

         for character in message:
             if character in alphabet:
                 position = alphabet.find(character)
                 newPosition = (position - key) % 26
                 newCharacter = alphabet[newPosition]
                 newMessage += newCharacter
             else:
                 newMessage += character

         print("Your decrypted message is:", newMessage)
         
#===============================SHARDS============================================
         
     elif 'shard-of-patience' in inventory and move[1] == 'shard-of-patience' or 'shard-of-patience' in inventory and move[1] == 'patience':
         print('''
Patience.
You turn the shard over in your hand and feel a sense of... fortitude.

A sense of calmness.

You've always felt frustrated when dealing with your family. Why didn't they just understand?
Why couldn't they just be content with you?

It's hard to make people think the way you do. To make them see your point of view.
But it isn't impossible.
You need persistence and patience. Hand in hand.

In time and in effort, anything is possible.

Be loving.
Be brave.
Be strong.
Be patient.
Be ready to sacrifice.
''')
         
     elif 'shard-of-love' in inventory and move[1] == 'shard-of-love' or 'shard-of-love' in inventory and move[1] == 'love':
         print('''
Love.
You turn the shard over in your hand and feel a sense of... warmth.

A sense of serenity.

You've struggled with love. Expressing it. Acknowledging it. Understanding it.
You've found it hard to feel deserving of it.
Yet at the same time craving it.

You don't need to understand why you deserve to be loved to know that you are.
You will though, in time.
Your closest ones will make you understand.
Your friends.
Your best friend.

Your family. Your true family.

Be loving.
Be brave.
Be strong.
Be patient.
Be ready to sacrifice.
''')
         
     elif 'shard-of-strength' in inventory and move[1] == 'shard-of-strength' or 'shard-of-strength' in inventory and move[1] == 'strength':
         print('''
Strength.
You turn the shard over in your hand and feel a sense of... power.

A sense of stability.

It's tough being strong. Because strength doesn't just lie in your arms or legs.
It lies in your heart. In your mind. In your soul.
Your ability to withhold pain and tolerate it. The ability to take criticism in stride.
That's strength.

You think about your mentor. The person you look up to.
How they carry themselves with real strength.
What they must've gone through to get there.
You wish you could be like them.

And you think, you believe, that you can be. In time.

Be loving.
Be brave.
Be strong.
Be patient.
Be ready to sacrifice.
''')
         
     elif 'shard-of-bravery' in inventory and move[1] == 'shard-of-bravery' or 'shard-of-bravery' in inventory and move[1] == 'bravery':
         print('''
Bravery.
You turn the shard over in your hand and feel a sense of... courage.

A sense of valour.

Your heart feels shaky yet strong. Your brain running at miles a second, but you feel ready.
Fear fuels your determination.

You wish you felt like this with them. Your crush.
That you could say you've never felt braver and more afraid at the same time.

You decide it is not good enough to pity yourself.
Instead, you will go back. And you will tell them.

Be loving.
Be brave.
Be strong.
Be patient.
Be ready to sacrifice.
''')
         
     elif 'shard-of-sacrifice' in inventory and move[1] == 'shard-of-sacrifice' or 'shard-of-sacrifice' in inventory and move[1] == 'sacrifice':
         print('''
Sacrifice.
You turn the shard over in your hand and feel a sense of... it all.

You feel every sense, in every sense there is to be sensed. Love, strength, bravery, patience...

Loss.

Anger.

Pain.

Misery.

Envy.

Everything you've ever felt, you feel it all at once. It's heavy.
Your knees buckle and you fall to the ground. Tears spill down your face as you let it out.
You've held it in for so long.

You scream. You sob. You laugh. You yell.

It's time to let it go.
Give it up. Give up your fear.

Sacrifice it.

It's okay.

You can love.
You can be brave.
You can be strong.
You can be patient.

Remember you need to be. You need them all.
All five of them.
All five shards.
''')

#===============================MIRROR============================================
         
     elif 'shard-of-patience' in inventory and 'shard-of-love' in inventory and 'shard-of-strength' in inventory and 'shard-of-bravery' in inventory and 'shard-of-sacrifice' in inventory and move[1] == 'shards':
         print('''
The five shards of glass suddenly seem to fit together like pieces of a puzzle.
You lay them down on the ground and the seams and jagged edges melt into each other and smooth out.
It looks like magic.
You see a beautiful oval mirror in front of you where the previous shards were.
''')
         inventory.remove('shard-of-patience')
         inventory.remove('shard-of-love')
         inventory.remove('shard-of-strength')
         inventory.remove('shard-of-bravery')
         inventory.remove('shard-of-sacrifice')
         inventory.append('mirror')
         
     elif 'mirror' in inventory and move[1] == 'mirror':
         print('''
You stare at yourself in the mirror.
It's difficult but you know you need to see yourself.
This entire adventure, or journey, or quest. Whatever you want to call it.
You've fought and you've reflected. You've struggled.
But with patience.
With love.
With strength.
With bravery.
And with sacrifice.
These are the things at the base of one's humanity.
The foundation of a human.

Maybe you didn't realize it at the start, but you do now.
Each shard was a piece of you that you needed to earn back.
This mirror is you as a whole. A representation of you.

A painting, or picture, of you even, you could say.

Where did you last see a painting?
''')

#============================LIVING ROOM==========================================         
         
     elif currentRoom == 'Living Room' and move[1] == 'living-room' or currentRoom == 'Living Room' and move[1] == 'room': #EXAMINING DOES NOT WORK WITH CAPITAL LETTERS
         if 'key' in inventory:
             print('Everything is strewn out of its place, the couch is flipped over, ')
             print('The TV is sitting on the floor, hollow and empty, somehow that brings you comfort.')
             print('There is a picture frame hung on the wall.')
             print('Your eyes skim over the windows.')
         else:
             print('Everything is strewn out of its place, the couch is flipped over, ')
             print('the TV is hanging off the wall in a dangerous manner,')
             print('there is a picture frame hung on the wall.')
             print('Your eyes skim over the windows.')
         
     elif currentRoom == 'Living Room' and move[1] == 'windows':
         print('The windows show you empty barren streets. Irritatingly unrecognizable.')
         print('')
         print('Someone must have tried to break open the windows, because')
         print('scuffs and marks are clearly seen on the otherwise pristine panes of glass.')
         print('The windows seem to be made of something not glass, though, much stronger.')
         print('')
         print('Looking outside through the windows for too long makes you nauseous somehow. ')
         print('')
         print('You walk away.')
         
     elif currentRoom == 'Living Room' and move[1] == 'tv':
         if 'key' in inventory:
             print('The TV is hollow inside, empty of any electronics or wires.')
             print('You wonder what made the sound of static.')
         else:
             print('You move closer to the black screen void of any answers to your questions.')
             print('')
             print('static… crackle… crack- it crashes onto the floor and breaks apart.')
             print('It is hollow inside. You notice something glistening inside. It is a key.')
             print('')
             print('Where was the static coming from?')
             inventory.append('key')
             
     elif currentRoom == 'Living Room' and move[1] == 'picture-frame' or currentRoom == 'Living Room' and move[1] == 'frame' or currentRoom == 'Living Room' and move[1] == 'picture':
         if 'mirror' in inventory:
             print('''
You look at the picture and back at yourself in the mirror. The missing piece was you.
The blank ripped out face in the frame was a smooth oval.
Exact shape of the mirror you held in your hands like it was a saving grace.
You place the mirror on the oval hole in the picture.

It melts seamlessly into the picture leaving only your own face in the frame.
Your face is painted delicately with grace. Each stroke of brush soft and precise.
Your eyes contain a shine you had forgotten you ever had.
The painted version of you is smiling. Laugh lines clear as day and bright as one too.
You realize so are you.

Your family is standing in the frame with joy. Happy to be a whole.
Finally, you think.
Finally, you feel joy in being whole with them too.

As you stare at the picture, you notice faces that weren't there before.
Along with your family, your mentor is there. Standing with strength and poise.

Your best friend is there. Their love of you shining in their grin as they are frozen in frame mid-punch.
Their fist aiming lightly for your shoulder.

Even your crush is there. You feel a bit star-struck. As you always do near them.
But what surprises you is that they seem to look the same.
Star-struck to be near you.
They are looking at you with the softest smile, and they look almost shy.
You've never felt more complete.

You finally understand. It was never about escaping.
You’ve done that all your life. Look where that got you.

You fought with power and bravery, you battled yourself and won.
You weren’t running away from this house, you were running away from yourself.

This was hard, but you did it. You went against yourself for your own wellbeing.

It’s time to wake up.
You’ve done beautifully, now go and rest.
Wake up and go home.

Go home.
''')
             inventory.remove('mirror')
             inventory.append('peace')
             
         else:
             print('''
You move closer to the only one untouched object in this room.
The frame looks as if stuck in time, unable to be tampered with.
The picture contains a few people, but one of the faces is ripped out haphazardly and angrily.

Why?

You do not know who the others are, yet they stare at you.
You feel unease rising in your throat like bile.

You walk away.
''')
         
#==================================FRONT DOOR========================================
         
     elif currentRoom == 'Front Entryway' and move[1] == 'front-door' or currentRoom == 'Front Entryway' and move[1] == 'door':
         print('''
The front door is locked. Stuck in place as if it is not even a door, but a wall.
The mail slot is as if glued shut.
''')
         examine_times['front-door', 'door'] += 1
         
     elif currentRoom == 'Front Entryway' and move[1] == 'entryway' or currentRoom == 'Front Entryway' and move[1] == 'front-entryway':
         if examine_times['front-door', 'door'] == 0:
             print('''
There are withering plants next to the front door.
A child's stroller is flipped on its side.
Hope rises in your heart when you catch sight of the front door.
''')
         else:
             print('''
There are withering plants next to the front door.
A child's stroller is flipped on its side.
The sight of the front door brings you nothing but despair and the feeling of helplessness.
''')
             
     elif currentRoom == 'Front Entryway' and move[1] == 'plants' or currentRoom == 'Front Entryway' and move[1] == 'plant':
         if 'leaves' in inventory or examine_times['leaves'] >=1:
             print('''
The plants do not resemble any that you would recognize.
They are not dead yet.
You can feel it and it brings you a sense of ease.
Or is it relief?
''')
         else:
             print('''
You notice that the plants have not fully withered.
There are still some leaves that could pass off as healthy and alive.
You pick the freshest four off the plant.
''')
             inventory.append('leaves')

     
     elif currentRoom == 'Front Entryway' and move[1] == 'stroller' or currentRoom == 'Front Entryway' and move[1] == 'childs-stroller':
         print('''
You expected to find something...
Or someone??
The stroller is empty.
''')
         
#====================================STAIRS==============================================
         
     elif currentRoom == 'Stairs' and move[1] == 'stairs':
         print('''
The stairs seem to go up and down.
''')
         
#====================================GARAGE==============================================
         
     elif currentRoom == 'Garage' and move[1] == 'garage':
         print('''
It's cold here, as if the garage was open for a long time and was only closed a while ago.
There's space for a car, a whitened rectangle where the car must've stood before it drove off.

Leaving you here.
Alone.
''')
         
#==================================DRAWING ROOM==========================================
         
     elif currentRoom == 'Drawing Room' and move[1] == 'drawing-room' or currentRoom == 'Drawing Room' and move[1] == 'room':
         print('''
The fancier version of the living room. Guests would gather here.

You remember something.

You would come here, with your best friend, when your family wasn't paying attention.
The sofas are laid out around a glass coffee table. You two would play board games here.

And you two would have pillow fights with the expensive pillows you were meant to never put your hands on.
You would joke about school, the people there, how you hated the snobby ones. Your friend calling you the snobby one.
You punching them off the sofa and laughing while they scowled. You getting hit in the face with a pillow. 

When the sound of your laughter would boom through the house your parents would drag the two of you out of the room.
You would still be laughing hours after you both got strongly scolded for breaking house rules.
You would sit outside together, eating left-overs and talking about everything, from crushes to homework.
Each word out of each other's mouths tightening the bond of friendship. 

You feel your chest tighten.

You'd fought here too. You can't remember about what... maybe you just don't want to remember.

You feel sick being here.
''')
        
#====================================TOILET==============================================
         
     elif currentRoom == 'Toilet' and move[1] == 'toilet':
         print('''
Nothing too special here.

...

Except for the mirror.
It was completely blacked out. You try scratching it and it stays the exact same.
You can't even glimpse at your reflection.
''')        
         
#====================================KITCHEN=============================================
         
     elif currentRoom == 'Kitchen' and move[1] == 'kitchen' or currentRoom == 'Kitchen' and move[1] == 'room':
         print('''
An ordinary looking kitchen, with ordinary looking utensils and ordinary looking appliances.

An aroma of something lingered. You couldn't put your finger on what, but it made you hungry.
''')

#==================================DINING ROOM===========================================
         
     elif currentRoom == 'Dining Room' and move[1] == 'dining-room' or currentRoom == 'Dining Room' and move[1] == 'room':
         print('''
The dining room was around the same size as the living room and the drawing room.
A kitchen table for 12 in the middle surrounded by chairs. 
''')

#====================================STORAGE=============================================
         
     elif currentRoom == 'Storage' and move[1] == 'storage' or currentRoom == 'Storage' and move[1] == 'room':
         print('''
There's not much in here. Old expired cans of food. Books with ripped pages that can't be used anymore.
Useless junk.

A door.

You see a door at the very back of the room. If your layout of this house is correct, then that door leads directly outside.
Outside. Finally.

You move closer to the door and you notice some writing.

"GET OUT... GO OUT!!" is scratched into the dark wood. The writing makes you nervous...

But you need to leave.
''')

#====================================GARDEN==============================================
         
     elif currentRoom == 'Garden' and move [1] == 'garden':
         print('''
There is a giant seemingly never ending stone wall surrounding the garden.
The grass has not been trimmed in months it seems, or years. 
You notice a wooden trapdoor almost buried in the long grass.
''')   

     elif currentRoom == 'Garden' and move [1] == 'trapdoor' or currentRoom == 'Garden' and move [1] == 'door':
         print('It is hard to tell what could be under it. Try going down.')
     
     elif currentRoom == 'Garden' and move [1] == 'wall' or currentRoom == 'Garden' and move [1] == 'stone-wall':
         print('You try to climb the wall but it is as slippery as if there was water running through the seams of the stone bricks.')
         print('...')
         print('You notice a crack, maybe even a hole you could fit through, in the wall.')
         print('You will need something sharp and strong to climb up.') #player can make a grappling hook using rope and a wall hook
         
#==============================SECRET BASEMENT=============================================
         
     elif currentRoom == 'Secret Basement' and move[1] == 'secret-basement' or currentRoom == 'Secret Basement' and move[1] == 'basement' or currentRoom == 'Secret Basement' and move[1] == 'room':
         print('''
A hidden basement. The air was extremely stale, it clearly hadn't been entered in quite a long time.
There's nothing too extra-ordinary here, just a replica of a normal basement.

Some weird devices were thrown around though, emitting strange noises and glows, you felt best to keep away for now.
''')
         
#=================================BASEMENT=================================================
         
     elif currentRoom == 'Basement' and move[1] == 'basement' or currentRoom == 'Basement' and move[1] == 'room':
         print('''
The basement is dark, but surprisingly not dark enough to impair your sight. There are boxes thrown around.
Old furniture, a broken box tv, an old games console. The static is loud here. You cover your ears.
You are looking around when a glow catches your eyes. A lock safe.
''')
         
     elif currentRoom == 'Basement' and move[1] == 'lock-safe' or currentRoom == 'Basement' and move[1] == 'lock' or currentRoom == 'Basement' and move[1] == 'safe':
         code = int(input('Enter numerical code:'))
         if code == 5932:
             print('You unlocked the safe!')
             inventory.append('library-key')
         else:
             print('Wrong code.')
             
#==================================ATTIC====================================================
             
     elif currentRoom == 'Attic' and move[1] == 'attic' or currentRoom == 'Attic' and move[1] == 'room':
         print('''
The attic is cold. You shudder and shiver. The skylights are barely representative of their namesake.
Neither do they show the sky, they are blacked out by... newspapers?
And neither do they provide any light.
The static is loud here. You cover your ears.
You are looking around when a glow catches your eyes. A lock safe.
''')
         
     elif currentRoom == 'Attic' and move[1] == 'lock-safe' or currentRoom == 'Attic' and move[1] == 'lock' or currentRoom == 'Attic' and move[1] == 'safe':
         code = int(input('Enter numerical code:'))
         if code == 1874:
             print('You unlocked the safe!')
             inventory.append('back-door-key')
         else:
             print('Wrong code.')
             
#=================================BEDROOM===================================================
             
     elif currentRoom == 'Bedroom' and move[1] == 'bedroom' or currentRoom == 'Bedroom' and move[1] == 'room':
         if player_wins == 5:
             print('''
Your bedroom.

You feel like a weight has been lifted off of you when you look around.
Everything feels familiar and has a feeling of home attached to it.

Your bedsheets are exactly the way you like them. Your various posters decorating the walls.
Your desk arranged pleasingly to your aesthetic. It feels like home.

You feel content in being here.
''')
         else:
             print('''
A bedroom. The atmosphere in the room is heavy, and grim. You feel unwell.
You look around anyway and everything seems hazy, and fuzzy.

You don't like being here.
''')
             
#==============================KIDS' BEDROOM================================================
             
     elif currentRoom == 'Kids Bedroom' and move[1] == 'kids-bedroom' or currentRoom == 'Kids Bedroom' and move[1] == 'bedroom' or currentRoom == 'Kids Bedroom' and move[1] == 'room':
         print('''
A brighter, more full room. The bedsheets strewn across the place. 
The walls painted in cartoons and colorful patterns, a nightlight next to each of the twin beds.

The room radiated innocence. 
''')
         
#================================PLAYROOM===================================================
     
     elif currentRoom == 'Playroom' and move[1] == 'playroom' or currentRoom == 'Playroom' and move[1] == 'room':
         print('''
The playroom was littered with toys, plushies, various playsets and beanbags.
The room was lit up by the giant windows lining the wall.

You carefully stepped over the legos, taking care not to disturb the setting of the room.

You pick up a toy train and pretend to drive it in the air. Feeling momentary joy for a fraction of time.
''')
             
#=================================LIBRARY===================================================
             
     elif currentRoom == 'Library' and move[1] == 'library' or currentRoom == 'Library' and move[1] == 'room':
         print('''
Bigger than all the other rooms in the house, the library was appropriately cold.
You rub your arms and exhale into your hands in an attempt to warm up.

You look around and notice none of the books in the tauntingly tall shelves are able to be read.
The words and letters are all jumbled up to form incohesive parallels of the original titles.

You catch sight of the desk and chair standing by one of the shelves, and it triggers a memory.

You, sitting in the desk chair, and your mentor, standing by the desk watching what you wrote.
They nod as you scribble and comment on your thoughts, praising and criticizing constructively.

You cracked a joke, at one point, and they countered your quip with a remark of your own.
For the next half hour or so, you two just bounced off of each other's wit.
Breaking into laughter at the end.
They slapped your shoulder and chuckled, easing off the laughter.
You looked up at them and found joy glistening in their eyes.
Your reflection masked by their pride in you.

Before you could say anything, they got back to work, chastising you for procrastinating, in jest.
You smiled and did as they asked.


Another memory, of another time.
Same desk, same chair. A different atmosphere altogether.
You'd just come back from a failed test. A test you'd spent months studying for.
The air was tense, so were you. Your mentor sighed, getting to the point.

You'd fought them then. The details unclear. The half memory leaving a sour taste in your throat.

You feel sick being here.
''')
         
#=============================MASTER BEDROOM================================================
         
     elif currentRoom == 'Master Bedroom' and move[1] == 'master-bedroom' or currentRoom == 'Master Bedroom' and move[1] == 'bedroom' or currentRoom == 'Master Bedroom' and move[1] == 'room':
         print('''
The biggest bedroom in the house. The walls were covered with velvet. The importance of the room clear.
Attached also was an en suite. The bathroom spacious and filled with every cream or serum you could want.
The dark red velvet walls made the room seem less brighter than it probably was.

You pan your eyes over the room and look at the bed. A king. Large enough to host a camping group on the mattress.
You remember being here.

Jumping on the bed carelessly, laughing when your foot would slip on the satin sheets and you'd faceplant on the bed.
Your parents scolding you for entering their room without permission. You scoffing back at them.


A harsher moment, when you'd been called up in this room.
The door had been shut to drown out the scathing words on each end.
A back and forth of complaints and insults.

You'd ran out quickly.
You feel the same way right now, trapped and wanting to flee.
''')
         
#=================================SUNROOM===================================================
         
     elif currentRoom == 'Sunroom' and move[1] == 'sunroom' or currentRoom == 'Sunroom' and move[1] == 'room':
         print('''
The sunroom, akin to the balcony, but with walls of glass.
If not for the sky blanketed by gray clouds, sunlight would be streaming in through the windows, sharp and strong.

A reading nook was built into the corner, some beanbags were laid out around a coffee table.
The perfect room for leaving everything and just relaxing. Embraced by the rays of the sun.
A room of warmth.


You look around the reading nook again, and your heart skips a beat.
Your crush. An echo of their laugh as they read one of your books.
You walk up to the nook as if expecting them to be sitting in the place the same way when you got there.

You'd had a surprise visit by them that day, you'd stood frozen at the front door, stuttering.
They'd shoved you lightly and teased you about your pajamas.
You'd brought them up nervously into the sunroom because your room was a mess.

They went on about school and their annoying teacher. You listened with intent, hooked on every word.

You suddenly interrupted them, blurting out you liked them. They froze, chuckled shortly, made a hasty excuse, and left.

You just stood, the sun burning your skin, your eyes burning too.

It hurts being here.
''')
         
#=================================BALCONY===================================================
         
     elif currentRoom == 'Balcony' and move[1] == 'balcony':
         print('''
The air is stale out, and the view is the same as the windows.
The railing surrounding the small openness is of medium height.
Easily... no. You’re in a back and forth with yourself.
In some deep frustrated part of you, you want to jump. “Go jump... do it... go jump... end it...”.
Will you?
''')
         
#=======================================BATHROOM============================================
         
     elif currentRoom == 'Bathroom' and move[1] == 'bathroom':
         print('''
Nothing too special here.

...

Except for the mirror.
It was completely blacked out. You try scratching it and it stays the exact same.
You can't even glimpse at your reflection.
''')
         
#==================================IF THEY CANT EXAMINE=====================================        
         
     else:
         print('What are you trying to see? Try looking around more.')

#================================ENEMY ENCOUNTERS===========================================
         
#==================================BEST FRIEND==============================================
         
  if currentRoom == 'Drawing Room':
      if currentRoom == 'Drawing Room' and room_visits['Drawing Room'] == 0:
          enemy_hp = 100
          Shieldhp = 70
          
          if player_wins == 0:
              print('You enter the room with caution. Something is very wrong here.')
          elif player_wins == 1:
              print('Your heart is beating rapidly in your chest as you fear for another encounter.')
          elif player_wins == 2:
              print('You feel a true sense of neautrality, and maybe for the first time, excitement. Who will it be this time?')
          elif player_wins == 3:
              print('Your heart feels heavy and your mind is running at miles a minute. You feel sad, not afraid.')
          
      if room_visits[currentRoom] == 0: #If this is your first time coming to this room, a message appears
           print("")
           print("You see a familiar face... your best friend. Before you can say anything they start dashing towards you.")
           room_visits[currentRoom] += 1 #No message appears if you enter this room a second time
      while player_hp > 0 and enemy_hp > 0:#Fight against enemy if both of you are above 0 hp
          print(" _______________________________________________________")
          print("|You have", player_hp, "health left. The enemy has", enemy_hp,"health left.") #Yours and Enemy HP           
          print("|Your Defense Hp =", defense_hp,)
          player_choice = str(input("Choose : punch (p), kick (k), scratch (s), defend (d), info (i): ")) #Your options
          computer_choice = random.choice(enemy_choice) #Computer chooses out of a list
          if player_choice == 'Info' or player_choice == 'info' or player_choice == 'i': #Player_choice == Info
            print('')
            print('''
Kick is your strongest attack, but against enemy's Strike you can lose up to 15 hp.
Punch is your second strongest attack. When picked against Shriek, you can deal up to 30 damage.
Scratch is one of your weakest attacks, but against Slash, can deal up to 25 damage.
Defend is your shield. You will lose defense hp every time you use defend, but gain hp. Except for when against Shriek, you will lose hp.
''')
            print('')
            
          elif player_choice == 'ohdip':
              enemy_hp = enemy_hp - enemy_hp
              print('Sneaky ;)')
             
#====================================KICK===================================================
             
          elif player_choice == 'kick' and computer_choice  == 'Slash' or player_choice == 'k' and computer_choice  == 'Slash': #kick vs slash
              player_hp = player_hp - slash_dmg
              enemy_hp = enemy_hp - kick_dmg
              print('Kick', kick_dmg, 'vs Slash', slash_dmg)
              print('You and your friend both hurt each other. You both stumble back.')
              print('They look angry and, it pains you to see, hurt.')
               
          elif player_choice == 'kick' and computer_choice  == 'Strike' or player_choice == 'k' and computer_choice  == 'Strike': #kick vs strike
              player_hp = player_hp - strike_dmg - 5
              enemy_hp = enemy_hp + 5
              print('Kick', kick_dmg, 'vs Strike', strike_dmg)
              print('Your friend strikes you brutally with their sword.')
              print('Why are they doing this? You feel anger bubbling up.')
               
          elif player_choice == 'kick' and computer_choice  == 'Shriek' or player_choice == 'k' and computer_choice  == 'Shriek': #kick vs shriek
              enemy_hp = enemy_hp - kick_dmg
              player_hp = player_hp + 7
              print('Kick', kick_dmg, 'vs Shriek', shriek_dmg)
              print('Your friend opens their mouth, but before they can make a sound you kick them strongly in the chest.')
              print('You look at them guiltily as they spit blood and stare at you with scorching hate.')
              if player_hp >= player_max:
                  player_hp = player_max
                  print("You've reached full health.")
               
          elif player_choice == 'kick' and computer_choice  == 'Shield' or player_choice == 'k' and computer_choice  == 'Shield': #kick vs shield
              print('Kick', kick_dmg, 'vs Shield', shield_hp)
              if shield_hp >= 0:
                  shield_hp = shield_hp - kick_dmg - 10
                  enemy_hp = enemy_hp + 3
                  print('Your friend puts up their shield and blocks your kick. The regain some health, while behind their shield.')
                  print('You wish you could somehow talk to them.')
                  if enemy_hp >= enemy_max:
                      enemy_hp = enemy_max
                      print('Your enemy has reached full health. Be wary.')
              else:
                  enemy_hp = enemy_hp - kick_dmg
                  print("Your friend's shield is too weak to defend against your kick.")
                  print('Your heel meets them directly in their ribs, making them double over.') 
                  
#====================================PUNCH================================================
               
          elif player_choice == 'punch' and computer_choice  == 'Slash' or player_choice == 'p' and computer_choice  == 'Slash': #punch vs slash
              player_hp = player_hp - slash_dmg - 5
              enemy_hp = enemy_hp + 5
              print('Punch', punch_dmg, 'vs Slash', slash_dmg)
              print('You drive your knuckle toward someone you thought you never would. They slash back at you.')
              print('But not before you skim their jaw with your fist.')
              print("You feel petty joy at getting a hit in, even though you're a great deal more hurt.")
              
          elif player_choice == 'punch' and computer_choice  == 'Strike' or player_choice == 'p' and computer_choice  == 'Strike': #punch vs strike
              player_hp = player_hp - strike_dmg
              enemy_hp = enemy_hp - punch_dmg
              print('Punch', punch_dmg, 'vs Strike', strike_dmg)
              print('You and your friend both hurt each other. You both stumble back.')
              print('They look angry and, it pains you to see, hurt.')
               
          elif player_choice == 'punch' and computer_choice  == 'Shriek' or player_choice == 'p' and computer_choice  == 'Shriek': #punch vs shriek
              enemy_hp = enemy_hp - punch_dmg - 10
              player_hp = player_hp + 9
              print('Punch', punch_dmg, 'vs Shriek', shriek_dmg)
              print('Before your friend even makes a sound, your fist collides with their jaw.')
              print('They stagger back, shocked and dazed.')
              print('You feel a sense of guilty joy.')
              if player_hp >= player_max:
                  player_hp = player_max
                  print("You've reached full health.")
                            
          elif player_choice == 'punch' and computer_choice  == 'Shield' or player_choice == 'p' and computer_choice  == 'Shield': #punch vs shield
              print('Punch', punch_dmg, 'vs Shield', shield_hp)
              if shield_hp >0:
                  shield_hp = shield_hp - 15
                  enemy_hp = enemy_hp - punch_dmg
                  print("Your friend's shield goes up, but you are quick to pull it away,")
                  print('and land a solid punch right in their stomach.')
                  print('They double over in agony. You do not feel any happiness.')
              else:
                  enemy_hp = enemy_hp - punch_dmg
                  print("Your friend's shield goes up, but it is too weak to protect them.")
                  print('You swing your fist and land a solid punch right in their stomach.')
                  print('They double over in agony. You do not feel any happiness.')
               
#====================================SCRATCH===============================================
               
          elif player_choice == 'scratch' and computer_choice  == 'Slash' or player_choice == 's' and computer_choice  == 'Slash': #scratch vs slash
              enemy_hp = enemy_hp - scratch_dmg - 15
              player_hp = player_hp + 10
              print('Scratch', scratch_dmg, 'vs Slash', slash_dmg)
              print('Your friend moves to slash your chest with their sword, but before they can execute their move,')
              print('you are quick to scratch their face, harshly.')
              print('You can see their skin turn red as blood emerges from under their skin.')
              print('You hate yourself in this moment.')
               
          elif player_choice == 'scratch' and computer_choice  == 'Strike' or player_choice == 's' and computer_choice  == 'Strike': #scratch vs strike
              player_hp = player_hp - strike_dmg - 10
              enemy_hp = enemy_hp + 5
              print('Scratch', scratch_dmg, 'vs Strike', strike_dmg)
              print("You attempt to reach for your friend's face, but they strike you in the abdomen with the hilt of their sword.")
              print('They scowl at you, their anger equivalent to your pain.')
              print('You cough up blood and look at them with... guilt? Why are you guilty?')
               
          elif player_choice == 'scratch' and computer_choice  == 'Shriek' or player_choice == 's' and computer_choice  == 'Shriek': #scratch vs shriek
              player_hp = player_hp - scratch_dmg
              enemy_hp = enemy_hp - shriek_dmg
              print('Scratch', scratch_dmg, 'vs Shriek', shriek_dmg)
              print('You and your friend both hurt each other. You both stumble back.')
              print('They look angry and, it pains you to see, hurt.')   
               
          elif player_choice == 'scratch' and computer_choice  == 'Shield' or player_choice == 's' and computer_choice  == 'Shield': #scratch vs shield
              print('Scratch', scratch_dmg, 'vs Shield', shield_hp)
              if shield_hp >= 0:
                  shield_hp = shield_hp - scratch_dmg - 10
                  enemy_hp = enemy_hp + 3
                  print('Your friend puts up their shield and blocks your scratch. The regain some health, while behind their shield.')
                  print('You wish you could somehow talk to them.')
                  if enemy_hp >= enemy_max:
                      enemy_hp = enemy_max
                      print('Your enemy has reached full health. Be wary.')
              else:
                  enemy_hp = enemy_hp - scratch_dmg
                  print("Your friend's shield is too weak to defend against your kick.")
                  print('Your heel meets them directly in their ribs, making them double over.')
                  
#====================================DEFEND=================================================
               
          elif player_choice == 'defend' and computer_choice  == 'Slash' or player_choice == 'd' and computer_choice  == 'Slash': #defend vs slash
              print('Defend', defense_hp, 'vs Slash', slash_dmg)
              if defense_hp >= 0:
                  defense_hp = defense_hp - slash_dmg + 20
                  player_hp = player_hp + 5
                  print("You put up your defense againt your friend's sword, you stumble backwards. Shaken.")
              else:
                  player_hp = player_hp - slash_dmg
                  print('You were too weak to protect yourself. You keel over in pain.')
               
          elif player_choice == 'defend' and computer_choice  == 'Strike' or player_choice == 'd' and computer_choice  == 'Strike': #defend vs strike
              print('Defend', defense_hp, 'vs Strike', strike_dmg)
              if defense_hp >= 0:
                  defense_hp = defense_hp - strike_dmg + 10
                  player_hp = player_hp + 5
                  print("You put up your defense againt your friend's strike, you stumble backwards. Shaken.")
              else:
                  player_hp = player_hp - slash_dmg
                  print('You were too weak to protect yourself. You keel over in pain.')
               
          elif player_choice == 'defend' and computer_choice  == 'Shriek' or player_choice == 'd' and computer_choice  == 'Shriek': #defend vs shriek
              print('Defend', defense_hp, 'vs Shriek', shriek_dmg)
              if defense_hp >0:
                  defense_hp = defense_hp - 10
                  player_hp = player_hp - shriek_dmg
                  print("Your defense goes up, but your friend is quick to screech.")
                  print('Their scream is deafening and leaves you quaking.')
              else:
                  player_hp = player_hp - shriek_dmg
                  print("Your defense goes up, but your friend is quick to screech.")
                  print('Their scream is deafening and leaves you quaking.')
               
          elif player_choice == 'defend' and computer_choice  == 'Shield' or player_choice == 'd' and computer_choice  == 'Shield': #defend vs shield
              print('Defend', defense_hp, 'vs Shield', shield_hp)
              player_hp = player_hp + 5
              enemy_hp = enemy_hp + 3
              print('You both charge at each other with defenses up. Neither open for attack.')
              print('You both take time to recover and stare at each other cautiously.')

#=====================================================================================================================================

          if player_hp >= 0 and enemy_hp <= 0:
              if room_visits['Drawing Room'] == 1:
                  print("")
                  print('''
You land the final hit. Your friend coughs up red. So much red.

Your friend laughs slightly, as if you just told a bad joke.
They seem relieved almost. You catch them before they hit the ground.

They tell you they love you.
That you are important to them.
That they are sorry for ever causing you hurt.

You repeat the kind words back to them through teary eyes.
They grab your hand and give you a shard.

They jokingly punch your shoulder lightly.

Then they fade out of your arms, your only remnant of them the jagged glass.
''')
                  print("")
                  inventory.append('shard-of-love')
                  room_visits['Drawing Room'] += 1
                  player_wins = player_wins +1
                  defense_hp = defense_max
                  player_hp = player_hp + 80              
              
#================================FAMILY MEMBER=============================================
              
  if currentRoom == 'Master Bedroom':
      if currentRoom == 'Master Bedroom' and room_visits['Master Bedroom'] == 0:
          enemy_hp = 100
          Shieldhp = 70
          
                
          if player_wins == 0:
              print('You enter the room with caution. Something is very wrong here.')
          elif player_wins == 1:
              print('Your heart is beating rapidly in your chest as you fear for another encounter.')
          elif player_wins == 2:
              print('You feel a true sense of neautrality, and maybe for the first time, excitement. Who will it be this time?')
          elif player_wins == 3:
              print('Your heart feels heavy and your mind is running at miles a minute. You feel sad, not afraid.')
          
      if room_visits[currentRoom] == 0: #If this is your first time coming to this room, a message appears
           print("")
           print("You see a familiar face... your family member. Before you can say anything they start dashing towards you.")
           room_visits[currentRoom] += 1 #No message appears if you enter this room a second time
      while player_hp > 0 and enemy_hp > 0:#Fight against enemy if both of you are above 0 hp
          print(" _______________________________________________________")
          print("|You have", player_hp, "health left. The enemy has", enemy_hp,"health left.") #Yours and Enemy HP           
          print("|Your Defense Hp =", defense_hp,)
          player_choice = str(input("Choose : punch (p), kick (k), scratch (s), defend (d), info (i): ")) #Your options
          computer_choice = random.choice(enemy_choice) #Computer chooses out of a list
          if player_choice == 'Info' or player_choice == 'info' or player_choice == 'i': #Player_choice == Info
            print('')
            print('''
Kick is your strongest attack, but against enemy's Strike you can lose up to 15 hp.
Punch is your second strongest attack. When picked against Shriek, you can deal up to 30 damage.
Scratch is one of your weakest attacks, but against Slash, can deal up to 25 damage.
Defend is your shield. You will lose defense hp every time you use defend, but gain hp. Except for when against Shriek, you will lose hp.
''')
            print('')
            
          elif player_choice == 'ohdip':
              enemy_hp = enemy_hp - enemy_hp
              print('Sneaky ;)')
             
#====================================KICK===================================================
             
          elif player_choice == 'kick' and computer_choice  == 'Slash' or player_choice == 'k' and computer_choice  == 'Slash': #kick vs slash
              player_hp = player_hp - slash_dmg
              enemy_hp = enemy_hp - kick_dmg
              print('Kick', kick_dmg, 'vs Slash', slash_dmg)
              print('You and your family both hurt each other. You both stumble back.')
              print('They look angry and, it pains you to see, hurt.')
               
          elif player_choice == 'kick' and computer_choice  == 'Strike' or player_choice == 'k' and computer_choice  == 'Strike': #kick vs strike
              player_hp = player_hp - strike_dmg - 5
              enemy_hp = enemy_hp + 5
              print('Kick', kick_dmg, 'vs Strike', strike_dmg)
              print('Your family member strikes you brutally with their sword.')
              print('Why are they doing this? You feel anger bubbling up.')
               
          elif player_choice == 'kick' and computer_choice  == 'Shriek' or player_choice == 'k' and computer_choice  == 'Shriek': #kick vs shriek
              enemy_hp = enemy_hp - kick_dmg
              player_hp = player_hp + 7
              print('Kick', kick_dmg, 'vs Shriek', shriek_dmg)
              print('Your family member opens their mouth, but before they can make a sound you kick them strongly in the chest.')
              print('You look at them guiltily as they spit blood and stare at you with scorching hate.')
              if player_hp >= player_max:
                  player_hp = player_max
                  print("You've reached full health.")
               
          elif player_choice == 'kick' and computer_choice  == 'Shield' or player_choice == 'k' and computer_choice  == 'Shield': #kick vs shield
              print('Kick', kick_dmg, 'vs Shield', shield_hp)
              if shield_hp >= 0:
                  shield_hp = shield_hp - kick_dmg - 10
                  enemy_hp = enemy_hp + 3
                  print('Your family member puts up their shield and blocks your kick. The regain some health, while behind their shield.')
                  print('You wish you could somehow talk to them.')
                  if enemy_hp >= enemy_max:
                      enemy_hp = enemy_max
                      print('Your enemy has reached full health. Be wary.')
              else:
                  enemy_hp = enemy_hp - kick_dmg
                  print("Your family member's shield is too weak to defend against your kick.")
                  print('Your heel meets them directly in their ribs, making them double over.') 
                  
#====================================PUNCH================================================
               
          elif player_choice == 'punch' and computer_choice  == 'Slash' or player_choice == 'p' and computer_choice  == 'Slash': #punch vs slash
              player_hp = player_hp - slash_dmg - 5
              enemy_hp = enemy_hp + 5
              print('Punch', punch_dmg, 'vs Slash', slash_dmg)
              print('You drive your knuckle toward someone you thought you never would. They slash back at you.')
              print('But not before you skim their jaw with your fist.')
              print("You feel petty joy at getting a hit in, even though you're a great deal more hurt.")
              
          elif player_choice == 'punch' and computer_choice  == 'Strike' or player_choice == 'p' and computer_choice  == 'Strike': #punch vs strike
              player_hp = player_hp - strike_dmg
              enemy_hp = enemy_hp - punch_dmg
              print('Punch', punch_dmg, 'vs Strike', strike_dmg)
              print('You and your family both hurt each other. You both stumble back.')
              print('They look angry and, it pains you to see, hurt.')
               
          elif player_choice == 'punch' and computer_choice  == 'Shriek' or player_choice == 'p' and computer_choice  == 'Shriek': #punch vs shriek
              enemy_hp = enemy_hp - punch_dmg - 10
              player_hp = player_hp + 9
              print('Punch', punch_dmg, 'vs Shriek', shriek_dmg)
              print('Before your family member even makes a sound, your fist collides with their jaw.')
              print('They stagger back, shocked and dazed.')
              print('You feel a sense of guilty joy.')
              if player_hp >= player_max:
                  player_hp = player_max
                  print("You've reached full health.")
                            
          elif player_choice == 'punch' and computer_choice  == 'Shield' or player_choice == 'p' and computer_choice  == 'Shield': #punch vs shield
              print('Punch', punch_dmg, 'vs Shield', shield_hp)
              if shield_hp >0:
                  shield_hp = shield_hp - 15
                  enemy_hp = enemy_hp - punch_dmg
                  print("Your family member's shield goes up, but you are quick to pull it away,")
                  print('and land a solid punch right in their stomach.')
                  print('They double over in agony. You do not feel any happiness.')
              else:
                  enemy_hp = enemy_hp - punch_dmg
                  print("Your family member's shield goes up, but it is too weak to protect them.")
                  print('You swing your fist and land a solid punch right in their stomach.')
                  print('They double over in agony. You do not feel any happiness.')
               
#====================================SCRATCH===============================================
               
          elif player_choice == 'scratch' and computer_choice  == 'Slash' or player_choice == 's' and computer_choice  == 'Slash': #scratch vs slash
              enemy_hp = enemy_hp - scratch_dmg - 15
              player_hp = player_hp + 10
              print('Scratch', scratch_dmg, 'vs Slash', slash_dmg)
              print('Your family member moves to slash your chest with their sword, but before they can execute their move,')
              print('you are quick to scratch their face, harshly.')
              print('You can see their skin turn red as blood emerges from under their skin.')
              print('You hate yourself in this moment.')
               
          elif player_choice == 'scratch' and computer_choice  == 'Strike' or player_choice == 's' and computer_choice  == 'Strike': #scratch vs strike
              player_hp = player_hp - strike_dmg - 10
              enemy_hp = enemy_hp + 5
              print('Scratch', scratch_dmg, 'vs Strike', strike_dmg)
              print("You attempt to reach for your loved one's face, but they strike you in the abdomen with the hilt of their sword.")
              print('They scowl at you, their anger equivalent to your pain.')
              print('You cough up blood and look at them with... guilt? Why are you guilty?')
               
          elif player_choice == 'scratch' and computer_choice  == 'Shriek' or player_choice == 's' and computer_choice  == 'Shriek': #scratch vs shriek
              player_hp = player_hp - scratch_dmg
              enemy_hp = enemy_hp - shriek_dmg
              print('Scratch', scratch_dmg, 'vs Shriek', shriek_dmg)
              print('You and your family both hurt each other. You both stumble back.')
              print('They look angry and, it pains you to see, hurt.')   
               
          elif player_choice == 'scratch' and computer_choice  == 'Shield' or player_choice == 's' and computer_choice  == 'Shield': #scratch vs shield
              print('Scratch', scratch_dmg, 'vs Shield', shield_hp)
              if shield_hp >= 0:
                  shield_hp = shield_hp - scratch_dmg - 10
                  enemy_hp = enemy_hp + 3
                  print('Your family member puts up their shield and blocks your scratch. The regain some health, while behind their shield.')
                  print('You wish you could somehow talk to them.')
                  if enemy_hp >= enemy_max:
                      enemy_hp = enemy_max
                      print('Your enemy has reached full health. Be wary.')
              else:
                  enemy_hp = enemy_hp - scratch_dmg
                  print("Your loved one's shield is too weak to defend against your kick.")
                  print('Your heel meets them directly in their ribs, making them double over.')
                  
#====================================DEFEND=================================================
               
          elif player_choice == 'defend' and computer_choice  == 'Slash' or player_choice == 'd' and computer_choice  == 'Slash': #defend vs slash
              print('Defend', defense_hp, 'vs Slash', slash_dmg)
              if defense_hp >= 0:
                  defense_hp = defense_hp - slash_dmg + 20
                  player_hp = player_hp + 5
                  print("You put up your defense againt your family member's sword, you stumble backwards. Shaken.")
              else:
                  player_hp = player_hp - slash_dmg
                  print('You were too weak to protect yourself. You keel over in pain.')
               
          elif player_choice == 'defend' and computer_choice  == 'Strike' or player_choice == 'd' and computer_choice  == 'Strike': #defend vs strike
              print('Defend', defense_hp, 'vs Strike', strike_dmg)
              if defense_hp >= 0:
                  defense_hp = defense_hp - strike_dmg + 10
                  player_hp = player_hp + 5
                  print("You put up your defense againt your family's strike, you stumble backwards. Shaken.")
              else:
                  player_hp = player_hp - slash_dmg
                  print('You were too weak to protect yourself. You keel over in pain.')
               
          elif player_choice == 'defend' and computer_choice  == 'Shriek' or player_choice == 'd' and computer_choice  == 'Shriek': #defend vs shriek
              print('Defend', defense_hp, 'vs Shriek', shriek_dmg)
              if defense_hp >0:
                  defense_hp = defense_hp - 10
                  player_hp = player_hp - shriek_dmg
                  print("Your defense goes up, but your family member is quick to screech.")
                  print('Their scream is deafening and leaves you quaking.')
              else:
                  player_hp = player_hp - shriek_dmg
                  print("Your defense goes up, but your family member is quick to screech.")
                  print('Their scream is deafening and leaves you quaking.')
               
          elif player_choice == 'defend' and computer_choice  == 'Shield' or player_choice == 'd' and computer_choice  == 'Shield': #defend vs shield
              print('Defend', defense_hp, 'vs Shield', shield_hp)
              player_hp = player_hp + 5
              enemy_hp = enemy_hp + 3
              print('You both charge at each other with defenses up. Neither open for attack.')
              print('You both take time to recover and stare at each other cautiously.')

#=====================================================================================================================================
        
          if player_hp >= 0 and enemy_hp <= 0:
              if room_visits['Master Bedroom'] == 1:
                  print("")
                  print('''
You land the final hit and your family member staggers backwards. As if suddenly broken from a trance.
They sway and you move to catch them as they hit the ground.

They look at you and smile. Their hand on the side of your face. Soft and warm.
You place your own hand over theirs.

They cough up some blood and then start talking.

"I'm sorry. I'm sorry I couldn't understand you."

"I'm sorry I wasn't there when you needed me."

"I'm sorry for not telling you how much I love you. How dear you are to me."

You realize you are crying when they blink as a drop of tear lands on their face from your chin.

You don't know what to say back but that's okay. They know.
They understand. They take your other hand and place a shard in it.

Before fading out of your arms.
Any trace of their existence vanishing instantly, except for the sharp shard in your hand.
''')
                  print("")
                  inventory.append('shard-of-patience')
                  room_visits['Master Bedroom'] += 1
                  player_wins = player_wins +1
                  defense_hp = defense_max
                  player_hp = player_hp + 80
                  
#===================================MENTOR=====================================================
                  
  if currentRoom == 'Library':     
      if currentRoom == 'Library' and room_visits['Library'] == 0:
          enemy_hp = 100
          Shieldhp = 70
          
          if player_wins == 0:
              print('You enter the room with caution. Something is very wrong here.')
          elif player_wins == 1:
              print('Your heart is beating rapidly in your chest as you fear for another encounter.')
          elif player_wins == 2:
              print('You feel a true sense of neautrality, and maybe for the first time, excitement. Who will it be this time?')
          elif player_wins == 3:
              print('Your heart feels heavy and your mind is running at miles a minute. You feel sad, not afraid.')
          
      if room_visits[currentRoom] == 0: #If this is your first time coming to this room, a message appears
           print("")
           print("You see a familiar face... your mentor. Before you can say anything they start dashing towards you.")
           room_visits[currentRoom] += 1 #No message appears if you enter this room a second time
      while player_hp > 0 and enemy_hp > 0:#Fight against enemy if both of you are above 0 hp
          print(" _______________________________________________________")
          print("|You have", player_hp, "health left. The enemy has", enemy_hp,"health left.") #Yours and Enemy HP           
          print("|Your Defense Hp =", defense_hp,)
          player_choice = str(input("Choose : punch (p), kick (k), scratch (s), defend (d), info (i): ")) #Your options
          computer_choice = random.choice(enemy_choice) #Computer chooses out of a list
          if player_choice == 'Info' or player_choice == 'info' or player_choice == 'i': #Player_choice == Info
            print('')
            print('''
Kick is your strongest attack, but against enemy's Strike you can lose up to 15 hp.
Punch is your second strongest attack. When picked against Shriek, you can deal up to 30 damage.
Scratch is one of your weakest attacks, but against Slash, can deal up to 25 damage.
Defend is your shield. You will lose defense hp every time you use defend, but gain hp. Except for when against Shriek, you will lose hp.
''')
            print('')
            
          elif player_choice == 'ohdip':
              enemy_hp = enemy_hp - enemy_hp
              print('Sneaky ;)')
             
#====================================KICK===================================================
             
          elif player_choice == 'kick' and computer_choice  == 'Slash' or player_choice == 'k' and computer_choice  == 'Slash': #kick vs slash
              player_hp = player_hp - slash_dmg
              enemy_hp = enemy_hp - kick_dmg
              print('Kick', kick_dmg, 'vs Slash', slash_dmg)
              print('You and your mentor both hurt each other. You both stumble back.')
              print('They look angry and, it pains you to see, hurt.')
               
          elif player_choice == 'kick' and computer_choice  == 'Strike' or player_choice == 'k' and computer_choice  == 'Strike': #kick vs strike
              player_hp = player_hp - strike_dmg - 5
              enemy_hp = enemy_hp + 5
              print('Kick', kick_dmg, 'vs Strike', strike_dmg)
              print('Your mentor strikes you brutally with their sword.')
              print('Why are they doing this? You feel anger bubbling up.')
               
          elif player_choice == 'kick' and computer_choice  == 'Shriek' or player_choice == 'k' and computer_choice  == 'Shriek': #kick vs shriek
              enemy_hp = enemy_hp - kick_dmg
              player_hp = player_hp + 7
              print('Kick', kick_dmg, 'vs Shriek', shriek_dmg)
              print('Your mentor opens their mouth, but before they can make a sound you kick them strongly in the chest.')
              print('You look at them guiltily as they spit blood and stare at you with scorching hate.')
              if player_hp >= player_max:
                  player_hp = player_max
                  print("You've reached full health.")
               
          elif player_choice == 'kick' and computer_choice  == 'Shield' or player_choice == 'k' and computer_choice  == 'Shield': #kick vs shield
              print('Kick', kick_dmg, 'vs Shield', shield_hp)
              if shield_hp >= 0:
                  shield_hp = shield_hp - kick_dmg - 10
                  enemy_hp = enemy_hp + 3
                  print('Your mentor puts up their shield and blocks your kick. The regain some health, while behind their shield.')
                  print('You wish you could somehow talk to them.')
                  if enemy_hp >= enemy_max:
                      enemy_hp = enemy_max
                      print('Your enemy has reached full health. Be wary.')
              else:
                  enemy_hp = enemy_hp - kick_dmg
                  print("Your mentor's shield is too weak to defend against your kick.")
                  print('Your heel meets them directly in their ribs, making them double over.') 
                  
#====================================PUNCH================================================
               
          elif player_choice == 'punch' and computer_choice  == 'Slash' or player_choice == 'p' and computer_choice  == 'Slash': #punch vs slash
              player_hp = player_hp - slash_dmg - 5
              enemy_hp = enemy_hp + 5
              print('Punch', punch_dmg, 'vs Slash', slash_dmg)
              print('You drive your knuckle toward someone you thought you never would. They slash back at you.')
              print('But not before you skim their jaw with your fist.')
              print("You feel petty joy at getting a hit in, even though you're a great deal more hurt.")
              
          elif player_choice == 'punch' and computer_choice  == 'Strike' or player_choice == 'p' and computer_choice  == 'Strike': #punch vs strike
              player_hp = player_hp - strike_dmg
              enemy_hp = enemy_hp - punch_dmg
              print('Punch', punch_dmg, 'vs Strike', strike_dmg)
              print('You and your mentor both hurt each other. You both stumble back.')
              print('They look angry and, it pains you to see, hurt.')
               
          elif player_choice == 'punch' and computer_choice  == 'Shriek' or player_choice == 'p' and computer_choice  == 'Shriek': #punch vs shriek
              enemy_hp = enemy_hp - punch_dmg - 10
              player_hp = player_hp + 9
              print('Punch', punch_dmg, 'vs Shriek', shriek_dmg)
              print('Before your mentor even makes a sound, your fist collides with their jaw.')
              print('They stagger back, shocked and dazed.')
              print('You feel a sense of guilty joy.')
              if player_hp >= player_max:
                  player_hp = player_max
                  print("You've reached full health.")
                            
          elif player_choice == 'punch' and computer_choice  == 'Shield' or player_choice == 'p' and computer_choice  == 'Shield': #punch vs shield
              print('Punch', punch_dmg, 'vs Shield', shield_hp)
              if shield_hp >0:
                  shield_hp = shield_hp - 15
                  enemy_hp = enemy_hp - punch_dmg
                  print("Your mentor's shield goes up, but you are quick to pull it away,")
                  print('and land a solid punch right in their stomach.')
                  print('They double over in agony. You do not feel any happiness.')
              else:
                  enemy_hp = enemy_hp - punch_dmg
                  print("Your mentor's shield goes up, but it is too weak to protect them.")
                  print('You swing your fist and land a solid punch right in their stomach.')
                  print('They double over in agony. You do not feel any happiness.')
               
#====================================SCRATCH===============================================
               
          elif player_choice == 'scratch' and computer_choice  == 'Slash' or player_choice == 's' and computer_choice  == 'Slash': #scratch vs slash
              enemy_hp = enemy_hp - scratch_dmg - 15
              player_hp = player_hp + 10
              print('Scratch', scratch_dmg, 'vs Slash', slash_dmg)
              print('Your mentor moves to slash your chest with their sword, but before they can execute their move,')
              print('you are quick to scratch their face, harshly.')
              print('You can see their skin turn red as blood emerges from under their skin.')
              print('You hate yourself in this moment.')
               
          elif player_choice == 'scratch' and computer_choice  == 'Strike' or player_choice == 's' and computer_choice  == 'Strike': #scratch vs strike
              player_hp = player_hp - strike_dmg - 10
              enemy_hp = enemy_hp + 5
              print('Scratch', scratch_dmg, 'vs Strike', strike_dmg)
              print("You attempt to reach for your mentor's face, but they strike you in the abdomen with the hilt of their sword.")
              print('They scowl at you, their anger equivalent to your pain.')
              print('You cough up blood and look at them with... guilt? Why are you guilty?')
               
          elif player_choice == 'scratch' and computer_choice  == 'Shriek' or player_choice == 's' and computer_choice  == 'Shriek': #scratch vs shriek
              player_hp = player_hp - scratch_dmg
              enemy_hp = enemy_hp - shriek_dmg
              print('Scratch', scratch_dmg, 'vs Shriek', shriek_dmg)
              print('You and your mentor both hurt each other. You both stumble back.')
              print('They look angry and, it pains you to see, hurt.')   
               
          elif player_choice == 'scratch' and computer_choice  == 'Shield' or player_choice == 's' and computer_choice  == 'Shield': #scratch vs shield
              print('Scratch', scratch_dmg, 'vs Shield', shield_hp)
              if shield_hp >= 0:
                  shield_hp = shield_hp - scratch_dmg - 10
                  enemy_hp = enemy_hp + 3
                  print('Your mentor puts up their shield and blocks your scratch. The regain some health, while behind their shield.')
                  print('You wish you could somehow talk to them.')
                  if enemy_hp >= enemy_max:
                      enemy_hp = enemy_max
                      print('Your enemy has reached full health. Be wary.')
              else:
                  enemy_hp = enemy_hp - scratch_dmg
                  print("Your mentor's shield is too weak to defend against your kick.")
                  print('Your heel meets them directly in their ribs, making them double over.')
                  
#====================================DEFEND=================================================
               
          elif player_choice == 'defend' and computer_choice  == 'Slash' or player_choice == 'd' and computer_choice  == 'Slash': #defend vs slash
              print('Defend', defense_hp, 'vs Slash', slash_dmg)
              if defense_hp >= 0:
                  defense_hp = defense_hp - slash_dmg + 20
                  player_hp = player_hp + 5
                  print("You put up your defense againt your mentor's sword, you stumble backwards. Shaken.")
              else:
                  player_hp = player_hp - slash_dmg
                  print('You were too weak to protect yourself. You keel over in pain.')
               
          elif player_choice == 'defend' and computer_choice  == 'Strike' or player_choice == 'd' and computer_choice  == 'Strike': #defend vs strike
              print('Defend', defense_hp, 'vs Strike', strike_dmg)
              if defense_hp >= 0:
                  defense_hp = defense_hp - strike_dmg + 10
                  player_hp = player_hp + 5
                  print("You put up your defense againt your mentor's strike, you stumble backwards. Shaken.")
              else:
                  player_hp = player_hp - slash_dmg
                  print('You were too weak to protect yourself. You keel over in pain.')
               
          elif player_choice == 'defend' and computer_choice  == 'Shriek' or player_choice == 'd' and computer_choice  == 'Shriek': #defend vs shriek
              print('Defend', defense_hp, 'vs Shriek', shriek_dmg)
              if defense_hp >0:
                  defense_hp = defense_hp - 10
                  player_hp = player_hp - shriek_dmg
                  print("Your defense goes up, but your mentor is quick to screech.")
                  print('Their scream is deafening and leaves you quaking.')
              else:
                  player_hp = player_hp - shriek_dmg
                  print("Your defense goes up, but your mentor is quick to screech.")
                  print('Their scream is deafening and leaves you quaking.')
               
          elif player_choice == 'defend' and computer_choice  == 'Shield' or player_choice == 'd' and computer_choice  == 'Shield': #defend vs shield
              print('Defend', defense_hp, 'vs Shield', shield_hp)
              player_hp = player_hp + 5
              enemy_hp = enemy_hp + 3
              print('You both charge at each other with defenses up. Neither open for attack.')
              print('You both take time to recover and stare at each other cautiously.')

#=====================================================================================================================================
        
          if player_hp >= 0 and enemy_hp <= 0:
              if room_visits['Library'] == 1:
                  print("")
                  print('''
You land the final hit and your mentor looks at you with something like... pride?
They lean backwards and you catch them as their knees buckle.

They say your name. They say it with contentment.

They tell you,

"I'm so proud of you. I'm so proud of how far you've come.
You've struggled, no doubt, but you managed to get here. All on your own.
I'm so honored to have been your guidance. To have taught you.

You can go the rest of the way on your own. I know you can. And you will.
Have strength."

They grip your hand with power and then slump in your arms, before fading away completely.

You're crying. Sobbing. You made them proud.

You notice a shard in your hand. Your only memorabilia of your role model.
''')
                  print("")
                  inventory.append('shard-of-strength')
                  room_visits['Library'] += 1
                  player_wins = player_wins +1
                  defense_hp = defense_max
                  player_hp = player_hp + 80
                  
#====================================CRUSH=====================================================
                  
  if currentRoom == 'Sunroom':
      if currentRoom == 'Sunroom' and room_visits['Sunroom'] == 0:
          enemy_hp = 100
          Shieldhp = 70
          
                
          if player_wins == 0:
              print('You enter the room with caution. Something is very wrong here.')
          elif player_wins == 1:
              print('Your heart is beating rapidly in your chest as you fear for another encounter.')
          elif player_wins == 2:
              print('You feel a true sense of neautrality, and maybe for the first time, excitement. Who will it be this time?')
          elif player_wins == 3:
              print('Your heart feels heavy and your mind is running at miles a minute. You feel sad, not afraid.')
          
      if room_visits[currentRoom] == 0: #If this is your first time coming to this room, a message appears
           print("")
           print("You see a familiar face... your crush. Before you can say anything they start dashing towards you.")
           room_visits[currentRoom] += 1 #No message appears if you enter this room a second time
      while player_hp > 0 and enemy_hp > 0:#Fight against enemy if both of you are above 0 hp
          print(" _______________________________________________________")
          print("|You have", player_hp, "health left. The enemy has", enemy_hp,"health left.") #Yours and Enemy HP           
          print("|Your Defense Hp =", defense_hp,)
          player_choice = str(input("Choose : punch (p), kick (k), scratch (s), defend (d), info (i): ")) #Your options
          computer_choice = random.choice(enemy_choice) #Computer chooses out of a list
          if player_choice == 'Info' or player_choice == 'info' or player_choice == 'i': #Player_choice == Info
            print('')
            print('''
Kick is your strongest attack, but against enemy's Strike you can lose up to 15 hp.
Punch is your second strongest attack. When picked against Shriek, you can deal up to 30 damage.
Scratch is one of your weakest attacks, but against Slash, can deal up to 25 damage.
Defend is your shield. You will lose defense hp every time you use defend, but gain hp. Except for when against Shriek, you will lose hp.
''')
            print('')
            
          elif player_choice == 'ohdip':
              enemy_hp = enemy_hp - enemy_hp
              print('Sneaky ;)')
             
#====================================KICK===================================================
             
          elif player_choice == 'kick' and computer_choice  == 'Slash' or player_choice == 'k' and computer_choice  == 'Slash': #kick vs slash
              player_hp = player_hp - slash_dmg
              enemy_hp = enemy_hp - kick_dmg
              print('Kick', kick_dmg, 'vs Slash', slash_dmg)
              print('You and your crush both hurt each other. You both stumble back.')
              print('They look angry and, it pains you to see, hurt.')
               
          elif player_choice == 'kick' and computer_choice  == 'Strike' or player_choice == 'k' and computer_choice  == 'Strike': #kick vs strike
              player_hp = player_hp - strike_dmg - 5
              enemy_hp = enemy_hp + 5
              print('Kick', kick_dmg, 'vs Strike', strike_dmg)
              print('Your crush strikes you brutally with their sword.')
              print('Why are they doing this? You feel anger bubbling up.')
               
          elif player_choice == 'kick' and computer_choice  == 'Shriek' or player_choice == 'k' and computer_choice  == 'Shriek': #kick vs shriek
              enemy_hp = enemy_hp - kick_dmg
              player_hp = player_hp + 7
              print('Kick', kick_dmg, 'vs Shriek', shriek_dmg)
              print('Your crush opens their mouth, but before they can make a sound you kick them strongly in the chest.')
              print('You look at them guiltily as they spit blood and stare at you with scorching hate.')
              if player_hp >= player_max:
                  player_hp = player_max
                  print("You've reached full health.")
               
          elif player_choice == 'kick' and computer_choice  == 'Shield' or player_choice == 'k' and computer_choice  == 'Shield': #kick vs shield
              print('Kick', kick_dmg, 'vs Shield', shield_hp)
              if shield_hp >= 0:
                  shield_hp = shield_hp - kick_dmg - 10
                  enemy_hp = enemy_hp + 3
                  print('Your crush puts up their shield and blocks your kick. The regain some health, while behind their shield.')
                  print('You wish you could somehow talk to them.')
                  if enemy_hp >= enemy_max:
                      enemy_hp = enemy_max
                      print('Your enemy has reached full health. Be wary.')
              else:
                  enemy_hp = enemy_hp - kick_dmg
                  print("Your crush's shield is too weak to defend against your kick.")
                  print('Your heel meets them directly in their ribs, making them double over.') 
                  
#====================================PUNCH================================================
               
          elif player_choice == 'punch' and computer_choice  == 'Slash' or player_choice == 'p' and computer_choice  == 'Slash': #punch vs slash
              player_hp = player_hp - slash_dmg - 5
              enemy_hp = enemy_hp + 5
              print('Punch', punch_dmg, 'vs Slash', slash_dmg)
              print('You drive your knuckle toward someone you thought you never would. They slash back at you.')
              print('But not before you skim their jaw with your fist.')
              print("You feel petty joy at getting a hit in, even though you're a great deal more hurt.")
              
          elif player_choice == 'punch' and computer_choice  == 'Strike' or player_choice == 'p' and computer_choice  == 'Strike': #punch vs strike
              player_hp = player_hp - strike_dmg
              enemy_hp = enemy_hp - punch_dmg
              print('Punch', punch_dmg, 'vs Strike', strike_dmg)
              print('You and your crush both hurt each other. You both stumble back.')
              print('They look angry and, it pains you to see, hurt.')
               
          elif player_choice == 'punch' and computer_choice  == 'Shriek' or player_choice == 'p' and computer_choice  == 'Shriek': #punch vs shriek
              enemy_hp = enemy_hp - punch_dmg - 10
              player_hp = player_hp + 9
              print('Punch', punch_dmg, 'vs Shriek', shriek_dmg)
              print('Before your crush even makes a sound, your fist collides with their jaw.')
              print('They stagger back, shocked and dazed.')
              print('You feel a sense of guilty joy.')
              if player_hp >= player_max:
                  player_hp = player_max
                  print("You've reached full health.")
                            
          elif player_choice == 'punch' and computer_choice  == 'Shield' or player_choice == 'p' and computer_choice  == 'Shield': #punch vs shield
              print('Punch', punch_dmg, 'vs Shield', shield_hp)
              if shield_hp >0:
                  shield_hp = shield_hp - 15
                  enemy_hp = enemy_hp - punch_dmg
                  print("Your crush's shield goes up, but you are quick to pull it away,")
                  print('and land a solid punch right in their stomach.')
                  print('They double over in agony. You do not feel any happiness.')
              else:
                  enemy_hp = enemy_hp - punch_dmg
                  print("Your crush's shield goes up, but it is too weak to protect them.")
                  print('You swing your fist and land a solid punch right in their stomach.')
                  print('They double over in agony. You do not feel any happiness.')
               
#====================================SCRATCH===============================================
               
          elif player_choice == 'scratch' and computer_choice  == 'Slash' or player_choice == 's' and computer_choice  == 'Slash': #scratch vs slash
              enemy_hp = enemy_hp - scratch_dmg - 15
              player_hp = player_hp + 10
              print('Scratch', scratch_dmg, 'vs Slash', slash_dmg)
              print('Your crush moves to slash your chest with their sword, but before they can execute their move,')
              print('you are quick to scratch their face, harshly.')
              print('You can see their skin turn red as blood emerges from under their skin.')
              print('You hate yourself in this moment.')
               
          elif player_choice == 'scratch' and computer_choice  == 'Strike' or player_choice == 's' and computer_choice  == 'Strike': #scratch vs strike
              player_hp = player_hp - strike_dmg - 10
              enemy_hp = enemy_hp + 5
              print('Scratch', scratch_dmg, 'vs Strike', strike_dmg)
              print("You attempt to reach for your crush's face, but they strike you in the abdomen with the hilt of their sword.")
              print('They scowl at you, their anger equivalent to your pain.')
              print('You cough up blood and look at them with... guilt? Why are you guilty?')
               
          elif player_choice == 'scratch' and computer_choice  == 'Shriek' or player_choice == 's' and computer_choice  == 'Shriek': #scratch vs shriek
              player_hp = player_hp - scratch_dmg
              enemy_hp = enemy_hp - shriek_dmg
              print('Scratch', scratch_dmg, 'vs Shriek', shriek_dmg)
              print('You and your crush both hurt each other. You both stumble back.')
              print('They look angry and, it pains you to see, hurt.')   
               
          elif player_choice == 'scratch' and computer_choice  == 'Shield' or player_choice == 's' and computer_choice  == 'Shield': #scratch vs shield
              print('Scratch', scratch_dmg, 'vs Shield', shield_hp)
              if shield_hp >= 0:
                  shield_hp = shield_hp - scratch_dmg - 10
                  enemy_hp = enemy_hp + 3
                  print('Your crush puts up their shield and blocks your scratch. The regain some health, while behind their shield.')
                  print('You wish you could somehow talk to them.')
                  if enemy_hp >= enemy_max:
                      enemy_hp = enemy_max
                      print('Your enemy has reached full health. Be wary.')
              else:
                  enemy_hp = enemy_hp - scratch_dmg
                  print("Your crush's shield is too weak to defend against your kick.")
                  print('Your heel meets them directly in their ribs, making them double over.')
                  
#====================================DEFEND=================================================
               
          elif player_choice == 'defend' and computer_choice  == 'Slash' or player_choice == 'd' and computer_choice  == 'Slash': #defend vs slash
              print('Defend', defense_hp, 'vs Slash', slash_dmg)
              if defense_hp >= 0:
                  defense_hp = defense_hp - slash_dmg + 20
                  player_hp = player_hp + 5
                  print("You put up your defense againt your crush's sword, you stumble backwards. Shaken.")
              else:
                  player_hp = player_hp - slash_dmg
                  print('You were too weak to protect yourself. You keel over in pain.')
               
          elif player_choice == 'defend' and computer_choice  == 'Strike' or player_choice == 'd' and computer_choice  == 'Strike': #defend vs strike
              print('Defend', defense_hp, 'vs Strike', strike_dmg)
              if defense_hp >= 0:
                  defense_hp = defense_hp - strike_dmg + 10
                  player_hp = player_hp + 5
                  print("You put up your defense againt your crush's strike, you stumble backwards. Shaken.")
              else:
                  player_hp = player_hp - slash_dmg
                  print('You were too weak to protect yourself. You keel over in pain.')
               
          elif player_choice == 'defend' and computer_choice  == 'Shriek' or player_choice == 'd' and computer_choice  == 'Shriek': #defend vs shriek
              print('Defend', defense_hp, 'vs Shriek', shriek_dmg)
              if defense_hp >0:
                  defense_hp = defense_hp - 10
                  player_hp = player_hp - shriek_dmg
                  print("Your defense goes up, but your crush is quick to screech.")
                  print('Their scream is deafening and leaves you quaking.')
              else:
                  player_hp = player_hp - shriek_dmg
                  print("Your defense goes up, but your crush is quick to screech.")
                  print('Their scream is deafening and leaves you quaking.')
               
          elif player_choice == 'defend' and computer_choice  == 'Shield' or player_choice == 'd' and computer_choice  == 'Shield': #defend vs shield
              print('Defend', defense_hp, 'vs Shield', shield_hp)
              player_hp = player_hp + 5
              enemy_hp = enemy_hp + 3
              print('You both charge at each other with defenses up. Neither open for attack.')
              print('You both take time to recover and stare at each other cautiously.')

#=====================================================================================================================================
        
          if player_hp >= 0 and enemy_hp <= 0:
              if room_visits['Sunroom'] == 1:
                  print("")
                  print('''
You land the final hit and immediately feel like throwing up. This is the last thing you ever wanted to do.
You have tears in your eyes when you see your crush staggering towards you, clutching their stomach.

They don't look angry, or hurt. They're smiling at you.
They fall forwards and you catch them before their knees hit the ground.

"Hi.", they say softly.

Your throat is choked up.

"You're a mean fighter.", they say with a light chuckle.

Your heart feels like it's suffocating.

"You're pretty cool you know.", they say while looking away, as if... shy.

You shake your head slightly, not knowing what you're denying.

"Here, something to remember me by. A memento even.", they wink at you, jokingly.
Then they hand you a shard. Closing your fist around it with their own.

They lean upwards, and when you register the feeling of something soft and warm against your cheek, they're already gone.
Faded away.
Their kiss lingering still on your face.
''')
                  print("")
                  inventory.append('shard-of-bravery')
                  room_visits['Sunroom'] += 1
                  player_wins = player_wins +1
                  defense_hp = defense_max
                  player_hp = player_hp + 80
                  
#==================================BOSS FIGHT==================================================
                  
  if currentRoom == 'Bedroom':
      if currentRoom == 'Bedroom' and room_visits['Bedroom'] == 0 and player_wins == 4:
          enemy_hp = boss_hp
          enemy_max = boss_max
          shield_hp = boss_shield_hp
          slash_dmg = boss_slash_dmg
          strike_dmg = boss_strike_dmg
          shriek_dmg = boss_shriek_dmg
          
          print('This is it. Your chance to prove it to yourself.')
          
          if room_visits[currentRoom] == 0 and player_wins == 4: #If this is your first time coming to this room, a message appears
              print("")
              print("You see a familiar face... it's you. You do not need to say anything, you charge.")
              room_visits[currentRoom] += 1 #No message appears if you enter this room a second time
          while player_hp > 0 and enemy_hp > 0:#Fight against enemy if both of you are above 0 hp
              print(" _______________________________________________________")
              print("|You have", player_hp, "health left. The enemy has", enemy_hp,"health left.") #Yours and Enemy HP           
              print("|Your Defense Hp =", defense_hp,)
              player_choice = str(input("Choose : punch (p), kick (k), scratch (s), defend (d), info (i): ")) #Your options
              computer_choice = random.choice(enemy_choice) #Computer chooses out of a list
              if player_choice == 'Info' or player_choice == 'info' or player_choice == 'i': #Player_choice == Info
                print('')
                print('''
Kick is your strongest attack, but against enemy's Strike you can lose up to 15 hp.
Punch is your second strongest attack. When picked against Shriek, you can deal up to 30 damage.
Scratch is one of your weakest attacks, but against Slash, can deal up to 25 damage.
Defend is your shield. You will lose defense hp every time you use defend, but gain hp. Except for when against Shriek, you will lose hp.
''')
                print('')
            
              elif player_choice == 'ohdip':
                  enemy_hp = enemy_hp - enemy_hp
                  print('Sneaky ;)')
             
#====================================KICK===================================================
             
              elif player_choice == 'kick' and computer_choice  == 'Slash' or player_choice == 'k' and computer_choice  == 'Slash': #kick vs slash
                  player_hp = player_hp - slash_dmg
                  enemy_hp = enemy_hp - kick_dmg
                  print('Kick', kick_dmg, 'vs Slash', slash_dmg)
                  print("You've hurt yourself. You both stumble back.")
                  print('Your counterpart looks angry and hurt.')
                   
              elif player_choice == 'kick' and computer_choice  == 'Strike' or player_choice == 'k' and computer_choice  == 'Strike': #kick vs strike
                  player_hp = player_hp - strike_dmg - 5
                  enemy_hp = enemy_hp + 5
                  print('Kick', kick_dmg, 'vs Strike', strike_dmg)
                  print('You strike yourself brutally with your sword.')
                  print('Why are they doing this? You feel anger bubbling up.')
                   
              elif player_choice == 'kick' and computer_choice  == 'Shriek' or player_choice == 'k' and computer_choice  == 'Shriek': #kick vs shriek
                  enemy_hp = enemy_hp - kick_dmg
                  player_hp = player_hp + 7
                  print('Kick', kick_dmg, 'vs Shriek', shriek_dmg)
                  print('Your doppelganger opens their mouth, but before they can make a sound you kick them strongly in the chest.')
                  print('You look at them guiltily as they spit blood and stare at you with scorching hate.')
                  if player_hp >= player_max:
                      player_hp = player_max
                      print("You've reached full health.")
               
              elif player_choice == 'kick' and computer_choice  == 'Shield' or player_choice == 'k' and computer_choice  == 'Shield': #kick vs shield
                  print('Kick', kick_dmg, 'vs Shield', shield_hp)
                  if shield_hp >= 0:
                      shield_hp = shield_hp - kick_dmg - 10
                      enemy_hp = enemy_hp + 3
                      print('Your clone puts up their shield and blocks your kick. The regain some health, while behind their shield.')
                      print('You wish you could somehow talk to them.')
                      if enemy_hp >= enemy_max:
                          enemy_hp = enemy_max
                          print('Your enemy has reached full health. Be wary.')
                  else:
                      enemy_hp = enemy_hp - kick_dmg
                      print("Your counterpart's shield is too weak to defend against your kick.")
                      print('Your heel meets them directly in their ribs, making them double over.') 
                  
#====================================PUNCH================================================
               
              elif player_choice == 'punch' and computer_choice  == 'Slash' or player_choice == 'p' and computer_choice  == 'Slash': #punch vs slash
                  player_hp = player_hp - slash_dmg - 5
                  enemy_hp = enemy_hp + 5
                  print('Punch', punch_dmg, 'vs Slash', slash_dmg)
                  print('You drive your knuckle toward someone you thought you never could. They slash back at you.')
                  print('But not before you skim their jaw with your fist.')
                  print("You feel petty joy at getting a hit in, even though you're a great deal more hurt.")
                  
              elif player_choice == 'punch' and computer_choice  == 'Strike' or player_choice == 'p' and computer_choice  == 'Strike': #punch vs strike
                  player_hp = player_hp - strike_dmg
                  enemy_hp = enemy_hp - punch_dmg
                  print('Punch', punch_dmg, 'vs Strike', strike_dmg)
                  print("You've hurt yourself. You both stumble back.")
                  print('Your counterpart looks angry and hurt.')
                   
              elif player_choice == 'punch' and computer_choice  == 'Shriek' or player_choice == 'p' and computer_choice  == 'Shriek': #punch vs shriek
                  enemy_hp = enemy_hp - punch_dmg - 10
                  player_hp = player_hp + 9
                  print('Punch', punch_dmg, 'vs Shriek', shriek_dmg)
                  print('Before your doppelganger even makes a sound, your fist collides with their jaw.')
                  print('They stagger back, shocked and dazed.')
                  print('You feel a sense of guilty joy.')
                  if player_hp >= player_max:
                      player_hp = player_max
                      print("You've reached full health.")
                                
              elif player_choice == 'punch' and computer_choice  == 'Shield' or player_choice == 'p' and computer_choice  == 'Shield': #punch vs shield
                  print('Punch', punch_dmg, 'vs Shield', shield_hp)
                  if shield_hp >0:
                      shield_hp = shield_hp - 15
                      enemy_hp = enemy_hp - punch_dmg
                      print("Your clone's shield goes up, but you are quick to pull it away,")
                      print('and land a solid punch right in their stomach.')
                      print('They double over in agony.')
                  else:
                      enemy_hp = enemy_hp - punch_dmg
                      print("Your clone's shield goes up, but it is too weak to protect them.")
                      print('You swing your fist and land a solid punch right in their stomach.')
                      print('They double over in agony.')
               
#====================================SCRATCH===============================================
               
              elif player_choice == 'scratch' and computer_choice  == 'Slash' or player_choice == 's' and computer_choice  == 'Slash': #scratch vs slash
                  enemy_hp = enemy_hp - scratch_dmg - 15
                  player_hp = player_hp + 10
                  print('Scratch', scratch_dmg, 'vs Slash', slash_dmg)
                  print('Your reflection moves to slash your chest with their sword, but before they can execute their move,')
                  print('you are quick to scratch their face, harshly.')
                  print('You can see their skin turn red as blood emerges from under their skin.')
                  print('You hate yourself in this moment.')
                   
              elif player_choice == 'scratch' and computer_choice  == 'Strike' or player_choice == 's' and computer_choice  == 'Strike': #scratch vs strike
                  player_hp = player_hp - strike_dmg - 10
                  enemy_hp = enemy_hp + 5
                  print('Scratch', scratch_dmg, 'vs Strike', strike_dmg)
                  print("You attempt to reach for your reflection's face, but they strike you in the abdomen with the hilt of their sword.")
                  print('They scowl at you, their anger equivalent to your pain.')
                  print('You cough up blood and look at them with... guilt? Why are you guilty?')
                   
              elif player_choice == 'scratch' and computer_choice  == 'Shriek' or player_choice == 's' and computer_choice  == 'Shriek': #scratch vs shriek
                  player_hp = player_hp - scratch_dmg
                  enemy_hp = enemy_hp - shriek_dmg
                  print('Scratch', scratch_dmg, 'vs Shriek', shriek_dmg)
                  print("You've hurt yourself. You both stumble back.")
                  print('Your counterpart looks angry and hurt.')  
                   
              elif player_choice == 'scratch' and computer_choice  == 'Shield' or player_choice == 's' and computer_choice  == 'Shield': #scratch vs shield
                  print('Scratch', scratch_dmg, 'vs Shield', shield_hp)
                  if shield_hp >= 0:
                      shield_hp = shield_hp - scratch_dmg - 10
                      enemy_hp = enemy_hp + 3
                      print('Your doppelganger puts up their shield and blocks your scratch. The regain some health, while behind their shield.')
                      print('You wish you could somehow talk to them.')
                      if enemy_hp >= enemy_max:
                          enemy_hp = enemy_max
                          print('Your enemy has reached full health. Be wary.')
                  else:
                      enemy_hp = enemy_hp - scratch_dmg
                      print("Your clone's shield is too weak to defend against your kick.")
                      print('Your heel meets them directly in their ribs, making them double over.')
                  
#====================================DEFEND=================================================
               
              elif player_choice == 'defend' and computer_choice  == 'Slash' or player_choice == 'd' and computer_choice  == 'Slash': #defend vs slash
                  print('Defend', defense_hp, 'vs Slash', slash_dmg)
                  if defense_hp >= 0:
                      defense_hp = defense_hp - slash_dmg + 20
                      player_hp = player_hp + 5
                      print("You put up your defense againt your doppelganger's sword, you stumble backwards. Shaken.")
                  else:
                      player_hp = player_hp - slash_dmg
                      print('You were too weak to protect yourself. You keel over in pain.')
                   
              elif player_choice == 'defend' and computer_choice  == 'Strike' or player_choice == 'd' and computer_choice  == 'Strike': #defend vs strike
                  print('Defend', defense_hp, 'vs Strike', strike_dmg)
                  if defense_hp >= 0:
                      defense_hp = defense_hp - strike_dmg + 10
                      player_hp = player_hp + 5
                      print("You put up your defense againt your own strike, you stumble backwards. Shaken.")
                  else:
                      player_hp = player_hp - slash_dmg
                      print('You were too weak to protect yourself. You keel over in pain.')
                   
              elif player_choice == 'defend' and computer_choice  == 'Shriek' or player_choice == 'd' and computer_choice  == 'Shriek': #defend vs shriek
                  print('Defend', defense_hp, 'vs Shriek', shriek_dmg)
                  if defense_hp >0:
                      defense_hp = defense_hp - 10
                      player_hp = player_hp - shriek_dmg
                      print("Your defense goes up, but your clone is quick to screech.")
                      print('Their scream is deafening and leaves you quaking.')
                  else:
                      player_hp = player_hp - shriek_dmg
                      print("Your defense goes up, but your clone is quick to screech.")
                      print('Their scream is deafening and leaves you quaking.')
                   
              elif player_choice == 'defend' and computer_choice  == 'Shield' or player_choice == 'd' and computer_choice  == 'Shield': #defend vs shield
                  print('Defend', defense_hp, 'vs Shield', shield_hp)
                  player_hp = player_hp + 5
                  enemy_hp = enemy_hp + 3
                  print('You both charge at each other with defenses up. Neither open for attack.')
                  print('You both take time to recover and stare at each other cautiously.')

#=====================================================================================================================================
        
              if player_hp >= 0 and enemy_hp <= 0:
                  if room_visits['Bedroom'] == 1:
                      print("")
                      print('''
You land the final hit. You see yourself stumble and stagger. Shaken.
Your jaw is clenched. You move forwards, knowing you will catch yourself.

Your doppelganger, or clone, or part of you. Whatever vesion of you. They grin.

"About time, huh."
You smile slightly, nodding.

"You did well. I'm proud of you."
You start tearing up.

"You're so brave," they chuckle, "real strong too."

"Didn't know you'd have the patience for this. Proved me wrong huh. Proved yourself wrong."
You open your mouth, wanting to say something. You don't know what, maybe anything.

They cut you off, "No need to, I'm you anyway, you know...", they cough violently, blood staining their mouth.

"You had to do this. You had to let me go. I was holding you back."

"I had to be sacrificed."

"No harsh feelings." They smile broadly.

"I wish the best for you. Good luck."
They smile, but for the first time, you notice their eyes glistening.
Tearing up.

"I love you."

You notice you're already crying, your throat as if in a vice grip. Unable to make a sound.
"I love you too.", you gasp out eventually, through heaving sobs.
The only thing you've said this entire time.

"Here, take this." You know what it is before it even reaches your palm.
Another shard.

"Last one, you know."

"Look at them all together."
"You'll know."

They go limp, their head slumping backwards and their hand hitting the ground.
You close your eyes and you know they've faded away.
''')
                      print("")
                      inventory.append('shard-of-sacrifice')
                      room_visits['Bedroom'] += 1
                      player_wins = player_wins +1
                      defense_hp = defense_max
                      player_hp = player_hp + 80
                  
#==============================HINT FOR BOSS FIGHT=============================================
                  
  if player_wins == 4 and bedroom_hint == 0:
      print('''
That was the last of them...
You're so exhausted. But exhilerated at the same time too.

You know what you have to do now. The bedroom at the second floor.
It's your bedroom.

There's something there you need to deal with.
''')
      bedroom_hint += 1
        
#===================================DEFEAT BY ENEMY ENDINGS====================================================
              
  if player_hp <= 0 and enemy_hp >= 0 and player_wins <= 3:
              print("")
              print('''
The enemy delivers the final blow.
Your eyes slowly close shut as you hear the sound of your body hitting the ground.
Before you see darkness you see the face of the enemy grinning at you.
And you know they are mocking you even in your last moments.
This is a nightmare.
Will you try again? (Ending 2/5)”
''')
  
  if player_hp <=0 and enemy_hp >= 0 and player_wins == 4:
      print('')
      print('''

Your Reflection, or maybe it was never just your reflection, delivers the final blow and you hit the ground hard.
Knowing you are gone before your head meets the carpet. You struggled long and hard.
You fought with all your might.

Why did this happen?
Why did you do this to yourself?
Were you not enough?
Did you not do enough?
Did you deserve this?

Why?
Why?
WHY?!

You are angry and you are dying, blaming yourself, when you see the Reflection of You, or maybe it is you, looking at you.
You are shocked to see that it looks sad, dejected and disappointed.

Why?

You see it slowly reaching for you, more human than maybe you’ve even felt yourself.
You start to reach for its hand…

It’s too late. As fast as the thoughts in your head, your life has ended.

Will you try again? (Ending 3/5)”
''')
                  
  if player_hp == 0 or player_hp <= 0:
      break

