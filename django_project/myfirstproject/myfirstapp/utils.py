# myfirstapp/utils.py
# myfirstapp/utils.py
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa

def generate_pdf(predicted_inpc):
    template_path = 'myfirstapp/pdf_template.html'  # Chemin du modèle HTML
    context = {'predicted_inpc': predicted_inpc}
    
    # Utilisez HttpResponse avec le type de contenu 'application/pdf'
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="prediction_report.pdf"'

    # Utilisez pisa pour générer le PDF à partir du modèle HTML
    template = get_template(template_path)
    html = template.render(context)
    pisa_status = pisa.CreatePDF(html, dest=response)

    if pisa_status.err:
        return HttpResponse('Error generating PDF', status=500)

    return response
