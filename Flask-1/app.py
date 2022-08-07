from flask import Flask, render_template, request
import re
app = Flask(__name__)

##########################################

@app.route('/',methods=['GET','POST'])
def fun_1():
    if request.method == 'POST':
            pattern = request.form['reg']
            string = str(request.form['str'])
            indices = [i.start() for i in re.finditer(pattern,string)]
            match_no = len(indices)
            return render_template("output.html",l=indices,n=match_no,p=pattern,s=string)
    return render_template("index.html")


##########################################

if __name__ == '__main__':
    app.run(debug=True)