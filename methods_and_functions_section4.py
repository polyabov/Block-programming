import pygame

with open('files/add.bmp') as file:
    add_image = pygame.image.load(file)
with open('files/append.bmp') as file:
    append_image = pygame.image.load(file)
with open('files/clear.bmp') as file:
    clear_image = pygame.image.load(file)
with open('files/copy.bmp') as file:
    copy_image = pygame.image.load(file)
with open('files/del.bmp') as file:
    del_image = pygame.image.load(file)
with open('files/elem_by_index.bmp') as file:
    elem_by_index_image = pygame.image.load(file)
with open('files/index.bmp') as file:
    index_image = pygame.image.load(file)
with open('files/remove.bmp') as file:
    remove_image = pygame.image.load(file)
with open('files/replace(1).bmp') as file:
    replace_1_image = pygame.image.load(file)
with open('files/replace(all).bmp') as file:
    replace_all_image = pygame.image.load(file)
with open('files/replace.bmp') as file:
    replace_image = pygame.image.load(file)
with open('files/slice.bmp') as file:
    slice_image = pygame.image.load(file)
with open('files/split.bmp') as file:
    split_image = pygame.image.load(file)
with open('files/slice_by_index.bmp') as file:
    slice_by_index_image = pygame.image.load(file)
with open('files/strip.bmp') as file:
    strip_image = pygame.image.load(file)
with open('files/len.bmp') as file:
    len_image = pygame.image.load(file)

name_img = {'add': add_image,
            'remove': remove_image,
            'append': append_image,
            'split': split_image,
            'clear': clear_image,
            'slice_by_index': slice_by_index_image,
            # 'del': del_image,
            'replace': replace_image,
            'elem_by_index': elem_by_index_image,
            'index': index_image,
            'len': len_image}


def init():
    result_list = []
    for name, i, coords in zip(name_img.keys(), name_img.values(),
                               [(220, 100), (220, 235), (220, 370), (220, 505),
                                (220, 640), (500, 40), (500, 190), (500, 340), (500, 490),
                                (500, 640)]):
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
    if name == 'add':
        print(f"{text2}.add({text1}", file=file)
    if name == 'remove':
        print(f"{text2}.remove{text1}", file=file)
    if name == 'append':
        print(f"{text2}.append({text1})", file=file)
    if name == 'clear':
        print(f"{text1}.clear", file=file)
    if name == 'slice_by_index':
        print(f"{text1} = {text2}[{text3}:{text4}]", file=file)
    # if name == 'del':
    #    print(f"")
    if name == 'replace':
        print(f"{text2}.replace({text1}, 1)", file=file)
    if name == 'elem_by_index':
        print(f"{text1} = {text3}[int({text2})]", file=file)
    if name == 'index':
        print(f"{text1} = {text3}.index({text2})", file=file)
    if name == 'split':
        print(f"{text1} = {text2}.split('{text3}')", file=file)
    if name == 'len':
        print(f"{text1} = len({text2})", file=file)


def helping_text(name, i):
    global texts
    return texts[name][i]


texts = {'add': [['Введите добавляемое значение:'], ['Введите имя существующего множества:']],
         'remove': [['Введите удаляемое значение:'], ['Введите имя существующего массива:']],
         'append': [['Введите имя добавляемой переменной:', 'либо любую строку в кавычках',
                     'если число вводите без кавычек'], ['Введите имя существующего списка:']],
         'split': [['Введите название нового списка:'], ['Введите имя существующей строки:',
                                                         'либо саму любую строку в двойных кавычках'],
                   ['Введите то, что будет являться разделителем без кавычек:']],
         'clear': [['Введите имя существующего списка:']],
         'slice_by_index': [['Введите имя присваемого списка'], ['Введите разрезаемый список:'],
                            ['Введите индекс(номер) первого элемента в срезе:', 'Индексация начинается с нуля'],
                            ['Введите индекс элемента конца среза:', 'Если вы хотите указать индекс с конца списка', 'используйте минус перед числом. Нумерация начинается с -1.', '-1 это индекс последнего элемента, -2 это индекс предпоследнего']],
         'replace': [['Введите имя изменяемой строки:'], ['Введите заменяемую часть(символы):'],
                     ['Введите на что заменить:']],
         'elem_by_index': [['Введите имя присваемой переменной:'], ['Введите номер элемента из списка:'],
                           ['Введите список:']],
         'index': [['Введите имя присваемой переменной:'], ['Введите элемент из списка:'], ['Введите список:']],
         'len': [['Введите имя присваемой переменной:'], ['Введите имя существующего списка:']]}
