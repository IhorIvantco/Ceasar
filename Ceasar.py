Language = 'АБВГҐДЕЄЖЗИІЇЙКЛМНОПРСТУФХЦЧШЩЬЮЯГҐДЕЄЖЗИІЇЙКЛМНОПРСТУФХЦЧШЩЬЮЯАБВ ABCDEFGHIGKLMNOPQRSTUVWXYZDEFGHIGKLMNOPQRSTUVWXYZABC абвгґдеєжзиіїйклмнопрстуфхцчшщьюягґдеєжзиіїйклмнопрстуфхцчшщьюяабв abcdefghigklmnopqrstuvwxyzdefghigklmnopqrstuvwxyzabc'
Tps = 23
while True:
    message = input("Print your words")
    result = ''
    for i in message:
        mr = Language.find(i)
        new_mr = mr + Tps
        if i in Language:
            result += Language[new_mr]
        else:
            result += i
    print(result)