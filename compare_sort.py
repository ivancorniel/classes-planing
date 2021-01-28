#  The function returns a python list of all items sorted in a ascending order.
#  The function takes a python list, a tuple, with at least 2 items to sort.
#  For objects with less than 2 items passed as the argument, a "not subscriptable" error is arised.
#  Repeated items are grouped between the next numbers lower and next number higher than them.
#  For objects with a text passed as the argument, a lexicographical comparison is performed on the characters of the string
#  For objects with multiple texts passed as the argument, a lexicographical comparison is performed on the items in the object
#  For objects with different types items passed as the argument, a "not supported" errot is arised

def compareSort(unsortEd):
    sortEd = [unsortEd[0],unsortEd[1]]

    if sortEd[1] < sortEd[0]: #  Sort first 2 initialized items
        sortEd.insert(0,sortEd[1])
        sortEd.pop(2)
    for i in range(2, len(unsortEd), 1): #  Loop through unsorted list
        for k in range(len(sortEd)): #  Loop through new created sorted list
            if unsortEd[i] < sortEd[k]:
                sortEd.insert(k, unsortEd[i]) #  Insert unsorted item in the sorted list
                break
        else:
            sortEd.append(unsortEd[i]) #  Add unsorted item to the end of the sorted list if a greater item not found
    return sortEd
