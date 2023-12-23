def get_distance(points):
  x_a = points["a"]["x"]
  y_a = points["a"]["y"]
  x_b = points["b"]["x"]
  y_b = points["b"]["y"]
  distance = ((x_b - x_a)**2 + (y_b - y_a)**2)**0.5
  distance = round(distance, 3)
  return distance

points = {"a": {"x": 1, "y": 2}, "b": {"x": 4, "y": 6}} 
distance = get_distance(points) 
print(distance) 
