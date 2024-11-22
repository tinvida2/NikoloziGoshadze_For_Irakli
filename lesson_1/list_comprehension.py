#  1) 1-დან 10-ის ჩათვლით ყველა რიცხვის კვადრატი

# result_list = [i**2 for i in range(1,11)]

# print(result_list)

# 2) 10 ცალი მსგავსი ელემენტის შექმნა

# result_list = [1 for _ in range(1,11)]

# print(result_list)

# 3) ნაშთის პოვნა თითოეული ელემენტის 3-ზე გაყოფისას

# lst = [6,13,45,24,80,76]

# result_list = [i%3 for i in lst]

# print(result_list)

# 4) მომხარებლის მიერ შემოტანილი რიცხვების მასივის ელემენტებად ქცევა

# numbers = input("Please enter the numbers: ")

# result_list = [int(i) for i in numbers.split(" ")]

# print(result_list)

# 5) სტრინგის ყველა ელემენტის სათითაოდ დაბეჭდვა

# str = "nikolozi"

# result_list = [i for i in str]

# print(result_list)

# 6) სტრინგის ყველა ელემენტის capitilize ება

# str = "nikolozi"

# result_list = [i.upper() for i in str]

# print(result_list)

# 7) 1-დან n-მდე 3 ისა და 2 ის ყველა ჯერადი რიცხვი

# n = 100

# result_list = [i for i in range(1,n+1) if i%3 == 0 and i%2 == 0]

# print(result_list)


# 8) ისეთი სტრინგების გადიდება რომელთა სიგრძეც n-ს აღემატება

# n = 6

# lst = ["berlini", "parizi", "londoni", "xashuri"]

# result_list = [i.capitalize() for i in lst if len(i)>6]

# print(result_list)

# 9) ლუწ-კენტობის გარკვევა

# lst = [12,52,23,65,24,20]

# result_list = ["even" if i%2 == 0 else "odd" for i in lst]

# print(result_list)

# 10) ელემენტების დაწყვილება

# lst1 = [1,5,8,10]

# lst2 = [2,4,6,9]

# result_list = [(i,x) for i in lst1 for x in lst2]

# print(result_list)

# 11) დანესტილი მასივის გახსნა

# lst = [[1,2],[2,3,4],[5,6,7,8]]

# result_list = [i for comb_elem in lst for i in comb_elem]

# print(result_list)