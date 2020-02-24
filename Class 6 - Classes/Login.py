#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class LoginManager():
    def __init__(self, username, password, isVerified):
        self.username = username
        self.password = password
        self.isVerified = isVerified
        
    def setVerifiedValue(self, data):
        if type(data) == bool:
            self.isVerified = data
    
    def checkVerified(self):
        if self.isVerified == True:
            print("User is verified")
            return True
        else:
            print("User is not verified")
            return False
        
    
    def loginUser(this):
        if this.username == "faizan" and this.password == "123456":
            if this.checkVerified():
                return "User logged in"
            else:
                print("Not verified")
        else:
            return "Incorrect details"

