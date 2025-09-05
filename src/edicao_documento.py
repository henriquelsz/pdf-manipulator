import argparse
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.colors import white, Color
from PyPDF2 import PdfReader, PdfWriter
import io

def main():
    parser = argparse.ArgumentParser(description="Add an overlay to a PDF file.")
    parser.add_argument("--input", required=True, help="Path to the input PDF file.")
    parser.add_argument("--output", required=True, help="Path to the output PDF file.")
    args = parser.parse_args()

    # Ler PDF original
    reader = PdfReader(args.input)
    writer = PdfWriter()

    # Criar camada de sobreposição
    packet = io.BytesIO()
    can = canvas.Canvas(packet, pagesize=letter)

    # Configurar fonte e texto
    can.setFont("Helvetica-Bold", 12)
    text = "Comprovante de Matrícula 2025/2"
    text_width = can.stringWidth(text, "Helvetica-Bold", 12)

    # Centralizar mais abaixo (ajustando a posição)
    page_width, page_height = letter
    x = ((page_width - text_width) / 2) - 20
    y = page_height - 135  # posição ajustada

    # Fundo branco (retângulo atrás do texto)
    padding_x = 10
    padding_y = 5
    can.setFillColor(white)
    can.rect(x - padding_x, y - padding_y, text_width + 1 * padding_x, 20, fill=1, stroke=0)

    # Texto em cinza escuro (menos contraste)
    gray = Color(0.2, 0.2, 0.2)
    can.setFillColor(gray)
    can.drawString(x, y, text)

    # ---------- Data no canto direito ----------
    date_text = "01/08/25"
    can.setFont("Helvetica", 10)
    date_width = can.stringWidth(date_text, "Helvetica", 10)

    # Definir posição: canto direito, meio-superior
    dx = page_width - date_width - 62  # ajusta afastamento da borda direita
    dy = page_height - 224             # ajusta altura vertical

    # Fundo branco atrás da data
    can.setFillColor(white)
    can.rect(dx - 5, dy - 4, date_width + 7, 16, fill=1, stroke=0)

    # Data em cinza escuro
    can.setFillColor(gray)
    can.drawString(dx, dy, date_text)

    # --------------------------------------

    can.save()
    packet.seek(0)

    # PDF com sobreposição
    overlay_pdf = PdfReader(packet)

    # Mesclar a sobreposição na primeira página
    page = reader.pages[0]
    page.merge_page(overlay_pdf.pages[0])
    writer.add_page(page)

    # Adicionar as demais páginas
    for i in range(1, len(reader.pages)):
        writer.add_page(reader.pages[i])

    # Salvar
    with open(args.output, "wb") as f:
        writer.write(f)

    print(f"PDF gerado: {args.output}")

if __name__ == "__main__":
    main()
