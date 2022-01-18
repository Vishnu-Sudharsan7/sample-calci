from flask import Flask,render_template,request
app= Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/cal',methods=['POST','GET'])
def cal():
    if request.method=='POST':
        tot=0
        n1=float(request.form['num1'])
        n2=float(request.form['num2'])
        tot=(n1+n2)
        return "The Answer is "+ str(tot)
    
if __name__=="__main__":
        app.run(debug=True)
