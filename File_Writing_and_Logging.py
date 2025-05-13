import datetime 

class Signup:
    def _init_(self, first_name, last_name,):
        self.first_name = first_name
        self.last_name = last_name
        self.username = first_name + last_name
        self.time= datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
    
    
        
    def log_entry(self):
        log_entry = f"\nUsername: {self.username}, Time: {self.time}"
        file_reader =open("log.txt", "a")
        file_reader.write(log_entry)
        file_reader.close()
    
    

if __name__ == "_main_":    #Can work without this, just unindent the subsequent code
    first_name=input("Enter your first name: ")
    last_name=input("Enter your last name: ")
    user = Signup(first_name, last_name) #Object
    user.log_entry()
    print(f"Your username is: {user.username}")
    print(f"Your log entry has been saved.")

#Have a log of sign in// 1.signup,2.signin // signup - use a name that does not exist signup.txt// signin - Must have already signed up signin.txt // 