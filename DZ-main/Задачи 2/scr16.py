def get_total_volume(boxes):
  total_volume = 0
  for box in boxes:
    a, b, c = box
    volume = a * b * c
    total_volume += volume
  return total_volume

boxes = [(10, 20, 30), (40, 50, 60), (70, 80, 90)] 
total_volume = get_total_volume(boxes) 
print(total_volume) 
