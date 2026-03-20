def say_tek(my_list):
    tek_ededler=[]

    for i in my_list:
        if i%2 !=0:
            tek_ededler.append(i)

    return len(tek_ededler)


print(say_tek([23,11,65,78,90]))