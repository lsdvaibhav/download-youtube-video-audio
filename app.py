from flask import Flask , render_template ,request ,send_from_directory , send_file

# import pafy to use its methods
import pafy

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/video',methods=["POST","GET"])
def video():
    if request.method == "POST":
        url = request.form["yturl"]
        try:
            video = request.form["video"]
            pafy.new(url).getbest().download('your-file-name.mp4')
            return send_from_directory(app.instance_path,filename='your-file-name.mp4',as_attachment=True)
        except :
            pass
    
        try:
            audio = request.form["audio"]
            pafy.new(url).getbestaudio().download('your-file-name.mp3')
            return send_from_directory(os.path.dirname(app.instance_path),filename='your-file-name.mp3',as_attachment=True)
        except :
            pass

if __name__ == "__main__":
    app.run(debug=True)
