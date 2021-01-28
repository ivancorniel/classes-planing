def compareSort(unsorted):
    sort = [unsorted[0],unsorted[1]]
    for i in range(2, len(unsorted), 1):
        for k in range(len(sort)):
            if unsorted[i] < sort[k]:
                sort.insert(k, unsorted[i])
                break
        else:
            sort.append(unsorted[i])
    print(unsorted, sort)

lst = [6,5,8,4,3,25,48,35]

compareSort(lst)
