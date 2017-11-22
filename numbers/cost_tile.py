import math

get_tile_cost = float(raw_input("What is the cost per tile?"))
get_tile_width = float(raw_input("What is the width of the tile?"))
get_tile_length = float(raw_input("What is the length of the tile?"))

print("The size of the room is 600sq ft")


number_of_tiles = 600/(get_tile_width * get_tile_length)
total_cost_for_room = number_of_tiles * get_tile_cost

print "This is the total cost: " + str(total_cost_for_room)
