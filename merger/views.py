from django.shortcuts import render
from django.http import HttpResponse
from pypdf import PdfReader, PdfWriter
from io import BytesIO
import base64


def home(request):
    return render(request, "index.html")


def merge_pdfs(request):
    if request.method == "POST":
        files = request.FILES.getlist("files")  # MUST MATCH HTML NAME

        if len(files) < 2:
            return render(request, "index.html", {
                "error": "Please upload at least 2 PDF files."
            })

        writer = PdfWriter()

        for file in files:
            reader = PdfReader(file)
            for page in reader.pages:
                writer.add_page(page)

        output = BytesIO()
        writer.write(output)

        # Convert to base64 (JSON safe for session)
        encoded_pdf = base64.b64encode(output.getvalue()).decode("utf-8")
        request.session["merged_pdf"] = encoded_pdf

        return render(request, "index.html", {
            "success": True,
            "default_name": "merged_file"
        })

    return render(request, "index.html")


def download_pdf(request):
    encoded_pdf = request.session.get("merged_pdf")

    if not encoded_pdf:
        return HttpResponse("No file available.")

    filename = request.GET.get("filename", "merged_file") + ".pdf"

    pdf_bytes = base64.b64decode(encoded_pdf)

    response = HttpResponse(pdf_bytes, content_type="application/pdf")
    response["Content-Disposition"] = f'attachment; filename="{filename}"'

    return response