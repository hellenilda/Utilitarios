from PIL import Image
import os

def images_to_pdf(input_folder, output_pdf, img_format='png'):
    """
    Converte imagens (PNG/JPG) em um único PDF.
    
    Args:
        input_folder (str): Pasta contendo as imagens.
        output_pdf (str): Nome do arquivo PDF de saída.
        img_format (str): Formato das imagens ('png' ou 'jpg').
    """
    images = []
    
    # Lista arquivos na pasta e filtra por formato
    for filename in sorted(os.listdir(input_folder)):
        if filename.lower().endswith((f'.{img_format}', f'.{img_format.upper()}')):
            img_path = os.path.join(input_folder, filename)
            images.append(Image.open(img_path).convert('RGB'))  # Converte para RGB (necessário para PDF)
    
    if not images:
        print(f"❌ Nenhuma imagem .{img_format} encontrada em '{input_folder}'.")
        return
    
    # Salva o PDF
    output_path = output_pdf if output_pdf.endswith('.pdf') else f"{output_pdf}.pdf"
    images[0].save(
        output_path,
        save_all=True,
        append_images=images[1:],
        resolution=100  # DPI (opcional)
    )
    print(f"✅ PDF criado com sucesso: '{output_path}' ({len(images)} imagens convertidas).")

if __name__ == "__main__":
    print("\n🖼️📄 Conversor de Imagens para PDF")
    
    # Entradas interativas
    input_folder = input("Digite a pasta com as imagens: ").strip('"')
    output_pdf = input("Nome do PDF de saída (sem extensão): ").strip()
    img_format = input("Formato das imagens (png/jpg, padrão: png): ").lower().strip() or "png"
    
    images_to_pdf(input_folder, output_pdf, img_format)