from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return {'pesan': 'Halo', 'nim': '230705054'}

@app.route('/health')
def health():
    return {'status': 'ok'}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
# test run 2 
# test run 3 
