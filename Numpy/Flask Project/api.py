import nlpcloud


class Api():
    def __init__(self):
        self.client =  nlpcloud.Client("finetuned-llama-3-70b", "873c85f03fc15252700c32c56320aabad4309625", gpu=True) 
        
    def ner(self,text,search):
        result = self.client.entities(text,searched_entity=search)
        return result