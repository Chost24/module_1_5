immutable_var = 1, True, 'string'
print(immutable_var)
#immutable_var[0] = 2 особенность кортежа является в том, что он сам по себе не изменяем
mutable_list = [1, False, 'mushroom']
mutable_list[1] = True
print(mutable_list)