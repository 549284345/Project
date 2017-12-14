import numpy as np
import tensorflow as tf
import matplotlib.pyplot  as plt

#                        Price = W*size + b
# Model linear regression y = Wx + b
x = tf.placeholder(tf.float32, [None, 1])  # None is placeholder, 1 is 1-D;eg[None, 784] represent all numbers in 784-D is unknown
W = tf.Variable(tf.zeros([1,1]))
b = tf.Variable(tf.zeros([1]))
product = tf.matmul(x,W)
y = product + b                            # y = Wx + b, y is predict price
y_ = tf.placeholder(tf.float32, [None, 1]) # y_ is actually price

# Cost function sum((y_-y)**2)
cost = tf.reduce_mean(tf.square(y_-y))     # cost is sum((y_-y)**2)

# Training using Gradient Descent to minimize cost
train_step = tf.train.GradientDescentOptimizer(0.0000001).minimize(cost)

sess = tf.Session()
init = tf.initialize_all_variables()
sess.run(init)
steps = 1000

x1 = []
y1 = []
x2 = []
y2 = []
for i in range(steps):
  # Create fake data for y = W.x + b where W = 2, b = 0
  xs = np.array([[i]])
  ys = np.array([[2*i]])
  # Train

  feed = { x: xs, y_: ys }  # update the value for placeholder
  sess.run(train_step, feed_dict=feed)
  print("iteration %s times:" % i)
  print("W: %f" % sess.run(W))
  print("b: %f" % sess.run(b))
  print("y: %f" % sess.run(y,  feed_dict=feed))
  print("y_: %f" % sess.run(y_, feed_dict=feed))
  print("cost: %f" % sess.run(cost, feed_dict=feed))
  x1.append(i)
  y1.append(int(sess.run(y,  feed_dict=feed)))
  x2.append(i)
  y2.append(int(sess.run(y_,  feed_dict=feed)))

plt.plot(x1, y1, label="predict price")
plt.plot(x2, y2, label="actual price")
plt.xlabel("house size")
plt.ylabel("house price")
plt.title("relationship between price and size")
#plt.legend()
plt.show()
print('test done!')