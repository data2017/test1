#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May  6 10:55:00 2018

@author: nvidia
"""
# /usr/bin/python2 
import platform

import rosbag

strBag = '/home/nvidia/Downloads/SlamData/MH_03_medium.bag'

bag = rosbag.Bag( strBag )

topics = [ '/cam0/image_raw' , '/cam1/image_raw' , '/imu0' ]
         
 

for topic, msg, t in bag.read_messages( topics=topics ):
    print topic 

bag.close()