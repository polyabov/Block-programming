import pygame

with open('files/var_to_int.bmp') as file:
    var_to_int_image = pygame.image.load(file)
with open('files/var_to_float.bmp') as file:
    var_to_float_image = pygame.image.load(file)
with open('files/var_to_str.bmp') as file:
    var_to_str_image = pygame.image.load(file)
with open('files/var_to_list.bmp') as file:
    var_to_list_image = pygame.image.load(file)
with open('files/var_to_set.bmp') as file:
    var_to_set_image = pygame.image.load(file)
with open('files/reversed.bmp') as file:
    reversed_image = pygame.image.load(file)

name_img = dict(var_to_int=var_to_int_image, var_to_float=var_to_float_image, var_to_str=var_to_str_image,
                var_to_list=var_to_list_image, var_to_set=var_to_set_image, reversed=reversed_image)


def init():
    result_list = []
    for name, i, coords in zip(name_img.keys(), name_img.values(),
                               [(200, 100), (200, 260), (200, 420), (470, 100), (470, 260)]):
        rect = i.get_rect()
        rect.topleft = coords
        result_list.append((name, rect))
    return result_list


def blit_img(screen, name, rect):
    screen.blit(name_img[name], rect)


def action(file, name, text1='', text2='', text3='', text4='', flag_first_tab=False):
    from basic_section1 import flag_tab
    if flag_tab:
        print('\t' * flag_tab, end='', file=file)
    if name == 'var_to_int':
        print(f"{text1} = int(float({text1}))", file=file)
    if name == 'var_to_float':
        print(f"{text1} = float({text1}", file=file)
    if name == 'var_to_str':
        print(f"{text1} = str({text1})", file=file)
    if name == 'var_to_list':
        print(f"{text1} = list({text1})", file=file)
    if name == 'var_to_set':
        print(f"{text1} = set({text1})", file=file)
    if name == 'reversed':
        print(f"{text2} = reversed({text1})", file=file)


def helping_text(name, i):
    global texts
    return texts[name][i]


texts = {'var_to_int': [['Введите имя существующей переменной:',
                         '(Значение переменной должно быть числом)',
                         'Если вы хотите ввести десятичную дробь, ',
                         'после целой части используйте точку, а не запятую.']],
         'var_to_float': [['Введите имя существующей переменной:',
                           '(Значение переменной должно быть числом)',
                         'Если вы хотите ввести десятичную дробь, ',
                         'после целой части используйте точку, а не запятую.']],
         'var_to_str': [['Введите имя существующей переменной:']],
         'var_to_list': [['Введите имя существующей переменной:',
                          'Элементами списка будут символы ее значения,',
                          'расположенные по порядку.']],
         'var_to_set': [['Введите имя существующей переменной:',
                         'Элементами множества будут неповторяющиеся символы ее значения',
                         'в разном порядке.']],
         'reversed': [['Введите имя присваемой переменной:'], ['Введите имя существующей переменной:']]}
