import pygame

with open('files/if.bmp') as file:
    if_image = pygame.image.load(file)
with open('files/else.bmp') as file:
    else_image = pygame.image.load(file)
with open('files/while.bmp') as file:
    while_image = pygame.image.load(file)
with open('files/for_elem_in.bmp') as file:
    for_elem_in_image = pygame.image.load(file)
with open('files/for_in_range.bmp') as file:
    for_in_range_image = pygame.image.load(file)
with open('files/if_contains.bmp') as file:
    if_contains_image = pygame.image.load(file)
with open('files/if_not_contains.bmp') as file:
    if_not_contains_image = pygame.image.load(file)

name_img = {'while': while_image,
            'for_elem_in': for_elem_in_image,
            'for_in_range': for_in_range_image,
            'if': if_image,
            'else': else_image,
            'if_contains': if_contains_image,
            'if_not_contains': if_not_contains_image}


def init():
    result_list = []
    for name, i, coords in zip(name_img.keys(), name_img.values(),
                               [(200, 100), (200, 300), (200, 500), (470, 100), (470, 280), (470, 460), (470, 640)]):
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
    if name == 'while':
        print(f"while {text1}:", file=file)
    elif name == 'for_elem_in':
        print(f"for elem in {text1}:", file=file)
    elif name == 'for_in_range':
        print(f"for _ in range({text1}):", file=file)
    elif name == 'if':
        print(f"if {text1}:", file=file)
    elif name == 'else':
        print('else:', file=file)
    elif name == 'if_contains':
        print(f"if {text1} in {text2}:", file=file)
    elif name == 'if_not_contains':
        print(f"if {text1} not in {text2}:", file=file)


def helping_text(name, i):
    global texts
    return texts[name][i]


texts = {'while': [['Введите условие:', 'Вместо равно используйте двойное равно.',
                    'После этого блока используйте блок "начало"',
                    'и "конец", когда тело цикла закончится.']],
         'for_elem_in': [['Введите имя массива:', 'После этого блока используйте блок "начало"',
                          'и "конец", когда тело цикла закончится.',
                          'При работе с перебираемыми элементами пишите "elem" как имя переменной.']],
         'for_in_range': [['Введите число или имя целочисленной переменной:',
                           'После этого блока используйте блок "начало"',
                           'и "конец", когда тело цикла закончится.']],
         'if': [['Введите условие:', 'Вместо равно используйте двойное равно.',
                 'После этого блока используйте блок "начало"',
                 'и "конец", когда тело цикла закончится.']],
         'if_contains': [['Введите значение:'], ['Введите значение:']],
         'if_not_contains': [['Введите значение:'], ['Введите значение:']]}
