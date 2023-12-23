
def make_points(x_array, y_array):
  if len(x_array) != len(y_array):
    return []
  points = []
  for i in range(len(x_array)):
    point = (x_array[i], y_array[i])
    points.append(point)
  return points

x_array = [1, 2, 3, 4, 5]
y_array = [6, 7, 8, 9, 10]

points = make_points(x_array, y_array)
print(points)
