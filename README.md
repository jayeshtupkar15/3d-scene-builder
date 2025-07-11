# 🏗️ 3D Scene Builder with Natural Language Prompts

This project allows **non-technical users** to generate 3D scenes in Unity by simply typing a natural language prompt like:

> "A park with two benches, a tree, and a small fountain"

The system will:
1. Extract keywords from your prompt
2. Search and download relevant 3D models from **Sketchfab**
3. Automatically generate a Unity-compatible scene description (`scene.json`)
4. Load it in Unity using a SceneBuilder script

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
