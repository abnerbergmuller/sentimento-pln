import re

stopwords = {
    "a", "o", "as", "os",
    "de", "do", "da", "dos", "das",
    "em", "no", "na", "e", "que", "com"
}

def limpar(texto, remover_stopwords=True):
     texto_lower = texto.lower()
     texto_lower_re = texto_lower.findall(r"[a-záàâãéêíóôõúçü]+", texto)
     texto_final = []
     if remover_stopwords:
         for palavra in texto_lower_re:
             if palavra not in stopwords:
                texto_final.append(palavra)
     return " ".join(texto_final)



