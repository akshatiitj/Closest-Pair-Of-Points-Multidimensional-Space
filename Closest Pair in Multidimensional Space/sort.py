# -*- coding: utf-8 -*-

#Use Quicksort to sort given collection by desired coordinate
def partition(alist, i):
    count = 0
    li = []    
    mid_pos = (len(alist)+1)//2
    mid_element = alist[mid_pos-1]
    if alist[0][i] < mid_element[i] < alist[-1][i] \
    or alist[-1][i] < mid_element[i] < alist[0][i]:
        alist[0], alist[mid_pos-1] = alist[mid_pos-1], alist[0]
    if alist[0][i] < alist[-1][i] < mid_element[i] \
    or mid_element[i] < alist[-1][i] < alist[0][i]:
        alist[0], alist[-1] = alist[-1], alist[0]
    start = 0
    pivot = alist[start]
    pindex = start+1
    for j in range(start+1, len(alist)):
        count = count + 1
        if alist[j][i] < pivot[i]:
            alist[j], alist[pindex] = alist[pindex], alist[j]
            pindex += 1
    li.append(count)
    alist[start], alist[pindex-1] = alist[pindex-1], alist[start]
    return alist[:pindex], alist[pindex:]

def quicksort(alist, i):
    start = 0
    end = len(alist)-1
    if start<end:
        left, right = partition(alist, i)
        return quicksort( left[:-1], i) + \
               quicksort([left[-1]], i) + \
               quicksort(right, i)
    else:
        return alist