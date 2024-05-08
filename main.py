from weasyprint import HTML

html_file='files/UseMeshesintheEditor.html'
pdf_file='UseMeshesintheEditor/pdf'
def convert_html_to_pdf(html_file, pdf_file):
    HTML(filename=html_file).write_pdf(pdf_file)