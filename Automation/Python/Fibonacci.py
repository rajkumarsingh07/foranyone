input_count = int(input("Enter the input count:" ))
a,b = 0,1
count = 0
print("Fibonacci Series")
while count < input_count:
    print(a)
    feb_sum = a + b
    a = b
    b = feb_sum
    count += 1
