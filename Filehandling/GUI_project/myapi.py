import nlpcloud


class API:
    def __init__(self):  
        self.client = nlpcloud.Client("finetuned-llama-3-70b", "ff6512b646c90296c8231dde2e33add336b14218", gpu=True)
        
    def sentiment_analysis(self,text):
        result = self.client.sentiment(text)
        return result
    
    def ner_analysis(self,text,search):
        result = self.client.entities(text,searched_entity=search)
        return result
    
    def text_summarization(self,text):
        result = self.client.summarization(text,size='small')
        return result