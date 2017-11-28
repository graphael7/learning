import math
import pdb


def distance_points(pt_one,pt_two):
    distance = math.sqrt(math.pow(pt_two[0] - pt_one[0],2) + math.pow(pt_two[1] - pt_one[1],2))
    return distance

def closest_point(arr):
    closest_point = [100,0,0]

    while len(arr) > 2:
        testing_num = arr.pop(0)
        for num in range(0,len(arr)-1):
            # pdb.set_trace()
            distance_closest1 = distance_points(testing_num,arr[num])
            if distance_closest1 < closest_point[0]:
                closest_point = [distance_closest1, testing_num, arr[num]]


        return closest_point


points_a = [[2,3],[3,5],[6,7]]
points_b = [[2,3],[3,5],[6,7],[1,3],[5,5],[9,7]]
points_c = [[2,3],[3,5]]

print closest_point(points_a)
print distance_points([2,3],[1,3])
print distance_points([2,3],[3,5])
