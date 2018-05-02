favourites = []
quit = input('Do you want to quit? yes or no ')
while quit == 'no':
    movies = input('What is one of your favourite movies?: ')
    quit = input('Do you want to quit? yes or no ')
    favourites.append(movies)
print('Thank you!')
print('This is how many favourite movies you added: ')
movies = len(favourites)
print(len(favourites))
