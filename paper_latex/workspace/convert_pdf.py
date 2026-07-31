import fitz # PyMuPDF
import os

pdf_path = '/ai-inventor/aii_data/runs/run_x0ETRmd6GgXY/4_gen_paper_repo/_4_assemble_paper/paper/workspace/paper.pdf'
output_dir = '/ai-inventor/aii_data/runs/run_x0ETRmd6GgXY/4_gen_paper_repo/_4_assemble_paper/paper/workspace/pdf_pages'
dpi = 150

def convert_pdf_to_png(pdf_path, output_dir, dpi):
    doc = fitz.open(pdf_path)
    for page_num in range(len(doc)):
        page = doc.load_page(page_num)
        pix = page.get_pixmap(matrix=fitz.Matrix(dpi / 72, dpi / 72))
        output_filename = os.path.join(output_dir, f'page_{page_num + 1}.png')
        pix.save(output_filename)
        print(f'Saved {output_filename}')
    doc.close()

convert_pdf_to_png(pdf_path, output_dir, dpi)
