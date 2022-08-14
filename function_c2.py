def read_file(filename):
    lines = []
    with open(filename, "r", encoding= "utf-8") as f:
        for line in f:
            lines.append(line.strip())
    return lines

def convert(lines):
    person = None
    jefferyHuang_count = 0
    jeffery_sticker_count = 0
    jeffery_image_count = 0
    sheng_count = 0
    sheng_sticker_count = 0
    sheng_image_count = 0
    for line in lines:
        s = line.split(" ")
        time = s[0]
        name = s[1]
        if name == "Jeffery":
            if s[3] == "貼圖":
                jeffery_sticker_count += 1
            elif s[3] == "圖片":
                jeffery_image_count += 1
            else: 
                for m in s[3:]:
                    jefferyHuang_count += len(m)
        elif name =="Sheng":
            if s[2] == "貼圖":
                sheng_sticker_count += 1
            elif s[2] == "圖片":
                sheng_image_count += 1
            else: 
                for m in s[2:]:
                    sheng_count += len(m)
    print("Jeffery說了", jefferyHuang_count, "個字")
    print("Jeffery傳了", jeffery_sticker_count, "個貼圖")
    print("Jeffery傳了", jeffery_image_count, "個圖片")
    print("Sheng說了", sheng_count, "個字")
    print("Sheng傳了", sheng_sticker_count, "個貼圖")
    print("Sheng傳了", sheng_image_count, "個圖片")


            
def write_file(filename, lines):
    with open(filename, "w", encoding= "utf-8") as f:
        for line in lines:
            f.write(line + "\n")

def main():
    lines = read_file("[LINE]Sheng.txt")
    lines = convert(lines)
    # write_file("output.txt", lines)

main()