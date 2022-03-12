# https://rubiks-cube-solver.com/fr/
def rotate_main(_arr, _cw):
    if _cw == 1:
        _arr[0][0], _arr[0][1], _arr[0][2], _arr[1][2], _arr[2][2], _arr[2][1], _arr[2][0], _arr[1][0] = \
            _arr[2][0], _arr[1][0], _arr[0][0], _arr[0][1], _arr[0][2], _arr[1][2], _arr[2][2], _arr[2][1]
    else:
        _arr[0][0], _arr[1][0], _arr[2][0], _arr[2][1], _arr[2][2], _arr[1][2], _arr[0][2], _arr[0][1] = \
            _arr[0][2], _arr[0][1], _arr[0][0], _arr[1][0], _arr[2][0], _arr[2][1], _arr[2][2], _arr[1][2]
    return _arr


def rotate_side(_face, _arr1, _arr2, _arr3, _arr4, _cw):
    if _face == 'U' or _face == 'D':
        y = 0 if _face == 'U' else 2
        if _cw == 1 and y == 0 or _cw == -1 and y == 2:
            for i in range(3):
                _arr1[y][i], _arr2[y][i], _arr3[y][i], _arr4[y][i] = \
                    _arr2[y][i], _arr3[y][i], _arr4[y][i], _arr1[y][i]
        else:
            for i in range(3):
                _arr1[y][i], _arr2[y][i], _arr3[y][i], _arr4[y][i] = \
                    _arr4[y][i], _arr1[y][i], _arr2[y][i], _arr3[y][i]
    elif _face == 'F':
        if _cw == 1:
            for i in range(3):
                _arr1[2][i], _arr2[i][0], _arr3[2][i], _arr4[2 - i][2] = \
                    _arr4[2 - i][2], _arr1[2][i], _arr2[i][0], _arr3[2][i]
        else:
            for i in range(3):
                _arr1[2][i], _arr2[i][0], _arr3[2][i], _arr4[2 - i][2] = \
                    _arr2[i][0], _arr3[2][i], _arr4[2 - i][2], _arr1[2][i]
    elif _face == 'B':
        if _cw == 1:
            for i in range(3):
                _arr1[0][i], _arr2[i][2], _arr3[0][i], _arr4[2 - i][0] = \
                    _arr2[i][2], _arr3[0][i], _arr4[2 - i][0], _arr1[0][i]
        else:
            for i in range(3):
                _arr1[0][i], _arr2[i][2], _arr3[0][i], _arr4[2 - i][0] = \
                    _arr4[2 - i][0], _arr1[0][i], _arr2[i][2], _arr3[0][i]
    elif _face == 'L':
        if _cw == 1:
            for i in range(3):
                _arr1[i][0], _arr2[i][0], _arr3[2 - i][2], _arr4[2 - i][2] = \
                    _arr4[2 - i][2], _arr1[i][0], _arr2[i][0], _arr3[2 - i][2]
        else:
            for i in range(3):
                _arr1[i][0], _arr2[i][0], _arr3[2 - i][2], _arr4[2 - i][2] = \
                    _arr2[i][0], _arr3[2 - i][2], _arr4[2 - i][2], _arr1[i][0]
    else:
        if _cw == 1:
            for i in range(3):
                _arr1[i][2], _arr2[i][2], _arr3[2 - i][0], _arr4[2 - i][0] = \
                    _arr2[i][2], _arr3[2 - i][0], _arr4[2 - i][0], _arr1[i][2]
        else:
            for i in range(3):
                _arr1[i][2], _arr2[i][2], _arr3[2 - i][0], _arr4[2 - i][0] = \
                    _arr4[2 - i][0], _arr1[i][2], _arr2[i][2], _arr3[2 - i][0]
    return _arr1, _arr2, _arr3, _arr4


for tc in range(int(input())):
    n = int(input())
    commands = list(input().split())
    cubes = {
        'U': [['w'] * 3 for _ in range(3)],
        'D': [['y'] * 3 for _ in range(3)],
        'F': [['r'] * 3 for _ in range(3)],
        'B': [['o'] * 3 for _ in range(3)],
        'L': [['g'] * 3 for _ in range(3)],
        'R': [['b'] * 3 for _ in range(3)]
    }

    for command in commands:
        face, clockwise = command[0], 1 if command[1] == '+' else -1
        cubes[face] = rotate_main(cubes[face], clockwise)
        if face == 'U' or face == 'D':
            cubes['F'], cubes['R'], cubes['B'], cubes['L'] = \
                rotate_side(face, cubes['F'], cubes['R'], cubes['B'], cubes['L'], clockwise)
        elif face == 'F' or face == 'B':
            cubes['U'], cubes['R'], cubes['D'], cubes['L'] = \
                rotate_side(face, cubes['U'], cubes['R'], cubes['D'], cubes['L'], clockwise)
        else:
            cubes['U'], cubes['F'], cubes['D'], cubes['B'] = \
                rotate_side(face, cubes['U'], cubes['F'], cubes['D'], cubes['B'], clockwise)
    for x in range(3):
        print(''.join(cubes['U'][x]))
