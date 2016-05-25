# -*- coding: utf-8 -*-

import math
import sort
import read_write

def distance(num1, num2):
    return math.sqrt((num1[0] - num2[0])**2 + (num1[1] - num2[1])**2 + \
                     (num1[2] - num2[2])**2 + (num1[3] - num2[3])**2)

glob_min = 9999999         #For comparing minimum distance globally
pair_1, pair_2 = [],[]     #To store closest pair of points
def find_min(collection):
    global glob_min, pair_1, pair_2
    #Sort points according to 1st coordinate
    collection = sort.quicksort(collection, 0)
    if len(collection) == 1:
        return 99999999
    elif len(collection) == 2:
        if distance(collection[0], collection[1]) < glob_min:
            glob_min = distance(collection[0], collection[1])
            pair_1 = collection[0]
            pair_2 = collection[1]
        return distance(collection[0], collection[1])
    else:
        #Divide points in 2 parts
        vertical_line = collection[len(collection)//2][0]
        min_distance = min(find_min(collection[:len(collection)//2]), \
                           find_min(collection[len(collection)//2:]))
        #Conquer the 2 divided parts
        strip = []
        for element in collection:
            if vertical_line - min_distance < element[0] < vertical_line:
                strip.append(element)
            elif vertical_line <= element[0] < vertical_line + min_distance:
                strip.append(element)
        #Sort strip by 2nd co-ordinate
        strip = sort.quicksort(strip, 1)
        """2 loops with time complexity O(n) and O(1) to find closest points in
        the given strip[]. Since the strip is sorted according to 2nd coordinate,
        all points have an upper bound on min_distance with other points.
        It can be proven geometrically that the maximum number of points outside
        min_distance of a given point in a strip will be:
        -> 8 for 2 dimension (outside a circle of radius min_distance)
        -> 43 for 3 dimension (outside a sphere of radius min_distance)
        -> 198 for 4 dimension (outside a hyper sphere of radius min_distance)
        Hence the inner loop will run for 198 times.        
        For proof on the reasoning , visit the link below:
        "http://euro.ecom.cmu.edu/people/faculty/mshamos/1976ShamosBentley.pdf".."""
        for i in range(len(strip)):
            if(i+198 < len(strip)):
                for j in range(i+1, i+198):
                    if  strip[j][1] - min_distance < strip[i][1] <= strip[j][1] + min_distance \
                    and strip[j][2] - min_distance < strip[i][2] <= strip[j][2] + min_distance \
                    and strip[j][3] - min_distance < strip[i][3] <= strip[j][3] + min_distance \
                    and distance(strip[i], strip[j]) < min_distance:
                        min_distance = distance(strip[i], strip[j])
                        if distance(strip[i], strip[j]) < glob_min:
                            glob_min = distance(strip[i], strip[j])
                            pair_1 = strip[i]
                            pair_2 = strip[j]
            else:
                for j in range(i+1, len(strip)):
                    if  strip[j][1] - min_distance < strip[i][1] <= strip[j][1] + min_distance \
                    and strip[j][2] - min_distance < strip[i][2] <= strip[j][2] + min_distance \
                    and strip[j][3] - min_distance < strip[i][3] <= strip[j][3] + min_distance \
                    and distance(strip[i], strip[j]) < min_distance:
                        min_distance = distance(strip[i], strip[j])
                        if distance(strip[i], strip[j]) < glob_min:
                            glob_min = distance(strip[i], strip[j])
                            pair_1 = strip[i]
                            pair_2 = strip[j]
        return min_distance

#Read input and write input to exterior file
collection = read_write.read_file()
minimum_distance = find_min(collection)
read_write.write_file(minimum_distance, pair_1, pair_2)