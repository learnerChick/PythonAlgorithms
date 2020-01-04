def atoi(inp: str) -> int:
    min_int, max_int = (-2147483648, 2147483647)

    inp = inp.strip(' ')
    if not inp:
        return 0
    sign = ''
    if inp[0] == '-':
        sign = '-'
        inp = inp[1:len(inp)]
    elif inp[0] == '+':
        inp = inp[1:len(inp)]

    if not inp or not inp[0].isnumeric():
        return 0

    num = ''

    for ch in inp:
        if ch.isnumeric():
            num += ch
            continue
        break

    num = int(sign + num)

    if num > max_int:
        return max_int
    elif num < min_int:
        return min_int

    return num


assert atoi('-1') == -1
assert atoi('') == 0
assert atoi('+6') == 6
assert atoi('6333') == 6333
assert atoi('4193 with words') == 4193
assert atoi('words and 987"') == 0
assert atoi('-91283472332') == -2147483648
assert atoi('91283472332') == 2147483647
