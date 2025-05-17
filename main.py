from flask import Flask, request, render_template_string

app = Flask(__name__)

# Global counter variable
counter = 0

HTML_TEMPLATE = '''
<!DOCTYPE html>
<html>
<head>
    <title>Counter App</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            height: 100vh;
            background: linear-gradient(to right, #667eea, #764ba2);
            color: white;
        }
        h1 {
            font-size: 4rem;
            margin-bottom: 1rem;
        }
        p {
            font-size: 3rem;
            margin: 2rem 0;
        }
        form {
            display: flex;
            gap: 1rem;
        }
        button {
            padding: 1rem 2rem;
            font-size: 2rem;
            border: none;
            border-radius: 10px;
            cursor: pointer;
            background-color: rgba(255, 255, 255, 0.2);
            color: white;
            transition: background-color 0.3s;
        }
        button:hover {
            background-color: rgba(255, 255, 255, 0.4);
        }
    </style>
</head>
<body>
    <h1>Counter App</h1>
    <p>{{ counter }}</p>
    <form method="post">
        <button name="action" value="add">➕ Adicionar</button>
        <button name="action" value="subtract">➖ Restar</button>
        <button name="action" value="reset">🔄 Reiniciar</button>
    </form>
</body>
</html>
'''

@app.route('/', methods=['GET', 'POST'])
def home():
    global counter
    if request.method == 'POST':
        action = request.form.get('action')
        if action == 'add':
            counter += 1
        elif action == 'subtract':
            counter -= 1
        elif action == 'reset':
            counter = 0
    return render_template_string(HTML_TEMPLATE, counter=counter)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)
