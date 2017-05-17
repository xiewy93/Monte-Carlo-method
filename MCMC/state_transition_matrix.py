# -*- coding: utf-8 -*-
"""
Created on Wed May 10 16:58:46 2017

@author: lenovo
"""
import numpy as np

class state_transition_matrix:
    
    def __init__(self,state_num, state_list):
        self.state_num = state_num
        self.state_list = state_list
        
    def  pre_state_transition_matrix(self):
        transition_matrix = {}
        for i in range(len(self.state_list)-1):
            transition_matrix.setdefault(self.state_list[i],[]).append(self.state_list[i+1])
        return transition_matrix

    def  calculate_state_transition_matrix(self):
        transition_matrix = self.pre_state_transition_matrix()
        state_transition_matrix = {}
        for key in transition_matrix:
           for i in range(1,self.state_num+1):
               prob = transition_matrix[key].count(i)/len(transition_matrix[key])
               state_transition_matrix.setdefault(key,[]).append(prob)        
        return state_transition_matrix

    def stable_state_transition_matrix(self):
       state_transition_matrix = self.calculate_state_transition_matrix()
       matrix = np.array(list( state_transition_matrix.values() ))
       matrix_1 =  matrix.T.dot(matrix)
       i = 0
       while matrix_1.all() != matrix.all():
           matrix_1 ,matrix =  matrix.T.dot(matrix) ,matrix_1
           i = i+1
           
       return matrix     

       
if __name__=='__main__':
    state_list = [1,2,3,3,2,1,2,3,1,2,1,3]
    state_num = 3
    pre_transition_matrix = state_transition_matrix(state_num, state_list)
    transition_matrix = pre_transition_matrix.stable_state_transition_matrix()
