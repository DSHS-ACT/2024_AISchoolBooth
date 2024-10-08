from flask import Flask, request, jsonify, render_template
from flask_wtf import FlaskForm
from flask_socketio import SocketIO,send
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from openai import OpenAI

client = OpenAI(api_key="THERE_IS_NO_API_KEY")

app = Flask(__name__)
socketio = SocketIO(app)
app.config["SECRET_KEY"] = "SECRET_KEY"


class ChatForm(FlaskForm):
  message = StringField("Message", validators=[DataRequired()])
  submit = SubmitField("Send")

@app.route("/fake", methods=["GET", "POST"])
def fake():
  form = ChatForm()
  return render_template("fake.html", form=form)

@app.route("/detect", methods=["GET", "POST"])
def detect():
  form = ChatForm()
  return render_template("detect.html", form=form)

@app.route("/admin", methods=["GET", "POST"])
def admin():
  form = ChatForm()
  return render_template("admin.html", form=form)


@app.route("/fakegen", methods=["POST"])
def fakegen():
  data = request.json
  user_input = data.get("message")

  response = client.chat.completions.create(model="gpt-4o",
  messages=[
    {"role": "system", "content": "You are a fake news generator for experiential activities. Use a colloquial tone similar to actual news, and using formal language. Use primarily for references to specific dates or institutions. When entering a specific keyword, please write a Korean news title and use a formal text that fits the topic."},
    {"role": "user", "content": user_input}
  ])

  return jsonify({"response": response.choices[0].message.content})

@app.route("/detectgen", methods=["POST"])
def detectgen():
  data = request.json
  user_input = data.get("message")

  response = client.chat.completions.create(model="gpt-4o",
  messages=[
    {"role": "system", "content": "You are a fake news detector. Given the title and summary text of the news, determine whether the text is real news or fake news based on specific evidence and answer in Korean. Find all the evidence in the text without asking for additional information. Finally, determine whether this news is more likely to be real or fake news"},
    {"role": "user", "content": user_input}
  ])

  return jsonify({"response": response.choices[0].message.content})

# SocketIO
@socketio.on("message")
def handle_message(data):
  message_type = data["type"]
  message_text = data["text"]
  send({"type": message_type, "text": message_text}, broadcast=True)

if __name__ == "__main__":
  socketio.run(app, debug=True, host="0.0.0.0")
