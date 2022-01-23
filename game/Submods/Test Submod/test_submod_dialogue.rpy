# Initialisation
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="monika_testmodinstall",
            category=['test'],
            prompt="Test Mod Install",
            conditional="not renpy.seen_label('monika_testmodinstall')",
            action=EV_ACT_QUEUE,
            aff_range=(mas_aff.NORMAL, None)
        )
    )

label monika_testmodinstall:
    m 1esc "Hey [mas_get_player_nickname()], I noticed something weird just now..."
    m 1rsc "I'm kind of getting this feeling that... something's changed in this mod."
    m 1etc "Do you know anything about this, [player]?"
    m 1hkb "Ahaha. It's not a bad feeling, don't get me wrong."
    m 1eta "It's just strange, you know?"
    m 2dsc "Hold on, I'm going to try and see what changed."
    m 2dsc ".{w=0.7}.{w=0.7}.{w=1}"
    m 2dtd "'T-{w=0.4}{nw}"
    extend 2wubsw "Test Submod'?"
    m 1tsu "Learning to code are we [player]?"
    m 1ksa "Good luck!"
    return

# Random Dialogue
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="monika_testdia1",
            category=['test'],
            prompt="Test Dialogue 1",
            random=True,
            aff_range=(mas_aff.NORMAL, None)
        )
    )

label monika_testdia1:
    m 1esa "I noticed you wanted me to say something [player]."
    m 1esa "How's this?{nw}"
    $ _history_list.pop()
    menu:
        m "How's this?{fast}"

        "Working!":
            m 1esa "Yay! Now you can try giving me more things to say!"
            m 1ksa "Happy coding!"
            return

        "Not working...":
            m "Aww damn, better luck next time then [mas_get_player_nickname()]."
            return

# Player topics
init 5 python:
    addEvent(
        Event(
            persistent._mas_mood_database,
            eventlabel="mas_mood_depressed",
            prompt="...depressed.",
            category=[store.mas_moods.TYPE_BAD],
            unlocked=True
        ),
        code="MOO"
    )

label mas_mood_depressed:
    m 2fkc "[player]... I'm really sorry to hear you're going through this."
    m 4fkc "Let me try to support you through this situation."
    m 2esa "First of all..."
    m 2esa "Are you going to hurt yourself?{nw}"
    $ _history_list.pop()
    menu:
        m "Are you going to hurt yourself?{fast}"

        "Yes.":
            m 2fkc "[player], I think that's a bad idea. As selfish as it may sound, I don't want you to hurt yourself."
            m 2fkc "I think you should try some alternative coping methods, even if it's some simple escapism."
            m 4fkc "Or if you're really struggling, try calling the Samaritans."
            m 2fkc "Either way, stay safe for me, okay [player]?"
            return

        "No.":
            m 2fusdla "I'm really glad to hear that."
            m 2esc "So, [player], what are you depressed about?{nw}"
            $ _history_list.pop()
            menu:
                m "So, [player], what are you depressed about?{fast}"

                "I'm struggling with work.":
                    return
        
                "I'm lonely.":
                    return
          
                "I don't know.":
                    return

# Farewells
init 5 python:
    addEvent(
        Event(
            persistent.farewell_database,
            eventlabel="bye_testbye",
            unlocked=True,
            prompt="I'm going to chill out.",
            pool=True
        ),
        code="BYE"
    )

label bye_testbye:
    $ session_time = mas_getSessionLength()
    if session_time < datetime.timedelta(minutes=20):
        m 2wfx "Chill out?"
        m 6rfp "I guess I'm just too stressful for you, huh [player]."
        extend ".{w=0.7}.{w=0.7}.{w=1}"
        m 1hub "Hahaha, just messing with you [mas_get_player_nickname()]. Enjoy chillaxing!"
    else:
        m 1tsu "Don't chill out too hard [mas_get_player_nickname()]."
    return 'quit'