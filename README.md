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
## 关于cnn
__pycache__文件夹里为运行后编译生成的代码。
data文件夹是数据集，spam代表垃圾邮件，ham代表正常邮件。
runs文件夹里保存训练过程、断点等信息，每组1702984710都是一个时间戳，代表了运行代码时的时间以做区分。
tool文件夹是阅读csv、词向量模型等的工具，和本任务本身无关。
data_helpers.py和word2vec_helpers.py用于定义一些函数来做词向量生成、数据处理等工作，text_cnn.py定义了这个CNN网络，train.py用于训练模型，eval.py用于评估模型。
如何训练一个模型？直接 python train.py
如何评估一个模型？直接 python eval.py，但需要修改eval.py的输入目录以及选择选择对应模型的断点目录，评估后的结果会保存在对应时间戳文件夹下，以一个csv的格式。（0为垃圾邮件，1为正常邮件）
请注意，运行环境的TensorFlow版本应为1.X。