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
                        if Moerinn_check >= 5:
                                $ caught = True
                                jump menu_2
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
                        if Moerinn_check >= 5:
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
                        if Moerinn_check >= 5:
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
                        if Moerinn_check >= 5:
                            $ caught = true
                            jump menu_2
                        else:
                            "I didn't find anything here."
                            jump menu_1
                    "Check curtains" if checkcurtains == False:
                        $ checkcurtains = True
                        $ Moerinn_check += 1
                        "I walked up to the curtains, lifting them up slightly."
                        if Moerinn_check >= 5:
                            $ caught = True
                            jump menu_2
                        else:
                            "It's cemented."
                            "It has a drawing of a sky and sun on it."
                            jump menu_1
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
            $ caught = True
            jump menu_2


label menu_2:
    if Moerinn_Anger >= 7 and caught == True:
        $ Moerinn_Anger += 15
        m "You have some nerve yelling at MY house after pissing me off yesterday."
    elif Moerinn_Anger >= 7 and caught == False:
        m "I honestly thought you'd run your mouth off like a dog again."
        m "Screaming or whatever."
        m "Or acting like a dog like how you were yesteday."
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
                $ Moerinn_anger -= 10
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
        m "Mind telling me why you were snooping around?"
    else:
        m "I really hope you don't mind me keeping you captive..."
        label menu_3:
            m "You hungry?"
