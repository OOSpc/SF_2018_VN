## Галерея #####################################################################
init python:
    gallery = Gallery()

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

        add gallery.make_button("nightForest")
