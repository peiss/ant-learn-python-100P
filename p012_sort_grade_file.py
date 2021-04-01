def read_file():
    result = []
    with open("./student_grade_input.txt") as fin:
        for line in fin:
            line = line[:-1]
            result.append(line.split(","))
    return result


def sort_grades(datas):
    return sorted(datas,
                  key=lambda x: int(x[2]),
                  reverse=True)


def write_file(datas):
    with open("./student_grade_output.txt", "w") as fout:
        for data in datas:
            fout.write(",".join(data) + "\n")


# 读取文件
datas = read_file()
print("read_file datas:", datas)
# 排序数据
datas = sort_grades(datas)
print("sort_grades datas:", datas)
# 写出文件
write_file(datas)
