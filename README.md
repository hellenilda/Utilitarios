# **Conversor de PDF para Imagem (PNG/JPG)**  

Este projeto converte arquivos PDF em imagens (PNG ou JPG) utilizando Python com as bibliotecas `pdf2image` e `Poppler`.

---

## **📋 Pré-requisitos**  

### **1. Instalação do Python**  
- Certifique-se de ter o [Python](https://www.python.org/downloads/) instalado (versão 3.6 ou superior).  
- Verifique a instalação com:  
  ```bash
  python --version
  ```

### **2. Instale as bibliotecas necessárias**  
```bash
pip install -r requirements.txt
```

### **3. Instale o Poppler (Obrigatório para `pdf2image` no Windows)**  
- **Windows**:  
  - Baixe o Poppler [aqui](https://github.com/oschwartz10612/poppler-windows/releases).  
  - Extraia o arquivo ZIP em uma pasta (ex: `C:\poppler\poppler-23.11.0\bin`).  
  - (Opcional) Adicione o caminho `bin` ao `PATH` do sistema ou especifique-o no script.

- **Linux (Debian/Ubuntu)**:  
  ```bash
  sudo apt-get install poppler-utils
  ```

- **MacOS**:  
  ```bash
  brew install poppler
  ```  

---

## **📂 Estrutura do Projeto**  
```
pdf_to_image/
│
├── pdf_to_image.py       # Script principal
├── requirements.txt	  # Dependências do projeto
├── input/                # Pasta para PDFs de entrada (opcional)
└── output/               # Pasta padrão para imagens geradas
```

---

## **🚀 Executando o Script**  
1. Salve o código em um arquivo `pdf_to_image.py`.  
2. Execute no terminal:  
   ```bash
   python pdf_to_image.py
   ```
3. Siga as instruções interativas para informar:  
   - Caminho do PDF.  
   - Pasta de saída (padrão: `output`).  
   - Formato da imagem (`png` ou `jpg`).  
   - Resolução em DPI.  

---

## **⚠️ Solução de Problemas**  
- **Erro `PDFInfoNotInstalledError`**:  
  - Verifique se o Poppler está instalado e no `PATH`.

- **Erro de permissão**:  
  - Execute o script como administrador ou escolha uma pasta de saída acessível.  

- **PDFs muito grandes**:  
  - Reduza o `DPI` para economizar memória.  