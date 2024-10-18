#!/usr/bin/env python
# coding: utf-8

# In[5]:


import cv2
import tensorflow as tf

CATEGORIES = ['Dog', 'Cat']

def prepare(filepath):
    IMG_SIZE = 50
    img_array = cv2.imread(filepath, cv2.IMREAD_GRAYSCALE)
    new_array = cv2.resize(img_array, (IMG_SIZE, IMG_SIZE))
    return new_array.reshape(-1, IMG_SIZE, IMG_SIZE, 1)

model = tf.keras.models.load_model("Dog_Cat_CNN.model")

prediction = model.predict([prepare('dog2.png')])
print(prediction[0][0])
print(CATEGORIES[int(prediction[0][0])])

prediction2 = model.predict([prepare('cat2.png')])
print(prediction2[0][0])
print(CATEGORIES[int(prediction2[0][0])])


# In[ ]:




