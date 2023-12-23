import tkinter as tk
import base64
from spam_filter import get_result
# 设置是否记录的标志 1表示记录 0表示不记录
remind_passwd = 0
def center_window(window, width, height):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    x = (screen_width - width) // 2
    y = (screen_height - height) // 2

    window.geometry(f'{width}x{height}+{x}+{y}')
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
    if remind_passwd == 0:
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
    root = tk.Tk()
    root.title("垃圾过滤系统")
    center_window(root, 400, 300)
    jaccount_label = tk.Label(root, text="jaccount账号")
    passwd_label = tk.Label(root, text="密码")
    jaccount_entry = tk.Entry(root)
    passwd_entry = tk.Entry(root)
    jaccount_label.place(x=50, y=50)  # Adjust the coordinates as needed
    jaccount_entry.place(x=150, y=50)  # Adjust the coordinates as needed
    passwd_entry.place(x=150,y=100)
    passwd_label.place(x=50,y=100)
    # 使用 IntVar 来跟踪勾选框的状态
    checkbox_var = tk.IntVar()
    # 创建勾选框，关联变量 checkbox_var，设置回调函数 on_checkbox_click
    checkbox = tk.Checkbutton(root, text="记住用户密码", variable=checkbox_var, command=on_checkbox_click)

    # 将勾选框放置到窗口中
    checkbox.place(x=150,y=150)
    # 创建按钮，并设置宽度和高度
    submit_button = tk.Button(root, text="提交", command=on_submit, width=5, height=1)
    # 将按钮放置到窗口中
    submit_button.place(x=150,y=200)
    root.mainloop()

