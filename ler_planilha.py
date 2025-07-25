import pandas as pd

def carregar_emails():
    # Como o arquivo está na mesma pasta, só o nome do arquivo basta
    df = pd.read_excel('lista de emails.ods', engine='odf')

    lista = []
    
    for _,row in df.iterrows():
        nome =row["Nome"]
        email = row["Email"]
        lista.append({"nome":nome,"email":email})
    return lista 

print(carregar_emails())