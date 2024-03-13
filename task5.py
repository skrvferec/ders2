# task1


# height = float(input("Zəhmət olmasa, boyunuzu daxil edin: "))


# if height < 150:
#     print("Boyunuz çox aşağıdır")
# elif 150 <= boy < 170:
#     print("Boyunuz normaldır. ")
# else:
#     print("Boyunuz çox yüksəkdir. ")

# task2


# basket = []


# tax = 0.18


# cupon = 0


# for _ in range(5):
#     product_name = input("Məhsul adını daxil edin: ")
#     product_price = float(input("Məhsulun qiymətini daxil edin (AZN): "))
    
   
#     basket.append((product_name, product_price))
    

# general_value = sum(product_name for _, product_name in basket)


# tax_sum = general_value * tax


# umumi_dəyər_ədv_daxil = general_value + tax_sum


# if general_value > 100:
#     cupon = 15
# elif general_value > 50:
#     cupon = 10


# if cupon > 0:
#     print(f" {cupon} AZN-lıq kupon qazandınız!")
# else:
#     print("Kupon qazanmadınız. ")


# print(f"Səbətdəki məhsullar: {basket}")
# print(f"Ümumi dəyər (ədv daxil): {general_value:.2f} AZN")

# task3


# distance_km = float(input("Səyahət məsafəsini kilometrlə daxil edin: "))
# vehicle = input("Nəqliyyat vasitəsinin növünü daxil edin (avtomobil/yük maşını/avtobus): ")


# if vehicle.lower() == "avtomobil":
#     price_km = 0.50
# elif vehicle.lower() == "yük maşını":
#     price_km = 1.00
# elif vehicle.lower() == "avtobus":
#     price_km = 2.00
# else:
#     print("Yanlış nəqliyyat növü daxil edildi. Zəhmət olmasa avtomobil, yük maşını və ya avtobus seçin.")
#     exit()


# general_value = distance_km * price_km


# print(f"Səyahətin ümumi dəyəri: {general_value:.2f} dollar")


