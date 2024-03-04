from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])

def index():
    if request.method == 'POST':
        user_input = request.form.get('user_input')
        image_sources = Image_generator(user_input)
        return render_template('index.html', image_sources=image_sources, user_input=user_input)
    return render_template('index.html')

def Image_generator(key):
    key= str(key)
    access_key= 'mM_7H-Ct9KFq2n38cS9IIy1tC-LZYznvUG-Jql1KiRI'
    response= requests.get(f'https://api.unsplash.com/search/photos/?query={key}&per_page=10&page=1&client_id={access_key}')
    response= response.json()

    x= []
    for i in response['results']:
        x.append(i['urls']['raw'])
    return x

if __name__ == '__main__':
    app.run(debug=True)
