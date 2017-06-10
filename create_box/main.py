"""This is the entry point of the program."""


def create_box(height, width, character):
  boxstring = ""
  for _ in range(height):
    for _ in range(width):
      boxstring += character
    boxstring = boxstring + '\n'
  return boxstring


if __name__ == '__main__':
    create_box(3, 4, '*')
