numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

sum1 = sum(numbers[0:4])
sum2 = sum(numbers[5:])
sum_ = sum1 + sum2
len_ = len(numbers)
sr = sum_ / len_

wrong = numbers[4]
truth = round(sr, 2)
numbers[4] = truth

print("Измененный список:", numbers)
