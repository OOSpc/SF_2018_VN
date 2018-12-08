################################################################################
## Инициализация
################################################################################

init offset = -1

## Экран главного меню #########################################################
##
## Используется, чтобы показать главное меню после запуска игры.
##
## https://www.renpy.org/doc/html/screen_special.html#main-menu

screen main_menu():

    ## Этот тег гарантирует, что любой другой экран с тем же тегом будет
    ## заменять этот.
    tag menu

    style_prefix "main_menu"

    add gui.main_menu_day_background

    $ snd_button_hover = "sound/gui/hvr.mp3"
    $ snd_button_activate = "sound/gui/clk.mp3"

    $ mm_day_btns_prefix = "gui/main_menu/main_menu_day_"
    imagebutton:
        auto mm_day_btns_prefix + "gallery_%s.png"
        xpos 0 ypos 0
        focus_mask True
        action ShowMenu("gallery")
        hover_sound snd_button_hover
        activate_sound snd_button_activate

    imagebutton:
        auto mm_day_btns_prefix + "load_%s.png"
        xpos 0 ypos 0
        focus_mask True
        action ShowMenu("load")
        hover_sound snd_button_hover
        activate_sound snd_button_activate

    imagebutton:
        auto mm_day_btns_prefix + "preferences_%s.png"
        xpos 0 ypos 0
        focus_mask True
        action ShowMenu("preferences")
        hover_sound snd_button_hover
        activate_sound snd_button_activate

    imagebutton:
        auto mm_day_btns_prefix + "start_%s.png"
        xpos 0 ypos 0
        focus_mask True
        action Start()
        hover_sound snd_button_hover
        activate_sound snd_button_activate

    imagebutton:
        auto mm_day_btns_prefix + "about_%s.png"
        xpos 0 ypos 0
        focus_mask True
        action ShowMenu("about")
        hover_sound snd_button_hover
        activate_sound snd_button_activate

    imagebutton:
        auto mm_day_btns_prefix + "music_room_%s.png"
        xpos 0 ypos 0
        focus_mask True
        action ShowMenu("music_room")
        hover_sound snd_button_hover
        activate_sound snd_button_activate

    imagebutton:
        auto mm_day_btns_prefix + "quit_%s.png"
        xpos 0 ypos 0
        focus_mask True
        action Quit(confirm=False)
        hover_sound snd_button_hover
        activate_sound snd_button_activate

    imagebutton:
        auto mm_day_btns_prefix + "link_%s.png"
        xpos 0 ypos 0
        focus_mask True
        action OpenURL("https://vk.com/sovyonok_party")
        hovered Notify("Сообщество \"Совёнок-феста\"")
        hover_sound snd_button_hover
        activate_sound snd_button_activate

    if gui.show_name:

        vbox:
            text "[config.name!t]":
                style "main_menu_title"

            text "[config.version]":
                style "main_menu_version"


# style main_menu_frame is empty
# style main_menu_vbox is vbox
style main_menu_text is gui_text
style main_menu_title is main_menu_text
style main_menu_version is main_menu_text

style main_menu_frame:
    xsize 420
    yfill True

    background "gui/overlay/main_menu.png"

style main_menu_vbox:
    xalign 1.0
    xoffset -30
    xmaximum 1200
    yalign 1.0
    yoffset -30

style main_menu_text:
    properties gui.text_properties("main_menu", accent=True)

style main_menu_title:
    properties gui.text_properties("title")

style main_menu_version:
    properties gui.text_properties("version")
