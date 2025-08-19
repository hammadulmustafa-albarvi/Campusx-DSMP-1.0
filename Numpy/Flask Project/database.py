import json

class DataBase:
    # def __init__(self,name,email,password):
    #     self.name = name
    #     self.email = email
    #     self.password = password
        
    def register_backend(self,name,email,password):
        with open('users.json','r') as rf:
            database = json.load(rf)
            if email not in database:
                database[email] = [name,password]
            else:
                return 0
        with open('users.json','w') as wf:
            json.dump(database,wf)
        
        return 1
    
    def login_backend(self,email,password):
        with open('users.json','r') as rf:
            database = json.load(rf)
            
            if email in database:
                if database[email][1] == password:
                    return 1
                else:
                    return 0
            else:
                return 0