import io
import os
import random
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from flask import Flask, render_template, Response
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

from matplotlib.backends.backend_template import FigureCanvas

app= Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///information.db'
db = SQLAlchemy(app)

graphUpload = os.path.dirname('static/image')
picFolder = os.path.join('static','image')

x = np.random.randint(100, size=10)
y = np.random.randint(100, size=10)
x.sort()
y.sort()
plt.plot(x, y, color = "green", linewidth = 2)
plt.title("Bitcoin Graph")
plt.xlabel("X - Axis")
plt.ylabel("Y - Axis")
plt.grid(True)

plt.savefig(graphUpload + '/image/BTCGraph.png')
plt.clf()

x = np.random.randint(100, size=10)
y = np.random.randint(100, size=10)
x.sort()
y.sort()
plt.plot(x, y, color = "green", linewidth = 2)
plt.title("Ethereum Graph")
plt.xlabel("X - Axis")
plt.ylabel("Y - Axis")
plt.grid(True)

plt.savefig(graphUpload + '/image/ETHGraph.png')
plt.clf()

x = np.random.randint(100, size=10)
y = np.random.randint(100, size=10)
x.sort()
y.sort()
plt.plot(x, y, color = "green", linewidth = 2)
plt.title("BNB Graph")
plt.xlabel("X - Axis")
plt.ylabel("Y - Axis")
plt.grid(True)

plt.savefig(graphUpload + '/image/BNBGraph.png')
plt.clf()

x = np.random.randint(100, size=10)
y = np.random.randint(100, size=10)
x.sort()
y.sort()
plt.plot(x, y, color = "green", linewidth = 2)
plt.title("XRP Graph")
plt.xlabel("X - Axis")
plt.ylabel("Y - Axis")
plt.grid(True)

plt.savefig(graphUpload + '/image/XRPGraph.png')
plt.clf()

x = np.random.randint(100, size=10)
y = np.random.randint(100, size=10)
x.sort()
y.sort()
plt.plot(x, y, color = "green", linewidth = 2)
plt.title("Cardano Graph")
plt.xlabel("X - Axis")
plt.ylabel("Y - Axis")
plt.grid(True)

plt.savefig(graphUpload + '/image/ADAGraph.png')
plt.clf()

x = np.random.randint(100, size=10)
y = np.random.randint(100, size=10)
x.sort()
y.sort()
plt.plot(x, y, color = "green", linewidth = 2)
plt.title("Solana Graph")
plt.xlabel("X - Axis")
plt.ylabel("Y - Axis")
plt.grid(True)

plt.savefig(graphUpload + '/image/SOLGraph.png')
plt.clf()

x = np.random.randint(100, size=10)
y = np.random.randint(100, size=10)
x.sort()
y.sort()
plt.plot(x, y, color = "green", linewidth = 2)
plt.title("Terra Graph")
plt.xlabel("X - Axis")
plt.ylabel("Y - Axis")
plt.grid(True)

plt.savefig(graphUpload + '/image/LUNAGraph.png')
plt.clf()

x = np.random.randint(100, size=10)
y = np.random.randint(100, size=10)
x.sort()
y.sort()
plt.plot(x, y, color = "green", linewidth = 2)
plt.title("Avalanche Graph")
plt.xlabel("X - Axis")
plt.ylabel("Y - Axis")
plt.grid(True)

plt.savefig(graphUpload + '/image/AVAXGraph.png')
plt.clf()

x = np.random.randint(100, size=10)
y = np.random.randint(100, size=10)
x.sort()
y.sort()
plt.plot(x, y, color = "green", linewidth = 2)
plt.title("Dogecoin Graph")
plt.xlabel("X - Axis")
plt.ylabel("Y - Axis")
plt.grid(True)

plt.savefig(graphUpload + '/image/DOGEGraph.png')
plt.clf()

x = np.random.randint(100, size=10)
y = np.random.randint(100, size=10)
x.sort()
y.sort()
plt.plot(x, y, color = "green", linewidth = 2)
plt.title("Polkadot Graph")
plt.xlabel("X - Axis")
plt.ylabel("Y - Axis")
plt.grid(True)

plt.savefig(graphUpload + '/image/DOTGraph.png')
plt.clf()

app.config['UPLOAD_FOLDER'] = picFolder

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/explore')
def explore():
    BTCGraph = os.path.join(app.config['UPLOAD_FOLDER'], 'BTCGraph.png')
    ETHGraph = os.path.join(app.config['UPLOAD_FOLDER'], 'ETHGraph.png')
    BNBGraph = os.path.join(app.config['UPLOAD_FOLDER'], 'BNBGraph.png')
    XRPGraph = os.path.join(app.config['UPLOAD_FOLDER'], 'XRPGraph.png')
    ADAGraph = os.path.join(app.config['UPLOAD_FOLDER'], 'ADAGraph.png')
    SOLGraph = os.path.join(app.config['UPLOAD_FOLDER'], 'SOLGraph.png')
    LUNAGraph = os.path.join(app.config['UPLOAD_FOLDER'], 'LUNAGraph.png')
    AVAXGraph = os.path.join(app.config['UPLOAD_FOLDER'], 'AVAXGraph.png')
    DOGEGraph = os.path.join(app.config['UPLOAD_FOLDER'], 'DOGEGraph.png')
    DOTGraph = os.path.join(app.config['UPLOAD_FOLDER'], 'DOTGraph.png')
    return render_template('explore.html', BTCGraph = BTCGraph, ETHGraph = ETHGraph, BNBGraph = BNBGraph, XRPGraph = XRPGraph, ADAGraph = ADAGraph,
                           SOLGraph = SOLGraph, LUNAGraph = LUNAGraph, AVAXGraph = AVAXGraph, DOGEGraph = DOGEGraph, DOTGraph = DOTGraph)

@app.route('/learn')
def learn():
    return render_template('learn.html')

@app.route('/aboutus')
def aboutus():
    return render_template('aboutus.html')

if __name__ == "__main__":
    app.run(debug=True)
