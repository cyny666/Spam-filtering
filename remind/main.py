import tkinter as tk
def close_window():
    root.destroy()
root = tk.Tk()
root.title("消息提示")
label = tk.Label(root, text="我们检测到这个邮件可能被错误搁置了")
label.pack(padx=20, pady=20)
button = tk.Button(root, text="确定", command=close_window)
button.pack(pady=10)
root.mainloop()




