from flask import Flask, render_template, request
import requests
from cohere_adapter import get_cohere_response

app = Flask(__name__)

# Set up your Cohere API key

@app.route('/')
def index():
    
    return render_template('landing.html')


@app.route('/cohere',methods=['GET'])
def cohere():

    return render_template('cohere.html')

@app.route('/cohere-request', methods=['POST'])
def compare():
    print(request.form)
    prompt = request.form.get('prompt')
    action = request.form.get('action')
    cohere_response = get_cohere_response(prompt,action)

    return render_template('result.html', prompt=prompt, cohere_response=cohere_response)


  

if __name__ == '__main__':
    app.run(debug=True)
