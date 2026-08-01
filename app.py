from flask import Flask, render_template, request, send_file
from moviepy import VideoFileClip
import os

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
OUTPUT_FOLDER = "output"

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/convert", methods=["POST"])
def convert():

    video = request.files["video"]
    audio_format = request.form["format"]

    video_path = os.path.join(
        UPLOAD_FOLDER,
        video.filename
    )

    video.save(video_path)

    output_name = (
        os.path.splitext(video.filename)[0]
        + "."
        + audio_format
    )

    output_path = os.path.join(
        OUTPUT_FOLDER,
        output_name
    )

    clip = VideoFileClip(video_path)
    clip.audio.write_audiofile(output_path)

    return render_template(
        "success.html",
        file_url=f"/download/{output_name}"
    )

@app.route("/download/<filename>")
def download(filename):
    return send_file(
        os.path.join(OUTPUT_FOLDER, filename),
        as_attachment=True
    )

if __name__ == "__main__":
    app.run(debug=True)