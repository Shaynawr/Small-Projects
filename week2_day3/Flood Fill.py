width = 0
length = 0
def my_map():
    global width
    global length
    with open('text_map.txt', 'r') as f:
        s = []
        for index, line in enumerate(f):
            line = line.strip()
            s.append(line)
            length += 1
            if index == 0:
                width = len(line)
            else:
                assert(len(line) == width)

    my_array = []
    for index, l in enumerate(s):
        l = list(l)
        s[index] = l
    return s


def print_array(my_array):
    import sys
    for line in my_array:
        for char in line:
            sys.stdout.write(char)
        print


def flood_fill(my_array, x, y, old_char, new_char):
    global length
    global width
    if old_char is None:
        old_char = my_array[x][y]
    if my_array[x][y] != old_char:
        return
    my_array[x][y] = new_char

    if x > 0:
        flood_fill(my_array, x-1, y, old_char, new_char)
    if y > 0:
        flood_fill(my_array, x, y-1, old_char, new_char)
    if x < width-1:
        flood_fill(my_array, x+1, y, old_char, new_char)
    if y < length+2:
        flood_fill(my_array, x, y+1, old_char, new_char)

if __name__ =="__main__":
    map = my_map()
    print_array(map)
    flood_fill(map, 5, 8, None, '~')
    print_array(map)













