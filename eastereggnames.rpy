label namesblunt:
    if povname in ["Moerinn"]:
        m "Oh my gosh!"
        m "We have the same name!"
        $ Moerinn_Met = True
        $ moerinn_name = "Moerinn"
        $ Moerinn_heart += 3
    elif povname in ["Venice"]:
        m "Venice?"
        m "VENICE???"
        m "{b}VENICE????"
        m "You're joking!"
        m "That's a place, that's not a person."
        m "Anyway."
    elif povname in ["Venice Vixen Solace"]:
        m "You-"
        m "You're joking."
        m "That's like... So specific."
        m "Either you're the creator..."
        m "She told you about this..."
        m "Or you went SNOOPING in the game files."
        m "Nosey lil guy."
        m "Anyway."
    elif povname in ["Anima"]:
        m "Oh!"
        m "Hey, I have a friend named that!"
        $ Moerinn_heart += 5
        m "She's really sweet!"
        m "I'm sure you are too!"
        m "She draws too, I really like her artworks!"
    elif povname in ["Evan"]:
        m "Heeeeyyyy."
        m "You said you wouldn't be here!"
        "She let out a soft giggle."
        m "Hah! Just kidding."
        m "I don't mind!"
        $ Moerinn_heart += 5
        pov "... Huh?"
        m "Nevermind that!"
    elif povname in ["Fishbone", "Adam"]:
        m "Oh! It's you!"
        m "We haven't met in a while!"
        m "You didn't tell me you'd be here!"
        $ Moerinn_heart += 5
        pov "Huh? What're you talking about?"
        m "... Nevermind!"
    elif povname in ["Ellie"]:
        m "Did your name used to be Star too?"
        m "Maybe even Ceito?"
        m "Or NoobMaster?"
        pov "What are you talking about?"
        m "Haha, guess you're not who I'm talking about."
        m "I do miss them though,"
        m "They're one of my bestest friends!"
        $ Moerinn_heart += 5
    elif povname in ["Tempest", "Contessa"]:
        m "Heeeeyyyyy giiiiiiiiiiirl!"
        m "I haven't seen your pretty face in a while!"
        $ Moerinn_heart += 5
        pov "Hah?"
        m "Nevermind! Sorry!"
    elif povname in ["Lester", "Lester The Molester"]:
        m "HOLY SHIT!"
        m "MY HOMIE!"
        $ Moerinn_heart += 5
        m "ONE OF MY AWESOMEST FRIENDS EVER"
        pov "What"
        m "Sorry, wrong person!"
    elif povname in ["Airl"]:
        $ Moerinn_heart += 5
        m "You know that there's no guys that'll appear in this game, right?"
        pov "Wha"
        m "Yeah. I'm the only character aside from you."
        m "I'll be honest, I still didn't expect you to come here."
        pov "What the hell are you talking about?"
        m "Nevermid it."
        "What the hell?"
        $ sanity -= 10
    elif povname in ["Valerie"]:
        m "Oh hey!"
        m "Oh my gosh!"
        m "We rarely talk but you're such a sweetheart still! Love you!"
        $ Moerinn_heart += 5
        pov "wait what"
    elif povname in ["Espoir"]:
        m "It means \"hope\" in french, right?"
        "She paused and let out a soft chuckle."
        $ Moerinn_heart += 5
        m "You're not recording, are you?"
        m "I mean there's chances you ARE."
        m "Or I could be very wrong and you're just some rando..."
        pov "Probably the latter."
        m "Haha, yeah. Anyway."
    elif povname in ["Kirari"]:
        m "Ooooooh?"
        m "Is that you, pretty girl?"
        $ Moerinn_heart += 5
        pov "What?"
        m "Nothing!"
    elif povname in ["Sen"]:
        $ Moerinn_heart += 5
        m "Chloroform?"
        pov "What"
        m "... Shortstack?"
        pov "What the hell are you talking about"
    else:
        m "Awww! Cute name! I like it!"
    jump after_menu2

label namesmeek:
    if povname in ["Moerinn"]:
        m "Oh my gosh!"
        m "We have the same name!"
        m "You're much meeker than I am though."
        $ Moerinn_Met = True
        $ moerinn_name = "Moerinn"
        $ Moerinn_heart += 3
    elif povname in ["Venice"]:
        m "You know you're not fooling anyone by acting meek, Creator."
    elif povname in ["Venice Vixen Solace"]:
        m "You're acting real shy, Venice."
        m "I'd feel bad if it wasn't for the fact you gave me all these ISSUES!"
    elif povname in ["Anima"]:
        m "Oh!"
        m "Hey, I have a friend named that!"
        $ Moerinn_heart += 5
        m "She's really sweet!"
        m "You're more shy than she is though."
    elif povname in ["Evan"]:
        m "Heeeeyyyy."
        m "You said you wouldn't be here!"
        "She let out a soft giggle."
        m "You're acting real strange though."
        m "You're not usually this timid!"
        $ Moerinn_heart += 5
        pov "... Huh?"
        m "Nevermind that!"
    elif povname in ["Fishbone", "Adam"]:
        m "Oh! It's you!"
        m "We haven't met in a while!"
        m "You didn't tell me you'd be here!"
        m "You're real quiet though!"
        $ Moerinn_heart += 5
        pov "Huh? What're you talking about?"
        m "... Nevermind!"
    elif povname in ["Ellie"]:
        m "Did your name used to be Star too?"
        m "Maybe even Ceito?"
        m "Or NoobMaster?"
        pov "What are you talking about?"
        m "Haha, guess you're not who I'm talking about."
        m "I do miss them though,"
        m "They're one of my bestest friends!"
        m "They're quiet but you're much more quiet."
        $ Moerinn_heart += 5
    elif povname in ["Tempest", "Contessa"]:
        m "Heeeeyyyyy giiiiiiiiiiirl!"
        m "I haven't seen your pretty face in a while!"
        m "Why so blue though? I though you'd be more enthusiastic!"
        $ Moerinn_heart += 5
        pov "Hah?"
        m "Nevermind! Sorry!"
    elif povname in ["Lester", "Lester The Molester"]:
        m "HOLY SHIT!"
        m "MY HOMIE!"
        $ Moerinn_heart += 5
        m "ONE OF MY AWESOMEST FRIENDS EVER"
        pov "What"
        m "Sorry, wrong person!"
        m "I did kinda expect more confidence from a name like that."
    elif povname in ["Airl"]:
        $ Moerinn_heart += 5
        m "... You're acting real meek, tramp."
        m "You good?"
        pov "What the hell are you talking about?"
        m "Nevermind it."
        "What the hell?"
        $ sanity -= 10
    elif povname in ["Valerie"]:
        m "Oh hey!"
        m "Oh my gosh!"
        m "We rarely talk but you're such a sweetheart still! Love you!"
        m "You're so... Shy? I didn't expect that."
        $ Moerinn_heart += 5
        pov "wait what"
    elif povname in ["Espoir"]:
        m "It means \"hope\" in french, right?"
        "She paused and let out a soft chuckle."
        $ Moerinn_heart += 5
        m "... You're much more meek than I expected!"
        m "You're one of my favorite creators though!"
        m "Or maybe you're just a rando I saw..."
        pov "Probably the latter."
        m "Haha, yeah. Anyway."
    elif povname in ["Kirari"]:
        m "Ooooooh?"
        m "Is that you, pretty girl?"
        m "You're so meek though!"
        $ Moerinn_heart += 5
        pov "What?"
        m "Nothing!"
    elif povname in ["Sen"]:
        $ Moerinn_heart += 5
        m "... Are you always this quiet, shortie?"
        pov "What the hell are you talking about"
        m "... Nuthin..."
    else:
        m "Awww! Cute name! I like it!"
        m "Don't be so shy! I don't bite yet!"
    jump after_menu2

label nameshappy:
    if povname in ["Moerinn"]:
        m "Oh my gosh!"
        m "We have the same name!"
        $ Moerinn_Met = True
        $ moerinn_name = "Moerinn"
        $ Moerinn_heart += 4
    elif povname in ["Venice"]:
        m "Venice?"
        m "VENICE???"
        m "{b}VENICE????"
        m "You're joking!"
        m "That's a place, that's not a person."
        m "Anyway."
    elif povname in ["Venice Vixen Solace"]:
        m "You-"
        m "You're joking."
        m "That's like... So specific."
        m "Either you're the creator..."
        m "She told you about this..."
        m "Or you went SNOOPING in the game files."
        m "Nosey lil guy."
        m "Anyway."
    elif povname in ["Anima"]:
        m "Oh!"
        m "Hey, I have a friend named that!"
        $ Moerinn_heart += 5
        m "She's really sweet!"
        m "You are too!"
        m "She draws too, I really like her artworks!"
    elif povname in ["Evan"]:
        m "Oh?"
        m "You're so happy!"
        m "Did you miss me all that much?"
        $ Moerinn_heart += 5
        pov "... Huh?"
        m "Nevermind that!"
    elif povname in ["Fishbone", "Adam"]:
        m "Oh! It's you!"
        m "We haven't met in a while!"
        m "You didn't tell me you'd be here!"
        m "You're as happy as I envisioned you!"
        $ Moerinn_heart += 5
        pov "Huh? What're you talking about?"
        m "... Nevermind!"
    elif povname in ["Ellie"]:
        m "I was honestly about to start listing off old names but you're too happy so I kinda don't wanna troll you anymore."
        pov "... what"
        $ Moerinn_heart += 5
    elif povname in ["Tempest", "Contessa"]:
        m "Heeeeyyyyy giiiiiiiiiiirl!"
        m "I haven't seen your pretty face in a while!"
        m "Still as positive as always, you go girl!"
        $ Moerinn_heart += 5
        pov "Hah?"
        m "Nevermind! Sorry!"
    elif povname in ["Lester", "Lester The Molester"]:
        m "HOLY SHIT!"
        m "MY HOMIE!"
        $ Moerinn_heart += 5
        m "ONE OF MY AWESOMEST FRIENDS EVER"
        m "YOU'RE AS AWESOME AS I ENVISIONED!"
        pov "What"
        m "Sorry, wrong person!"
    elif povname in ["Airl"]:
        $ Moerinn_heart += 5
        m "What're you acting all happy about?"
        m "There's no hot guys here."
        pov "??? wha"
        m "Nevermind it."
        "What the hell?"
        $ sanity -= 10
    elif povname in ["Valerie"]:
        m "Oh hey!"
        m "Oh my gosh!"
        m "We rarely talk but you're such a sweetheart still! Love you!"
        m "You're such a delight!"
        $ Moerinn_heart += 5
        pov "wait what"
    elif povname in ["Espoir"]:
        m "It means \"hope\" in french, right?"
        "She paused and let out a soft chuckle."
        $ Moerinn_heart += 5
        m "You're so fun and positive!"
        m "... Or are you some rando?"
        pov "Probably the latter."
        m "Haha, yeah. Anyway."
    elif povname in ["Kirari"]:
        m "Ooooooh?"
        m "Is that you, pretty girl?"
        m "I rarely see you, you're so fun though..."
        m "You got any gossip?"
        $ Moerinn_heart += 5
        pov "What?"
        m "Nothing!"
    elif povname in ["Sen"]:
        $ Moerinn_heart += 5
        m "HEYYY!"
        m "I'm surprised your parents let you out."
        pov "???"
        m "... Sorry, wrong person."
    else:
        m "Ooooh?"
        m "I love the enthusiasm!"
    jump after_menu2