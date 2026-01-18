label start:
 scene black
 with fade
 centered "{color=B50E0E}{size=80}WARNING{/100}\n \nThis game contains topics such as: \nKidnapping \nPhysical Harm \nDeath \nScreenshakes \n and possibly more as I update it. \n \nBy continuing, you agree that you understand these warnings. \nPLEASE click off if any of them are\npossibly triggering for you."

 $ povname = renpy.input ("What is your name?", length=32)
 $ povname = povname.strip()

 "I was walking around the mall."

 "It just so happened to be the day a cosplay convention was scheduled."

 "Crowds of people surrounding my line of sight no matter where I looked."

 "As I sat down to rest for a moment,"
 
 "As I sat down to rest for a moment, a girl sat down next to me."

 "I felt her glance at me, but once I stared back at her-"

 "She had already looked away."

 "Aside from the crowd nearby,"
 
 "It was mostly silent between the two of us sitting there."
 
 "I had assumed she's waiting for a friend until she spoke up suddenly."

 m "There's a lot of people here, haha." 
 
 "She laughed awkwardly, seemingly trying to break the silence. But it felt like it just got worse."

 menu:
        "Be sarcastic":
               $ Moerinn_heart -= 5
               $ Moerinn_Anger += 5
               $ povrude += 1 
               pov "Yeah, really? You think?"
               m "Yeah, there's like 10 people just right ther-"
               m "Oh."
               m "That's not a very nice tone..."
        "Awkwardly reply":
               $ Moerinn_heart += 5
               $ povmeek += 1
               pov "Haha, yeah... There's an event going on."
               m "It's a... Uhm..."
               m "What's the word again...?"
               m "Cosplay convention!"
               "She smiled brightly, excited by the idea of it."
        "Be blunt":
               $ povblunt += 1
               pov "There's an event going on."
               m "... Yeah. It's cosplay convention."
               m "..."
               "She looked back away from me immediately after."
        "...":
               $ povquiet += 1
               m "..."
               "She stopped attempting to talk to me for a few moments."

label after_menu:
    "She fidgeted with her hands quietly before opening her mouth once more."
    m "Are you here for the convention or...?"
    "She paused as if waiting for my answer."
    menu:
        "Yeah, I am.":
            $ cosconreply = True
            m "Really?"
            $ Moerinn_heart += 5
            m "So am I!"
            m "It's just so much fun for me to see my interests liked by so many others!"
            m "You don't mind talking with me, right?"
            m "It's not often I meet new people!"
        "No, I'm not.":
            $ Moerinn_heart += 3
            m "Oh."
            m "That's alright!"
            m "I guess you just got here the wrong time!"
            "She softly smiled as she stared at me."
            m "You don't mind chatting with me, right?"
        "(lie) I'm waiting for a friend.":
         $ lie_meter += 1
         $ friendreply = True
         "She stared at me for a moment."
         m "Oh."
         m "Alright!"
         m "You don't mind chatting while you wait, right?"
         m "It's not often I meet new people!"
        "Why do you even wanna know?":
            $ Moerinn_heart -= 2
            $ Moerinn_Anger += 1
            $ povblunt += 1
            $ wdyewk = True
            m "I was just curious, sorry...?"
            "She looked away and kept fidgeting with her fingers."
        "...":
            $ povquiet += 1
            m "You don't talk much, do you?"

label after_menu1:
    m "... Thinking about it now, it's probably really weird of a stranger to randomly start a conversation..."
    m "I mean, I haven't even asked about your day or your name!"

    if wdyewk == True or povquiet >= 2:
       m "Some stranger I am, haha..."
    else:
       m "Some stranger I am, haha!"
    m "If you want, I'll let you introduce yourself first!"

    menu:
        "You go first.":
            $ Moerinn_heart += 1
            jump after_menu2
        "I'm [povname].":
                $ givename == True
                $ povblunt += 1
                m "Woah! I like your name!"
        "... I'm [povname].":
            $ givename = True
            $ povmeek += 1
            m "Woah! I like your name!"
            $ Moerinn_heart += 3
        "I'm [povname]!":
            $ givename = True
            $ povhappy += 1
            m "Haha!"
            m "Your enthusiasm is infectious!"
            $ Moerinn_heart += 3
            m "I like it!"
            m "I like your name!"
        "...":
            $ povquiet += 1
            $ Moerinn_Anger += 1
            if povquiet >= 3:
             m "Do you really not talk or..?"
            else:
             m "... Oooookay."
             $ dddres = True


label after_menu2:
    if dddres == True:
        m "I'm Moerinn."
    else:
     m "I'm Moerinn!"
    $ Moerinn_Met = True
    $ moerinn_name = "Moerinn"
    m "It's nice to meet you!"
    m "Weeelll... I know you're here in the mall for a reason."

    if cosconreply == True and friendreply == True:
        m "You and your friend are probably planning to shop together for merch..."
    elif cosconreply == True:   
        m "You know... The coscon."
    elif friendreply == True:
        m "Waiting for your friend to maybe hang out or pick you up..."
    else:
        m "I don't know what exactly, but definitely some reason."
    "Oh wow."
    "This girl talks a lot."
    if povquiet >= 3:
        m "Do you even wanna talk?"
    else:
        m "Anyway, what do you wanna talk about?"

label after_menu3:
    menu:
        "..." if povquiet >= 3:
            m "It's like talking to a brick wall."
            m "Are you there or...?"
        "I don't wanna talk, thank you.":
            m "It's alright! I understand."
            m "Not everyone is super into talking."
        "Talk about yourself":
            "I talked to her about myself."
            $ Moerinn_heart += 5
            "Nothing too personal. Surface level things."
            "It'd be weird to tell her something personal anyway, we just met. And I'd probably never see her again."
            "I hope not."
        "Ask about her" if aah == False:
            $ aah = True
            m "You wanna learn about me?"
            $ Moerinn_heart += 3
            m "Aw! You're so sweet!"
            m "Well... I'm flattered, haha!"
            m "I like anime and uhm..."
            m "cute stuff, and music!"
            m "I'm super into drawing and I love rabbits! And stripes!"
            m "You are sure you don't wanna tell me about yourself?"
            jump after_menu3


label after_menu4:
    "She was silent soon after once more, leading to another awkward silence between us."
    "She opened her bag and took out her phone."
    m "Oh. I have to leave now."
    if Moerinn_heart >= 7:
        m "I can give you my socials or something..."
        m "Do you want it?"
        "She held out a small, pink card."
        menu:
            "Take the card":
                $ pinkcard = True
                $ Moerinn_heart += 5
                m "Alright! I'll uhm... Chat you soon?"
                m "Bye!"
            "Refuse":
                m "Oh! Okay! Cool, see you-"
                m "Somewhere, I guess?"
                m "Bye!"
    else:
        m "I'll see you around."

    "And... Just like that..."
    "She disappeared into the crowd."

label after_menu5:
    "I wandered around the mall for a bit more."
    "I haven't been to this mall much before. I don't completely remember the layout."
    if pinkcard == True:
        "My hands went into my pockets as I passed by a trash can."
        "Oh, right."
        "That girl gave me her card thing."
        "Should I throw it away?"
        menu:
            "Throw the card away":
                "I don't really feel like keeping it."
                "Or wanting to talk to her again."
                "I reached into my pocket and threw it into the trash." 
                $ pinkcard = False
            "Keep it":
                "I don't know, maybe I'll chat her."
                "But she's odd."
                "I'll keep it though."
                "Just for fun."
    "As I walked, I felt... Something odd."
    "Like eyes upon me."
    "It'd be hard to spot anyone in this crowd unless they stood out."
    "Should I look around?"
    menu:
        "Look around":
            $ Moerinn_Anger += 5
            "I didn't see anything."
        "Nevermind it":
            $ Moerinn_heart += 2
            "I guess it was nothing."
            "There's too many people here anyway."
    "As I got closer to the main exit of the mall, I noticed the amount of people blocking the way."
    "How is that even possible?"
    "I could just wait it out but... I also remembered another exit."
    "I didn't really see anyone near it earlier too."
    "But it is in an alley."
    menu:
        "Wait it out":
            "It took almost a 30 minutes for the people to clear out."
            "But atleast I could leave now."
            "I'm too tired, I can't wait to get home."
            scene black
            with fade
            centered "{size=150}ENDING: YOU WENT HOME"
        "Go to the other exit":
            "This wasn't worth the wait."
            "I just wanna get home."
            "I turned around and walked to the side of the mall."
            "As I got closer to the exit, the sounds in the mall had already started to fade further and further away."
            "Until it was almost silent once I was in the alley."
            "I didn't even know being in the mall can get this tiring."
            "But as I lowered my guard down, I heard the sounds of something moving in the nearby dumpster."
            "I honestly wanted to check it out but suddenly got worried at the idea of it being a person dumpster diving."
            "Odd fear but..."
            menu:
                "Check the dumpster":
                    "I stepped closer to the it and-"
                    an "{size=*2}{b}WOOO!" with vpunch
                    "What the-!?"
                    an "Oh, hi!"
                    "It was... Talking."
                    "It definitely sounded like a girl. Her voice had a hint of squeakiness to it."
                    menu:
                        "Hello?":
                            pov "Hello?"
                            "She paused for a moment, tilting her head to the side."
                            an "Hi."
                            "Something felt wrong."
                            "Her tone immediately changed. I can't really tell what tone it took but it sounded..."
                            "Mischievous."
                            transform alpha_dissolve:
                                alpha 0.0
                                linear 0.5 alpha 1.0
                                on hide:
                                    linear 0.5 alpha 0

                            screen countdown(timer_jump, time=1):
                                timer time repeat False action [ Hide('countdown'), Jump(timer_jump) ]
                                bar value AnimatedValue(0, time, time, time) at alpha_dissolve

                            label after_menu6:
                                    show screen countdown(timer_jump="menu1_hit", time=1)
                                    menu:
                                        "DODGE":
                                            hide screen countdown
                                            "I moved and turned around."
                                            m "DAMMIT!"
                                            "What the hell!?"
                                            $ sanity -= 2
                                            jump menu1_missed
                            label menu1_hit:
                                with vpunch
                                $ health -= 10
                                "I heard her voice as I was losing consciousness."
                                jump day1_start
                                if Moerinn_Anger >= 7:
                                    $ health -= 5
                                    m "{size=*0.5}You've been pissing me off since earlier. I hope I hit hard enough."
                                else:
                                    m "{size=*0.5}I really hope that doesn't leave a concussion..."
                                jump day1_start
                "Don't check it":
                        "Thinking about it again, I don't really wanna know what's in there."
                        "Why did I feel I was getting watched again?"
                        jump after_menu6

label menu1_missed:
    if Moerinn_Anger >= 7:
        m "HOLD STILL, JERK!"
        m "YOU'VE BEEN PISSING ME OFF SINCE EARLIER!"
        "She was already breathing heavily, her hands gripping a baseball bat."
        $ sanity -= 5
        show screen countdown(timer_jump="menu1_hit", time=0.5)
    else:
        m "Hold still, please."
        "She was already breathing heavily, her hands gripping a baseball bat."
        show screen countdown(timer_jump="menu1_hit", time=1)
    menu:
        "DODGE":
            hide screen countdown
            m "I TOLD YOU TO-"
            "I quickly sped past her, running as fast as I could."
            "My thoughts were all piling up so fast, I could hardly think."
            "All I knew was to run as far away as I could from her."
            "{size=*2.0}{b}BANG!" with vpunch
            if Moerinn_Anger >= 7:
                $ health -= 15
            else:
                $ health -= 10
            jump day1_start
return