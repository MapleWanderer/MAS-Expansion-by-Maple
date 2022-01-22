init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="monika_testmodinstall",
            category=['sex'],
            prompt="Test Mod Install",
            conditional="not renpy.seen_label('monika_testmodinstall')",
            action=EV_ACT_QUEUE,
            aff_range=(mas_aff.NORMAL, None)
        )
    )

label monika_:
    m 1esc "Hey [mas_get_player_nickname()], I noticed something weird just now..."
    m 1rsc "I'm kind of getting this feeling that... something's changed in this mod."
    m 1etc "Do you know anything about this, [player]?"
    m 1hkb "Ahaha. It's not a bad feeling, don't get me wrong."
    m 1eta "It's just strange, you know?"
    m 2dsc "Hold on, I'm going to try and see what changed."
    m 2dsc ".{w=0.7}.{w=0.7}.{w=1}"
    m 2dtd "'N-{w=0.4}{nw}"
    extend 2wubsw "Test Submod'?"
    m 1tsu "Learning to code are we [player]?"
    m 1ksa "Good luck!"
    return