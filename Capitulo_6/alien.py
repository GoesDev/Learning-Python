# alien_0 = {'color': 'green', 'points': 5}
# new_points = alien_0['points']
# print(f"You judy earned {new_points} points!")

# print(alien_0)
# alien_0['x_position'] = 0
# alien_0['y_position'] = 25

# print(alien_0)

alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print(f"Original x-position: {alien_0['x_position']}")

if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3

alien_0['x_position'] += x_increment
print(f"New position: {alien_0['x_position']}")
