########## Angkan Baidya ##########
########## abaidya ##############
########## 112309655 #############
import re


def is_pwd_strong(password):
    pattern  ="^(?=.*[a-z])(?=.*[A-Z])(?=.*\\d)[a-zA-Z\\d\\W]{8,}$"
    return re.match(pattern,password)
    
       

