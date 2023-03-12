import sys

import pip

pip.main(['install', '--upgrade', 'pip'])
pip.main(['install', 'pygame'])
pip.main(['install', 'pygame-widgets'])

import pygame
import pygame_widgets
from pygame_widgets.textbox import TextBox
import basic_section1
import vars_section2
import math_section3
import methods_and_functions_section4
import conditions_and_loops_section5
import os
from pathlib import Path


def start_menu():
    global WIDTH, HEIGHT, screen, clock, FPS, WHITE, BLACK, big_font, small_font, back1

    text_title = big_font.render('БЛОЧНОЕ ПРОГРАММИРОВАНИЕ', True, WHITE)
    text_start = medium_font.render('Начать', True, BLACK)
    text_esc = small_font.render('Чтобы выйти нажмите Escape', True, WHITE)

    running = True
    while running:
        screen.blit(back1, (0, 0))

        button_start = pygame.Rect \
            ((WIDTH * 0.5 - main_button_image.get_width() // 2, HEIGHT * 0.4), (WIDTH * 0.2 + 150, HEIGHT * 0.1))

        screen.blit(text_title, (WIDTH * 0.2, HEIGHT * 0.2))

        screen.blit(main_button_image, button_start)

        screen.blit(text_start, (button_start.centerx - 150, button_start.centery - 30))
        screen.blit(text_esc, (button_start.centerx - 250, HEIGHT * 0.9))

        for i in pygame.event.get():
            if i.type == pygame.QUIT or (i.type == pygame.KEYDOWN and i.key == pygame.K_ESCAPE):
                running = False
            if button_start.collidepoint(pygame.mouse.get_pos()):
                if i.type == pygame.MOUSEBUTTONDOWN:
                    return main()

        pygame.display.update()
        clock.tick(FPS)


def menu():
    global WIDTH, HEIGHT, screen, clock, FPS, WHITE, BLACK, small_font, medium_font, big_font, back1, back2, back

    text_title = big_font.render('МЕНЮ:', True, BLACK)
    text_continue = medium_font.render('Продолжить', True, BLACK)
    text_exit = medium_font.render('Выйти', True, BLACK)
    text_menu = medium_font.render('Сменить фон', True, BLACK)

    button_continue = pygame.Rect((WIDTH * 0.5 - main_button_image.get_width() // 2, HEIGHT * 0.3),
                                  (WIDTH * 0.2 + 150, HEIGHT * 0.1))
    button_exit = pygame.Rect((WIDTH * 0.5 - main_button_image.get_width() // 2, HEIGHT * 0.5),
                              (WIDTH * 0.2 + 150, HEIGHT * 0.1))
    button_menu = pygame.Rect \
        ((WIDTH * 0.5 - main_button_image.get_width() // 2, HEIGHT * 0.7), (WIDTH * 0.2 + 150, HEIGHT * 0.1))

    running = True
    while running:
        screen.blit(back2, (0, 0))

        screen.blit(text_title, (WIDTH * 0.5 - 100, HEIGHT * 0.1))

        screen.blit(main_button_image, button_continue)
        screen.blit(main_button_image, button_exit)
        screen.blit(main_button_image, button_menu)

        screen.blit(text_continue, (button_continue.centerx - 180, button_continue.centery - 30))
        screen.blit(text_exit, (button_exit.centerx - 140, button_exit.centery - 30))
        screen.blit(text_menu, (button_menu.centerx - 190, button_menu.centery - 30))

        for i in pygame.event.get():
            if i.type == pygame.QUIT:
                running = False
            elif i.type == pygame.KEYDOWN and i.key == pygame.K_ESCAPE:
                return
            if button_continue.collidepoint(pygame.mouse.get_pos()):
                if i.type == pygame.MOUSEBUTTONDOWN:
                    return
            elif button_exit.collidepoint(pygame.mouse.get_pos()):
                if i.type == pygame.MOUSEBUTTONDOWN:
                    return False
            elif button_menu.collidepoint(pygame.mouse.get_pos()):
                if i.type == pygame.MOUSEBUTTONDOWN:
                    back1, back2, back = back2, back, back1

        pygame.display.update()
        clock.tick(FPS)


def input_text(helping_text_list):  # функция окна для ввода текста
    global WIDTH, HEIGHT, screen, clock, FPS, WHITE, BLACK, medium_font, small_font, back2

    textbox = TextBox(screen, 1000, 100, 400, 60, fontSize=50, borderColour=(0, 0, 0), textColour=(0, 0, 200),
                      radius=10, borderThickness=4)

    running = True
    while running:
        screen.blit(back2, (0, 0))

        events = pygame.event.get()
        for i in events:
            if i.type == pygame.QUIT:
                return None
            elif i.type == pygame.KEYDOWN and i.key == pygame.K_ESCAPE:
                if menu() == False:
                    running = False
            elif i.type == pygame.KEYDOWN and i.key == pygame.K_RETURN and textbox.getText():
                pygame_widgets.update(
                    events)  # обновляем события и передаем нажатое (введенные буквы) при нажатии Enter
                return textbox.getText()

        y = 100  # координата по оси у первой строчки текста
        for helping_text in helping_text_list:
            text_out = medium_font.render(helping_text, True, BLACK)
            screen.blit(text_out, (100, y))
            y += 60

        pygame_widgets.update(events)
        pygame.display.update()
        clock.tick(FPS)


def draw_the_arrow(x0, y0, h):
    pygame.draw.polygon(screen, (0, 0, 0),
                        ((x0 - 3, y0), (x0 + 3, y0), (x0 + 3, y0 + h - 5), (x0 + 7, y0 + h - 5), (x0, y0 + h),
                         (x0 - 7, y0 + h - 5), (x0 - 3, y0 + h - 5)))


def main():
    global WIDTH, HEIGHT, screen, clock, FPS, WHITE, BLACK, medium_font, small_font, text

    program = []
    module = None
    names_rects = None
    run_button = None
    delete_button = None

    len_button = buttons['pink'].get_width()  # pink, т. к. у всех жемчужин одинаковый размер
    for k in range(1, 10, 2):
        section.append(pygame.Rect((WIDTH // 18 - len_button // 2, HEIGHT * k // 14 - len_button // 2),
                                   (len_button * 2, len_button * 2)))
    for k, j in enumerate(range(1, 10, 2)):
        section[k].topleft = (len_button // 2, HEIGHT * j // 10 - len_button // 2)
        section[k].size = (len_button, len_button)

    title_of_section = ''
    circle_fast_text = ''
    index_of_colid_circle = -1
    text_from_consol = None
    last_elem = None
    program_scroller = 0
    console_scroller = 0

    running = True
    while running:
        screen.blit(back2, (0, 0))

        for i in pygame.event.get():
            if i.type == pygame.QUIT:
                running = False
            if i.type == pygame.KEYDOWN and i.key == pygame.K_ESCAPE:
                if menu() == False:
                    running = False
            if i.type == pygame.MOUSEWHEEL:
                if WIDTH - 750 < pygame.mouse.get_pos()[0] < WIDTH and 0 < pygame.mouse.get_pos()[1] < HEIGHT - 180:
                    program_scroller += i.y
                elif WIDTH - 750 < pygame.mouse.get_pos()[0] < WIDTH and HEIGHT - 180 < pygame.mouse.get_pos()[
                    1] < HEIGHT:
                    console_scroller += i.y
            for j, name_module in enumerate(sections_names):
                if section[j].collidepoint(pygame.mouse.get_pos()):
                    index_of_colid_circle = 2 * j + 1
                    circle_fast_text = name_module[1]
                    if i.type == pygame.MOUSEBUTTONDOWN:
                        title_of_section = name_module[1]
                        if not module or module != name_module[0]:
                            module = name_module[0]
                            names_rects = module.init()
                        else:
                            module = None
                            names_rects = None
                            title_of_section = ''
                    break
            else:
                index_of_colid_circle = -1

            if names_rects is not None and module is not None:
                for name_of_rect, rect in names_rects:
                    if i.type == pygame.MOUSEBUTTONDOWN and rect.collidepoint(pygame.mouse.get_pos()):
                        if run_button is None:
                            run_button = pygame.Rect((800, 150), (200, 50))
                        if delete_button is None:
                            delete_button = pygame.Rect((800, 250), (200, 50))
                        textpr = ['', '', '', '']
                        for number_of_rects_list, rects_list in enumerate(
                                [['print_phrase', 'print_var', 'var_to_int', 'var_to_float', 'var_to_str',
                                  'var_to_list', 'var_to_set', 'clear', 'while', 'for_elem_in',
                                  'for_in_range', 'if'],
                                 ['var', 'copy', 'reversed', 'len', 'min', 'max', 'add', 'remove',
                                  'append', 'if_contains', 'if_not_contains'],
                                 ['plus', 'minus', 'multiplication', 'div',
                                  'mod', 'replace', 'elem_by_index', 'index', 'split'], ['slice_by_index']]):
                            if name_of_rect in rects_list:
                                for textpr_i in range(number_of_rects_list + 1):
                                    textpr[textpr_i] = input_text(module.helping_text(name_of_rect, textpr_i))
                                    if textpr[textpr_i] is None:
                                        return

                        program.append((module, name_of_rect, rect.copy(), textpr[0], textpr[1], textpr[2], textpr[3]))

            if i.type == pygame.MOUSEBUTTONDOWN and delete_button is not None and delete_button.collidepoint(
                    pygame.mouse.get_pos()):
                if len(program) == 1:
                    run_button = None
                    delete_button = None
                    text_from_consol = None
                program.pop(-1)

            if i.type == pygame.MOUSEBUTTONDOWN and run_button is not None and run_button.collidepoint(
                    pygame.mouse.get_pos()):
                flag_first_tab = True
                text_from_consol = []

                try:
                    file_path = str(Path.home()) + '\\Documents\\python_output_program'
                    if sys.platform not in ['win32', 'win64', 'win86']:
                        file_path = file_path.replace('\\', '/').replace('//', '/')
                    if not os.path.exists(file_path):
                        os.makedirs(file_path)
                    file_path = file_path.replace('\\', '\\\\') + '\\'
                    if sys.platform not in ['win32', 'win64', 'win86']:
                        file_path = file_path.replace('\\', '/').replace('//', '/')
                    with open(file_path + 'output.py', 'w', encoding='UTF-8') as file:
                        file.write(
                            f"with open('{file_path}\console.txt', 'w') as file:\n\tfile.write('')\nfile = open('{file_path}\console.txt', 'a')\n")
                    with open(file_path + 'output.py', 'a', encoding='UTF-8') as file:
                        for p in program:
                            p[0].action(file, p[1], p[3], p[4], p[5], flag_first_tab=flag_first_tab)
                            flag_first_tab = False
                        file.write('\nfile.close()')
                    with open(file_path + 'output.py', 'r', encoding='UTF-8') as file:
                        command = ''.join(file.readlines())
                        if sys.platform not in ['win32', 'win64', 'win86']:
                            command = command.replace('\\', '/').replace('//', '/')
                        exec(command)
                    with open(file_path + 'console.txt', 'r', encoding='UTF-8') as file:
                        text_from_consol = []
                        for line in file.readlines():
                            text_from_consol.append(small_font.render(line[:-1], True, BLACK))

                except IndentationError:
                    text_from_consol.append(small_font.render('Ошибка отступа.', True, BLACK))
                    text_from_consol.append(
                        small_font.render('Вероятно, вы неправильно использовали блоки "Начало" или "Конец",', True,
                                          BLACK))
                    text_from_consol.append(
                        small_font.render('которые должны быть только в начале и конце тела цикла.', True, BLACK))
                except NameError:
                    text_from_consol.append(small_font.render('Ошибка имени переменной.', True, BLACK))
                    text_from_consol.append(
                        small_font.render('Переменная,которую вы используете, не определена.', True, BLACK))
                    text_from_consol.append(
                        small_font.render('Присвойте ей значение, использовав блок', True, BLACK))
                    text_from_consol.append(
                        small_font.render('"имя переменной = значение" перед тем, как ее вызвать.', True, BLACK))
                except TypeError:
                    text_from_consol.append(small_font.render('Ошибка типа.', True, BLACK))
                    text_from_consol.append(
                        small_font.render('Произошла попытка объединить два несовместимых объекта.', True, BLACK))
                    text_from_consol.append(
                        small_font.render('(Например строку и число)', True, BLACK))
                except IndexError:
                    text_from_consol.append(small_font.render('Ошибка индекса.', True, BLACK))
                    text_from_consol.append(
                        small_font.render('Вы использовали индекс, которого не существует в этом списке.', True, BLACK))
                    text_from_consol.append(
                        small_font.render('или он находится вне его диапазона.', True, BLACK))
                except ZeroDivisionError:
                    text_from_consol.append(small_font.render('Ошибка деления на ноль.', True, BLACK))
                except ValueError:
                    text_from_consol.append(small_font.render('Ошибка значения.', True, BLACK))
                    text_from_consol.append(
                        small_font.render('Вы использовали аргумент с недопустимым значением.', True, BLACK))
                    text_from_consol.append(
                        small_font.render('Невозможно преобразовать используемую Вами строку в нужный тип.', True,
                                          BLACK))
                except Exception:
                    text_from_consol.append(small_font.render('Произошла неизвестная ошибка.', True, BLACK))
                    text_from_consol.append(small_font.render('Перепроверьте блок-схему.', True, BLACK))

        if module:
            # pygame.draw.rect(screen, (210, 210, 210, 128), ((160, 0), (600, HEIGHT)))
            surface = pygame.Surface((570, HEIGHT), pygame.SRCALPHA)
            surface.fill((255, 255, 255))
            surface.set_alpha(60)
            screen.blit(surface, (160, 0))

            for name_of_rect, rect in names_rects:
                module.blit_img(screen, name_of_rect, rect.topleft)  # отрисовка блоков открытого модуля
                # изображения блоков для каждого модуля, тексты для них и отрисовывающая функция находится в файлах папки main
                # basic_section1, vars_section2, math_section3, methods_and_functions_section4,
                # conditions_and_loops_section5

        title_of_section_text_print = medium_font.render(title_of_section, True, BLACK)
        circle_fast_text_print = small_font.render(circle_fast_text, True, BLACK)

        if index_of_colid_circle != -1:
            screen.blit(circle_fast_text_print, (len_button // 2 - index_of_colid_circle * 3,
                                                 HEIGHT * index_of_colid_circle // 10 - len_button // 2 + 80))

        screen.blit(title_of_section_text_print, (len_button * 2 + 10, len_button // 2))

        for i, color in enumerate(buttons.keys()):
            screen.blit(buttons[color], section[i].topleft)

        text_title = medium_font.render('ПОЛЕ БЛОК-СХЕМЫ', True, BLACK)

        if program:
            screen.blit(text_title, (780, 50))

            screen.blit(main_button_image, run_button)
            screen.blit(main_button_image, delete_button)

            text_run = small_font.render('Выполнить программу', True, BLACK)
            text_delete = small_font.render('Удалить последний блок', True, BLACK)
            screen.blit(text_run, (823, 175))
            screen.blit(text_delete, (818, 275))

            surface = pygame.Surface((WIDTH - 750, 180), pygame.SRCALPHA)
            surface.fill((255, 255, 255))
            surface.set_alpha(120)
            screen.blit(surface, (750, HEIGHT - 180))

            pygame.draw.line(screen, BLACK, (750, HEIGHT - 180), (750, HEIGHT), 4)
            pygame.draw.line(screen, BLACK, (750, HEIGHT - 180), (WIDTH, HEIGHT - 180), 4)

            if len(program) > 5:
                count = len(program) - 5
            else:
                count = 0
            for elem in program:
                if program.index(elem) == 0:
                    last_elem = elem
                    elem[2].topleft = (1200, 20 - count * (elem[2].height + 10) + program_scroller * 15)
                else:
                    elem[2].topleft = (last_elem[2].left, last_elem[2].bottom + 10)
                    if elem[2].bottom >= HEIGHT - 180:
                        continue
                    draw_the_arrow(last_elem[2].centerx, last_elem[2].bottom, 10)
                    last_elem = elem
                if elem[2].bottom >= HEIGHT - 180:
                    continue
                elem[0].blit_img(screen, elem[1], elem[2].topleft)

                cords_with_1text_in_program_for_names = {'print_phrase': (elem[2].centerx - 100, elem[2].centery + 25),
                                                         'print_var': (elem[2].centerx + 12, elem[2].centery - 12),
                                                         'var_to_int': (elem[2].centerx + 20, elem[2].centery - 20),
                                                         'var_to_float': (elem[2].centerx + 20, elem[2].centery - 20),
                                                         'var_to_str': (elem[2].centerx + 20, elem[2].centery - 20),
                                                         'var_to_list': (elem[2].centerx + 20, elem[2].centery - 20),
                                                         'var_to_set': (elem[2].centerx + 20, elem[2].centery - 20),
                                                         'clear': (elem[2].centerx + 15, elem[2].centery),
                                                         'while': (elem[2].centerx - 5, elem[2].centery - 22),
                                                         'for_elem_in': (elem[2].centerx - 30, elem[2].centery + 36),
                                                         'for_in_range': (elem[2].centerx + 22, elem[2].centery - 18),
                                                         'if': (elem[2].centerx - 20, elem[2].centery - 20)}
                cords_with_2texts_in_program_for_names = {'var': [(elem[2].centerx + 18, elem[2].centery - 40),
                                                                  (elem[2].centerx - 35, elem[2].centery - 5)],
                                                          'copy': [(elem[2].centerx - 45, elem[2].centery - 42),
                                                                   (elem[2].centerx - 5, elem[2].centery - 5)],
                                                          'reversed': [(elem[2].centerx - 35, elem[2].centery + 20),
                                                                       (elem[2].centerx - 35, elem[2].centery - 5)],
                                                          'len': [(elem[2].centerx - 35, elem[2].centery - 40),
                                                                  (elem[2].centerx, elem[2].centery)],
                                                          'min': [(elem[2].centerx - 38, elem[2].centery - 50),
                                                                  (elem[2].centerx + 60, elem[2].centery + 8)],
                                                          'max': [(elem[2].centerx - 35, elem[2].centery - 45),
                                                                  (elem[2].centerx + 15, elem[2].centery)],
                                                          'add': [(elem[2].centerx + 18, elem[2].centery - 35),
                                                                  (elem[2].centerx + 25, elem[2].centery - 10)],
                                                          'remove': [(elem[2].centerx + 15, elem[2].centery - 23),
                                                                     (elem[2].centerx + 50, elem[2].centery)],
                                                          'append': [(elem[2].centerx + 18, elem[2].centery - 35),
                                                                     (elem[2].centerx + 5, elem[2].centery - 5)],
                                                          'if_contains': [(elem[2].centerx - 66, elem[2].centery - 30),
                                                                          (elem[2].centerx - 13, elem[2].centery - 4)],
                                                          'if_not_contains': [
                                                              (elem[2].centerx - 8, elem[2].centery - 45),
                                                              (elem[2].centerx - 13, elem[2].centery + 8)]}
                cords_with_3texts_in_program_for_names = {'plus': [(elem[2].centerx - 35, elem[2].centery - 35),
                                                                   (elem[2].centerx - 80, elem[2].centery),
                                                                   (elem[2].centerx + 15, elem[2].centery)],
                                                          'minus': [(elem[2].centerx - 35, elem[2].centery - 35),
                                                                    (elem[2].centerx - 80, elem[2].centery),
                                                                    (elem[2].centerx + 15, elem[2].centery)],
                                                          'multiplication':
                                                              [(elem[2].centerx - 35, elem[2].centery - 35),
                                                               (elem[2].centerx - 80, elem[2].centery - 5),
                                                               (elem[2].centerx + 15, elem[2].centery - 5)],
                                                          'div': [(elem[2].centerx - 70, elem[2].centery - 50),
                                                                  (elem[2].centerx - 80, elem[2].centery + 10),
                                                                  (elem[2].centerx + 15, elem[2].centery + 10)],
                                                          'mod': [(elem[2].centerx - 70, elem[2].centery - 55),
                                                                  (elem[2].centerx - 80, elem[2].centery + 10),
                                                                  (elem[2].centerx + 15, elem[2].centery + 10)],
                                                          'replace': [(elem[2].centerx + 12, elem[2].centery - 63),
                                                                      (elem[2].centerx + 25, elem[2].centery - 8),
                                                                      (elem[2].centerx - 10, elem[2].centery + 20)],
                                                          'elem_by_index': [
                                                              (elem[2].centerx - 35, elem[2].centery - 45),
                                                              (elem[2].centerx + 20, elem[2].centery - 22),
                                                              (elem[2].centerx + 45, elem[2].centery + 5)],
                                                          'index': [(elem[2].centerx - 80, elem[2].centery - 48),
                                                                    (elem[2].centerx - 20, elem[2].centery - 18),
                                                                    (elem[2].centerx + 45, elem[2].centery + 8)],
                                                          'split': [(elem[2].centerx, elem[2].centery - 45),
                                                                    (elem[2].centerx + 55, elem[2].centery - 20),
                                                                    (elem[2].centerx + 30, elem[2].centery + 5)]}
                cords_with_4texts_in_program_for_names = {
                    'slice_by_index': [(elem[2].centerx - 80, elem[2].centery - 45),
                                       (elem[2].centerx + 25, elem[2].centery - 45),
                                       (elem[2].centerx + 20, elem[2].centery - 18),
                                       (elem[2].centerx + 23, elem[2].centery + 8)]}

                if elem[6] != '':
                    text1_on_block = small_font.render(elem[3], True, BLACK)
                    text2_on_block = small_font.render(elem[4], True, BLACK)
                    text3_on_block = small_font.render(elem[5], True, BLACK)
                    text4_on_block = small_font.render(elem[6], True, BLACK)
                    screen.blit(text1_on_block, cords_with_4texts_in_program_for_names[elem[1]][0])
                    screen.blit(text2_on_block, cords_with_4texts_in_program_for_names[elem[1]][1])
                    screen.blit(text3_on_block, cords_with_4texts_in_program_for_names[elem[1]][2])
                    screen.blit(text4_on_block, cords_with_4texts_in_program_for_names[elem[1]][3])

                elif elem[5] != '':
                    text1_on_block = small_font.render(elem[3], True, BLACK)
                    text2_on_block = small_font.render(elem[4], True, BLACK)
                    text3_on_block = small_font.render(elem[5], True, BLACK)
                    screen.blit(text1_on_block, cords_with_3texts_in_program_for_names[elem[1]][0])
                    screen.blit(text2_on_block, cords_with_3texts_in_program_for_names[elem[1]][1])
                    screen.blit(text3_on_block, cords_with_3texts_in_program_for_names[elem[1]][2])

                elif elem[4] != '':
                    text1_on_block = small_font.render(elem[3], True, BLACK)
                    text2_on_block = small_font.render(elem[4], True, BLACK)
                    screen.blit(text1_on_block, cords_with_2texts_in_program_for_names[elem[1]][0])
                    screen.blit(text2_on_block, cords_with_2texts_in_program_for_names[elem[1]][1])

                elif elem[3] != '':
                    text1_on_block_block = small_font.render(elem[3], True, BLACK)
                    screen.blit(text1_on_block_block, cords_with_1text_in_program_for_names[elem[1]])

        k = 0
        if text_from_consol is not None:
            while k < len(text_from_consol):
                k += 1
                if HEIGHT // 2 + 250 + k * 30 + console_scroller * 2 < HEIGHT - 160:
                    continue
                screen.blit(text_from_consol[k - 1], (760, HEIGHT // 2 + 250 + (k - 1) * 30 + console_scroller * 2))

        pygame.display.update()
        clock.tick(FPS)


pygame.init()

FPS = 60

screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
WIDTH = screen.get_width()
HEIGHT = screen.get_height()
if WIDTH > 1600 or HEIGHT > 900:
    WIDTH = 1536
    HEIGHT = 864
    screen = pygame.display.set_mode((WIDTH, HEIGHT))

clock = pygame.time.Clock()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

pygame.font.get_fonts()
small_font = pygame.font.SysFont('segoeprint', 20)
medium_font = pygame.font.SysFont('segoeprint', 30)
big_font = pygame.font.SysFont('segoeprint', 50)

text = ''

sections_names = [(basic_section1, 'Основные'), (vars_section2, 'Переменные'),
                  (math_section3, 'Математика'),
                  (methods_and_functions_section4, 'Методы'),
                  (conditions_and_loops_section5, 'Условия и циклы')]

buttons = dict()
for color in ['orange', 'pink', 'white', 'violet', 'blue']:
    with open(f'files/pearls_{color.upper()}_small.bmp') as button_file:
        buttons[color] = pygame.image.load(button_file)

with open('files/фон.bmp') as file:
    back = pygame.image.load(file)
with open('files/фон1.bmp') as file:
    back1 = pygame.image.load(file)
with open('files/фон2.bmp') as file:
    back2 = pygame.image.load(file)
with open('files/main_button.bmp') as file:
    main_button_image = pygame.image.load(file)

section = []

start_menu()

pygame.quit()
