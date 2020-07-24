from flask import Flask, render_template, request, make_response

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('01_Home.html')


@app.route('/typo')
def typo():
    return render_template('03_text.html')


@app.route('/project')
def project():
    return render_template('./team_web/dl_temp.html')


@app.route('/iris', methods=['GET', 'POST'])
def iris():
    if request.method == 'GET':
        return render_template('12_form iris.html')
    else:
        slen1 = float(request.form['slen'])
        plen1 = float(request.form['plen'])
        pwid1 = float(request.form['pwid'])
        sel11 = int(request.form['sel1'])
        comment1 = request.form['comment']
        return render_template('12_iris-result.html', slen=slen1, plen=plen1, pwid=pwid1, sel1=sel11, comment=comment1)

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name = None):
    return render_template('hello.html', name = name)

if __name__ == '__main__':
    app.run(debug=True)
