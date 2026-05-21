label day1_start:
    scene black
    with dissolve
    if moerinn.anger >= 7:
        $ moerinn.passive_aggression = True
    "My head hurts."
    if moerinn.anger >= 7:
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
            if player.pov["quiet"] >= 3:
                $ moerinn.check += 0
                "I quietly took a step frontwards, sighing in relief."
                "I didn't make any noise. That's good."
            else:
                $ moerinn.check += 4
                "The house's silence was broken by the creak of the floor as I took a step forward."
                "There didn't seem to be any movement nearby."
            label menu_1:
                menu:
                    "Check the drawers" if world.check_drawers == False:
                        $ world.check_drawers = True
                        $ moerinn.check += 1
                        "I opened the drawers gently as I could. Though, it still made some noise."
                        "I tried looking for anything useful."
                        "Something that can help me leave."
                        if moerinn.check >= 5 and world.scene_finished == False:
                                $ moerinn.caught = True
                                jump menu_2
                        elif world.butterfly == True:
                            "There's nohing worth checking here anymore."
                        else:
                            "There's a world.butterfly knife here."
                        label bfk:
                                menu:
                                    "Take it":
                                        $ world.butterfly = True
                                        "This might come in handy."
                                        jump menu_1
                                    "Leave it":
                                        jump menu_1
                    "Check the boxes" if world.check_boxes == False:
                        $ world.check_boxes = True
                        $ moerinn.check += 1
                        "Some boxes weren't taped properly."
                        "I opened them up."
                        "These are filled with so many toys..."
                        if moerinn.check >= 5 and world.scene_finished == False:
                            $ moerinn.caught = True
                            jump menu_2
                        else:
                            "I didn't find anything here."
                            jump menu_1
                    "Check the potted plant" if world.check_plant == False:
                        $ world.check_plant = True
                        $ moerinn.check += 1
                        "There was only one potted plant."
                        "I walked up to it, getting on my knees and inspecting."
                        "It seems regular enough... I guess no one would really hide anything here."
                        if moerinn.check >= 5 and world.scene_finished == False:
                            $ moerinn.caught = True
                            jump menu_2
                        else:
                            "I didn't find anything here."
                            jump menu_1
                    "Check the floors" if world.check_floors == False:
                        $ world.check_floors = True
                        $ moerinn.check += 1
                        "I tried looking at floors for anything."
                        "Maybe someone dropped something there?"
                        if moerinn.check >= 5 and world.scene_finished == False:
                            $ moerinn.caught = true
                            jump menu_2
                        else:
                            "I didn't find anything here."
                            jump menu_1
                    "Check curtains" if world.check_curtains == False:
                        $ world.check_curtains = True
                        $ moerinn.check += 1
                        "I walked up to the curtains, lifting them up slightly."
                        if moerinn.check >= 5 and world.scene_finished == False:
                            $ moerinn.caught = True
                            jump menu_2
                        else:
                            "It's cemented."
                            "It has a drawing of a sky and sun on it."
                            jump menu_1
                if world.check_boxes == True, world.check_curtains == True, world.check_floors == True, world.check_plant == True, world.check_drawers == True:
                    jump scenefood
        "Wait":
            if moerinn.passive_aggression == True:
                $ moerinn.caught = False
            jump menu_2
        "Scream":
            pov "HELLO!?"
            pov "SOMEBODY!?"
            if player.pov["meek"] >= 3 or player.pov["quiet"] >= 3:
                $ player.pov["loud"] += 1
                pov "Help..."
            else:
                pov "HELP!!!"
            $ player.yelling_diag = True
            $ moerinn.caught = True
            jump menu_2

label menu_2:
    $ world.scene_finished = True
    if moerinn.anger >= 7 and moerinn.caught == True and player.yelling_diag:
        $ moerinn.anger += 15
        m "You have some nerve yelling at MY house after pissing me off yesterday."
    elif moerinn.anger >= 7 and moerinn.caught == False:
        m "I honestly thought you'd run your mouth off like a dog again."
        m "But you didn't! Color me impressed. My standards for you were pretty low though."
        $ moerinn.heart += 5
    if player.pov["meek"] >= 3 or player.pov["quiet"] >= 3 and player.pov["loud"] >= 1:
        m "I didn't expect you to be able to yell, you've been so quiet!"
    elif moerinn.anger <= 7:
        m "Oh! You're awake already!"
    elif moerinn.anger >= 7:
        m "Oh."
    "I didn't even hear her footsteps!" with vpunch
    if moerinn.anger >= 7:
        m "So... Did you sleep well, jerk?"
    else:
        m "So... Did you sleep well?"
    m "I chose that bed for you specifically."
    menu:
        "Yeah":
            $ player.pov["blunt"] += 1
            pov "Yeah. It was pretty nice."
            $ moerinn.heart += 5
            m "That's great to hear!"
            m "I DID get you a pretty nice bed."
        "No.":
            $ player.pov["blunt"] += 1
            pov "No, I didn't."
            if moerinn.anger >= 7:
                $ moerinn.anger += 3
                m "Well, captives can't necessarily be picky, can they?"
                m "Besides, it's quite fitting for you."
            else:
                m "Really? But it's such a nice bed!"
                m "Any animal would love it! It's so soft!"
            "I looked at where my bed was."
            "There laid a dog bed."
        "K-Kinda...":
            $ player.pov["meek"] += 1
            pov "Yeah... A little...?"
            if moerinn.anger >= 10:
                $ moerinn.anger -= 5
                m "Better be grateful then."
            m "Are you responding or are you questioning?"
            m "Whatever it is,"
            $ moerinn.heart += 5
            m "Your tone makes the answer all the much cuter!"
        "Maybe":
            "I shrugged."
            pov "I don't know, you tell me."
            if moerinn.anger >= 7:
                "She raised an eyebrow before bursting into a fit of laughter."
                m "HAHAHA—!!!"
                m "Oh man, that moerinn.caught me off guard."
                m "I'm not even mad at you anymore, jerk."
                $ moerinn.anger = 0
                $ Moerinn_tease = True
            m "You're not sure?"
            "She giggled slightly at my answer."
            $ moerinn.heart += 5
            m "Hah! You're funny."
            m "I'll take that as a yes though, I'm not buying a new bed for you."
            m "Unless you're good!"
    if moerinn.caught == True:
        m "So..."
        if moerinn.anger >= 10:
            m "Not only are you rude, you're also nosey."
            m "You really should work for the police,"
            m "Having more nosey bitches would really help them!"
        elif moerinn.anger >= 25 and player.yelling_diag == True:
            m "Will you ever stop barking like a dog?"
        else:
            m "Mind telling me why you were snooping around?"
            menu:
                "I was curious":
                    $ moerinn.heart += 15
                    m "Oh."
                    m "Atleast you're honest!"
                    m "Can you see if any of my stuff got lost in there?"
                    m "Especially my world.butterfly knife."
                    m "I think I lost it."
                    m "Anyway."
                "Get me out of here!":
                    if moerinn.anger >= 25:
                        $ moerinn.anger += 15
                    else:
                        $ moerinn.anger += 10
                    m "... I don't wanna."
                    m "Not yet."
                    m "Or ever."
                    m "You might tell the police."
                    m "You're acting so mean..."
                "(lie) Looking for you...?":
                    $ player.lie_meter += 1
                    m "Oh?"
                    if player.lie_meter >= 2:
                        $ moerinn.anger += 15
                        m "You're telling the truth this time, right?"
                    else:
                        $ moerinn.heart += 5
                        m "How sweet!"
                        m "You could've yelled for me, though."
                        m "I might've heard."
                        pov "Might've?"
                        m "I have bad hearing sometimes... And usually zoned out."
                        m "My friends have told me about it before."
                        m "Anywho, anyshoe!"
                "...":
                    m "..."
                    if player.pov["quiet"] >= 3:
                        $ player.pov["quiet"] += 1
                        m "You know..."
                        m "There's people who always have so everything to say,"
                        m "And there's you, who never has anything to say."
                        if moerinn.anger >= 10:
                            $ moerinn.anger += 10
                    else:
                        m "Guess you're still processing."
            jump menu_3
    else:
        m "I really hope you don't mind me keeping you captive."
label menu_3:
    m "You hungry?"
    m "I can cook something up for you."
    if moerinn.anger >= 10:
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
            if moerinn.anger >= 25 and moerinn.heart >= -10:
                m "You know how people say \"The best way to someone's heart is their stomach\"?"
                m "MAYBE you'll be in mine if your stomach is full!"
                m "... That made no sense. Nevermind."
                m "I hate you, that's YOUR fault I can't speak."
                $ moerinn.heart -= 10
            elif moerinn.anger >= 25:
                m "You won't mind getting fed dog food, do you?"
                m "Just... You know. Thought of treating you the way you're acting."
                $ moerinn.sadism += 5
            else:
                m "I'll get you something, be good!"
            "She left before I could say anything else..."
            $ world.check_floors = False
            $ world.check_plant = False
            $ world.check_boxes = False
            $ world.check_curtains = False
            $ world.check_drawers = False
            jump menu_1
        "No":
            $ moerinn.anger += 5
            m "Okay!"
            m "I'll be back really quick though."
            "She left before I could say anything else..."
            jump menu_1

label scenefood:
    if world.dont_eat == False:
        "I heard the sound of something dropping, then breaking."
        "Similar to a vase falling off a table."
        m "{size=*0.5}Fu- Fiddlesticks-!"
        "This time, I heard footsteps as she went up the stairs."
        m "I'm back!"
        "She walked up to me and placed a dog bowl on the floor."
        m "... I don't completely trust you yet, sorry."
        m "Actually, it's because I broke the bowl I was gonna give you and this is the closest I have."
        if player.pov["quiet"] <= 3:
            pov "You don't have another bowl?"
            m "No, I do. I just have a specific bowl for you."
            m "There's a bowl if you're good and there's a bowl if you're bad."
            if moerinn.anger <= 15:
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
            "Do you ever shut up?" if player.pov["rude"] >= 3:
                $ world.dont_eat = True
                pov "Do you ever shut the fuck up?"
                m "..."
                m "Oh."
                m "Well, screw you too, then!"
                "She let out a choked laugh before kicking the dog bowl."
                $ moerinn.sadism += 3
                m "Waste of food."
                m "I'll feed you again tommorrow, you don't deserve dinner or even snacks."
                jump donteat
            "...":
                m "Awww, it's ok. You don't have to speak!"
                m "Just eat and tell me how you feel, okaaaay?"
                $ player.drugged += 1
                "So I just started eating."
            "Eat the food":
                $ player.drugged += 1
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
                $ moerinn.heart += 10
                "She coughed for a moment."
                m "I mean, really?"
                menu:
                    "Yeah":
                        $ player.drugged += 1
                        pov "Yeah."
                        m "I'm so glad!"
                    "no":
                        $ player.lie_meter += 1
                        pov "No."
                        m "..."
                        if player.lie_meter >= 3:
                            m "I'm just curious..."
                            m "Do you ever go one day without lying?"
                        else:
                            m "Don't lie to me next time."
            "No...":
                $ player.drugged += 1
                if moerinn.anger >= 35:
                    $ moerinn.anger += 25
                    m "Well, keep eating because I'm not cooking another meal for you."
                    m "So ungrateful. I went out of my way to cook for you even if you've been rude."
                else:
                    m "That bad...?"
                    m "I should've practiced beforehand..."
                    if player.pov["quiet"] <= 3:
                        pov "Wait, you didn't practice beforehand?"
                        m "Yeah, it's my first time cooking that."
                        m "I should've added more lemon or something..."
            "...":
                $ player.drugged += 1
                m "I'll take that as a yes."
                m "Good job me, doing so good you left 'em speechless."
                "She struggled to pat herself at the back, unable to tell how she should before just smacking her chest."
                m "Take that, grandma!"
            "Don't eat it":
                m "... Why aren't you touching your food anymore?"
                m "Did I do something wrong?"
                m "{size=*0.5}Did they find out I added something in it...?"
                "She took the bowl away and smiled awkwardly."
                jump donteat
            "Pretend to eat it":
                m "Oh!"
                $ moerinn.heart += 10
                m "You liked it that much?"
                "She seemed... Happy by my response."
                $ world.pretend_eat = True
                jump donteat
        "At some point, I had stopped eating, and looked up at her."
        "She's still staring at me!" with vpunch
        m "Oh! Sorry, I'll take that away now."
        "She picked up the bowl and left."
        if player.drugged >= 2:
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
            if givename == True:
                m "{size=*0.3}Goodnight, [povname]"
            else:
                m "{size=*0.3}Goodnight."
            "I felt her hand caress my head softly as I black out."
            scene black
            with fade
        jump night1

label donteat:
    if world.dont_eat == True:
        "She left me alone."
        # add stuff here laterrrr
    else:
        m "I'll come back later to give you snacks or something else, okay? Just... Try to rest in the mean time."
        "She left quickly after, holding the bowl of unfinished food in her hands."
    label doorthoughts:
        "I've already checked her things, there's nowhere else to—"
        "Wait."
        "She left the door unlocked."
        "Maybe I can go out and—"
        "No, I have to be careful."
        "She might hear me, the floorboards creak."
        "I heard her going up the stairs again."
        m "Okay, so."
        if world.pretend_eat:
            m "{size=*0.5} The drugs might take a while to take effect.."
            "Was she mumbling something?"
        "She rubbed her wet hands against her shirt."
        m "Be good. Rest or something."
        m "{size=*0.3}Don't do anything funky just because I couldn't drug you."
        m "Wait-"
        m "Actually... Do you wanna play?"
        if moerinn.anger >=50:
            m "I'm just kidding!"
            m "You don't have a choice."
            m "You're playing with me."
        else:
            menu:
                "Play":
                    m "Great! Cool!"
                    m "Uhm..." 
                    m "We're gonna play..."
                "Refuse":
                    m "Oh..."
                    m "I kinda..."
                    m "Wanted to play."
        "She paused for a moment, finally refusing my gaze."
        "Her eye contact was so..."
        "Overwhelming."
        "She looked around again."
        "Then walked up to the boxes at the end of the room."
        m "... Hmmm... What to play... What to plaaay....?"
        m "Oh!"
        "She stood up and walked in front of me, her smile wider than her usual."
        m "It's not really a game but it's an old thing I have because.."
        "She yawned." # I actually yawned before this
        m "Because my little brother used to use them..."
        m "Well, my grandmother and little brother."
        m "She used to teach him, he was... Different. So she tried to school him instead."
        m "It worked for a while but then he got a phone."
        "She stood up and turned around, blank faced as she walked up to me."
        m "Anyway."
        m "Let's play this!"
        "She beamed as she held out the the \"game\"."
        "It was a bunch of flashcards. The kind for toddlers."
        m "It'll be our first player.bonding time with eachother!"
        $ player.bonding += 1
        m "You'll be the one answering, okay?"
        m "This is easy so you'll probably know anyway! You're smarter than me, right?"
        "She sat down in front of me and held the first card out."
        jump flashcards

label after_game:
    m "Anyway! That was fun!"
    m "I'm gonna go leave you alone now, bye bye!"
    "Once again, she rushed out the door before I could say anything."
    "I let out a deep exhale, I didn't even know I was holding my breath in until it had left my lungs."
    pov "It's not like I can look around the room again..."
    pov "I mean I could but it'd be a waste."
    pov "I can't use the window, and she's probably nearby."
    "I didn't even know who I was talking to there."
    "Myself?"
    "Had I lost my mind on just the first day?"
    $ player.sanity -= 5
    "It's fine... Doesn't matter."
    "I should rest. I'm exhausted."
    "Her energy is exhausting."
    "{b}She's{/b} exhausting."
    scene black
    with fade
    jump night1