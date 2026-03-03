# 📄 PDF Merger

A simple and clean web application to merge multiple PDF files into one, built with **Django**.

## Features
- Upload multiple PDF files
- Merge them into a single PDF instantly
- Download the merged PDF with a custom filename
- Clean, responsive UI

## Tech Stack
- **Backend**: Django (Python)
- **Frontend**: HTML, CSS, JavaScript (served via Django templates)
- **PDF Processing**: pypdf

## Local Setup

### 1. Clone the repository
```bash
git clone https://github.com/YOUR_USERNAME/pdf-merger.git
cd pdf-merger
```

### 2. Create and activate a virtual environment
```bash
python -m venv venv
# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the development server
```bash
python manage.py migrate
python manage.py runserver
```

Open your browser and go to: `http://127.0.0.1:8000`

## Deployment (Render)

This app is deployed on [Render](https://render.com).

### Steps to deploy:
1. Push this repo to GitHub.
2. Create a new **Web Service** on Render.
3. Connect your GitHub repo.
4. Set:
   - **Build Command**: `chmod a+x build.sh && ./build.sh`
   - **Start Command**: `gunicorn pdf_merger.wsgi:application`
5. Add Environment Variables:
   - `SECRET_KEY` = (a long random string)
   - `RENDER` = `True`

## Project Structure
```
pdf_merger_project/
├── merger/             # Django app (views, urls, models)
├── pdf_merger/         # Project settings and wsgi
├── templates/          # HTML templates
├── static/             # CSS and JS files
├── build.sh            # Render build script
├── requirements.txt    # Python dependencies
└── manage.py
```

## License
MIT
