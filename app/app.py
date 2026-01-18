from flask import Flask, request

app = Flask(__name__)

SECRET_KEY = "hardcoded_secret"  # Intentional vulnerability

@app.route('/')
def home():
    name = request.args.get("name")
    return f"Hello {name}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
