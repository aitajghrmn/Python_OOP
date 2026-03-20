def say_cut(my_list):
    cut_ededler = []

    for i in my_list:
        if i % 2 == 0:
            cut_ededler.append(i)

    return len(cut_ededler)

print(say_cut([1,2,3,4,6]))