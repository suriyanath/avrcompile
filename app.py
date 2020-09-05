from flask import Flask, request
from werkzeug.utils import secure_filename
import os, random, string
import shutil
from subprocess import PIPE, Popen

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
    board = request.form.get('board')
    file = request.files['file']
    if allowed_file(file.filename):
        #board = request.headers.get('board')
        randomness = str(rand())
        filename = randomness+secure_filename(file.filename)
        directory=filename[0:len(filename)-4]
        project = "Files/"+directory
        os.mkdir(project)
        file.save(project+"/"+filename)
        p = Popen("./arduino-cli compile --fqbn arduino:avr:"+board+" "+project, shell=True, stdout=PIPE, stderr=PIPE)
        stdout, stderr = p.communicate()
        print("stdout: '%s'" % stdout)
        print("stderr: '%s'" % stderr)
        output=str(stderr)
        print(output)
        output = output.replace(os.getcwd()+"/"+project+"/"+randomness, "")
        
        print("output: '%s'" % output)
        if output == "b''":
            output = open(project+"/build/arduino.avr."+board+"/"+directory+".ino.hex").read()
            print(project)
        remove(project)
        output = output.replace("b\"", "ERROR: ")
        return output
    return "Please send a valid file"

def remove(mydir):
    try:
        shutil.rmtree(mydir)
    except OSError as e:
        print ("Error: %s - %s." % (e.filename, e.strerror))

@app.route('/test')
def test():
    return 'Test OK'