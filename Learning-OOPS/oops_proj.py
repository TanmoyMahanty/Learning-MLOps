class chatbot:
    def __init__(self):
        self.username = ''
        self.password = ''
        self.loggedin = False
        self.menu()
    
    def menu(self):
        user_input = input('''Welcome to Chatbot || how would you like to procced 
                           1. Press 1 to signup
                           2. Press 2 to signin
                           3. Press 3 to write a post
                           4. Press 4 to message a friend
                           5. Press any key to exit 
                           
                           ''')
        
        if user_input == "1":
            self.signup()
        
        elif user_input == "2":
            self.signin()
        
        elif user_input == "3":
            pass
        
        elif user_input == "4":
            pass
        
        elif user_input == "5":
            pass
        
        else:
            exit()
            
            
    def signup(self):
        email = input("Enter your email / / username: ")
        password = input("Enter your password: ")
        self.username = email
        self.password = password
        print("You have successfully looged in ")
        print("\n")
        self.menu()
    
    def signin(self):
        if self.username=='' and self.password=='':
            print("please sign up first by pressing 1 in the main menu")
        else:
            user_name = input("Enter your email / / username here: ")
            password = input("Enter you password here: ")
            if self.username == user_name and self.password == password:
                print("You have successefully signed in")
                self.loggedin = True
            else:
                print("Please enter correct login credentials ")   
        print("\n")
        self.menu()        

obj = chatbot() 