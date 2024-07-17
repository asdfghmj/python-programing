def swapPositions(list, pos1, pos2):
  list[pos1], list[pos2] = list[pos2], list[pos1]
  return list

#taking input from the user
List = [23, 65, 19, 90]
#taking multiple inputs at a time separated by comma
pos1, pos2  = [int(x) for x in input("Enter two values: ").split(",")]
print(swapPositions(List, pos1-1, pos2-1))
