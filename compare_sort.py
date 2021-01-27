my_list = [1,8,6,5,3,7,2]

new_list = []

def compareSort(my_list):
    #new_list.append(my_list[0])
    for i in range(len(my_list)):
        new_list_len = len(new_list)
        if new_list_len < 1:
            new_list.append(my_list[0])
        for k in range(len(new_list) - 1):
            if my_list[i] > new_list[k] and my_list[i] < new_list[k + 1]:
                new_list.insert(k, my_list[i])
            else:
                next



    print(my_list,new_list)

compareSort(my_list)
