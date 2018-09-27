## Галерея #####################################################################
init python:
    gallery = Gallery()
    gallery.locked_button = "images/gui/gallery/not_opened_idle.png"
    gallery.idle_border = "images/gui/gallery/thumbnail_idle.png"
    gallery.hover_border = "images/gui/gallery/thumbnail_hover.png"

    gallery.button("nightForest")
    gallery.unlock_image("bg night_forest")

    gallery.button("nightForestClouds")
    gallery.unlock_image("bg night_forest_clouds")

    gallery.transition = fade

screen gallery:
    tag menu

    add "#000"

    grid 1 3:
        xfill True
        yfill True

        add gallery.make_button(
            "nightForest",
            "images/bg/thumb_night_forest.jpg",
            xalign=0.5, yalign=0.5
        )
        add gallery.make_button("nightForestClouds", "images/bg/thumb_night_forest_clouds.jpg", xalign=0.5, yalign=0.5)
        textbutton "Return" action Return() xalign 0.5 yalign 0.5
