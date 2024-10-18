#!/usr/bin/env python
# coding: utf-8

# In[1]:


import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, Activation, Flatten, Conv2D, MaxPooling2D
import pickle
import numpy as np
from tensorflow.keras.callbacks import TensorBoard
import time

NAME = "Cats-vs-dog-cnn-64x2-{}".format(int(time.time()))
tensorboard = TensorBoard(log_dir = "logs\{}".format(NAME))


X = pickle.load(open("X.pickle", "rb"))
y = pickle.load(open("y.pickle", "rb"))

X = np.array(X/255.0)
y = np.array(y)


# In[2]:


model = Sequential()
model.add(Conv2D(63, (3, 3), input_shape = X.shape[1:]))

model.add(Activation("relu"))
model.add(MaxPooling2D(pool_size = (2, 2)))


# In[3]:


model.add(Conv2D(64, (3, 3)))
model.add(Activation("relu"))
model.add(MaxPooling2D(pool_size = (2, 2)))


# In[4]:


model.add(Flatten())
model.add(Dense(64))

model.add(Dense(1))
model.add(Activation("sigmoid"))


# In[ ]:


model.compile(loss = "binary_crossentropy", optimizer = "adam", metrics = ["accuracy"])
model.fit(X, y, batch_size = 32, epochs = 30, validation_split = 0.1, callbacks = [tensorboard])


# In[6]:


model.save('Dog_Cat_CNN.model')


# In[ ]:




