from flask import Flask, render_template

app = Flask(__name__)

@app.route('/nutrisys')
def homeview():
    return 'Welcome to Nutrition Recommendation System!'

@app.route('/myview')
def myhomeview():
    return render_template('mypage.html')

if __name__ == '__main__':
    app.run(debug=True)
