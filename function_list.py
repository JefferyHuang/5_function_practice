
s = list()
number = int(input("請輸入數字(按-1即結束): "))
while number != -1 :
    s.append(number)
    number = int(input("請輸入數字(按-1即結束): "))

def sum_of_list(s):
    result = sum(s)
    print(result)
    

sum_of_list(s)
