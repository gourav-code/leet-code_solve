import math
def find_max_volume(perimeter, area):
    l = (perimeter-math.sqrt((perimeter*perimeter)-(24*area)))/12
    v = ((l*area)/2)-(((l*l)*perimeter)/4)+(l*l*l)
    return round(v,2)

# Example values
P = 20  # Example perimeter
A = 5  # Example surface area

max_volume = find_max_volume(P, A)
print(f"Maximum volume: {max_volume:.2f}")
