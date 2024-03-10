# 1

# numbers = [1, 2, 3, 4, 5]


# total = sum(numbers)


# print("Toplam:", total)

# import functools
# import operator


# numbers = [1, 2, 3, 4, 5]


# product = functools.reduce(operator.mul, numbers)


# print("Hasil:", product)

# 2


# numbers = [1, 2, 3, 4, 5]


# numbers.reverse()


# print("Sağdan sola:", numbers)

# 3


# list1 = [1, 2, 3]
# list2 = ['a', 'b', 'c']


# merged_list = list(zip(list1, list2))


# print( merged_list)

# 4


# list = [[1, 2], [3, 4], [5, 6]]


# list[2][1] = '99'


# print(":", list)

# 5


# my_list = [10, 20, 30, 40, 50]


# value_to_find = 30
# index_of_value = my_list.index(value_to_find)


# new_value = 35
# my_list.insert(index_of_value + 1, new_value)


# print(my_list)

# 6


# numbers = [10, 20, 30, 40, 50]


# average = sum(numbers) / len(numbers)


# print(average)

# 8


# list1 = [1, 2, 2, 3, 4, 4, 5]


# list2 = list(set(list1))


# print( list1)
# print( list2)

# 9

# from itertools import permutations


# numbers = [1, 2, 3]


# combinations = list(permutations(numbers))


# for combo in combinations:
#     print(combo)

# 10

# a = {'ad': ['Rashford', 'Bruno', 'Dalot']}

# def menu():
#     secim = input("Seçim Edin: (1) Əlavə et (2) Sil\n")
#     if secim == '1':
#         yeni_ad = input("Əlavə ediləcək adı daxil edin: ")
#         if yeni_ad:
#             a['ad'].append(yeni_ad)
#             print(f"{yeni_ad} adı əlavə edildi.")
#         else:
#             print("Ad daxil etmədiniz.")
#     elif secim == '2':
#         silinecek_ad = input("Silinecək adı daxil edin: ")
#         if silinecek_ad in a['ad']:
#             a['ad'].remove(silinecek_ad)
#             print(f"{silinecek_ad} adı silindi.")
#         else:
#             print("Bu ad bazada yoxdur.")
#     else:
#         print("Yanlış seçim etdiniz.")


# menu()


# 11

# def virtual_printer(soz, say):
#     for i in range(1, say + 1):
#         print(f"{i} {soz}")


# daxil_edilen_soz = "Java"
# daxil_edilen_say = 6


# virtual_printer(daxil_edilen_soz, daxil_edilen_say)






