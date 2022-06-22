def move(_pos, _dir):
    x, y = _pos
    if _dir == 'U':
        return [x - check_movable(x - 1, y), y]
    if _dir == 'D':
        return [x + check_movable(x + 1, y), y]
    if _dir == 'L':
        return [x, y - check_movable(x, y - 1)]
    if _dir == 'R':
        return [x, y + check_movable(x, y + 1)]


def check_movable(_x, _y):
    return 0 <= _x < N and 0 <= _y < M and playground[_x][_y] != '#'


def execute():
    x, y = char['POS']
    pos = playground[x][y]
    if pos == '.':
        return 0
    if pos == 'B':
        open_box()
        return 0
    if pos == '^':
        return get_spike()
    return get_battle()


def open_box():
    x, y = char['POS']
    box = boxes[x][y]
    if box['TYPE'] == 'W':
        char['EQUIPMENT']['WEAPON'] = box['SPEC']
    elif box['TYPE'] == 'A':
        char['EQUIPMENT']['ARMOR'] = box['SPEC']
    else:
        if len(char['EQUIPMENT']['ORNAMENTS']) < 4 and char['EQUIPMENT']['ORNAMENTS'].get(box['SPEC']) is None:
            char['EQUIPMENT']['ORNAMENTS'][box['SPEC']] = True
    playground[x][y] = '.'


def get_spike():
    char['HP'] -= 1 if char['EQUIPMENT']['ORNAMENTS'].get('DX') else 5
    if char['HP'] <= 0:
        if char['EQUIPMENT']['ORNAMENTS'].get('RE'):
            revive()
        else:
            return 1
    return 0


def get_battle():
    x, y = char['POS']
    is_boss = playground[x][y] == 'M'
    char_atk = char['ATK'] + char['EQUIPMENT']['WEAPON']
    char_def = char['DEF'] + char['EQUIPMENT']['ARMOR']
    monster = monsters[x][y]
    monster_hp = monster['HP']
    if is_boss and char['EQUIPMENT']['ORNAMENTS'].get('HU'):
        char['HP'] = char['MAX_HP']

    first_atk_magnification = \
        3 if char['EQUIPMENT']['ORNAMENTS'].get('CO') and char['EQUIPMENT']['ORNAMENTS'].get('DX') else\
        2 if char['EQUIPMENT']['ORNAMENTS'].get('CO') else 1

    monster_hp -= max(1, char_atk * first_atk_magnification - monster['DEF'])
    if monster_hp <= 0:
        set_battle_result(monster['EXP'])
        return 1 if is_boss else 0

    if not (is_boss and char['EQUIPMENT']['ORNAMENTS'].get('HU')):
        char['HP'] -= max(1, monster['ATK'] - char_def)
        if char['HP'] <= 0:
            if char['EQUIPMENT']['ORNAMENTS'].get('RE'):
                revive()
                return 0
            else:
                return 1

    while True:
        monster_hp -= max(1, char_atk - monster['DEF'])
        if monster_hp <= 0:
            set_battle_result(monster['EXP'])
            return 1 if is_boss else 0
        char['HP'] -= max(1, monster['ATK'] - char_def)
        if char['HP'] <= 0:
            if char['EQUIPMENT']['ORNAMENTS'].get('RE'):
                revive()
                return 0
            else:
                return 1


def set_battle_result(_exp):
    char['EXP'] += int(_exp * (1.2 if char['EQUIPMENT']['ORNAMENTS'].get('EX') else 1))
    if char['EXP'] >= char['MAX_EXP']:
        char['LV'] += 1
        char['MAX_HP'] += 5
        char['HP'] = char['MAX_HP']
        char['ATK'] += 2
        char['DEF'] += 2
        char['MAX_EXP'] += 5
        char['EXP'] = 0
    if char['EQUIPMENT']['ORNAMENTS'].get('HR'):
        char['HP'] = min(char['HP'] + 3, char['MAX_HP'])
    x, y = char['POS']
    playground[x][y] = '.'


def revive():
    char['HP'] = char['MAX_HP']
    char['POS'] = initial_char_pos[:]
    del(char['EQUIPMENT']['ORNAMENTS']['RE'])


def print_result():
    char_x, char_y = char['POS']
    if char['HP'] > 0:
        playground[char_x][char_y] = '@'
    for x in range(N):
        print(''.join(playground[x]))
    print(f"""Passed Turns : {T}
LV : {char['LV']}
HP : {max(0, char['HP'])}/{char['MAX_HP']}
ATT : {char['ATK']}+{char['EQUIPMENT']['WEAPON']}
DEF : {char['DEF']}+{char['EQUIPMENT']['ARMOR']}
EXP : {char['EXP']}/{char['MAX_EXP']}""")
    boss_x, boss_y = boss_pos
    if playground[boss_x][boss_y] != 'M':
        print('YOU WIN!')
    elif char['HP'] <= 0:
        print(f'YOU HAVE BEEN KILLED BY {"SPIKE TRAP" if playground[char_x][char_y] == "^" else monsters[char_x][char_y]["NAME"]}..')
    else:
        print('Press any key to continue.')


char = {
    'HP': 20,
    'ATK': 2,
    'DEF': 2,
    'LV': 1,
    'EXP': 0,
    'EQUIPMENT': {
        'WEAPON': 0,
        'ARMOR': 0,
        'ORNAMENTS': {},
    },
    'POS': [0, 0],
    'MAX_HP': 20,
    'MAX_EXP': 5,
}

N, M = map(int, input().split())
monsters = [[''] * M for _ in range(N)]
boxes = [[''] * M for _ in range(N)]
playground = []
initial_char_pos = [0, 0]
boss_pos = [0, 0]

monster_cnt = box_cnt = 0
for i in range(N):
    row = list(input())
    for j in range(M):
        if row[j] == '@':
            row[j] = '.'
            initial_char_pos = [i, j]
            char['POS'] = [i, j]
        elif row[j] == 'B':
            box_cnt += 1
        elif row[j] == '&':
            monster_cnt += 1
        elif row[j] == 'M':
            boss_pos = [i, j]
            monster_cnt += 1
    playground.append(row)

commands = input()

for _ in range(monster_cnt):
    R, C, S, W, A, H, E = map(str, input().split())
    monsters[int(R) - 1][int(C) - 1] = {
        'NAME': S,
        'ATK': int(W),
        'DEF': int(A),
        'HP': int(H),
        'EXP': int(E)
    }

for _ in range(box_cnt):
    R, C, T, S = map(str, input().split())
    boxes[int(R) - 1][int(C) - 1] = {
        'TYPE': T,
        'SPEC': S if T == 'O' else int(S)
    }

T = 0
for command in commands:
    T += 1
    char['POS'] = move(char['POS'], command)
    if execute():
        break
print_result()
