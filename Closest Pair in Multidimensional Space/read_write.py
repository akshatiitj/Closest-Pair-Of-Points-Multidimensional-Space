# -*- coding: utf-8 -*-

def read_file():
    input_file = open("input.txt", "r")
    points = []
    points = input_file.read().split(' ')
    #Removing the extra element at the end    
    points.pop(4000000)
    #Forming 1,000,000 numbers in 4 dimensions for collection of points
    rand_4 = []
    count = 1
    collection = []
    for item in points:
        rand_4.append(int(item))
        if count % 4 == 0:
            collection.append(rand_4)
            rand_4 = []    
        count+=1
    #Print collection of points to a text file
    collection_file = open("collection.txt", "w")
    collection_file.write("%s" % collection)
    collection_file.close(), input_file.close()
    return collection

def write_file(answer, pair_1, pair_2):
    text_file = open("output.txt", "w")
    text_file.write("Minimum distance = %s\n" % answer)
    text_file.write("First Pair  = %s\n" %pair_1)
    text_file.write("Second Pair = %s" %pair_2)
    text_file.close()
