from curriculo import extrair_texto_docx

def test_extrair_texto_docx_completo():
    texto = extrair_texto_docx("pytest/exemplo.docx")

    assert "Jezuino Motta" in texto
    assert "Formação Acadêmica" in texto
    assert "Experiência Profissional" in texto
    assert "Habilidades Técnicas" in texto
    assert "Idiomas" in texto
    assert len(texto) > 100  # Verifica se o texto tem conteúdo suficiente
