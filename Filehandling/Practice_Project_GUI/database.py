import json
class DataBase:
    
    def add_data(self,email,name,password):
        with open('database.json','r') as rf:
            database = json.load(rf)
        
        with open('database.json','w') as wf:
            if email not in database:
                database[email] = [name,password]
                json.dump(database,wf)
                return 1 
            else:
                return 0 
    
    def login(self,email,password):
        with open('database.json','r') as rf:
            database = json.load(rf) 
        
        if email in database:
            if password == database[email][1]:
                return 1 
            else:
                return 0 
        else:
            return 0
            
            