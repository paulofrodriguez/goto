from flask import Flask,redirect
from markupsafe import escape
import os


urls = {
     "google":"http://www.google.com",
     "uol": "http://www.uol.com.br",
     "gmail": "http://gmail.com"
}

app = Flask(__name__)


@app.route('/')
def index():
     return redirect("http://www.google.com", code=302)


@app.route('/<alias>')
def goto(alias):
     print(alias)
     print(urls[alias])
     #if (alias=='google'):
          # return redirect("http://www.google.com", code=302)
     return redirect(urls[alias], code=302)
     #elif (alias=='uol'):
     #     return redirect("http://www.uol.com", code=302)

if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)