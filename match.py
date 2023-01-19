data = [
  [23, 11, 5, 14],
  [8, 32, 20, 5]
]
percent = 0
color = input()
#your code goes here
match color:
  case "brown":
    percent = int(data[0][0]+data[1][0])
  case "blue":
    percent = int(data[0][1]+data[1][1])
  case "green":
    percent = int(data[0][2]+data[1][2])
  case "black":
    percent = int(data[0][3]+data[1][3])

print(percent)
