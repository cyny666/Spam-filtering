## Spam-filtering
运行前要现在main.py中输入自己的甲亢账号和密码

#### 推荐在python3.9下运行，不支持python3.12

需要在该目录下创建一个imgs文件夹

```python
# 输入甲亢账号
name = "" 
# 输入甲亢密码
passwd = ""
```
然后
```shell
pip install -r requirements.txt
```
即可运行main.py即可

输出的结果保留在mail_content.csv中

## 有关login与remind
在login中，运行程序，首先点击“用户”按钮绑定用户，输入JAccount账号和密码即可绑定，账号和密码会存储在user.txt中（因为只针对一个用户所以user.txt中最多存储一组账号密码），绑定账号后在主界面输入账号和密码即可登录。如果想登录其他用户首先要对已绑定账号进行解绑，点击用户中的“解除绑定”，输入已绑定的账号和密码即可。

在remind中，运行程序，即可弹出弹窗提示“我们检测到这个邮件可能被错误搁置了”