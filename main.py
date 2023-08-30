# def print_op(show_list):
#     for key in show_list:
#         print(f"{key} - {show_list[key]}")
def print_op(list_value):
    if len(list_value) < 3:
        print(list_value, end=" ")
        temp = list_value.copy()
    else:
        print(list_value[0:2], end=" ")
        temp = list_value[0:2].copy()
    return temp








dict1 = {"aaa":["bww","cq","d2","h11"], "bbbb":["e","r","t"]}
show(dict1)