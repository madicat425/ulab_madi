
#radii_temp_module.py

radii = [1.2, 0.8, 1.5, 2.0, 1.0, 0.6]
temperatures = [300, 400, 350, 280, 500, 450] # Kelvin

#find planets w temps below 350 K
def find_planets(temperatures, radii):
    filtered_radii = []
    for i in range(len(temperatures)):
        if temperatures[i] < 350:
            filtered_radii.append(radii[i])
    return filtered_radii
    
result = find_planets(temperatures, radii)       
print(result)