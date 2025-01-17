# -*- coding: utf-8 -*-
"""
Created on Sun Jun 17 14:02:46 2018

@author: Luke
"""

import tensorflow as tf


#==============================================================================
# Session
#==============================================================================
m1 = tf.constant([[2, 2]])
m2 = tf.constant([[3],
                  [3]])
dot_operation = tf.matmul(m1, m2)

print(dot_operation)  # wrong! no result

# method1 use session
#sess = tf.Session()
#result = sess.run(dot_operation)
#print(result)
#sess.close()

# method2 use session
with tf.Session() as sess:
    result_ = sess.run(dot_operation)
    print(result_)


#==============================================================================
# Variable
#==============================================================================
state = tf.Variable(0, name='counter')

# 定义常量 one
one = tf.constant(1)

# 定义加法步骤 (注: 此步并没有直接计算)
new_value = tf.add(state, one)

# 将 State 更新成 new_value
update = tf.assign(state, new_value)
init = tf.global_variables_initializer()
# 使用 Session
with tf.Session() as sess:
    sess.run(init)
    for _ in range(3):
        sess.run(update)
        print(sess.run(state))
        
#==============================================================================
# Placeholder
#==============================================================================
input1 = tf.placeholder(tf.float32)
input2 = tf.placeholder(tf.float32)
ouput = tf.multiply(input1, input2)

with tf.Session() as sess:
    print(sess.run(ouput, feed_dict={input1: [7.], input2: [2.]}))