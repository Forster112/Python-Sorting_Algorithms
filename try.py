# for reference
array_2d = [
   [1, 2, 3, 4],
   [5, 6, 7, 8],
   [9, 0, 10, 11],
   [1, 2, 4, 5]
]
hour_glass = []
for row in range(2):
      for col in range(2):
         sum = 0
         sum += array_2d[row][col]
         sum += array_2d[row][col + 1]
         sum += array_2d[row][col + 2]
         sum += array_2d[row + 1][col + 1]
         sum += array_2d[row + 2][col]
         sum += array_2d[row + 2][col + 1]
         sum += array_2d[row + 2][col + 2]
         hour_glass.append(sum)
         sum = 0
print(hour_glass)
print(max(hour_glass))
