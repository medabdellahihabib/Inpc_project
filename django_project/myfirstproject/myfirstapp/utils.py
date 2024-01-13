# myfirstapp/utils.py
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from reportlab.pdfgen import canvas

def generate_pdf(predicted_inpc, prediction_date):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="prediction_report.pdf"'

    p = canvas.Canvas(response)

    # Début de la génération du contenu PDF
    p.setFont("Helvetica", 12)

    # Page 1: Prediction
    p.drawString(100, 800, "Page 1")
    p.drawString(100, 780, f"Prédiction INPC pour le {prediction_date.strftime('%F')} : {predicted_inpc:.2f}")

    # Page 2: Image
    p.showPage()
    p.drawString(100, 800, "Page 2")
    image_path_2 = "myfirstapp/images/page1.png"
    p.drawInlineImage(image_path_2, 100, 700, width=400, height=200)

    # Page 3: Image
    p.showPage()
    p.drawString(100, 800, "Page 3")
    image_path_3 = "myfirstapp/images/page3.png"
    p.drawInlineImage(image_path_3, 100, 700, width=400, height=200)

    # Fin de la génération du contenu PDF
    p.save()

    return response

