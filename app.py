from flask import Flask, request
from werkzeug.utils import secure_filename
import os, random, string
import shutil

app = Flask(__name__)

UPLOAD_FOLDER = 'Files'
ALLOWED_EXTENSIONS = {'ino'}

def rand():
    res = ''.join(random.choices(string.ascii_uppercase + string.digits, k = 3))
    return str(res)

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods = ['POST'])
def compile():
    file = request.files['file']
    if allowed_file(file.filename):
        board = request.headers.get('board')
        filename = rand()+secure_filename(file.filename)
        directory=filename[0:len(filename)-4]
        project = "Files/"+directory
        os.mkdir(project)
        file.save(project+"/"+filename)
        os.popen("./arduino-cli compile --fqbn arduino:avr:"+board+" "+project).read()
        hexval = open(project+"/build/arduino.avr."+board+"/"+directory+".ino.hex").read()
        print(project)
        remove(project)
        return hexval
    return "Please send a valid file"
    #output = stream.read()
    #return output

def remove(mydir):
    try:
        shutil.rmtree(mydir)
    except OSError as e:
        print ("Error: %s - %s." % (e.filename, e.strerror))

@app.route('/test')
def test():
    return 'Test OK'