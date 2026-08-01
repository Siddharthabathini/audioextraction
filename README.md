# 🎵 Audio Extraction from Video

A simple and efficient web application that extracts audio from video files and converts them into high-quality audio formats such as MP3 and WAV. Built using **Python**, **Flask**, and **MoviePy**, this project provides an easy-to-use interface for uploading videos and downloading the extracted audio.

---

## 🚀 Features

- 📁 Upload video files through a web interface
- 🎵 Extract audio from videos
- 💾 Convert and save audio in MP3 or WAV format
- ⚡ Fast and simple processing
- 🌐 User-friendly Flask web application
- ❌ Error handling for unsupported or invalid files

---

## 🛠️ Tech Stack

### Frontend
- HTML5
- CSS3
- JavaScript

### Backend
- Python
- Flask

### Libraries
- MoviePy
- FFmpeg
- Werkzeug

---

## 📂 Project Structure

```
audio-extraction-from-video/
│
├── app.py
├── requirements.txt
├── README.md
├── uploads/
├── outputs/
│
├── templates/
│   ├── index.html
│   └── success.html
│
├── static/
│   ├── css/
│   ├── js/
│   └── images/
│
└── assets/
```

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/audio-extraction-from-video.git
```

### 2. Navigate to the project

```bash
cd audio-extraction-from-video
```

### 3. Create a virtual environment (Optional)

```bash
python -m venv venv
```

### 4. Activate the virtual environment

Windows

```bash
venv\Scripts\activate
```

Linux/Mac

```bash
source venv/bin/activate
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

### 6. Install FFmpeg

Download and install FFmpeg, then add it to your system PATH.

---

## ▶️ Run the Application

```bash
python app.py
```

Open your browser and visit

```
http://127.0.0.1:5000
```

---

## 📸 Screenshots

Add screenshots here.

Example:

- Home Page
- Upload Page
- Audio Download Page

---

## 📋 How It Works

1. Upload a supported video file.
2. The server processes the video using MoviePy.
3. Audio is extracted from the video.
4. The extracted audio is saved in the selected format.
5. The user can download the generated audio file.

---

## 📌 Supported Formats

### Input

- MP4
- AVI
- MOV
- MKV
- WMV

### Output

- MP3
- WAV

---

## 🔮 Future Enhancements

- Drag-and-drop file upload
- Batch video processing
- Progress bar during extraction
- Multiple output formats
- Audio trimming
- Audio quality selection
- User authentication
- Cloud storage integration

---

## 🤝 Contributing

Contributions are welcome!

1. Fork the repository.
2. Create a new feature branch.
3. Commit your changes.
4. Push to your branch.
5. Open a Pull Request.

---

## 📄 License

This project is licensed under the MIT License.

---

## 👨‍💻 Author

**Siddhartha Bathini**

- GitHub: https://github.com/yourusername
- LinkedIn: https://linkedin.com/in/yourprofile

---

## ⭐ Support

If you found this project helpful, consider giving it a ⭐ on GitHub!
