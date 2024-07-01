import ollama

class Chatbot:
    def __init__(self):
        pass
    
    def ollama_func(self, txt_lst):
        response = ollama.chat(model='llama3', messages=txt_lst)
        print("**RESPONSE['MESSAGE']", response['message'])
        txt_lst.append(response['message'])
        return txt_lst