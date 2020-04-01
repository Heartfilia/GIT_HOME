
import numpy as np
from scipy import misc
from keras.applications.xception import preprocess_input

number = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']
all_class = number + alphabet

MAX_NUM = 6
CLASS_NUM = len(all_class)
# model_path = 'C:\ThirdPack\CODE\LEARN_ALL\ML\keras\model\model.h5'
model_path = '.\model\model.h5'
img_size = (50, 120, 1)

def data_generator(data, batch_size):  # 样本生成器，节省内存
    while True:
        batch = np.random.choice(data, batch_size)
        x, y = [], []
        for img in batch:
            x.append(misc.imresize(misc.imread(img)[:50, :], img_size))
            temp = []
            for i in img[-10:-4]:
                if i in [str(k) for k in range(10)]:
                    temp.append(int(i))
                else:
                    if ord(i) >= 97:
                        temp.append(ord(i) - ord('a') + 10)
                    else:
                        temp.append(ord(i) - ord('A') + 10)
            y.append(temp)

        x = preprocess_input(np.array(x).astype(float))
        y = np.array(y)
        # print([y[:, i] for i in range(6)])
        yield x, [y[:, i] for i in range(6)]

if __name__ == '__main__':
    temp = []
    img = '8UUqaC'
    for i in img:
        if i in [str(k) for k in range(10)]:
            temp.append(int(i))
        else:
            if ord(i) >= 97:
                temp.append(ord(i) - ord('a') + 10)
            else:
                temp.append(ord(i) - ord('A') + 10)
    print(temp)
