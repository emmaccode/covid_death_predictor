import flask
from flask import Flask, render_template, request
import pickle as pkl
import numpy as np
# <--- Deps --->
# (Main)
app = Flask(__name__)
if __name__ == '__main__':
    app.run()

@app.route('/')
def template():
    mdl = pkl.load( open( "model.pkl", "rb" ) )
    try:
        txt = request.args['cases']
    except KeyError as e:
        return ('Some Values are missing')
    return(mdl.predict(txt))

if __name__ == '__main__':
    app.run(debug=False)
