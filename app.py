from flask import Flask, render_template

app = Flask(__name__)
@app.route('/')
def home():
    chart_data = get_cooking_trends() 
    return render_template('index.html', data=chart_data)
if __name__ == "__main__":
    app.run(debug=True)
