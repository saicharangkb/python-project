# s=[1,2,-5,6]
# print([x*2 for x in s])
# vec = [-4, -2, 0, 2, 4]

# print([x*2 for x in vec])


# print([x for x in vec if x >= 0])


# print([abs(x) for x in vec])
# # call a method on each element
# freshfruit = ['  banana', '  loganberry ', 'passion fruit  ']
# print([we.strip() for we in freshfruit])
#print(freshfruit.strip())

# # create a list of 2-tuples like (number, square)
print([(x, x**2) for x in range(6)])


# vec = [[1,2,3], [4,5,6], [7,8,9]]
# print([num for elem in vec for num in elem])
# #[1, 2, 3, 4, 5, 6, 7, 8, 9]
#print(vec)


# from math import pi
# print([str(round(pi, i)) for i in range(1, 6)])