from flask import Flask, render_template, request , jsonify

app = Flask(__name__)

@app.route('/', methods=['GET'])
def welcome():
    return '<h2>welcome to welcome page</h2>'

@app.route('/first',methods=['GET'])
def first():
    return "<h2>This is first page</h2>"

@app.route('/second/<marks>',methods=['GET'])
def get_marks(marks):
    return f"<h2>Your marks are : {marks} </h2>"    

@app.route('/form', methods=['GET', 'POST'])
def get_form():
    if request.method == 'GET':
        return render_template('form.html')
    
    elif request.method == 'POST':
        maths = request.form.get('maths')
        history = request.form.get('history')
        data_science = request.form.get('data_science') 
        
        average = float(maths) + float(history) + float(data_science) / 3        
        return render_template('form.html', score=average)
    
@app.route('/api', methods=['POST'])
def sum():
    data = request.get_json()
    a = data.get('a')
    b = data.get('b')
    return jsonify({'sum': a + b})
    
if __name__ == '__main__':
    app.run()