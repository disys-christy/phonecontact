class contact_info:                                                                           
    
    def __init__(self):
        print("Add to phonebook")
        self.mobile=input("enter your mobile no:")
        self.name=input("enter name:")
        self.ringtone=input("select ringtone:")
        
        
    def open_contact(self):
        print("contact saved")
        
   
    def mobile_verification(self):
        if (len(self.mobile)==10):
            if type(self.mobile) == "int":                                                                            
                print("phone number verified")
        else:
            raise ValueError("invalid phone number")
        
    def name_verification(self):
            if len(self.name) <= 20:
                 if type(self.name) == str:
                     print("name verified")
                 else:
                     raise TypeError("invalid name")

    def set_ringtone(self,tune):
        self.ringtone=tune
        if type(self.ringtone)==str:
            print("successfully created ringtone")
        else:
            raise ValueError("Invalid set_ringtone")

def main():
    print("open contact")
    print("mobile_verification")
    print("name_verification")
    print("set_ringtone")
    print("add successfully")

christy=contact_info()
christy.open_contact()
christy.mobile_verification()
christy.name_verification()

    
