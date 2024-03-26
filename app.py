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
        doc_ref = db.collection("apropriacao").document()
        doc_ref.set({
            "patient": field_value('patient'),
            "date": field_value('date'),
            "doctor": field_value('doctor'),
            "price": field_value('price')
        })
        
        # Retrieve the inserted document
        inserted_doc = doc_ref.get().to_dict()
        
        return render_template('index.html', inserted_doc=inserted_doc)
    
    return render_template('index.html')

@app.route('/report')
def report():
    aprops = db.collection("apropriacao").get()
    return render_template('report.html', aprops=aprops)
 
if __name__ == '__main__':
    app.run(debug=True)
    
