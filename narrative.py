import chara
class Text:
    
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
    
    def OpeningTxt(self, pc):
        
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
kingdom,and his army, though still in it's jurisdictin,
has torn apart by goblins and giant mutants. Such 
creatures were only believed to be legends, that is
until they came to attack. A carrier pigeon alerted 
King Hargrave to the dire circumstances taking place
in Bullingham, alas, Hargrave's kingdom has been 
under threat by a foregin foe for many years. He 
makes an executive decision to pull the best from
amongst his ranks,
{string} 
Will you be able to stop the mosters from reigning their
terror on the settlers? Can you find out who's behind
this? 
+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=''')
        pressenter = input("press enter to continue >>")
        
    def begin(self):
        print(f'''
+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=
You arrive in the village of Bullingham after a arduous
and long cart ride. The townspeople are primarily barricaded
within their homes, there are only two establishments left
open in Bullingham, a bar, and a general store.
+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=
// What would you like to do?''')