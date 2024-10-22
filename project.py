from termcolor import cprint
from tabulate import tabulate
import re
import os
import random
import pyfiglet
import time





moji_empty = ['🈲' * 32]


def main():
    difx, dify, flip, number = welcome()
    convert_table(emoji(4), difx)
    moj = emoji(number)
    moji = cut(moj, difx, dify)
    clear()
    emptytable = scramble(moji_empty, difx, dify)
    table = scramble(moji, difx, dify)
    convert_table(emptytable, difx)
    check_fruit(emptytable, table, difx, dify, flip)


def emoji(n):
    list = {
        1: [
            "🍉", "🍇", "🍊", "🍍", "🍋", "🍒", "🍌", "🍓", "🍅", "🥝",
            "🍏", "🍎", "🥥", "🥭", "🍈", "🥑", "🍆", "🥒", "🌽", "🥕",
            "🍤", "🧄", "🍠", "🥔", "🥦", "🥬", "🍄", "🥗", "🥢", "🌰",
            "🧂", "🥄"
        ],
        2: [
            "🌸", "🌼", "🌻", "🌺", "🌹", "🥀", "🌷", "🍃", "🌿", "💮",
            "🍀", "🍁", "🍂", "🍄", "🌱", "🌲", "🌳", "🌴", "🌵", "🌾",
            "🌺", "🌹", "🌻", "🌼", "🌸", "🌷", "🥀", "🍁", "🌳", "🌴",
            "🌱", "🌿"
        ],
        3: [
            "🦁", "🦋", "🐬", "🐢", "🦄", "🐶", "🐱", "🐻", "🐘", "🐒",
            "🦓", "🦊", "🦉", "🐦", "🐠", "🐇", "🦈", "🦙", "🐉", "🐖",
            "🐏", "🦒", "🦅", "🦋", "🐧", "🐕", "🦺", "🐫", "🦘", "🦏",
            "🐩", "🦭"
        ],
        4: [
            "⚽", "🏀", "🏈", "🎾", "🏊", "🏹", "🛼", "🏉", "🥇", "⚾",
            "🥅", "🏓", "🎳", "🥈", "🥉", "🎱", "🏒", "🥋", "🤿", "🥊",
            "🏇", "🛷", "🎣", "🥍", "🎯", "🥌", "🏏", "🎿", "🏆", "🏸",
            "🏐", '🪂'
        ]
    }
    return list.get(n, [])

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def cut(moji, dx, dy):
    n = (int(dx)*int(dy))/2
    return moji[:int(n)]


def scramble(l, difx, dify):
    values = l * 2
    random.shuffle(values)
    return format_moji(''.join(values), difx, dify)


def welcome():
    clear()
    red = lambda x: cprint(x, "red")
    f = pyfiglet.Figlet(font='colossal')
    red(f.renderText('Welcome.'))
    red('To adjust the Card Flip Rate type "adjust",\nto continue press enter')
    adjust = input()
    flip = 2
    if adjust == 'adjust':
        red('Set the "Card Flip Rate" to control how fast cards turn over after an incorrect guess.\nThe default value is 2 seconds. Please input an integer...')
        while True:
            flip = input()
            if flip.isdigit():
                break
            else:
                red('Input is not an integer')
                continue
    clear()
    red("Set the card amount by specifying the number of cards in a 𝑛x𝑛 format,\nwhere 𝑛 is an positive integer and their product is an even number.\nThe total number of cards must be less than 64.\nA square layout(e.g; 4x4) is recommended but not required.")
    while True:
        try:
            inp = re.search(r'^(\d\d?)(\w)(\d\d?)$', input('-->'))
            if int(inp.group(1)) * int(inp.group(3)) < 2:
                red('Card amount too small, please input a total of atleast 2 cards.')
                continue
            if int(inp.group(1)) * int(inp.group(3)) > 64:
                red('Card amount too big, please input a total of less than 64 cards.')
                continue
            if int(inp.group(1)) * int(inp.group(3)) % 2 != 0:
                red('Make sure the 𝑛x𝑛 equals an even number.')
                continue
            elif inp.group(2) != 'x':
                red('Please make sure your input is in a 𝑛x𝑛 format.')
                continue
            if int(inp.group(1)) > 10 or int(inp.group(3)) > 10:
                red('The deck might become unstable with too many cards on one axis,\ndo you wish to continue?(Y/N)')
                yn = input('-->')
                if yn == 'y' or yn == 'Y' or 'yn' == 'Yes' or 'yn' == 'yes' or 'yn' == 'Yes':
                    pass
                else:
                    continue
        except:
            red('Please make sure your input is in a 𝑛x𝑛 format.')
            continue
        while True:
            red('Please select theme:\n[1]-Fruits and nature\n[2]-Nature\n[3]-Animals\n[4]-Sports')
            try:
                number = input('-->')
                number = int(number)
            except:
                print('Invalid input')
                continue
            if (0 < number < 5) == False:
                continue
            else:
                break
        return inp.group(1), inp.group(3), flip, number



def format(F):
    if F.isdigit() == True:
        return F
    return f'╔════════╗ \n║ {F}  {F} ║\n║   {F}   ║\n║ {F}  {F} ║\n╚════════╝'


def convert_table(table, dx):
    a = ['B', 'C', 'D', 'E', 'F', 'G', 'H', 'I',
           'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    formatted_table = []
    for row in table:
        formatted_row = []
        for item in row:
            formatted_row.append(format(item))
        formatted_table.append(formatted_row)
    print(f'    A             {"            ".join(a[:int(dx)-1])}')
    print(tabulate(formatted_table, tablefmt='plain').replace('║    ║', '║   ║').replace('║     ║', '║   ║'))
    formatted_table = []


def format_moji(E, x, y):
    x, y = int(x), int(y)
    x2 = x
    a = 0
    b = 1
    result = []
    txt = []
    for j in range(y):
        txt += f'{b}'
        for j in range(a, x):
            txt += E[j]
        a += x2
        x += x2
        b += 1
        result.append(txt)
        txt = []
    return result


def is_finished(empty):
    for sublist in empty:
        if '🈲' in sublist:
            return False
    return True


def convert_time(seconds):
    m = seconds // 60
    s = seconds % 60
    return m, s

def end_screen(time, incorrect, total, streak):
    clear()
    red = lambda x: cprint(x, "red")
    f = pyfiglet.Figlet(font='big')
    red(f.renderText('Cogratulations'))
    m, s = convert_time(time)
    formatted_time = f"{int(m):02d}:{int(s):02d}"
    red(f'-->time elapsed: {formatted_time}')
    red(f'-->incorrect guesses: {incorrect}')
    red(f'-->amount of cards turned around: {total}')
    red(f'-->highest streak: {max(streak)}')


def check_fruit(empty, moji, difx, dify, seconds=2):
    print('Please format your input as numberletter(e.g;1a|2b) or number letter(e.g;2 a)')
    start_time = time.time()
    incorrect = 0
    total = 0
    streak = 0
    streak_list = []
    while True:
        while True:
            x,y = inputF(difx, dify)
            if empty[x][y] != '🈲':
                print()
                continue
            break
        empty[x][y] = moji[x][y]
        clear()
        convert_table(empty, difx)
        while True:
            j, k = inputF(difx, dify)
            if x == j and y == k:
                print('Please select 2 unique squares')
                continue
            elif empty[j][k] != '🈲':
                continue
            break
        empty[j][k] = moji[j][k]
        streak += 1
        clear()
        convert_table(empty, difx)
        if moji[x][y] != moji[j][k]:
            streak = 0
            incorrect += 1
            empty[x][y] = '🈲'
            empty[j][k] = '🈲'
            time.sleep(int(seconds))
            clear()
            convert_table(empty, difx)
        total += 2
        streak_list.append(streak)
        if is_finished(empty) == True:
            end_time = time.time()
            elapsed_time = end_time - start_time
            end_screen(elapsed_time, incorrect, total, streak_list)
            break





def inputF(dx, dy):
    abc = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p']
    print()
    while True:
        inp = input('-->')
        try:
            x, y = inp.split()
        except:
            try:
                x, y = inp[0], inp[1]
            except:
                print('Invalid input')
                continue
        if x.isdigit() == False or y.isalpha() == False:
            continue
        if (0 < int(x) <= int(dy)) == False:
            continue
        if y.lower() not in abc[:int(dx)]:
            continue
        y = ord(y.lower()) - 96
        return int(x) - 1, int(y)






if __name__ == "__main__":
    main()

