from flask import Flask, render_template, request
from chatbot_demo import Chatbot
# import ollama
global convo
convo = [{
    'role': 'system',
    'content': 'You are an interviewer and you need to interview the candidate. You are very smart and have good observational skills. You pay attention to intricate details and also tell the candidate where to improve.'
  }]
app = Flask(__name__)
chatbot = Chatbot()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ask', methods=['POST'])
def ask():
    user_message = request.form['message']
    global convo
    convo.append({'role':'user','content':user_message})
    print(convo)
    convo = chatbot.ollama_func(convo)
    bot_response = convo[-1]['content']
    print(convo)
    return bot_response

if __name__ == '__main__':
    app.run(debug=True)