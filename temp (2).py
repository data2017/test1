# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import yaml  
import cv2
#strFile = r'./KITTI00-02.yaml'

def Test1():
    strFile = r'./EuRoC.yaml'
    
    fs = cv2.FileStorage( strFile , cv2.FILE_STORAGE_READ )
    
    #node: mat string real
    
    node1 = fs.getNode( 'RIGHT.K' )
    
    fn = fs.getNode("Camera.fx")
    fx = fs.getNode("Camera.fx").real()
    
    
    fn = fs.getNode( 'RIGHT' )
    subfn = fn.getNode( 'K' )
    #print(fn.mat())

def Test2():
    print( yaml.dump( 1 ) )
    print( yaml.dump( 'aaa' ) )
    
    #Dict = {'age': 37, 'spouse': {'age': 25, 'name': 'Jane Smith'}, 'name': 'Tom Smith', 'children': [{'age': 15, 'name': 'Jimmy Smith'}, {'age1': 12, 'name1': 'Jenny Smith'}]}  
    Dict = {
        'man.name' : 'andrew' , 
        'man.age'  : 37 
            }
    print( Dict )
    with open( './test.yaml' , 'w' ) as out :
        yaml.dump( Dict , out )
    
with open( './YamlForLoad.yaml' , 'r' ) as f :
    Dict = yaml.load( f )