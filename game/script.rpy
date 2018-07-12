﻿# Вы можете расположить сценарий своей игры в этом файле.

# Определение персонажей игры.
define u = Character('Юля', color="#ff0000")

# Вместо использования оператора image можете просто
# складывать все ваши файлы изображений в папку images.
# Например, сцену bg room можно вызвать файлом "bg room.png",
# а eileen happy — "eileen happy.webp", и тогда они появятся в игре.

#Изображения заставок
image preface =  "img/scr/preface.jpg"
image un_day =  "img/scr/un_day.jpg"

#Изображения фонов
image nf =  "img/scn/night_forest.jpg"
image nfc =  "img/scn/night_forest_clouds.jpg"

#Добавление звукового канала
$ renpy.music.register_channel(u"bgs", "sfx", loop=True)


# Игра начинается здесь:
label start:

    stop music fadeout 3


    scene black with Dissolve(1)
    scene preface with Dissolve(5.0)
    $ renpy.pause (5.0, hard=True)
    scene black with Dissolve(1)

    scene black with Dissolve(3)
    scene un_day with Dissolve(5.0)
    $ renpy.pause (5.0, hard=True)
    scene black with Dissolve(3)

    play music "snd/mus/night_forest.mp3" fadein 3

    scene nf with Dissolve(5.0)

    "Ночь, опустившаяся на Совёнок, окутала сосны и домики сизой дымкой, наполняя пространство некой густотой, означающей скорое приближение лета."

    "Время подходило, и я не могла не думать о том, что вскоре, должно было произойти то, чего я жду."

    "Луна пробивалась сквозь листву, освещая всё вокруг своим призрачно-голубым светом."

    u "“Так давно это было…”"

    u "“Они не появлялись уже очень долгое время.{w} Но, с недавних пор, они начали возвращаться.”"

    "Я сидела в логове, на толще сосновых иголок, обняв колени, и думала о своём."

    "В лесу было тихо."

    u "“Два лета подряд, они приезжают сюда, спустя долгие годы.”"

    u "“Пионеры, как они себя называют.”"

    u "“Я помню, как много лет назад, из Совёнка уезжала последняя смена этих ребят. С тех пор, они не появлялись.”"

    "Всё это время я ждала их, и была здесь почти в одиночестве."

    "Я скучала по ним, меня тянуло к ним, не знаю, почему."

    "И вот, спустя годы, неожиданно, они снова начали приезжать."

    "Это были уже не те весёлые, заводные ребятишки, которые приезжали тогда."

    "Они были намного взрослее, и вели себя странно - поклонялись каким-то фигуркам девочек с большими глазами, иногда ходили шаткой походкой в обнимку друг с другом, и шумели по ночам, будя лесных жителей."

    "Всё же, они были такими же добрыми, открытыми и радостными, как те ребята, что приезжали тогда, поэтому я не могла не встретиться с ними."

    u "“Больше всего, я хочу разобраться с тем непонятным чувством, которое меня тянет к ним.”"

    "Два года подряд я наблюдала за ними, пытаясь понять, что они делают, и почему снова начали приезжать."

    u "“Я не знаю, когда точно они прибудут в этом году, поэтому мне надо быть начеку.”"

    u "“В первый раз, они приехали зимой, и их было совсем немного.{w} Тогда я не смогла проследить за ними…”"
    "Той зимой, что-то внутри меня вздрогнуло, когда я увидела, что они несут фигурки девочек, в той самой форме, что была на пионерах много лет назад."

    "Тогда я не стала приближалаться, так как опасалась, потому что не знала, кто они."

    u "“Но, тем же летом, пионеров приехало намного больше.”"

    u "“Они шумели и веселились, играли в разные игры и разожгли костёр – всё то же самое, что делали ребята тех лет.”"

    u "“В тот раз, с ними были какие-то странные девочки с разноцветными причёсками, похожие на тех, что были на их фигурах...”"

    u "“И самое удивительное то, что одна из них очень похожа на меня!”"

    "Ещё одну зиму и лето, я наблюдала за ними, но не понимала, зачем они приносят эти фигурки, и почему среди них есть моя."

    u "“Я очень волнуюсь, и хочу разгадать эту тайну.{w} Сколько бы ни думала об этом - ни на шаг не приблизилась к тому, что на самом деле кроется за этими пионерами, и почему они так странно себя ведут.”"

    "Моё волнение усиливается тем, что этой зимой их не было в Совёнке."

    scene nfc with dissolve

    "Луну начали медленно затягивать облака."

    u "“Пора спать, а то могу пропустить их приезд!”"

    "С этой мыслью я улеглась, и укрывшись листьями папоротника и украденным одеялом, сладко уснула."

    scene black with Dissolve(3.0)

    return
