#create directory
mkdir devsecops-app && cd devsecops-app
#Install python and flask
sudo apt install -y python3 python3-pip pip3 install flask

**If installation shows error**
#create virtual environment
python3 -m venv venv
cd ~/devsecops-app
python3 -m venv venv
#Activate virtual environment
source venv/bin/activate
#Install Flask safely
pip install flask

#create vulnerable app file
vi app.py
#file content
from flask import Flask, request

app = Flask(__name__)

SECRET_KEY = "hardcoded_secret"  # Intentional vulnerability

@app.route('/')
def home():
    name = request.args.get("name")
    return f"Hello {name}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
