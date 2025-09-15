# 📄 Analisador de Currículos ATS com IA

Este projeto tem como objetivo criar um sistema inteligente para analisar currículos e verificar sua compatibilidade com sistemas de rastreamento de candidatos (ATS). Utiliza Python, Streamlit e IA generativa (Google Gemini) para oferecer recomendações personalizadas.

---

## 🚀 Funcionalidades

- Upload de currículos em `.pdf`, `.docx` ou `.txt`
- Entrada de requisitos da vaga em linguagem natural
- Análise com IA para pontuação ATS
- Justificativas e recomendações geradas automaticamente
- Interface web interativa com Streamlit

---

## 🧠 Tecnologias utilizadas

- Python 3.10+
- Streamlit
- Google Gemini API
- pdfminer.six / python-docx
- dotenv / requests

---

## 📦 Instalação

```bash
git clone https://github.com/jfmotta/cv.git
cd cv
python -m venv .venv
source .venv/bin/activate  # ou .venv\\Scripts\\activate no Windows
pip install -r requirements.txt
