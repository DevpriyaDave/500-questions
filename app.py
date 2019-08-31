from flask import Flask, render_template, request
import pandas as pd


app = Flask(__name__)
pd.set_option('display.max_columns', None)
pd.set_option('display.max_colwidth', -1)
df_questions = pd.read_csv("C:\\Users\\Dev\\PycharmProjects\\500questions\\app\\questions.csv")
test = ""
df_done = pd.read_csv("C:\\Users\\Dev\\PycharmProjects\\500questions\\app\\done.csv")
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/getquestion", methods=["GET"])
def get_question():
    test = df_questions.sample()
    print(test)
    return render_template("index.html", value=test)

#remove the number from question and add it to the done csv
@app.route("/donequestion", methods=["POST"])
def done_question():
    print(test)
    return render_template("index.html", value="done")

def run():
    app.run(debug=True, port=5690, host="0.0.0.0")



if __name__ == "__main__":
    run()