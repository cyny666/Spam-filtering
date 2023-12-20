import pickle
# 加载保存的超参数
with open("training_params.pickle", "rb") as file:
    params = pickle.load(file)
# 查看超参数的值
print(params)
