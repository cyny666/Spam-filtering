import tkinter as tk
from tkinter import simpledialog
from tkinter import messagebox
class LoginSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("上海交通大学垃圾邮件分类系统")
        self.username = ""
        self.password = ""
        file_path = "user.txt"
        with open(file_path,'r') as file:
            lines = file.readlines()
            if lines:
              self.username = lines[0].strip()
              self.password = lines[1].strip()
        self.label_username = tk.Label(root, text="JAccount账号")
        self.label_password = tk.Label(root, text="密码")
        self.entry_username = tk.Entry(root)
        self.entry_password = tk.Entry(root, show="*")
        self.button_user = tk.Button(root, text="用户", command=self.show_user_dialog)
        self.button_login = tk.Button(root, text="登录", command=self.login)
        self.label_username.grid(row=0, column=0, padx=10, pady=10)
        self.label_password.grid(row=1, column=0, padx=10, pady=10)
        self.entry_username.grid(row=0, column=1, padx=10, pady=10)
        self.entry_password.grid(row=1, column=1, padx=10, pady=10)
        self.button_user.grid(row=2, column=0, columnspan=2, pady=10)
        self.button_login.grid(row=3, column=0, columnspan=2, pady=10)
    def show_user_dialog(self):
        user_dialog = tk.Toplevel(self.root)
        user_dialog.title("用户")
        button_bind = tk.Button(user_dialog, text="绑定用户", command=self.bind_user)
        button_unbind = tk.Button(user_dialog, text="解绑用户", command=self.unbind_user)
        button_bind.grid(row=0, column=0, padx=10, pady=10)
        button_unbind.grid(row=0, column=1, padx=10, pady=10)
    def bind_user(self):
        if not self.username and not self.password:
            self.username = simpledialog.askstring("绑定用户", "JAccount账号")
            self.password = simpledialog.askstring("绑定用户", "密码")
            messagebox.showinfo("绑定成功", "绑定成功")
            file_path = "user.txt"
            with open(file_path, 'w') as file:
                file.write(f"{self.username}\n{self.password}")
        else:
            messagebox.showinfo("绑定失败", "已绑定用户")
    def unbind_user(self):
        user_dialog = tk.Toplevel(self.root)
        user_dialog.title("解绑用户")
        label_username = tk.Label(user_dialog, text="JAccount账号")
        label_password = tk.Label(user_dialog, text="密码")
        entry_username = tk.Entry(user_dialog)
        entry_password = tk.Entry(user_dialog, show="*")
        button_unbind = tk.Button(user_dialog, text="解绑", command=lambda: self.unbind_confirm(entry_username.get(), entry_password.get()))
        label_username.grid(row=0, column=0, padx=10, pady=10)
        label_password.grid(row=1, column=0, padx=10, pady=10)
        entry_username.grid(row=0, column=1, padx=10, pady=10)
        entry_password.grid(row=1, column=1, padx=10, pady=10)
        button_unbind.grid(row=2, column=0, columnspan=2, pady=10)
    def unbind_confirm(self, entered_username, entered_password):
        if entered_username == self.username and entered_password == self.password:
            messagebox.showinfo("解绑成功", "解绑成功")
            self.username = ""
            self.password = ""
            file_path = "user.txt"
            with open(file_path, 'w') as file:
                file.truncate()
        else:
            messagebox.showinfo("解绑失败", "解绑失败")
    def login(self):
        entered_username = self.entry_username.get()
        entered_password = self.entry_password.get()

        if entered_username == self.username and entered_password == self.password:
            messagebox.showinfo("登录成功", "登录成功")
        else:
            messagebox.showinfo("登录失败", "登录失败，请确认账号密码的正确性或绑定用户")

if __name__ == "__main__":
    root = tk.Tk()
    app = LoginSystem(root)
    root.mainloop()
