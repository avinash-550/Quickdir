# -*- coding: utf-8 -*-
"""
Created on Sun Nov 22 08:58:59 2020

@author: AVINASH
"""

import os
#import config

class Quickdir:
    def __init__(self,path="Quickdir"):
        """ initialize path or create dir if name given"""
        self.path = path
        try:
            os.mkdir(self.path + '/')
        except:
            pass
    
    def make(self, json, path = ""):
        """recursively traverse json object and make directories."""
        
        for key, value in json.items():
            pathr = path
            path += key + '/'
            if value == 1:
                path = path[:-1]
                f = open(self.path + '/' + path,'a')
                f.close()
                path = pathr
                continue
            elif value == 0:
                os.mkdir(self.path + '/' + path)
                path = pathr
                continue
            else:
                os.mkdir(self.path + '/' + path)
                self.make(value, path)
                path = pathr
                
            


# if __name__ == "__main__":
    
#     quick = Quickdir("hello")
#     quick.make(config.json)
      
        
