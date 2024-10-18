#[1]
'''
-Machine Learning 목표 => input 을 통해 output을 찾는거
-각각의 output, input 을 neuron.
-Hidden Layer에 각각의 input neuron.
-Hidden Layer가 하나면 그냥 neural network 하지만 
'''
#[2]
import tensorflow as tf
mnist = tf.keras.datasets.mnist
(x_train, y_train), (x_test, y_test) = mnist.load_data()
##print(x_train[0])
##Normalization
x_train = tf.keras.utils.normalize(x_train, axis = 1)
x_test = tf.keras.utils.normalize(x_test, axis = 1)
##print(x_train[0])
model = tf.kerat.models.Sequential()#패턴을 찾는 딥러닝

model.add(tf.keras.layers.Flatten())#reshape

model.add(tf.keras.layers.Dense(128, activation = tf.nn.relu))
model.add(tf.keras.layers.Dense(128, activation = tf.nn.relu))

model.add(tf.keras.layers.Dense(10, activation = tf.nn.softmax))

model.compile(optimizer = 'adam', loss = 'sparse_categorical_crossentropy', metrics = ["accuracy"])

model.fit(x_train, y_train, epochs = 3)


#[3]
val_loss, val_acc = model.evaluate(x_test, y_test)

#[4]
import matplotlib.pyplot as plt
plt.imshow(x_train[0], cmap = plt.cm.binary)