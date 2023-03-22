email_tmpl = """
Olá, %(nome)s

Tem interesse de comprar %(produto)s?

Esse produto é ótimo para 
%(texto)s

Clique agora no link %(link)s

Apenas %(quantidade)d disponíveis.

Preço promocional R$ %(preco).2f
"""

clientes = ["Maria", "João", "Paulo"]

for cliente in clientes:
    print(email_tmpl % {
            "nome": cliente,
            "produto": "Caneta",
            "texto": "escrever seu testamento",
            "quantidade": 1,
            "preco": 40.34,
        }
    )
