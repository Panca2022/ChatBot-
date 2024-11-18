"""
    i) Flask: The Flask Library is used to handle large amount and data and the traffic. Also it is used to crete a light weight web framework and provide the easier features that make the creation of the web page more easier  
    
    ii) request: It is  library for making HTTP requests. It gives the interface easy-to-use that makes working with the HTTP very simple. This request library simplifies the process of sending and receiving data from websites for GET & POST 
    methods

    iii) jsonify: It converts the python data structures into the formt of JSON. So convert the python into the JSON makes the data to exchange between web applications. So it returns a response object 
"""
from flask import Flask, request, jsonify 

import openai # Provide convinient access to the OpenAI REST API from any Python 3.8+ Application 
"""
    This provide the easy-to-use function for intercting with the Operating System like File & Directory Management, OS Information, Process Control, Portable functionality 
"""

import os 

"""
    i) dotenv: It keep settings in a separate file, making the code cleaner and easier to manage. It also makes the code more secure, as sensitive data like API keys are not exposed in the codebase.
    ii) load_dotenv: Easy to handle environment variables in python applications from start and finish
"""
from dotenv import load_dotenv

openai.api_key = os.getenv("OPENAI_API_KEY")
app = Flask(__name__)
@app.route('/')
def home():
    return "AI Chatbot is running!"

@app.route('/chat', methods = ['POST'])
def chat():
    user_input = request.json.get('message')
    if not user_input:
        return jsonify({"error": "No Message Provided"}), 404
    
    try: 
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=f"User:{user_input}\nAI:",
            max_token=150,
            temperature=0.7
        )
        reply = response.choice[0].text.strip()
        return jsonify({"reply": reply})
    except Exception as e:
        return jsonify({"error": str(e)}), 500
if __name__ == 'main':
    app.run(debug=True)
