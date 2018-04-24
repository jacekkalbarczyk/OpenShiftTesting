from flask import Flask

app = Flask(__name__)

@app.route('/', methods=['GET'])
def info():
    return "Witam"

@app.route("/add/<int:liczba1>/<int:liczba2>")
def add(liczba1, liczba2):
    return str(liczba1 + liczba2)

if __name__ == '__main__':
    app.run(debug=True)
