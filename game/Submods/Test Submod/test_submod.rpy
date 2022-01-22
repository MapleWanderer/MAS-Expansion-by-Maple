init -990 python in mas_submod_utils:
    mwt_submod = Submod(
        author="MapleWanderer",
        name="Test Submod",
        description="A submod for playing around with MAS.",
        version="0.0.1",
        version_updates={},
        settings_pane="mwt_submod_screen"
    )

init -989 python in mwt_utils:
    import store

    #Register the updater if needed
    if store.mas_submod_utils.isSubmodInstalled("Submod Updater Plugin"):
        store.sup_utils.SubmodUpdater(
            submod=store.mas_submod_utils.ahc_submod,
            user_name="MapleWanderer",
            repository_name="MAS-Submod-Test",
            tag_formatter=lambda x: x[x.index('_') + 1:],
            update_dir="",
            attachment_id=None,
        )

screen mwt_submod_screen():
    $ submods_screen_tt = store.renpy.get_screen("submods", "screens").scope["tooltip"]
    vbox:
        box_wrap False
        xfill True
        xmaximum 1000
        
        hbox:
            style_prefix "check"
            box_wrap False

            if _tooltip:
                textbutton _("NSFW dud setting #1"):
                    action NullAction()
                    hovered SetField(_tooltip, "value", "This is an NSFW submod button which is inactive")
                    unhovered SetField(_tooltip, "value", _tooltip.default())

            else:
                textbutton _("NSFW dud setting #1"):
                    action NullAction()