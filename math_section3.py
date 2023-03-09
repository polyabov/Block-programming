import pygame


with open('files/plus.bmp') as file:
    plus_image = pygame.image.load(file)
with open('files/minus.bmp') as file:
    minus_image = pygame.image.load(file)
with open('files/multiplication.bmp') as file:
    multiplication_image = pygame.image.load(file)
with open('files/div.bmp') as file:
    div_image = pygame.image.load(file)
with open('files/mod.bmp') as file:
    mod_image = pygame.image.load(file)
with open('files/max.bmp') as file:
    max_image = pygame.image.load(file)
with open('files/min.bmp') as file:
    min_image = pygame.image.load(file)
with open('files/division.bmp') as file:
    division_image = pygame.image.load(file)


name_img = dict(plus=plus_image, minus=minus_image, multiplication=multiplication_image, division=division_image,
                div=div_image, mod=mod_image, max=max_image, min=min_image)


def init():
    result_list = []
    for name, i, coords in zip(name_img.keys(), name_img.values(),
                                   [(200, 100), (200, 260), (200, 420), (200, 580),
                                    (470, 100), (470, 260), (470, 420), (470, 580)]):
        rect = i.get_rect()
        rect.topleft = coords
        result_list.append((name, rect))
    return result_list


def blit_img(screen, name, rect):
    screen.blit(name_img[name], rect)


def action(file, name, text1='', text2='', text3='', text4='', flag_first_tab=False):
    from basic_section1 import flag_tab
    if flag_tab:
        print('\t'*flag_tab, end='', file=file)
    if name == 'plus':
        print(f"{text1} = {text2} + {text3}", file=file)
    if name == 'minus':
        print(f"{text1} = {text2} - {text3}", file=file)
    if name == 'multiplication':
        print(f"{text1} = {text2} * {text3}", file=file)
    if name == 'division':
        print(f"{text1} = {text2} / {text3}", file=file)
    if name == 'div':
        print(f"{text1} = {text2} // {text3}", file=file)
    if name == 'mod':
        print(f"{text1} = {text2} % {text3}", file=file)
    if name == 'max':
        print(f"{text1} = max({text2})", file=file)
    if name == 'min':
        print(f"{text1} = min({text2})", file=file)


def helping_text(name, i):
    global texts
    return texts[name][i]


texts = {'min': [['Введите имя присваемой переменной:', 'Если такой еще не существует она будет создана.'],
                 ['Введите имя существующего массива:']],
             'max': [['Введите имя присваемой переменной:', 'Если такой еще не существует она будет создана.'],
                     ['Введите имя существующего массива:']],
             'plus': [['Введите имя присваемой переменной:', 'Если такой еще не существует она будет создана.',
                       'Эту операцию можно использовать для склеивания двух строк или списков в один',
                       'или для добавления элемента в список.'],
                      ['Введите первое слагаемое:', 'число, либо имя строки/списка к которому хотите присоединить следующее,',
                       'либо саму строку в кавычках.'],
                      ['Введите второе слагаемое:']],
             'minus': [['Введите имя присваемой переменной:', 'Если такой еще не существует она будет создана.'],
                       ['Введите уменьшаемое:'], ['Введите вычитаемое:']],
             'multiplication': [['Введите имя присваемой переменной:', 'Если такой еще не существует она будет создана.'],
                                ['Введите первый множитель', 'Если вы введете значение строки в кавычках, либо имя строковой переменной',
                                 'а затем число, то переменная будет равна данной строке повторенной это число раз.'], ['Введите второй множитель:']],
             'division': [['Введите имя присваемой переменной:', 'Если такой еще не существует она будет создана.'],
                          ['Введите делимое:'],
                          ['Введите делитель:', 'Не должен быть равен нулю.']],
             'div': [['Введите имя присваемой переменной:', 'Если такой еще не существует она будет создана.'],
                     ['Введите делимое:'],
                     ['Введите делитель:', 'Не должен быть равен нулю.']],
             'mod': [['Введите имя присваемой переменной:', 'Если такой еще не существует она будет создана.'],
                     ['Введите делимое:'],
                     ['Введите делитель:', 'Не должен быть равен нулю.']]}