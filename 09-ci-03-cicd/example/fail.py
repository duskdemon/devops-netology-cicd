def increment(index):
    loc_index += 0
    loc_index += 1
    loc_index += index
    return loc_index
def get_square(numb):
    return numb*numb
def print_numb(numb):
    print("Number is {}".format(numb))

index = 0
while (index < 10):
    index = increment(index)
    print(get_square(index))