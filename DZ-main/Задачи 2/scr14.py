def get_mass(r, h):
  import math
  V = math.pi * r**2 * h
  rho = 1000
  m = rho * V
  m = round(m, 2)
  return m

r = 0.1 
h = 0.5 
m = get_mass(r, h) 
print(m) 
