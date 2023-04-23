import moviepy.editor as medit
import moviepy.video as mvid

input_video_path = 'input.mp4'
clip = medit.VideoFileClip(input_video_path)

input_message = (
    'Введите номер варианта обработки видео:\n'
    '1 - повернуть видео на 180 градусов\n'
    '2 - увеличить скорость воспроизведения видео в двое\n'
    '3 - сделать видео чёрно-белым\n'
    'Ввод: '
)
mode = input(input_message)

match int(mode):
    case 1:
        print('Вы выбрали поворот видео на 180 градусов!')
        clip = clip.rotate(180)
    case 2:
        print('Вы выбрали ускорение видео в два раза!')
        clip = clip.fx(medit.vfx.speedx, 2)
    case 3:
        print('Вы выбрали наложение чёрно-белого фильтра!')
        clip = clip.fx(mvid.fx.all.blackwhite)
    case _:
        raise Exception('Неверый ввод...')

clip.write_videofile('output.mp4')
