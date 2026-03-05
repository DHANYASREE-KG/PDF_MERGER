# 📄 PDF Merger Web Application

A simple web application built using **Django** that allows users to upload multiple PDF files and merge them into a single PDF file.

This project demonstrates basic full-stack web development using Python and Django with PDF file handling.

---

## 🚀 Features

- Upload multiple PDF files
- Merge PDFs into a single file
- Remove selected files before merging
- Download the merged PDF
- Simple and user-friendly interface

---

## 🛠️ Technologies Used

- **Backend:** Python, Django
- **Frontend:** HTML, CSS, JavaScript
- **PDF Processing:** pypdf
- **Version Control:** Git, GitHub

---

## 📂 Project Structure

```
pdf_merger_project/
│
├── manage.py
├── pdf_merger/
│
├── merger/
│   ├── views.py
│   ├── urls.py
│   └── models.py
│
├── templates/
│   └── index.html
│
├── static/
│   ├── style.css
│   └── script.js
│
└── images/
    ├── home.png
    └── success.png
```

---

## 🖼️ Project Screenshots

### Main Interface

![Home Page](images/home.png)

### PDF Merge Success

![Success Page](images/success.png)

---

## ⚙️ How It Works

1. User selects multiple PDF files.
2. Files are uploaded to the Django backend.
3. The **pypdf** library reads each PDF.
4. All pages are merged into a single file.
5. The merged PDF is generated and downloaded.

---

## 💻 Installation

Clone the repository

```bash
git clone https://github.com/DHANYASREE-KG/PDF_MERGER.git
```

Move into the project folder

```bash
cd PDF_MERGER
```

Create a virtual environment

```bash
python -m venv venv
```

Activate the environment (Windows)

```bash
venv\Scripts\activate
```

Install dependencies

```bash
pip install django pypdf
```

Run the server

```bash
python manage.py runserver
```

Open the project in browser

```
http://127.0.0.1:8000/
```

---

## 📌 Future Improvements

- Drag and drop file upload
- PDF page reordering
- Add PDF split feature
- Deploy the application online

---

## 👩‍💻 Author

**Dhanya Sree K G**

GitHub: https://github.com/DHANYASREE-KG
