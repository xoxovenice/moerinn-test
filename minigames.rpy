label flashcards:
    menu:
        "Cat":
            m "Yes! That's right!"
            m "Great job!"
        "Dog":
            $ Moerinn_Anger += 0.5
            m "... Okay. What."
            m "Do you need glasses too?"
            m "That's wrong. But I guess you're still disoriented from the dru-"
            m "The meal I gave you."
            m "It's a cat."
        "I don't know":
            pov "I have no idea."
            m "... Me too bro, me too."
    "She paused, putting the card down on the floor next to her thighs."
    m "Next one!"
    menu:
        "Rabbit":
            m "Mhm! mhm! Yes!"
            m "Do you remember what I told you back then?"
            m "Yesterday?"
            menu:
                "Yes":
                    $ Moerinn_heart += 3
                    pov "You like rabbits."
                    m "You remember!"
                    if Moerinn_Anger >= 50:
                        m "This is why I still keep you even if you're mean!"
                        m "You DO listen!"
                        m "It makes me so happy!"
                        "Obviously."
                    else:
                        m "You're seriously the best!"
                "No":
                    pov "Not... Really."
                    m "Oh..."
                    m "It's alright! No worries!"
                    m "I have short memory too!"
                "Shut up" if Moerinn_Anger >= 50:
                        pov "Shut the fuck uuuupppp."
                        $ Moerinn_Anger = 100
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
                                $ health -= 30
                                m "YOU LOWLIFE NUISIANCE!"
                                with vpunch
                                $ health -= 10
                                m "DID YOUR MOTHER EVER TEACH YOU ANY MANNERS?"
                                with vpunch
                                $ health -= 10
                                m "Wait... Did you even have one?"
                                m "Ugh, Whatever."
                                m "DID ANYONE IN YOUR LIFE EVER TEACH YOU MANNERS?"
                                with vpunch
                                $ health -= 10
                                m "OR WERE YOU JUST BORN A LOUSY SCUM?"
                                with vpunch
                                $ health -= 10
                                with vpunch
                                $ health -= 10
                                with vpunch
                                $ health -= 10
                                "Eventually, I felt too tired to keep up with her."
                                "My eyes were already drooping down."
                                with vpunch
                                $ health -= 10
                                m "{size=*0.5}Sorry... I... Didn't mean to..."
                                scene black
                                with dissolve
                                return
                            
                "I don't know":
                    $ Moerinn_Anger += 1
                    m "You... Don't know?" # add the if later on
                    m "S... Seriously?"
                    m "Whatever, I guess."