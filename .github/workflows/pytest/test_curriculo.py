from curriculo import extrair_texto_docx

def test_extrair_texto_docx():
    caminho = "pytest/exemplo.docx"
    texto = extrair_texto_docx(caminho)
    assert "Jezuino" in texto
    assert len(texto) > 10
