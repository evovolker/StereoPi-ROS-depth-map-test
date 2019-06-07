# -*- coding: utf-8 -*-
"""
@author: evovolker
"""
import numpy as np

image_width=640
image_height=480

def print_parameter(data,rows,cols,fout):
    print(' rows: '+str(rows), file = fout ) 
    print(' cols: '+str(cols), file = fout ) 
    print('data:'+np.array2string(data, 
                      separator=',', 
                      suppress_small=True, 
                      formatter={'float_kind':'{:.9g}'.format}).replace('\n',''), 
            file = fout)
    return 0

def print_yaml(camera_name):

    yaml_file = open(camera_name+'.yaml', 'w') 
      
    print('image_width: {:f}'.format(image_width), file = yaml_file ) 
    print('image_height: {:f}'.format(image_height), file = yaml_file ) 
    print('camera_name: '+camera_name, file = yaml_file ) 
    print('camera_matrix:', file = yaml_file ) 
    
    data=np.load('cam_mats_'+camera_name+'.npy').flatten()
    print_parameter(data,3,3,yaml_file)
    
    # need to verify meaning/adequacy of plumb_bob model
    print('distortion_model: plumb_bob', file = yaml_file ) 
    print('distortion_coefficients:', file = yaml_file ) 
    data=np.load('dist_coefs_'+camera_name+'.npy').flatten()
    print_parameter(data,1,5,yaml_file)
    
    print('rectification_matrix:', file = yaml_file ) 
    data=np.load('rect_trans_'+camera_name+'.npy').flatten()
    print_parameter(data,3,3,yaml_file)
    
    print('projection_matrix:', file = yaml_file ) 
    data=np.load('proj_mats_'+camera_name+'.npy').flatten()
    print_parameter(data,3,4,yaml_file)
    
    yaml_file.close()
    return 0

camera_name='left'
print_yaml(camera_name)
camera_name='right'
print_yaml(camera_name)