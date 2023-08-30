
def print_op(list_value):
    if len(list_value) < 3:
        print(list_value, end=" ")
        temp = list_value.copy()
    else:
        print(list_value[0:3], end=" ")
        temp = list_value[0:3].copy()
    print()


def get_list(list_value):
    if len(list_value) < 3:
        temp = list_value.copy()
    else:
        temp = list_value[0:3].copy()
    return temp
def question(thisdict):
    for name in thisdict:
        print_op(thisdict[name])
        user_input = input()
        # func
        flag = True
        sym = get_list(thisdict[name])
        if flag:
            sym.remove(user_input)




question({"aaa":["21","121"], "bbbb":["111","222","333","444"]})




