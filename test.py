def display(width, height, x, y):
    """Prints the rectangle using '#'."""
    if width == 0 or height == 0:
        print("")
        return

    [print("") for y in range(y)]
    for h in range(height):
        [print(" ", end='') for x in range(x)]
        [print("#", end='') for w in range(width)]
        print("")
    
display(2, 3, 2, 2)