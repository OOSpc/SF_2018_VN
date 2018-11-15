init python:
    import os
    from PIL import Image, ImageFilter

    def get_temp_dir():
        tempdir = config.gamedir + "/temp/"
        if(os.path.isdir(tempdir) == False):
            os.mkdir(tempdir)

        return tempdir

    def save_screenshot(filename):
        filename = get_temp_dir() + filename
        renpy.screenshot(filename)

        return filename

    def blur_image(filename):
        im = Image.open(filename)
        blurred = im.filter(ImageFilter.GaussianBlur(15))
        filename = get_temp_dir() + "/blurred.jpg"
        blurred.save(filename)

        return filename
