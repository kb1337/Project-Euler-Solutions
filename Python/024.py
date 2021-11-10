from itertools import permutations

my_list = list(permutations('0123456789'))
my_list = [''.join(number) for number in my_list]
print(my_list[999999])
