#1-misol
my_tuple = ("a", "b", "c", "d")

result = tuple((i, my_tuple[i]) for i in range(len(my_tuple)))
print(result)

#2-misol
my_tuple = ("apple", "banana", "ok")

result = tuple(word[::-1] for word in my_tuple)
print(result)

#3-misol
my_dict = {"a": "1", "b": "2"}

result = {value: key for key, value in my_dict.items()}
print(result)

#4-misol
animals = {"it": "vov", "mushuk": "miyov", "sigir": "muu"}

animal = input("Hayvon kiriting: ")

if animal in animals:
    print(animals[animal])
else:
    print("Bunday hayvon bazada yo'q")



