def max_list(my_list):
    en_boyuk = my_list[0]

    for i in my_list:
        if i > en_boyuk:
            en_boyuk = i

    return en_boyuk

print(max_list([23,98,1,45,67,23]))