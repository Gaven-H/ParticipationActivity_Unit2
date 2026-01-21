name = "Gaven H"

name_with_spaces = "     " + name + "     "

print(f"{name_with_spaces.lower()}")

print(f"{name_with_spaces.upper()}")

print(f"{name_with_spaces.title()}")

width = 15

print(f"{name_with_spaces.center(width, "_").ljust(width, "_")}")

print(f"{name_with_spaces.rjust(width, "_")}")

print(f"{name_with_spaces.center(width, "_")}")