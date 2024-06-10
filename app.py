from flask import Flask, render_template, request

import threading
from tkinter import Tk
from tkinter.filedialog import askopenfilename, askdirectory
import ffmpeg
import temp
import os

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html", input_file = temp.inpf, output_folder = temp.outf)
    
@app.route("/input")
def input():
    root = Tk()
    root.withdraw()
    temp.inpf = askopenfilename()
    root.destroy()
    return render_template("index.html", input_file = temp.inpf, output_folder = temp.outf)

@app.route("/output")
def output():
    root = Tk()
    root.withdraw()
    temp.outf = askdirectory()
    root.destroy()
    return render_template("index.html", input_file = temp.inpf, output_folder = temp.outf)

@app.route("/convert", methods=['GET', 'POST'])
def convert():
    temp.extension = request.args.get("ext")
    print(request.args.get("ext"))
    return render_template("convert.html", input_file = temp.inpf, output_folder = temp.outf, extension = temp.extension)

@app.route("/converted", methods=['GET', 'POST'])
def converted():
    finalfile = temp.inpf.split("/")[-1].split(".")[0]
    print(temp.inpf)
    print(finalfile)
    ffmpeg.input(temp.inpf).output(f"{temp.outf}/{finalfile}.{temp.extension}").run()
    inpf = temp.inpf
    outf = temp.outf
    extension = temp.extension
    temp.inpf = ""
    temp.outf = ""
    temp.extension = ""
    return render_template("converted.html", output_folder = outf)

@app.route("/openfolder", methods=['GET', 'POST'])
def openfolder():
    path = request.args.get("path")
    path = os.path.realpath(path)
    os.startfile(path)
    return render_template("converted.html", output_folder = path)

if __name__ == "__main__":
    app.run(debug=True)