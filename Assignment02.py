# guess_me = 7
# start = 1
# while True:
#     if start < guess_me:
#         print('too low')
#     elif start == guess_me:
#         print('Found it!')
#         break
#     else:
#         print('Error')
#         break
#     start +=1
# for value in [3,2,1,0] :
#     print(value)
#
#
# def callGood() :
#     return ['Herry','Ron','Hermione']
#
# print(callGood())

# def get_odds():
#     for number in range(1, 10, 2):
#         yield number
#
# for count, number in enumerate(get_odds(), 1):
#     print(number)

titles = ['Creature of Habit', 'Crewel Fate']
plots = ['A nun turns into a monster', 'A haunted yarn shop']
movies = dict(zip(titles, plots))
print(movies)
