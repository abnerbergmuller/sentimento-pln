import pandas as pd
import numpy as np
import sklearn as sk

avaliacoes = "data/Avaliacoes.csv"
exploracao = "resultados/exploracao.txt"

df = pd.read_csv(avaliacoes)

with (open(exploracao, mode="w",encoding="utf-8") as ex_df):
    total_linhas = len(df).__str__()
    ex_df.write(f"Total de linhas: {total_linhas}\n\n")
    print(total_linhas)

    linhas_sentimento = df["sentimento"].value_counts().__str__()
    ex_df.write(f"Linhas por sentimento: \n{linhas_sentimento}\n\n")
    print(linhas_sentimento)

    palavras_por_texto = df["texto"].str.split().str.len()
    palavras_por_classe = palavras_por_texto.groupby(df["sentimento"]).mean().__str__()
    ex_df.write(f"Média de palavras por classe:\n{palavras_por_classe}\n\n")
    print(palavras_por_classe)

    exemplos_positivos = df[df["sentimento"] == "positivo"]["texto"].head(3)
    exemplos_negativos = df[df["sentimento"] == "negativo"]["texto"].head(3)

    ex_df.write("Exemplos positivos: \n")
    for texto in exemplos_positivos:
        ex_df.write(f"- {texto}\n")
        print(f"- {texto}\n")

    ex_df.write("\nExemplos negativos: \n")
    for texto in exemplos_negativos:
        ex_df.write(f"- {texto}\n")
        print(f"- {texto}\n")




