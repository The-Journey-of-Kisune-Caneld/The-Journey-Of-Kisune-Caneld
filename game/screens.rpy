init offset = -1

screen say(who, what):
    style_prefix "say"

    window:
        id "window"

        if who is not None:
            window:
                id "namebox"
                style "namebox"
                text who id "who"

        text what id "what"

    if not renpy.variant("small"):
        add SideImage() xalign 0.0 yalign 1.0

    use quick_menu

style window is default
style say_label is default
style say_dialogue is default
style say_thought is say_dialogue

style namebox is default
style namebox_label is say_label

style window:
    xalign 0.5
    xfill True
    yalign gui.textbox_yalign
    ysize gui.textbox_height
    background "#18181be6"

style namebox:
    xpos gui.name_xpos
    xanchor gui.name_xalign
    xsize gui.namebox_width
    ypos gui.name_ypos
    ysize gui.namebox_height
    padding (15, 6, 15, 6)
    background "#27272a"

style say_label:
    properties gui.text_properties("name", accent=True)
    bold True

style say_dialogue:
    properties gui.text_properties("dialogue")
    xpos gui.dialogue_xpos
    xsize gui.dialogue_width
    ypos gui.dialogue_ypos

screen choice(items):
    style_prefix "choice"

    vbox:
        for i in items:
            textbutton i.caption action i.action

style choice_vbox is vbox
style choice_button is default
style choice_button_text is default

style choice_vbox:
    xalign 0.5
    ypos 405
    yanchor 0.5
    spacing gui.choice_spacing

style choice_button is default:
    properties gui.button_properties("choice_button")
    background "#27272a"
    hover_background "#3f3f46"
    padding (30, 15, 30, 15)

style choice_button_text is default:
    properties gui.button_text_properties("choice_button")

screen quick_menu():
    zorder 100

    if quick_menu:
        hbox:
            style_prefix "quick"
            xalign 0.5
            yalign 0.99
            spacing 15

            textbutton _("Back") action Rollback()
            textbutton _("History") action ShowMenu('history')
            textbutton _("Skip") action Skip() alternate Skip(fast=True)
            textbutton _("Auto") action Preference("auto-forward", "toggle")
            textbutton _("Save") action ShowMenu('save')
            textbutton _("Q.Save") action QuickSave()
            textbutton _("Q.Load") action QuickLoad()
            textbutton _("Prefs") action ShowMenu('preferences')

default quick_menu = True

style quick_button is default
style quick_button_text is button_text

style quick_button:
    properties gui.button_properties("quick_button")

style quick_button_text:
    properties gui.button_text_properties("quick_button")

screen navigation():
    vbox:
        style_prefix "navigation"
        xpos gui.navigation_xpos
        yalign 0.5
        spacing gui.navigation_spacing

        if main_menu:
            textbutton _("Start") action Start()
        else:
            textbutton _("History") action ShowMenu("history")
            textbutton _("Save") action ShowMenu("save")

        textbutton _("Load") action ShowMenu("load")
        textbutton _("Preferences") action ShowMenu("preferences")

        if main_menu:
            textbutton _("About") action ShowMenu("about")

        if renpy.variant("pc"):
            textbutton _("Help") action ShowMenu("help")

        if not main_menu:
            textbutton _("Main Menu") action MainMenu()

        if renpy.variant("pc"):
            textbutton _("Quit") action Quit(confirm=not main_menu)

style navigation_button is default:
    properties gui.button_properties("navigation_button")

style navigation_button_text is default:
    properties gui.button_text_properties("navigation_button")

screen main_menu():
    tag menu

    add gui.main_menu_background

    frame:
        background None
        xalign 0.5
        yalign 0.2
        text "[config.name]" size gui.title_text_size color gui.accent_color bold True

    use navigation

screen game_menu(title, scroll=None, yinitial=0.0):
    style_prefix "game_menu"

    if main_menu:
        add gui.main_menu_background
    else:
        add gui.game_menu_background

    frame:
        style "game_menu_outer_frame"

        hbox:
            frame:
                style "game_menu_navigation_frame"
                use navigation

            frame:
                style "game_menu_content_frame"

                if scroll == "viewport":
                    viewport:
                        yinitial yinitial
                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True
                        side_yfill True

                        vbox:
                            transclude
                elif scroll == "vpgrid":
                    vpgrid:
                        cols gui.file_slot_cols
                        yinitial yinitial
                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True
                        side_yfill True

                        transclude
                else:
                    transclude

    label title

    if main_menu:
        key "game_menu" action ShowMenu("main_menu")

style game_menu_outer_frame is empty
style game_menu_navigation_frame is empty
style game_menu_content_frame is empty
style game_menu_viewport is viewport
style game_menu_side is side
style game_menu_scrollbar is vscrollbar

style game_menu_label is gui_label
style game_menu_label_text is gui_label_text

style game_menu_outer_frame:
    bottom_padding 45
    top_padding 180
    background None

style game_menu_navigation_frame:
    xsize 420
    yfill True

style game_menu_content_frame:
    left_margin 60
    right_margin 180
    top_margin 15

style game_menu_label:
    xpos 75
    ysize 180

style game_menu_label_text:
    size gui.title_text_size
    color gui.accent_color
    yalign 0.5

screen about():
    tag menu
    use game_menu(_("About"), scroll="viewport"):
        style_prefix "about"
        vbox:
            label "[config.name!t]"
            text _("Version [config.version!t]\n")
            if gui.about:
                text "[gui.about!t]\n"
            text _("Made with {a=https://www.renpy.org/}Ren'Py{/a} [renpy.version_only].\n")

style about_label is gui_label
style about_label_text is gui_label_text
style about_text is gui_text

style about_label_text:
    size gui.label_text_size

screen save():
    tag menu
    use file_slots(_("Save"))

screen load():
    tag menu
    use file_slots(_("Load"))

screen file_slots(title):
    default page_name_value = FilePageNameInputValue()

    use game_menu(title):
        fixed:
            order_reverse True

            button:
                style "page_label"
                key_events True
                xalign 0.5
                action page_name_value.Toggle()
                input:
                    style "page_label_text"
                    value page_name_value

            grid gui.file_slot_cols gui.file_slot_rows:
                style_prefix "slot"
                xalign 0.5
                yalign 0.5
                spacing gui.slot_spacing

                for i in range(gui.file_slot_cols * gui.file_slot_rows):
                    $ slot = i + 1
                    button:
                        action FileAction(slot)
                        has vbox
                        add FileScreenshot(slot) xalign 0.5
                        text FileTime(slot, format=_("{#file_time}%Y-%m-%d %H:%M"), empty=_("empty slot")):
                            style "slot_time_text"
                        text FileSaveName(slot):
                            style "slot_name_text"
                        key "save_delete" action FileDelete(slot)

            hbox:
                style_prefix "page"
                xalign 0.5
                yalign 1.0
                spacing gui.page_spacing
                textbutton _("<") action FilePagePrevious()
                textbutton _("{#auto_page}A") action FilePage("auto")
                textbutton _("{#quick_page}Q") action FilePage("quick")
                for page in range(1, 10):
                    textbutton "[page]" action FilePage(page)
                textbutton _(">") action FilePageNext()

style page_label is gui_label
style page_label_text is gui_label_text
style page_button is gui_button
style page_button_text is gui_button_text

style slot_button is gui_button
style slot_button_text is gui_button_text
style slot_time_text is slot_button_text
style slot_name_text is slot_button_text

style page_label:
    xpadding 75
    ypadding 5

style page_label_text:
    text_align 0.5
    layout "subtitle"
    hover_color gui.hover_color

style slot_button:
    properties gui.button_properties("slot_button")

style slot_button_text:
    properties gui.button_text_properties("slot_button")

screen preferences():
    tag menu
    use game_menu(_("Preferences"), scroll="viewport"):
        vbox:
            hbox:
                box_wrap True
                vbox:
                    style_prefix "check"
                    label _("Display")
                    textbutton _("Window") action Preference("display", "window")
                    textbutton _("Fullscreen") action Preference("display", "fullscreen")
                vbox:
                    style_prefix "check"
                    label _("Skip")
                    textbutton _("Unseen Text") action Preference("skip", "toggle")
                    textbutton _("After Choices") action Preference("after choices", "toggle")
                    textbutton _("Transitions") action InvertSelected(Preference("transitions", "toggle"))
            null height 30
            hbox:
                box_wrap True
                vbox:
                    style_prefix "slider"
                    box_wrap True
                    label _("Text Speed")
                    bar value Preference("text speed")
                    label _("Auto-Forward Time")
                    bar value Preference("auto-forward time")
                vbox:
                    style_prefix "slider"
                    box_wrap True
                    label _("Music Volume")
                    bar value Preference("music volume")
                    label _("Sound Volume")
                    bar value Preference("sound volume")

screen history():
    tag menu
    predict False
    use game_menu(_("History"), scroll="viewport", yinitial=1.0):
        style_prefix "history"
        for h in _history_list:
            window:
                has fixed:
                    yfit True
                if h.who:
                    label h.who:
                        style "history_name"
                        substitute False
                $ what = renpy.filter_text_tags(h.what, allow=gui.history_allow_tags)
                text what:
                    substitute False
        if not _history_list:
            label _("The dialogue history is empty.")

style history_window is empty
style history_name is gui_label
style history_name_text is gui_label_text
style history_text is gui_text

style history_window:
    xfill True
    ysize gui.history_height

style history_name:
    xpos gui.history_name_xpos
    xanchor gui.history_name_xalign
    ypos gui.history_name_ypos
    xsize gui.history_name_width

style history_name_text:
    min_width gui.history_name_width
    text_align gui.history_name_xalign

style history_text:
    xpos gui.history_text_xpos
    ypos gui.history_text_ypos
    xsize gui.history_text_width
    min_width gui.history_text_width
    text_align gui.history_text_xalign
    layout ("subtitle" if gui.history_text_xalign else "tex")

screen help():
    tag menu
    use game_menu(_("Help"), scroll="viewport"):
        style_prefix "help"
        vbox:
            spacing 23
            label _("Keyboard")
            text _("Enter / Space: Advance dialogue and activate the interface.")
            text _("Arrow Keys: Navigate the interface.")
            text _("Escape: Access the game menu.")
            text _("Ctrl: Skips dialogue while held down.")
            text _("Tab: Toggles dialogue skipping.")
            text _("Page Up / Page Down: Roll back and forward.")

screen confirm(message, yes_action, no_action):
    modal True
    zorder 200
    style_prefix "confirm"
    add "#000000cc"
    frame:
        xalign 0.5
        yalign 0.5
        padding (45, 45, 45, 45)
        background "#27272a"
        has vbox:
            xalign 0.5
            spacing 45
        label _(message):
            style "confirm_prompt"
            xalign 0.5
        hbox:
            xalign 0.5
            spacing 150
            textbutton _("Yes") action yes_action
            textbutton _("No") action no_action

style confirm_prompt is gui_prompt
style confirm_prompt_text is gui_prompt_text
style confirm_prompt_text:
    text_align 0.5
    layout "subtitle"

screen skip_indicator():
    zorder 100
    style_prefix "skip"
    frame:
        background "#18181be6"
        xpos 30
        ypos 30
        padding (15, 8, 15, 8)
        text _("Skipping")

screen notify(message):
    zorder 100
    style_prefix "notify"
    frame:
        at notify_appear
        background "#18181be6"
        xpos 30
        ypos 30
        padding (15, 8, 15, 8)
        text "[message!t]"

transform notify_appear:
    on show:
        alpha 0.0
        linear 0.25 alpha 1.0
    on hide:
        linear 0.5 alpha 0.0

screen nvl(dialogue, items=None):
    window:
        style "nvl_window"
        has vbox:
            spacing gui.nvl_spacing
        for d in dialogue:
            window:
                id d.window_id
                fixed:
                    yfit True
                    if d.who is not None:
                        text d.who id d.who_id
                    text d.what id d.what_id
        for i in items:
            textbutton i.caption:
                action i.action
                style "nvl_choice_button"

style nvl_window is default:
    xfill True
    yfill True
    background "#000000cc"
    padding (150, 75, 150, 75)
