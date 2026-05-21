label flashcards:
    menu:
        "Cat":
            $ player.corrans += 1
            m "Yes! That's right!"
            m "Great job!"
        "Dog":
            $ moerinn.anger += 0.5
            m "... Okay. What."
            m "Do you need glasses too?"
            m "That's wrong. But I guess you're still disoriented from the dru-"
            m "The meal I gave you."
            m "It's a cat."
        "Skunk":
            m "... What?"
            m "No."
        "I don't know":
            $ player.idk += 1
            pov "I have no idea."
            m "... Me too bro, me too."
    "She paused, putting the card down on the floor next to her thighs."
    m "Next one!"
    menu:
        "Fox":
            m "N-no-???"
            m "Huh..???"
            m "Wha-"
            m "How is that even remotely close???"
        "I don't know":
            if player.idk >= 1:
                $ player.idk += 1
                m "You... Don't know?"
                m "S...{b}{i}STILL???"
                m "Whatever, I guess."
            else:
                $ player.idk += 1
                $ moerinn.anger += 0.5
                m "..."
                m "Dawg"
        "Rabbit":
            $ player.corrans += 1
            m "Mhm! mhm! Yes!"
            m "Do you remember what I told you back then?"
            m "Yesterday?"
            menu:
                "Yes":
                    $ moerinn.heart += 3
                    pov "You like rabbits."
                    m "You remember!"
                    if moerinn.anger >= 50:
                        m "This is why I still keep you even if you're mean!"
                        m "You DO listen!"
                        m "It makes me so happy!"
                        "Obviously."
                    else:
                        m "You're seriously the best!"
                "(Lie) Yes":
                    $ player.lie_meter += 1
                    if player.lie_meter >= 4:
                        m "..."
                        m "Damn" # I CANNOT BE A REAL WRITER STOP IT
                        m "You're a liar."
                        m "You lie."
                    else:
                        $ player.lie_meter += 1
                        m "That makes me so happy!"
                        m "I like when people pay attention to my nonsensical words!"
                "No":
                    pov "Not... Really."
                    m "Oh..."
                    m "It's alright! No worries!"
                    m "I have short memory too!"
                "Shut up" if moerinn.anger >= 50:
                        pov "Shut the fuck uuuupppp."
                        $ moerinn.anger = 100
                        "She stopped smiling and stared at me."
                        "Before standing up and grabbing the potted plant."
                        m "You've got some nerve."
                        "She turned around and threw the plant at me."
                        show screen countdown(timer_jump="menu1_hit", time=1)
                        menu:
                            "DODGE":
                                m "Oh my Go-"
                                "She screeched at the sound of the hardened clay shattering against the wall."
                                m "{i}ADOBO KA BA!?"
                                m "{i}PALAGING MAY TOYO KA!"
                                "Before I knew it, she lunged at me, aiming at my chest."
                                "My back hit against the wall."
                                $ player.health -= 30
                                m "YOU LOWLIFE NUISIANCE!"
                                with vpunch
                                $ player.health -= 10
                                m "DID YOUR MOTHER EVER TEACH YOU ANY MANNERS?"
                                with vpunch
                                $ player.health -= 10
                                m "Wait... Did you even have one?"
                                m "Ugh, Whatever."
                                m "DID ANYONE IN YOUR LIFE EVER TEACH YOU MANNERS?"
                                with vpunch
                                $ player.health -= 10
                                m "OR WERE YOU JUST BORN A LOUSY SCUM?"
                                with vpunch
                                $ player.health -= 10
                                with vpunch
                                $ player.health -= 10
                                with vpunch
                                $ player.health -= 10
                                "Eventually, I felt too tired to keep up with her."
                                "My eyes were already drooping down."
                                with vpunch
                                $ player.health -= 10
                                m "{size=*0.5}Sorry... I... Didn't mean to..."
                                scene black
                                with dissolve
                                return
                        "The vase hit me on the head!" with vpunch
                        $ player.health -= 45
                        "She's crazier than I thought!"
                        "She lunged at me, fist connecting to my face with loud-"
                        "{size=*2}{b}CRACK" with vpunch
                        $ player.health -10
                        m "You're such a jerk!"
                        "She hit me again. Harder." with vpunch
                        $ player.health -= 15
                        m "I tried to be nice! EVEN IF I WAS ALSO BEING A JERK SOMETIMES!"
                        m "I tried to treat you nice even though you pissed me off!"
                        $ player.health -= 15
                        with vpunch
                        $ player.health -= 13
                        with vpunch
                        "I felt her punches getting weaker."
                        $ player.health -= 10
                        with vpunch
                        $ player.health -= 7
                        with vpunch
                        $ player.health -= 4
                        with vpunch
                        m "You're-"
                        "I felt her collapse onto my chest. The fabric of my clothing soaking up her tears."
                        m "I really wanted to befriend you..."
                        "A hic and sob left her throat before she finally sighed and went quiet."
                        m "... I guess I chose wrong."
                        "She grabbed a sharp fragment from the shattered pot."
                        $ player.health -= 20
                        "And slashed through my throat."
                        scene black with fade
                        return
        "Cat":
            if player.corrans >= 1:
                m "That's the answer earlier. You don't have to repeat it."
            else:
                m "That answer's a bit belated, don't you think?"
    m "Next carrrrrrdddd..."
    menu:
        "Bear":
            m "Wrong."
            m "Sorry. I was too blunt."
            m "Still wrong though."
        "Wolf":
            m "... Close, kinda."
            m "Still wrong."
        "Lion":
            $ player.corrans += 1
            m "Mhm! That's right! The king of the jungle!"
            m "You're doing pretty well!"
            m "I think."
        "I don't know":
            if player.idk >= 2:
                $ player.idk += 1
                m "Do you liiiiiiike..."
                m "Not know anything?"
                m "At all?"
                "Maybe I don't."
            else:
                $ player.idk += 1
                " "
                m "Ok."
    m "Did you know all the options you had for the last thing were all predators of nature?"
    m "You probably noticed maybe."
    pov "Huh?"
    m "Last card!"
    menu:
        "Pig":
            m "No... That's your dad."
            "The hell?"
        "Beaver":
            m "Nooooo... Wrong."
        "Raccoon":
            $ player.corrans += 1
            m "Yes! That's right!"
            pov "Hey wait, that raccoon looks familiar-"
        "I don't know":
            if player.idk >= 3:
                $ player.idk += 1
                m "..."
            else:
                $ player.idk += 1
                m "ok"
    m "Okaaaaaaaay!"
    m "So..."
    m "You got-"
    m "I didn't tell you it was graded, it is."
    "I'm back in school again, dammit."
    if player.idk >= 4:
        $ moerinn.anger += 10
        m "You have to be an NPC, actually."
        m "Or a badly made ai."
        m "Do we gotta start studying together??"
    elif player.corrans >= 4:
        $ moerinn.heart += 10
        m "You're so smart! Good job!"
        m "You got em all right!"
    elif player.corrans >= 3 and player.idk == 1:
        $ moerinn.heart += 5
        m "You didn't know only one which is okay!"
        m "You still did well!"
    elif player.corrans >= 3:
        $ moerinn.heart += 6
        m "Close enough, you only got one wrong!"
        m "Still a good job!"
    elif player.corrans >= 2 and player.idk == 2:
        $ moerinn.heart += 3
        m "... That's okay, you tried."
        m "You didn't know half though."
    elif player.corrans >= 2:
        $ moerinn.heart += 4
        m "Oh."
        m "Only half, jeez..."
        m "It's okay!"
        m "Half is still good!"
        m "You tried! Hopefully!"
    elif player.corrans >= 1 and player.idk == 3:
        m "How did you mess up this bad?"
        m "This is like primary level."
    elif player.corrans <= 1:
        $ moerinn.heart += 1
        m "Ohh..."
        m "Yikes..."
        m "Let's uhmm... Do better next time."
    else:
        m "..."
        m "I don't wanna read this out loud, this is sad."
    jump after_game