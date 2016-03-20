#!/usr/bin/env python3
# -*- coding : utf-8 -*-

import random

pattern = [1,0,0,0,0]

words=["ズン","ドコ"]

class myq:

    def __init__(self):                  # コンストラクタ
        self.Q = ['','','','',''] 

    def setQ(self,item):
        self.Q[4]=self.Q[3]
        self.Q[3]=self.Q[2]
        self.Q[2]=self.Q[1]
        self.Q[1]=self.Q[0]
        self.Q[0]=item
        return True

    def checkQ(self):
        if (self.Q[0] == pattern[0]) and \
           (self.Q[1] == pattern[1]) and \
           (self.Q[2] == pattern[2]) and \
           (self.Q[3] == pattern[3]) and \
           (self.Q[4] == pattern[4]):
            
            print("ヒ・ロ・シ!") 
            return True 
       


if __name__ == "__main__":

    q = myq()
    while 1:
        item = random.randint(0,1)
        if q.setQ(item):
            print(words[item])
        
        if q.checkQ():
            break
