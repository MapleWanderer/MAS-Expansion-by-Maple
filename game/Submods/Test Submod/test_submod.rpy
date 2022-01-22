init -990 python in mas_submod_utils:
    mwt_submod = Submod(
        author="MapleWanderer",
        name="Test Submod",
        description="A submod for playing around with MAS.",
        version="0.0.1",
        version_updates={},
        settings_pane=None
    )

init -989 python in mwt_utils:
    import store

    #Register the updater if needed
    if store.mas_submod_utils.isSubmodInstalled("Submod Updater Plugin"):
        store.sup_utils.SubmodUpdater(
            submod=store.mas_submod_utils.mwt_submod,
            user_name="MapleWanderer",
            repository_name="MAS-Submod-Test",
            tag_formatter=lambda x: x[x.index('_') + 1:],
            update_dir="",
            attachment_id=None,
        )

screen mwt_submod_screen():
    python:
        submods_screen = store.renpy.get_screen("submods", "screens")

        if submods_screen:
            _tooltip = submods_screen.scope.get("tooltip", None)
        else:
            _tooltip = None
    
    vbox:
        box_wrap False
        xfill True
        xmaximum 1000
        
        hbox:
            style_prefix "check"
            box_wrap False

            if _tooltip:
                textbutton _("My dud setting #1"):
                    action NullAction()
                    hovered SetField(_tooltip, "value", "This is my submod button which is inactive")
                    unhovered SetField(_tooltip, "value", _tooltip.default())

            else:
                textbutton _("My dud setting #1"):
                    action NullAction()