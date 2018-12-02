## Галерея #####################################################################
init python:
    gallery = Gallery()
    gallery.locked_button = "images/gui/gallery/not_opened_idle.png"
    gallery.idle_border = "images/gui/gallery/thumbnail_idle.png"
    gallery.hover_border = "images/gui/gallery/thumbnail_hover.png"

    gallery_mode = GALLERY_MODE_BG         # init gallery mode: bg or cg
    thumbnail_width = 320
    thumbnail_height = 180

    rows = 3
    cols = 4
    cells = rows * cols
    current_page = 0            # init page

    gallery_bg = [
        "night_forest",
        "night_forest_clouds"
    ]

    gallery_cg = []

    for bg in gallery_bg:
        gallery.button(bg)
        gallery.unlock_image("bg " + bg)

    for cg in gallery_cg:
        gallery.button(cg)
        gallery.unlock_image("cg " + cg)

    gallery.transition = fade

screen gallery:
    tag menu

    $ renpy.take_screenshot((1920, 1080))
    # $ renpy.image("scr_bg", im.MatrixColor(FileCurrentScreenshot(), im.matrix.tint(0.8, 0.8, 0.8)))
    add FileCurrentScreenshot()
    add "/gui/shading_70pc.png"

    $ gallery_table = []
    if gallery_mode == GALLERY_MODE_BG:
        $ gallery_table = gallery_bg
    elif gallery_mode == GALLERY_MODE_CG:
        $ gallery_table = gallery_cg

    grid cols rows:
        xfill True
        yfill True

        $ next_page = current_page + 1
        if next_page > int(len(gallery_table)/(cells)):
            $ next_page = 0

        $ i = 0
        for glr_item in gallery_table:
            $ i += 1
            if i > current_page*cells and i <= (current_page + 1)*cells:
                python:
                    if gallery_mode == GALLERY_MODE_CG:
                        thumbnail = im.Scale(
                            im.Crop("images/cg/" + glr_item + ".jpg" , (0,0,1920,1080)),
                            thumbnail_width, thumbnail_height
                        )
                    elif gallery_mode == GALLERY_MODE_BG:
                        thumbnail = im.Scale(
                            im.Crop("images/bg/" + glr_item + ".jpg" , (0,0,1920,1080)),
                            thumbnail_width, thumbnail_height
                        )

                add gallery.make_button(glr_item, thumbnail, xalign=0.5, yalign=0.5)

        for j in range(i, (current_page+1)*cells):
            null

    if current_page != 0:
        imagebutton:
            auto "/gui/dialogue_box/backward_%s.png"
            yalign 0.5 xalign 0.01
            action (SetVariable('current_page', current_page - 1), ShowMenu("gallery"))

    imagebutton:
        auto "/gui/dialogue_box/forward_%s.png"
        yalign 0.5 xalign 0.99
        action (SetVariable('current_page', next_page), ShowMenu("gallery"))

    textbutton "← Назад":
        xalign 0.015 yalign 0.92
        text_size 60
        text_kerning 3
        action Return()
