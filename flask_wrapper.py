from flask import Flask, render_template, request, session, url_for, redirect
import os
from flask.helpers import send_file
from flask.wrappers import Response
from werkzeug.utils import secure_filename
from subprocess import Popen, list2cmdline
import re
import pandas as pd
import time

root = "home/"
aux_root = "home/"
app = Flask(__name__, template_folder="./templates")

app.config['STATIC_FOLDER'] = "home/"

uploads_dir = os.path.join(app.instance_path, 'uploads')




@app.route("/")
def index():
    folders, files = get_file_tree()
    
    
    return render_template("index.html", folders = folders, files = files)

def get_file_tree():
    
    folders  = []
    files = []

    for f in os.listdir(app.config.get('STATIC_FOLDER')):
        
        if os.path.isdir(app.config.get('STATIC_FOLDER')+f):
            
            folders.append(f)
        else:
            files.append(f)
                
    return folders, files


@app.route("/download/<string:file>")
def send(file):
    
    try:
        return send_file(os.path.join(app.config.get('STATIC_FOLDER'),file), as_attachment= True)
        
    except:
        
        return "Something went wrong"
        
    

@app.route("/goto/<string:filename>")
def goto(filename):
    
    app.config['STATIC_FOLDER'] = os.path.join(app.config.get('STATIC_FOLDER'), filename)
    folders, files = get_file_tree()
    
    return render_template("index.html", folders = folders, files = files)
    

if __name__ == '__main__':

    app.run("192.168.11.1",  port=5000)

    