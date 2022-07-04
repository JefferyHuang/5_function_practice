
s = int(input("請輸入要查詢的年份: "))
def year(s):
    if s % 4 != 0:
        print("平年")
    elif s % 100 != 0:
        print("閏年")
    elif s % 400 != 0:
        print("平年")
    elif s % 3200 != 0:
        print("閏年")

year(s)