numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO заменить значение пропущенного элемента средним арифметическим

len_ = len(numbers)
sum_ = sum(filter(None, numbers))
#for_sum =  numbers.remove[4]
#sum_ = sum(for_sum)
#numbers[4] = sum_ / len_
numbers[4] = sum_ / len_
print("Измененный список:", numbers)
#print(sum_)

