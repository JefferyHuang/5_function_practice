
import os #作業系統(operating system)

#讀取檔案
def read_file(filename):
    products = []
    with open(filename, "r", encoding="Big5") as f:
        for line in f:
            if "商品,價格" in line:
                continue 
            name, price = line.strip().split(",")
            products.append([name, price])
    return products

#使用者輸入
def user_input(products):
    while True:
        name = input("請輸入商品名稱: ")
        if name == "q":
            break
        price = int(input("請輸入商品價格: "))
        products.append([name, price])
    print(products)
    return products

#印出購買紀錄
def print_products(products):
    for product in products:
        print(product[0], "的價格是", product[1])

#寫入檔案
def write_file(filename, products):
    with open(filename, "w", encoding = "Big5") as f:
        f.write("商品,價格\n")
        for product in products:
            f.write(product[0] + "," + str(product[1]) + "\n")

#主要執行的程式檔
def main():
    filename = "products.csv"
    if os.path.isfile(filename):
        print("Yeah~找到檔案了!")
        products = read_file(filename)
    else:
        print("此檔案不存在")

    products = user_input(products)
    print_products(products)
    write_file("products.csv", products)


main()