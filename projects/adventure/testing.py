
# def future_path(starting_room, already_visited=set()):
#     visited = set()

#     for room in already_visited: visited.add(room)

#     path = []
#     opposite = {'n': 's', 'e': 'w', 's': 'n', 'w': 'e'}

#     def add_to_path(room, back = None):
#         visited.add(room)
#         exits = room.get_exits()
#         for direction in exits:
#             if room.get_room_in_direction(direction) not in visited:
#                 path.append(direction)
#                 add_to_path(room.get_room_in_direction(direction), opposite[direction])
#         if back: path.append(back)

#     add_to_path(starting_room)

#     return path

# def new_path(starting_room, visited=set()):
#     path = []
#     opposite = {'n': 's', 'e': 'w', 's': 'n', 'w': 'e'}

#     def add_to_path(room, back=None):
#         visited.add(room)
#         exits = room.get_exits()
#         path_lengths = {}
#         for direction in exits:
#             path_lengths[direction] = len(future_path(room.get_room_in_direction(direction), visited))
#         traverse_order = []
#         for key, _ in sorted(path_lengths.items(), key=lambda x: x[1]): traverse_order.append(key)
#         for direction in traverse_order:
#             if room.get_room_in_direction(direction) not in visited:
#                 path.append(direction)
#                 add_to_path(room.get_room_in_direction(direction), opposite[direction])
#         if len(visited) == len(world.rooms): return
#         elif back: path.append(back)
#     add_to_path(starting_room)
#     return path
    
# traversal_path = new_path(world.starting_room)