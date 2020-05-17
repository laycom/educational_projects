# На вход подается строка содержащее выражение, необходимо определить 
# правильность расстановки скобок различного вида ( {}, (), [] )


test_list = [
    '(([((a+ {b + c - [e * g]}))]))',
    '{{[[mkrkj]]})',
    '()',
    '',
    '}',
    '(',
    '{}{}{}',
    '{a + b * (c - a})',
]

def is_valid(test_str):
    turn = []
    bracket_pair = {
        ')': '(',
        ']': '[',
        '}': '{',
    }
    open_pair = ['(', '[', '{']
    close_pair = [')', ']', '}']
    for symbol in test_str:
        if len(turn) == 0 and (symbol == ')' or symbol == ']' or symbol == '}'):
            return 'not valid'
        if symbol in open_pair:
            turn.append(symbol)
        if symbol in close_pair:
            if len(turn) > 0:
                if bracket_pair[symbol] != turn.pop():
                    return 'not valid'
    if len(turn) == 0:
        return 'valid'
    else:
        return 'not valid'


for test_str in test_list:
    print(test_str, is_valid(test_str))


