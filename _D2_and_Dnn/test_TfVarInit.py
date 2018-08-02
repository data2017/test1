#!/usr/bin/env python  
# coding=utf-8  
  
import tensorflow as tf  
  
#create  a variable with a random value.  
weights=tf.Variable(tf.random_normal([5,3],stddev=0.35),name="weights")  
#Create another variable with the same value as 'weights'.  
w2=tf.Variable(weights.initialized_value(),name="w2")  
#Create another variable with twice the value of 'weights'  
w_twice=tf.Variable(weights.initialized_value()*0.2, name="w_twice")  
  
init=tf.initialize_all_variables()  
with tf.Session() as sess:  
    sess.run(init)  
    weights_val,w2_val,w_twice_val=sess.run([weights,w2,w_twice])  
    print( weights_val  )
    print( w2_val  )
    print( w_twice_val  )