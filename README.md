# 🏗️ 3D Scene Builder with Natural Language Prompts

This project allows **non-technical users** to generate 3D scenes in Unity by simply typing a natural language prompt like:

> "A park with two benches, a tree, and a small fountain"

The system will:
1. Extract keywords from your prompt
2. Search and download relevant 3D models from **Sketchfab**
3. Automatically generate a Unity-compatible scene description (`scene.json`)
4. Load it in Unity using a SceneBuilder script

---

## ✨ Project Structure

3d-scene-builder/
│
├── backend/ # Python Flask API
│ ├── app.py # Main backend app
│ ├── utils/ # Keyword extraction
│ ├── sketchfab/ # Sketchfab model search + download
│ └── generator/ # Unity script + scene JSON generator
│
├── frontend/ # Simple HTML/CSS/JS prompt UI
│ ├── index.html
│ ├── style.css
│ └── script.js
│
├── output/ # Stores downloaded 3D models
│
├── .gitignore # Ignore files/folders (e.g. Unity project)
├── requirements.txt # Python dependencies
└── README.md # You're reading this 🙂

yaml
Copy
Edit

---

## 🚀 How to Run It

### 1. 🔧 Setup Python Backend

```bash
cd backend
python -m venv venv
venv\Scripts\activate  # (or source venv/bin/activate on Mac/Linux)
pip install -r ../requirements.txt
SKETCHFAB_API_TOKEN=your_token_here
python app.py
