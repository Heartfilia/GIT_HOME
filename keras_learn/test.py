import glob
import time
import numpy as np
# from tqdm import tqdm
from keras.models import load_model
from utils import data_generator
import os

model_path = './model/model.h5'
# print("Using loaded model to predict...")

load_model = load_model(model_path)

total = 0.
right = 0.
step = 0
all_class = list('0123456789abcdefghijklmnopqrstuvwxyz')

qq = 1
while True:
    file_name = f'./img_folder/{qq}.jpg'
    if not os.path.isfile(file_name):
        break
    samples = glob.glob(file_name)
    img_predict = data_generator(samples, 1)
    for x, y in img_predict:
        _ = load_model.predict(x)
        _ = np.array([i.argmax(axis=1) for i in _]).T
        predi = [''.join([all_class[k] for k in i]) for i in _]
        print(predi[0]) 
        break

    qq += 1
    time.sleep(1)



# for x, y in data_generator(samples, 1):
#     _ = load_model.predict(x)
#     _ = np.array([i.argmax(axis=1) for i in _]).T
#     print('=='*20)
#     predict = [''.join([all_class[k] for k in i]) for i in _]
#     print('predict:', predict)
#     break


# print('总计{}张验证码，模型全对率：{}'.format(total, right / total))
