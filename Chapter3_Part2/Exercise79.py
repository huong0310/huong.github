import random

max_value = 0
update_count = 0

for _ in range(100):
    random_integer = random.randint(1, 100)
    print(random_integer, end=' ')

    # Kiểm tra xem số hiện tại có lớn hơn số tối đa không
    if random_integer > max_value:
        max_value = random_integer
        update_count += 1
        print("<== Update")
    else:
        print()
        
print("The maximum value fount was:", max_value)
print("The maximum value was updated", update_count,"times")
