f = open('input4.yaml', 'r')
s = "" # здесь будет результат
depth = 0 # текущий уровень вложенности
prev_depth = -1 # уровень вложенности предыдущей строки

def join_list(value):
    value = '{"' + value[value.find("- ") + 2:-2] + '":['
    return value

def join_string(value):
    value = '{"' + value[value.find('- ') + 2:-1] + '}'
    value = value.replace(':', '":', 1)
    return value

def close_depth(depth):
    s = ""
    while depth > 0:
        s += "]}"
        depth -= 4
    return s

for i in f.readlines():
    if i[0] == "#": continue  # комментарии пропускам
    new_depth = i[:i.find('- ')].count(" ") # сохраняем глубину вложенности
    if new_depth > prev_depth: # если вложенность увеличилась
        if i[-2] == ":": s += join_list(i)
        else: s += join_string(i)
    elif new_depth == prev_depth: # если вложенность не изменилась
        s += "," # значит, предыдущая строка - элемент того же списка, что и эта
        if i[-2] == ":": s += join_list(i)
        else: s += join_string(i)
    else: # если вложенность уменьшилась
        s += close_depth(prev_depth - new_depth) + ',' # закрываем все списки с большей вложенностью, чем текущая строка
        if i[-2] == ":": s += join_list(i)
        else: s += join_string(i)

    prev_depth = new_depth

s += close_depth(prev_depth)
f = open('output4.json', 'w')
f.write(s)
print(s)

