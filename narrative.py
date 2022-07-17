import chara
import items
class Text:
    
    pressenter = ''
    
    def choose_character_menu(self):
        
        print('''

       Select your character!         
+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=
//                                              //
//             1) Hero:                         //
// Stats: (HP: 25, STR: 4, ARM: 1, EV:0)        //
// Hero is the default character with a         //
// decent balance in starting stats. Hero's     //
// special ability is 'Heroic Swing' which      //
// will occasionally double his attack.         //
// his starting HP is 25, and can be raised     //
// to a maximum of 45 HP with health items      //
//                                              //
// (All stats on all characters can be raised)  //
//                                              //
//                                              //
+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=
// Press Enter to continue >>
''')
        
        pressenter = input()
        print( '''

       Select your character!         
+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+
//                                                 //
//             2) Medic:                           //
// Stats: (HP: 25, STR: 2, ARM: 0, EV:0)           //
// Medic is a good choice for for someone          //
// who would rather not gamble with their HP.      //
// Medic's special ability is occasionally healing //
// in the heat of battle.                          //
// his starting HP is 25, and can be raised        //
// to a maximum of 55 HP with health items         //
//                                                 //
//                                                 //
//                                                 //
+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+
// Press Enter to continue >>
''')
        pressenter = input()
        print( '''
       Select your character!         
+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=
//                                            //
//             3) Assassian:                  //
// Stats: (HP: 15, STR: 3, ARM: 0, EV:3)      //
// Assassian is as the stats and name imply   //
// he has relativley good STR, but is         //
// severely lacking in HP. Despite these      //
// shortcommigs, he has two special           //
// abilites: 1) Assassian's evasion is        // 
// unmatchable, with the highest potential    //
// EV score of up to 40%. 2) 'Devilish Plunge'//
// occasionaly increases damage by 50% while  //
// attacking. Assassian's starting HP         //
// is 15, and his maximum HP is 35            //
//                                            //
//                                            //
+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=
// Press Enter to continue >>
''')

    pressenter = input()
    
    def Backstory(self, pc):
        
        pressenter = ''
        string = ''
        
        if isinstance(pc, chara.Hero):
            string = "a war Hero who has saved and ended many."
        if isinstance (pc, chara.Medic):
            string = "A noble Medic who's life's work was saving."
        if isinstance (pc, chara.Assassian):
            string = "A ruthless Assassian with no remorse for his foes."
        print(f'''
+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=
The village of of Bullingham has been under seige 
by mysterious forces for the past several days.
The once quiet settlement far from King Hargrave's 
kingdom, and his army, though still in his jurisdiction,
has been torn apart by goblins and giant mutants. Such 
creatures were only believed to be legends, that is
until they came to attack. A carrier pigeon alerted 
King Hargrave to the dire circumstances taking place
in Bullingham, alas, Hargrave's kingdom has been 
under threat by a foregin foe for many years. He 
makes an executive decision to pull the best soldier
his ranks to allieviate some of the tension in the region,
{string} 
Will you be able to stop the mosters from reigning their
terror on the settlers? Can you find out who's behind
this? 
+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=''')
        pressenter = input("press enter to continue >>")
        
    def begin(self):
        print(f'''
+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=
You arrive in the village of Bullingham after a arduous
and long cart ride. The townspeople are primarily barricaded
within their homes. There are only two establishments left
open in Bullingham, a bar, and a general store.
+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=
// What would you like to do?''')
        
    def choice_0(self):
        print( '''
+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=
1. Go to the Tavern
2. Go to the General Store
+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=''')
    
    
    def General_Store(self):
        print('''
+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=
You walk into the general store unsure of what to expect.
Being used to military armaments, you are joyful to see
such a fine yet odd selection of goods; that is until
your remember you spent your last gold coin on the way 
over to Bullingham. The clerk greets you funnily and asks
of you not to take your business elsewhere before laughing
to himself.
+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=
// Press enter to continue

''')
        pressenter = input()
        
        
    def Tavern (self, pc):
        print('''
+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=
You walk into the Tavern unsure of what to expect. Your
immediate worries are put to rest as the atmosphere is
far more calm, though somber. You ask around the tavern
to find some sort of clue that would bring you closer to 
finding out what's been going on in Bullingham. You can
surmise from your small and reluctanct conversations 
with the townsfolk that the fiends started showing up
sporadically from the deep woods south west of the 
village about a week and a half ago. The onslaught has
been so severe that most of the townsfolk simply avoid 
going outside save for the bussiest hours. A young lad  
is encouraged and thankful for your pressence, and so,
he rewards you with 6 gold to aid in your journey. You
walk out of the Tavern and into the courtyard.
+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=
//Press Enter to continue
''')
        pc.bank += 6
        pressenter = input()
        
    def Bullingham(self):
        print('''
+=+=+=+=+=+=+=+=+=+=+=+=+=+
1. Go to the General Store
2. Go to the Deep Woods
=+=+=+=+=+=+=+=+=+=+=+=+=+=''')
        
    def Deep_Woods_0(self):
        print('''
+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=
You walk out of the village down a narrow and infrequently
traveled path. The foliage surrounding your feet and the 
trees sheilding your body from the sunrays become thicker,
larger, more intimidating with every step. You feel woefully
unprepared with your worn down dagger and lack of supply. 
+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=
// Press enter to continue
''')
        
        pressenter = input()
        
        print('''
+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=
You continue down the path as the light of day begins to 
cease. Just as your nerves begin settle you hear a nefarious
and disgusting snarl that sharply morphs into a symphony of 
many
+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=
// Press enter to continue
''')
        pressenter = input()
        
        print('''
+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=
Just as was told to you by the townspeople, you are suddenly
attacked by a band of goblins!
+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=
// Press enter to continue
''')
        pressenter = input()
        
    def Deep_Woods_1(self):
        print('''
+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=
You triumph over the goblins, yet you feel your wounds ache
greatly. Your lack of armor and a good weapon may be your 
end if the threats become more severe, yet your proceed anyway.
+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=
// Press enter to continue
''')
        pressenter = input()
        print('''
+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=
As you march through the woods you notice a clearing with what
appears to be a long since abandoned horse cart about 30 meters
west.
+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=
//What would you like to do?

+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=
1. Aprroach the abandoned cart
2. Keep on down the trail
+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=''')
            
    def abandoned_cart(self):
        print('''
+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=
You try your best to be calm and quiet as you traverse through 
the thick brush and un-paved ground. Despite your best
efforts to remain undetected, you notice as you approach the
cart a person lying on the ground in a pool of filth next to
it. You ask them if they are alright; the being springs up and
shrieks louder than you've heard a person scream before! He
lunges at you forthrightly!
+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=
// Press enter to continue''')
        
        pressenter = input()
    
    def abandoned_cart_win(self):
        print('''
+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=
You leave the cave dwelling goul fallen where he stood. 
After your victory, you look to see if there is anything 
that may be useful left behind in the cart.
+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=
// Press enter to continue''')
        pressenter = input()
            

        