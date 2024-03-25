from flask import Flask, render_template, request
from firebase_admin import credentials, firestore, initialize_app
from extensions.mapfield_extension import field_value

cred = credentials.Certificate('credentials/credentials.json')
initialize_app(cred)

db = firestore.client()

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
       
        # Create a document in the "apropriacao" collection with properties based on the form fields
        db.collection("apropriacao").document().set({
            "patient": field_value('patient'),
            "date": field_value('date'),
            "doctor": field_value('doctor'),
            "price": field_value('price')
        })
        
        return 'Success'
    return render_template('index.html')

@app.route('/report')
def report():
    aprops = db.collection("apropriacao").get()
    return render_template('report.html', aprops=aprops)

if __name__ == '__main__':
    app.run(debug=True)
    
