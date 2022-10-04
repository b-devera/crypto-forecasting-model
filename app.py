import os
import matplotlib.pyplot as plt
import numpy as np
from flask import Flask, render_template

app = Flask(__name__)

graphUpload = os.path.dirname('static/image')
picFolder = os.path.join('static','image')

y = np.random.randint(20000, size=10)
y.sort()
plt.plot(y, color = "green", linewidth = 2)
plt.title("Bitcoin Graph")
plt.ylabel("Price")
plt.grid(True)

plt.savefig(graphUpload + '/image/BTCGraph.png')
plt.clf()

y = np.random.randint(1500, size=10)
y.sort()
plt.plot(y, color = "green", linewidth = 2)
plt.title("Ethereum Graph")
plt.ylabel("Price")
plt.grid(True)

plt.savefig(graphUpload + '/image/ETHGraph.png')
plt.clf()

y = np.random.randint(300, size=10)
y.sort()
plt.plot(y, color = "green", linewidth = 2)
plt.title("BNB Graph")
plt.ylabel("Price")
plt.grid(True)

plt.savefig(graphUpload + '/image/BNBGraph.png')
plt.clf()

y = np.random.randint(100, size=10)
y.sort()
plt.plot(y, color = "green", linewidth = 2)
plt.title("XRP Graph")
plt.ylabel("Price")
plt.grid(True)

plt.savefig(graphUpload + '/image/XRPGraph.png')
plt.clf()

y = np.random.randint(50, size=10)
y.sort()
plt.plot(y, color = "green", linewidth = 2)
plt.title("Cardano Graph")
plt.ylabel("Price")
plt.grid(True)

plt.savefig(graphUpload + '/image/ADAGraph.png')
plt.clf()

y = np.random.randint(40, size=10)
y.sort()
plt.plot(y, color = "green", linewidth = 2)
plt.title("Solana Graph")
plt.ylabel("Price")
plt.grid(True)

plt.savefig(graphUpload + '/image/SOLGraph.png')
plt.clf()

y = np.random.randint(10, size=10)
y.sort()
plt.plot(y, color = "green", linewidth = 2)
plt.title("Terra Graph")
plt.ylabel("Price")
plt.grid(True)

plt.savefig(graphUpload + '/image/LUNAGraph.png')
plt.clf()

y = np.random.randint(20, size=10)
y.sort()
plt.plot(y, color = "green", linewidth = 2)
plt.title("Avalanche Graph")
plt.ylabel("Price")
plt.grid(True)

plt.savefig(graphUpload + '/image/AVAXGraph.png')
plt.clf()

y = np.random.randint(30, size=10)
y.sort()
plt.plot(y, color = "green", linewidth = 2)
plt.title("Dogecoin Graph")
plt.ylabel("Price")
plt.grid(True)

plt.savefig(graphUpload + '/image/DOGEGraph.png')
plt.clf()

y = np.random.randint(10, size=10)
y.sort()
plt.plot(y, color = "green", linewidth = 2)
plt.title("Polkadot Graph")
plt.ylabel("Price")
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

@app.route('/news')
def news():
    return render_template('news.html')

@app.route('/aboutus')
def aboutus():
    return render_template('aboutus.html')

if __name__ == "__main__":
    app.run(debug=True)
