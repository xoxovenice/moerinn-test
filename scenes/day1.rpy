label day1_start:
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
                "Check the drawers" if checkdrawers == False:
                    $ checkdrawers = True
                    $ Moerinn_check += 1
                    "I opened the drawers gently as I could. Though, it still made some noise."
                    "I tried looking for anything useful."
                    "Something that can help me leave."
                        label menu_2:
                        if Moerinn_check >= 5:
                            m "Oh! You're awake already!" with vpunch
                            "I didn't even hear her footsteps!"
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
                        jump menu_2
                    else:
                        "I didn't find anything here."
                "Check the floors" if checkfloors == False:
                    $ checkfloors = True
                    $ Moerinn_check += 1
                    "I tried looking at floors for anything."
                    "Maybe someone dropped something there?"
                    if Moerinn_check >= 5:
                        jump menu_2
                    else:
                        "I didn't find anything here."
                        jump menu_1
                "Check curtains" if checkcurtains == False:
                    $ checkcurtains = True
                    $ Moerinn_check += 1
                    "I walked up to the curtains, lifting them up slightly."
                    if Moerinn_check >= 5:
                        jump menu_2
                    else:
                        "It's cemented."
                        "It has a drawing of a sky and sun on it."
                        jump menu_1