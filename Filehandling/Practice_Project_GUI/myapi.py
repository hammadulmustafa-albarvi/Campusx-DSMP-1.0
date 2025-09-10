import nlpcloud

class API:
    def __init__(self):
        self.client = nlpcloud.Client("finetuned-llama-3-70b", "ff6512b646c90296c8231dde2e33add336b14218", gpu=True)

    def grammer_correction(self,text):
        result = self.client.gs_correction(text)
        return result