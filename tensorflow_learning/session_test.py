# -*- coding: utf-8 -*-

import tensorflow as tf

matrix1 = tf.constant([[3, 3]])
matrix2 = tf.constant([[2], [2]])

product = tf.matmul(matrix1, matrix2)  # matrix multiply

session = tf.Session()
result = session.run(product)
print(result)
session.close()

with tf.Session() as sess:
    print(sess.run(product))
