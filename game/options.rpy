define config.name = _("The Journey of Kisune Caneld")
define gui.show_name = True
define config.version = "1.0"
define gui.about = _("The Journey of Kisune Caneld")
define build.name = "TheJourneyOfKisuneCaneld"
define config.has_sound = True
define config.has_music = True
define config.has_voice = True
define config.main_menu_music = None
define config.enter_transition = dissolve
define config.exit_transition = dissolve
define config.intra_transition = dissolve
define config.after_load_transition = None
define config.end_game_transition = None
define config.window = "auto"
define config.window_show_transition = Dissolve(.2)
define config.window_hide_transition = Dissolve(.2)
default preferences.text_cps = 50
default preferences.afm_time = 15
define config.save_directory = "TheJourneyOfKisuneCaneld-1728740000"
define config.window_icon = ""

init python:
    build.classify('**~', None)
    build.classify('**.bak', None)
    build.classify('**/.**', None)
    build.classify('**/#**', None)
    build.classify('**/thumbs.db', None)
    build.classify('game/**.png', 'archive')
    build.classify('game/**.jpg', 'archive')
    build.classify('game/**.ogg', 'archive')
    build.classify('game/**.rpy', None)
    build.classify('game/**.rpyc', 'archive')
    build.documentation('*.html')
    build.documentation('*.txt')
