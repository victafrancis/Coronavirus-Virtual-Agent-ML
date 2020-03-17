from flask import Flask, render_template, url_for, request
# from flask_wtf import FlaskForm
# from wtforms import StringField
# from wtforms.validators import DataRequired
import pickle
import keras
import responses, functions
import numpy as np
import pandas as pd

from sklearn.feature_extraction.text import CountVectorizer

import keras.backend.tensorflow_backend as tb
tb._SYMBOLIC_SCOPE.value = True

app = Flask(__name__)

# loading the model from pickle
virtual_agent_model = pickle.load(open('covid19_virtual_agent.pickle','rb'))
#loading the vectorizer from pickle
vectorizer = pickle.load(open('cv_vector.pickle','rb'))

print("keras: " + keras.__version__)

@app.route('/', methods=['POST', 'GET'])
def home():

    content = {'question':'','confidence':'','response_title':'','response_content':''}
    
    if request.method == 'POST':
        question = request.form['question']  #get question from form

        print(question)
        content['question'] = question
        question = functions.check(question)
        print('corrected question: ' + question)
        qtn = vectorizer.transform([question])  #transform to a vector
        qtn = qtn.toarray()  #transform to array
        prediction = virtual_agent_model.predict(qtn)
        print("confidence: " + str(np.amax(prediction[0])))
        content['confidence'] = str(np.amax(prediction[0]))
        print(responses.class_names[np.argmax(prediction[0])])
        content['response_title'] = responses.class_names[np.argmax(prediction[0])]

    return render_template('index.html', content=content)


if __name__ == '__main__':
    app.run(debug=False, threaded=False)