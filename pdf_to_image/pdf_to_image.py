from pdf2image import convert_from_path
import os

def pdf_to_images(pdf_path, output_folder, fmt='png', dpi=200):
    """
    Converte um PDF em imagens (uma por página).
    """
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    # Caminho para o Poppler (ajuste conforme sua instalação)
    poppler_path = r"C:\poppler\poppler-23.11.0\bin"
    
    # Converter PDF em imagens
    images = convert_from_path(
        pdf_path,
        dpi=dpi,
        fmt=fmt,
        poppler_path=poppler_path  # <<< E AQUI
    )
    
    # Salvar cada página como imagem
    base_name = os.path.splitext(os.path.basename(pdf_path))[0]
    for i, image in enumerate(images):
        image.save(os.path.join(output_folder, f"{base_name}_page_{i+1}.{fmt}"))
        print(f"Página {i+1} salva como {base_name}_page_{i+1}.{fmt}")

if __name__ == "__main__":
    pdf_path = input("Digite o caminho do arquivo PDF: ").strip('"')
    output_folder = input("Digite a pasta de saída (padrão: 'output'): ").strip('"') or "output"
    fmt = input("Formato da imagem (png/jpg, padrão: png): ").lower().strip() or "png"
    dpi = int(input("DPI (resolução, padrão: 200): ") or 200)

    pdf_to_images(pdf_path, output_folder, fmt, dpi)