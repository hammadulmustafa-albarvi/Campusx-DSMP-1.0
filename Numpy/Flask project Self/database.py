import json

class Database:
    def register_data(self,name,email,password):
        with open('database.json','r') as rf:
            database = json.load(rf)
            
            if email in database:
                return 0
            else:
                database[email] = [name,password]
                
        with open('database.json','w') as wf:
            json.dump(database,wf)
        
        return 1
    
    
    def login_backend(self,email,password):
        with open('database.json','r') as rf:
            database = json.load(rf)
            if email in database:
                if database[email][1] == password:
                    return 1
                else:
                    return 0
            else:
                return 0