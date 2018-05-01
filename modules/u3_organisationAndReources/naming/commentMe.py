#display a welcome message
print('Welcome to the Circle Calculator!')

#ask the user for a radius
r = input('Enter a radius: ')
r = int(r)

#calculate the area of the circle and print
area = 3.14 * r * r
print('The area is', area)

#calculate the perimeter of the circle and print
perimeter = 3.14 * r * 2
print('The perimeter is', perimeter)
