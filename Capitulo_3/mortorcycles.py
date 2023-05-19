motorcycles = ['honda', 'yamaha', 'suzuki', 'ducatti']
print(motorcycles)

# motorcycles.append('ducatti')
# motorcycles.insert(0, 'ducatti')
# del motorcycles[0]

# popped_motorcycle = motorcycles.pop(1)
# print(popped_motorcycle)
# print("Tha last motorcycle I owned was a " + popped_motorcycle.title())

too_expensive = 'ducatti'
motorcycles.remove(too_expensive)
print("\nA " + too_expensive.title() + " is too expensive for me.")

print(motorcycles)
