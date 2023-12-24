import tkinter as tk
import base64
import os
from spam_filter import get_result
from get_content.main import get_content
import subprocess
import csv
from tkinter import messagebox
# 设置是否记录的标志 1表示记录 0表示不记录
remind_passwd = 1
def center_window(window, width, height):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    x = (screen_width - width) // 2
    y = (screen_height - height) // 2

    window.geometry(f'{width}x{height}+{x}+{y}')
def evaluation():
    username = jaccount_entry.get()
    passwd = passwd_entry.get()
    username = username.strip()
    passwd = passwd.strip()
    print(username)
    print(passwd)
    # 开始爬取获得结果
    get_content(username, passwd)
    # cnn生成文件
    subprocess.run('./cnn.bat',shell=True)
    # 获取result
    targets = get_result()
    print(targets)
    titles = []
    with open('mail_content.csv', newline='', encoding='utf-8') as csvfile:
        csv_reader = csv.reader(csvfile)
        # 逐行读取数据
        # 逐行读取第一列的值
        first_column_values = [row[0] for row in csv_reader]
        for target in targets:
            titles.append(first_column_values[target + 1])
    # 将列表转换为字符串
    titles_str = ", ".join(titles)
    # 在消息框中显示标题
    messagebox.showinfo("提示", f"我们检测到可能被错误放置的垃圾邮件为: {titles_str}")

def on_checkbox_click():
    global remind_passwd
    # 获取勾选框的状态
    checked = checkbox_var.get()

    # 根据勾选框的状态进行相应的操作
    if checked:
        remind_passwd = 1
    else:
        remind_passwd = 0
def on_submit():
    global remind_passwd
    evaluation()
    if remind_passwd == 0:
        with open('user.txt', 'w') as file:
            file.truncate(0)
        root.destroy()
        return 1
    else:
        jaccount_value = jaccount_entry.get()
        passwd_value = passwd_entry.get()
        # 将 jaccount_value 和 passwd_value 写入到 user.txt 中，要求全覆盖
        # Base64 encode the values
        encoded_jaccount = base64.b64encode(jaccount_value.encode()).decode()
        encoded_passwd = base64.b64encode(passwd_value.encode()).decode()

        # Write the encoded values to user.txt
        with open('user.txt', 'w') as file:
            file.write(f'{encoded_jaccount}\n{encoded_passwd}')
        root.destroy()
        return 1

if __name__ == "__main__":
    if os.path.getsize("./user.txt") != 0:
        data = []
        with open('user.txt', 'r') as file:
            for line in file:
                encoded_string = line.strip()
                print(encoded_string)
                data.append(encoded_string)
        # 解码用户名和密码
        username = base64.b64decode(data[0]).decode('utf-8')
        password = base64.b64decode(data[1]).decode('utf-8')
    else:
        username = ""
        password = ""

    # The rest of your code remains unchanged...

    root = tk.Tk()
    root.title("垃圾过滤系统")
    center_window(root, 400, 300)
    jaccount_label = tk.Label(root, text="jaccount账号")
    passwd_label = tk.Label(root, text="密码")
    jaccount_entry = tk.Entry(root)
    jaccount_entry.insert(0,username)
    passwd_entry = tk.Entry(root,show='*')
    passwd_entry.insert(0,password)
    jaccount_label.place(x=50, y=50)  # Adjust the coordinates as needed
    jaccount_entry.place(x=150, y=50)  # Adjust the coordinates as needed
    passwd_entry.place(x=150,y=100)
    passwd_label.place(x=50,y=100)
    # 使用 IntVar 来跟踪勾选框的状态
    checkbox_var = tk.IntVar()
    checkbox_var.set(1)
    # 创建勾选框，关联变量 checkbox_var，设置回调函数 on_checkbox_click
    checkbox = tk.Checkbutton(root, text="记住用户密码", variable=checkbox_var, command=on_checkbox_click)

    # 将勾选框放置到窗口中
    checkbox.place(x=150,y=150)
    # 创建按钮，并设置宽度和高度
    submit_button = tk.Button(root, text="提交", command=on_submit, width=5, height=1)
    # 将按钮放置到窗口中
    submit_button.place(x=150,y=200)
    root.mainloop()

