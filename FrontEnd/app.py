from flask import Flask, render_template

app = Flask(__name__)

# route = endpoint
@app.route('/')
def hello_world():
    return render_template("views/index.html")
    # don't need "template/" because Flask objeect looks for template folder

if __name__ == "__main__":
    app.run(debug=True)