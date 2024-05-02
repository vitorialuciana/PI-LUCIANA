perfumes = [
    {"nome":"quasar","marca":"boticario"},
    {"nome":"portiolli","marca":"jequiti"},
    {"nome":"kaiak","marca":"natura"},
]

def cadastroperfume():
    nome = input("digite o nome do perfume: ")
    marca = input("digite a marca: ")
    infos = {"nome":nome, "marca":marca}
    perfumes.append(infos)
    cheiro()
    

def cheiro():
    print(f'{'Nome perfume'.ljust(22)} | marca')
    for p in perfumes:
        nomeperfume= p("nome")
        marcaperfume= p("marca")
        print(f'{nomeperfume.ljust(22)} | {marcaperfume}')
        
def main():
    cadastroperfume()
    
    
        