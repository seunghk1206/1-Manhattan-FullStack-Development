#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np
import matplotlib.pyplot as plt
import os
import cv2

DATADIR = "C:/Users/seunghyeon/Desktop/PetImages"
CATEGORIES = ['Dog', 'Cat']
for category in CATEGORIES:
    path = os.path.join(DATADIR, category)# path to pic
    for img in os.listdir(path):
        img_array = cv2.imread(os.path.join(path, img), cv2.IMREAD_GRAYSCALE)#cv2.IMREAD_GRAYSCALE
        plt.imshow(img_array, cmap = "gray")
        plt.show()
        break
    break


# In[2]:


print(img_array.shape)


# In[7]:


IMG_SIZE = 50
new_array = cv2.resize(img_array, (IMG_SIZE, IMG_SIZE))
plt.imshow(new_array, cmap = 'gray')
plt.show()


# In[17]:


training_data = []
#숫자형태의 레이블링으로 바꿔야함 Cat = 1, Dog = 1이런식으로
#매우중요함!!
def create_training_data():
    for category in CATEGORIES:
        path = os.path.join(DATADIR, category) #path to cats or dogs dir
        class_num = CATEGORIES.index(category) #Dog or Cat
        for img in os.listdir(path):
            try:
                img_array = cv2.imread(os.path.join(path,img), cv2.IMREAD_GRAYSCALE)
                new_array = cv2.resize(img_array, (IMG_SIZE, IMG_SIZE))
                training_data.append([new_array, class_num])
            except Exception as e:
                pass #some images are broken!!
create_training_data()


# In[18]:


print(training_data[1])
print(len(training_data))


# In[ ]:


import random
random.shuffle(training_data)


# In[14]:


X = []
Y = []
for features, label in training_data:
    X.append(features)
    Y.append(label)
X = np.array(X).reshape(-1, IMG_SIZE, IMG_SIZE, 1)


# In[ ]:




