from flask import Flask
from bp_app1.bp_app1 import bp_app1

from bp_app2.bp_app2 import bp_app2


app = Flask(__name__)


app.register_blueprint(bp_app1)

app.register_blueprint(bp_app2, url_prefix='/calculator')




if __name__ == '__main__':
    app.run(debug=True)