label day1_start:
    scene black
    with dissolve
    if Moerinn_Anger >= 7:
        $ passagg = True
    "My head hurts."
    if Moerinn_Anger >= 7:
        "It felt more than migraine."
        "I hope I don't have a brain injury or anything."
    "I looked at my surroundings."
    "This isn't my place."
    "The room seemed like it was supposed to be cleaned up, but there were boxes lying around."
    "And some older looking posters was also plastered on the walls."
    "It looked like someone had moved out of this room maybe months ago, or that this room used to be someone else's."
    "The wall looks unclean. And the \"cleaner\" area has silhouttes of what I assume to be stickers and maybe polaroids."
    "I realized that I was able to get out and walk around."
    "But I'm not sure where I am exactly, and if I should."
    menu:
        "Get up and look around":
            if povquiet >= 3:
                $ Moerinn_check += 0
                "I quietly took a step frontwards, sighing in relief."
                "I didn't make any noise. That's good."
            else:
                $ Moerinn_check += 4
                "The house's silence was broken by the creak of the floor as I took a step forward."
                "There didn't seem to be any movement nearby."
            label menu_1:
                menu:
                    "Check the drawers" if checkdrawers == False:
                        $ checkdrawers = True
                        $ Moerinn_check += 1
                        "I opened the drawers gently as I could. Though, it still made some noise."
                        "I tried looking for anything useful."
                        "Something that can help me leave."
                        if Moerinn_check >= 5 and scenefinish == False:
                                $ caught = True
                                jump menu_2
                        elif butterfly == True:
                            "There's nohing worth checking here anymore."
                        else:
                            "There's a butterfly knife here."
                        label bfk:
                                menu:
                                    "Take it":
                                        $ butterfly = True
                                        "This might come in handy."
                                        jump menu_1
                                    "Leave it":
                                        jump menu_1
                    "Check the boxes" if checkboxes == False:
                        $ checkboxes = True
                        $ Moerinn_check += 1
                        "Some boxes weren't taped properly."
                        "I opened them up."
                        "These are filled with so many toys..."
                        if Moerinn_check >= 5 and scenefinish == False:
                            $ caught = True
                            jump menu_2
                        else:
                            "I didn't find anything here."
                            jump menu_1
                    "Check the potted plant" if checkplant == False:
                        $ checkplant = True
                        $ Moerinn_check += 1
                        "There was only one potted plant."
                        "I walked up to it, getting on my knees and inspecting."
                        "It seems regular enough... I guess no one would really hide anything here."
                        if Moerinn_check >= 5 and scenefinish == False:
                            $ caught = True
                            jump menu_2
                        else:
                            "I didn't find anything here."
                            jump menu_1
                    "Check the floors" if checkfloors == False:
                        $ checkfloors = True
                        $ Moerinn_check += 1
                        "I tried looking at floors for anything."
                        "Maybe someone dropped something there?"
                        if Moerinn_check >= 5 and scenefinish == False:
                            $ caught = true
                            jump menu_2
                        else:
                            "I didn't find anything here."
                            jump menu_1
                    "Check curtains" if checkcurtains == False:
                        $ checkcurtains = True
                        $ Moerinn_check += 1
                        "I walked up to the curtains, lifting them up slightly."
                        if Moerinn_check >= 5 and scenefinish == False:
                            $ caught = True
                            jump menu_2
                        else:
                            "It's cemented."
                            "It has a drawing of a sky and sun on it."
                            jump menu_1
                if checkboxes == True, checkcurtains == True, checkfloors == True, checkplant == True, checkdrawers == True:
                    jump scenefood
        "Wait":
            if passagg == True:
                $ caught = False
            jump menu_2
        "Scream":
            pov "HELLO!?"
            pov "SOMEBODY!?"
            if povmeek >= 3 or povquiet >= 3:
                $ povloud += 1
                pov "Help..."
            else:
                pov "HELP!!!"
            $ yellingdiag = True
            $ caught = True
            jump menu_2

label menu_2:
    $ scenefinish = True
    if Moerinn_Anger >= 7 and caught == True and yellingdiag:
        $ Moerinn_Anger += 15
        m "You have some nerve yelling at MY house after pissing me off yesterday."
    elif Moerinn_Anger >= 7 and caught == False:
        m "I honestly thought you'd run your mouth off like a dog again."
        m "But you didn't! Color me impressed. My standards for you were pretty low though."
        $ Moerinn_heart += 5
    if povmeek >= 3 or povquiet >= 3 and povloud >= 1:
        m "I didn't expect you to be able to yell, you've been so quiet!"
    elif Moerinn_Anger <= 7:
        m "Oh! You're awake already!"
    "I didn't even hear her footsteps!" with vpunch
    if Moerinn_Anger >= 7:
        m "So... Did you sleep well, jerk?"
    else:
        m "So... Did you sleep well?"
    m "I chose that bed for you specifically."
    menu:
        "Yeah":
            $ povblunt += 1
            pov "Yeah. It was pretty nice."
            $ Moerinn_heart += 5
            m "That's great to hear!"
            m "I DID get you a pretty nice bed."
        "No.":
            $ povblunt += 1
            pov "No, I didn't."
            if Moerinn_Anger >= 7:
                $ Moerinn_Anger += 3
                m "Well, captives can't necessarily be picky, can they?"
                m "Besides, it's quite fitting for you."
            else:
                m "Really? But it's such a nice bed!"
                m "Any animal would love it! It's so soft!"
            "I looked at where my bed was."
            "There laid a dog bed."
        "K-Kinda...":
            $ povmeek += 1
            pov "Yeah... A little...?"
            if Moerinn_Anger >= 10:
                $ Moerinn_Anger -= 5
                m "Better be grateful then."
            m "Are you responding or are you questioning?"
            m "Whatever it is,"
            $ Moerinn_heart += 5
            m "Your tone makes the answer all the much cuter!"
        "Maybe":
            "I shrugged."
            pov "I don't know, you tell me."
            if Moerinn_Anger >= 7:
                "She raised an eyebrow before bursting into a fit of laughter."
                m "HAHAHA—!!!"
                m "Oh man, that caught me off guard."
                m "I'm not even mad at you anymore, jerk."
                $ Moerinn_anger = 0
                $ Moerinn_tease = True
            m "You're not sure?"
            "She giggled slightly at my answer."
            $ Moerinn_heart += 5
            m "Hah! You're funny."
            m "I'll take that as a yes though, I'm not buying a new bed for you."
            m "Unless you're good!"
    if caught == True:
        m "So..."
        if Moerinn_Anger >= 10:
            m "Not only are you rude, you're also nosey."
            m "You really should work for the police,"
            m "Having more nosey bitches would really help them!"
        elif Moerinn_Anger >= 25 and yellingdiag == True:
            m "Will you ever stop barking like a dog?"
        else:
            m "Mind telling me why you were snooping around?"
            menu:
                "I was curious":
                    $ Moerinn_heart += 15
                    m "Oh."
                    m "Atleast you're honest!"
                    m "Can you see if any of my stuff got lost in there?"
                    m "Especially my butterfly knife."
                    m "I think I lost it."
                    m "Anyway."
                "Get me out of here!":
                    if Moerinn_Anger >= 25:
                        $ Moerinn_Anger += 15
                    else:
                        $ Moerinn_Anger += 10
                    m "... I don't wanna."
                    m "Not yet."
                    m "Or ever."
                    m "You might tell the police."
                    m "You're acting so mean..."
                "(lie) Looking for you...?":
                    $ lie_meter += 1
                    m "Oh?"
                    if lie_meter >= 2:
                        $ Moerinn_Anger += 15
                        m "You're telling the truth this time, right?"
                    else:
                        $ Moerinn_heart += 5
                        m "How sweet!"
                        m "You could've yelled for me, though."
                        m "I might've heard."
                        pov "Might've?"
                        m "I have bad hearing sometimes... And usually zoned out."
                        m "My friends have told me about it before."
                        m "Anywho, anyshoe!"
                "...":
                    m "..."
                    if povquiet >= 3:
                        $ povquiet += 1
                        m "You know..."
                        m "There's people who always have so everything to say,"
                        m "And there's you, who never has anything to say."
                        if Moerinn_Anger >= 10:
                            $ Moerinn_Anger += 10
                    else:
                        m "Guess you're still processing."
            jump menu_3
    else:
        m "I really hope you don't mind me keeping you captive."
        label menu_3:
            m "You hungry?"
            m "I can cook something up for you."
            if Moerinn_Anger >= 10:
                m "Even if you piss me off."
            if friendreply == True:
                m "Also, your friend never came."
                "What is she talking about?"
                m "Like... Yesterday?"
                m "You either lied or they cancelled on you. Or something!"
                m "Whatever it is, I checked. I waited a few hours."
                pov "How would you even know which one was my friend?"
                m "I know a bit about you, that's all I can say."
                m "So...?"
                m "Do you wanna eat?"
            menu:
                "Yes":
                    m "Oh, great!"
                    m "Cool."
                    if Moerinn_Anger >= 25 and Moerinn_heart >= -10:
                        m "You know how people say \"The best way to someone's heart is their stomach\"?"
                        m "MAYBE you'll be in mine if your stomach is full!"
                        m "... That made no sense. Nevermind."
                        m "I hate you, that's YOUR fault I can't speak."
                        $ Moerinn_heart -= 10
                    elif Moerinn_Anger >= 25:
                        m "You won't mind getting fed dog food, do you?"
                        m "Just... You know. Thought of treating you the way you're acting."
                        $ Moerinn_sadism += 5
                    else:
                        m "I'll get you something, be good!"
                    "She left before I could say anything else..."
                    $ checkfloors = False
                    $ checkplant = False
                    $ checkboxes = False
                    $ checkcurtains = False
                    $ checkdrawers = False
                    jump menu_1
                "No":
                    $ Moerinn_Anger += 5
                    m "Okay!"
                    m "I'll be back really quick though."
                    "She left before I could say anything else..."
                    jump menu_1

label scenefood:
    if donteat == False:
        "I heard the sound of something dropping, then breaking."
        "Similar to a vase falling off a table."
        m "{size=*0.5}Fu- Fiddlesticks-!"
        "This time, I heard footsteps as she went up the stairs."
        m "I'm back!"
        "She walked up to me and placed a dog bowl on the floor."
        m "... I don't completely trust you yet, sorry."
        m "Actually, it's because I broke the bowl I was gonna give you and this is the closest I have."
        if povquiet <= 3:
            pov "You don't have another bowl?"
            m "No, I do. I just have a specific bowl for you."
            m "There's a bowl if you're good and there's a bowl if you're bad."
            if Moerinn_Anger <= 15:
                m "I'll buy a different bowl for you tommorrow."
        m "... You're not vegan or anything, right?"
        m "Because if you are then you probably won't like that meal."
        "It looks like-"
        m "It's porksteak!"
        m "I uhm.... I got the recipe from my mom."
        m "I really like how she cooked it back then."
        "She then started giggling softly once more."
        m "\"Back then\"? What am I? 53?"
        m "Anyway... She makes it real well."
        m "It's fairly simple but I like that about it."
        menu:
            "Do you ever shut up?" if povrude >= 3:
                $ donteat = True
                pov "Do you ever shut the fuck up?"
                m "..."
                m "Oh."
                m "Well, screw you too, then!"
                "She let out a choked laugh before kicking the dog bowl."
                $ Moerinn_sadism += 3
                m "Waste of food."
                m "I'll feed you again tommorrow, you don't deserve dinner or even snacks."
                jump donteatfood
            "...":
                m "Awww, it's ok. You don't have to speak!"
                m "Just eat and tell me how you feel, okaaaay?"
                $ drugged += 1
                "So I just started eating."
            "Eat the food":
                $ drugged += 1
                "She smiled as I started eating."
                "Atleast she gave me utensils to eat with."
        
    label scenefood1:
        "As I ate, I felt her just..."
        "Stare."
        "She didn't say anything, just smiled at me."
        "It was unsettling, especially with her weirdo bug-eyes barely blinking."
        m "Do you like it?"
        menu:
            "Yes":
                pov "Yeah."
                m "Really!?"
                $ Moerinn_heart += 10
                "She coughed for a moment."
                m "I mean, really?"
                menu:
                    "Yeah":
                        $ drugged += 1
                        pov "Yeah."
                        m "I'm so glad!"
                    "no":
                        $ lie_meter += 1
                        pov "No."
                        m "..."
                        if lie_meter >= 3:
                            m "I'm just curious..."
                            m "Do you ever go one day without lying?"
                        else:
                            m "Don't lie to me next time."
            "No...":
                $ drugged += 1
                if Moerinn_Anger >= 35:
                    $ Moerinn_Anger += 25
                    m "Well, keep eating because I'm not cooking another meal for you."
                    m "So ungrateful. I went out of my way to cook for you even if you've been rude."
                else:
                    m "That bad...?"
                    m "I should've practiced beforehand..."
                    if povquiet <= 3:
                        pov "Wait, you didn't practice beforehand?"
                        m "Yeah, it's my first time cooking that."
                        m "I should've added more lemon or something..."
            "...":
                $ drugged += 1
                m "I'll take that as a yes."
                m "Good job me, doing so good you left 'em speechless."
                "She struggled to pat herself at the back, unable to tell how she should before just smacking her chest."
                m "Take that, grandma!"
            "Don't eat it":
                m "... Why aren't you touching your food anymore?"
                m "Did I do something wrong?"
                m "{size=*0.5}Did they find out I added something in it...?"
                "She took the bowl away and smiled awkwardly."
                jump donteatfood
            "Pretend to eat it":
                m "Oh!"
                $ Moerinn_heart += 10
                m "You liked it that much?"
                "She seemed... Happy by my response."
        "At some point, I had stopped eating, and looked up at her."
        "She's still staring at me!" with vpunch
        m "Oh! Sorry, I'll take that away now."
        "She picked up the bowl and left."
        if drugged >= 2:
            "I felt..."
            "Off."
            "She came back to the room, but instead of fully entering—she just peeked her head out."
            m "{size=*0.9}You alright?"
            "She sounded a bit far."
            m "{size=*0.7}You look woozy."
            "I was."
            if givename == False:
                m "{size=*0.5}I didn't even get your name yet..."
            else:
                m "{size=*0.5}That's a shame, I didn't even get to know you all that well yet."
            "What was she saying..?"
            m "{size=*0.3}Goodnight, [povname]."
        jump night1

label donteatfood:
    if donteat == True:
        "She left me alone."
        # add stuff here laterrrr
    else:
        m "I'll come back later to give you snacks, okay? Just... Try to rest in the mean time."
        "She left quickly after, holding the bowl of unfinished food in her hands."
    label doorthoughts:
        "I've already checked her things, there's nowhere else to—"
        "Wait."
        "She left the door unlocked."
        "Maybe I can go out and—"
        "No, I have to be careful."
        