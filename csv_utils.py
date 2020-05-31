# @author zhangchao
# @date 2020/5/30 14:18
import csv


def read_contents(file_path,codec="utf-8"):
    contents = []
    with open(file_path, newline='\n', encoding=codec) as csv_file:
        rows = csv.reader(csv_file)
        for i, row in enumerate(rows):
            if i == 0:
                continue
            contents.append(row)
    return contents


def update_item(file_path, item_list):
    head = ['URL', 'STATUS']
    write_head = True
    with open(file_path, 'w+', encoding='utf-8', newline='') as f:  # 1. 创建文件对象
        csv_writer = csv.writer(f)       # 2. 基于文件对象构建 csv写入对象
        if write_head:                   # 3. 构建列表头
            csv_writer.writerow(head)
        csv_writer.writerows(item_list)   # 4. 写入csv文件内容
    pass


if __name__ == '__main__':

    print(read_contents("comments.csv",codec="gbk"))
    pass