# task1
# def calculate_remaining_budget(expenses, income):

#     remaining_budget = income - expenses
#     return remaining_budget

# def main():
   
#     expenses = float(input("Aylıq xərcləri daxil edin: "))
#     income = float(input("Aylıq gəliri daxil edin: "))

    
#     remaining_budget = calculate_remaining_budget(expenses, income)

    
#     print("Qalan Büdcə:", remaining_budget)

# if __name__ == "__main__":
#     main()

# task2

# def calculate_bmi(weight, height):
 
#     bmi = weight / (height ** 2)
#     return bmi

# def get_bmi_category(bmi):
  
#     if bmi < 18.5:
#         return "Az çəki"
#     elif 18.5 <= bmi < 25:
#         return "Normal çəki"
#     elif 25 <= bmi < 30:
#         return "Artıq çəki"
#     else:
#         return "Piylənmə"

# def main():
   
#     weight = float(input("Kiloqramla çəki daxil edin: "))
#     height = float(input("Metrlə boy daxil edin: "))

    
#     bmi = calculate_bmi(weight, height)

    
#     bmi_category = get_bmi_category(bmi)

    
#     print("Bədən Kütləsi İndeksi (BMI): {:.2f}".format(bmi))
#     print("Kateqoriya:", bmi_category)

# if __name__ == "__main__":
#     main()


# task3
# def calculate_average(scores):
   
#     total = sum(scores)
#     average = total / len(scores)
#     return average

# def evaluate_performance(average):
 
#     if average >= 90:
#         return "Mükəmməl"
#     elif 80 <= average < 90:
#         return "Yaxşı"
#     elif 70 <= average < 80:
#         return "Orta"
#     elif 60 <= average < 70:
#         return "Kafi"
#     else:
#         return "Zəif"

# def main():
    
#     scores = []
#     num_subjects = int(input("Dərslərin sayını daxil edin: "))
#     for i in range(num_subjects):
#         score = float(input("{}. dərs üzrə xalı daxil edin: ".format(i + 1)))
#         scores.append(score)

    
#     average = calculate_average(scores)

    
#     performance = evaluate_performance(average)

    
#     print("Orta Qiymət:", average)
#     print("Fəaliyyət Qiyməti:", performance)

# if __name__ == "__main__":
#     main()

