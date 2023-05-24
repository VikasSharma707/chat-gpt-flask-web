from flask import Flask, render_template, request
import openai
import config

app = Flask(__name__)
openai.api_key = config.OPENAI_API_KEY

messages = [
    {"role": "system", "content": "You are a helpful Financial assistant."}
]

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        user_input = request.form['user_input']

        if user_input.lower() == "quit":
            return render_template('index.html', assistant_reply='Conversation ended.')

        messages.append({"role": "user", "content": user_input})

        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages,
            max_tokens=50
        )

        assistant_reply = response['choices'][0]['message']['content']
        messages.append({"role": "assistant", "content": assistant_reply})

        return render_template('index.html', assistant_reply=assistant_reply)
    else:
        return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
