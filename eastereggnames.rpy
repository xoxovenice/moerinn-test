label namesblunt:
    if povname == "Moerinn" or "moerinn":
        m "Oh my gosh!"
        m "We have the same name!"
        $ Moerinn_Met = True
        $ moerinn_name = "Moerinn"
        $ Moerinn_heart += 3
    if povname == "Anima" or "anima" or "Nicole" or "nicole":
        m "Oh!"
        m "Hey, I have a friend named that!"
        $ Moerinn_heart += 5
        m "She's really sweet!"
        m "I'm sure you are too!"
        m "She draws too, I really like her artworks!"
    if povname == "Evan" or "evan":
        m "Heeeeyyyy."
        m "You said you wouldn't be here!"
        "She let out a soft giggle."
        m "Hah! Just kidding."
        m "I don't mind!"
        $ Moerinn_heart += 5
        pov "... Huh?"
        m "Nevermind that!"
    if povname == "Fishbone" or "fishbone" or "Adam" or "adam":
        m "Oh! It's you!"
        m "We haven't met in a while!"
        m "You didn't tell me you'd be here!"
        $ Moerinn_heart += 5
        pov "Huh? What're you talking about?"
        m "... Nevermind!"
    if povname == "Ellie" or "ellie":
        m "Did your name used to be Star too?"
        m "Maybe even Ceito?"
        m "Or NoobMaster?"
        pov "What are you talking about?"
        m "Haha, guess you're not who I'm talking about."
        m "I do miss them though,"
        m "They're one of my bestest friends!"
        $ Moerinn_heart += 5
    if povname == "Tempest" or "tempest" or "Contessa" or "contessa":
        m "Heeeeyyyyy giiiiiiiiiiirl!"
        m "I haven't seen your pretty face in a while!"
        $ Moerinn_heart += 5
        pov "Hah?"
        m "Nevermind! Sorry!"
    if povname == "Lester" or "lester":
        m "HOLY SHIT!"
        m "MY HOMIE!"
        $ Moerinn_heart += 5
        m "ONE OF MY AWESOMEST FRIENDS EVER"
        pov "What"
        m "Sorry, wrong person!"
    if povname == "Airl" or "airl":
        $ Moerinn_heart += 5
        m "You know that there's no guys that'll appear in this game, right?"
        pov "Wha"
        m "Yeah. I'm the only character aside from you."
        m "I'll be honest, I still didn't expect you to come here."
        pov "What the hell are you talking about?"
        m "Nevermid it."
        "What the hell?"
        $ sanity -= 10
    if povname == "Valerie" or "valerie":
        m "Oh hey!"
        m "Oh my gosh!"
        m "We rarely talk but you're such a sweetheart still! Love you!"
        $ Moerinn_heart += 5
        pov "wait what"
    if povname == "Espoir" or "espoir":
        m "It means \"hope\" in french, right?"
        "She paused and let out a soft chuckle."
        $ Moerinn_heart += 5
        m "You're not recording, are you?"
        m "I mean there's chances you ARE."
        m "Since no one really gets this link aside from maybe people I know or people I want to play it."
label namesmeek:

label nameshappy: