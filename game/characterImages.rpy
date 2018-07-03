init -50 python:

    import json
    import renpy.exports

    def register_images(characterImageFile):
        with open(characterImageFile) as data_file:
            data = json.load(data_file)
        image(name, d)
