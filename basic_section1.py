import pygame

with open('files/begin.bmp') as file:
    begin_image = pygame.image.load(file)
with open('files/end.bmp') as file:
    end_image = pygame.image.load(file)
with open('files/var.bmp') as file:
    var_image = pygame.image.load(file)
with open('files/input_var.bmp') as file:
    input_var_image = pygame.image.load(file)
with open('files/print_var.bmp') as file:
    print_var_image = pygame.image.load(file)
with open('files/print_next_phrase.bmp') as file:
    print_next_phrase_image = pygame.image.load(file)
with open('files/copy.bmp') as file:
    copy_image = pygame.image.load(file)

name_img = dict(begin=begin_image, end=end_image, var=var_image, copy=copy_image,
                print_var=print_var_image, print_phrase=print_next_phrase_image)


def init():
    # Возвращает список объектов, имеющих координаты для модуля
    result_list = []
    for name, i, coords in zip(name_img.keys(), name_img.values(),
                               [(200, 100), (200, 240), (200, 390), (200, 550), (470, 120), (470, 260), (470, 400)]):
        rect = i.get_rect()
        rect.topleft = coords
        result_list.append((name, rect))
    return result_list


def blit_img(screen, name, cords):
    # Отрисовывает объекты рект (как для модуля, так и для программы)
    screen.blit(name_img[name], cords)



flag_tab = 0

def action(file, name, text1='', text2='', text3='', text4='', flag_first_tab=False):
    global flag_tab
    if flag_first_tab:
        flag_tab = 0
    if name == 'begin':
        flag_tab += 1
    elif name == 'end':
        flag_tab -= 1
    if flag_tab and name not in ['begin', 'end']:
        print(str('\t' * flag_tab), end='', file=file)
    if name == 'print_phrase':
        print(f"print('{text1}', file=file)", file=file)
    elif name == 'var':
        print(f"{text1} = '{text2}'", file=file)
    elif name == 'print_var':
        print(f"print({text1}, file=file)", file=file)
    elif name == 'copy':
        print(f"copy_var = {text2}\n{text1} = copy_var", file=file)


def helping_text(name, i):
    global texts
    return texts[name][i]


texts = {'print_phrase': [['Введите фразу без кавычек:']],
         'var': [['Введите имя создаваемой переменной:',
                  'Рекомендуемая длина имени переменной до 5 символов.',
                  'В имени должна быть хотя бы 1 латинская буква.',
                  'Использование других алфавитов, пробелов, символов: #, $, %, &, !, запрещено'],
                 ['Введите значение переменной без кавычек:', 'по умолчанию  будет иметь строковый тип']],
         'print_var': [['Введите имя существующей переменной,', 'значение которой вы хотите вывести на экран.']],
         'copy': [['Введите имя присваемой переменной:'], ['Введите имя существующей переменной:']]}
