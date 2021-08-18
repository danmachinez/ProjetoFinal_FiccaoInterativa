class Distancia:
    def __init__(self):
        self.km = 120

    def Avanca_Distancia(self):
        self.km -= 5
        if self.km in [100, 80, 60, 40, 20]:
            personagem.fome = personagem.sede = True
        if self.km in [95, 65, 35]:
            personagem.cansado = True        
        
        if personagem.fome == True:
            self.km -= 0
            return 'VOCÊ ESTÁ FAMINTO! Coma algo antes de prosseguir!'
        
        if personagem.cansado == True:
            self.km -= 0
            return 'VOCÊ ESTÁ EXAUSTO! Pare e descanse!'
        else:
            if self.km == 10 and self.km == 5:
                return f"******AGUENTA FIRME! Só faltam {self.km} Km!*******"
            elif self.km == 0:
                return "Parabéns! Você chegou à civilização!!"
            else:
                return f"AINDA FALTAM {self.km}KM!\n CONTINUE EM FRENTE!" 
            
class Personagem:
    def __init__(self):
        self.machucado = True
        self.fome = True
        self.sede = True
        self.cansado = False
        self.gritos = 0

        
    def __str__(self):
        return "Você está " + ("machucado" if personagem.machucado == True else "saudável")+",\n "+("sem" if personagem.fome == False else "com")+" fome, \n "+("com " if personagem.sede == True else "sem ")+"sede\n e "+('cansado!' if personagem.cansado == True else 'descansado!')
    
    def Dormir(self):
        self.cansado = False
        return 'Você recuperou suas energias. BORA CONTINUAR!!'

    def Beber(self):
        self.sede = False
        itens.cantil -= 1

    def jaGritou(self):
        self.gritos += 1
        if self.gritos > 0:
            return '<<<<<<  VOCÊ JA FEZ ISSO ANTES! Não adiantou de nada, aceite seu destino e continue o caminho!  >>>>>>>'            
        
class Itens:
    def __init__(self):
        self.primeirosSocorros = True
        self.barrinha = 3
        self.cantil = 2


    def Primeiros_Socorros(self):
        personagem.machucado = False

    def Barrinha(self):
        if self.barrinha == 0:
            
            return 'Você comeu todas as barrinhas disponíveis.'
        else:
            personagem.fome = False 
            objetosPersonagem['barrinhas de cereal'] -= 1
            self.barrinha -= 1
            return 'Nhac Nhac\n Cuidado! Suas barrinhas estão acabando!'   


def pergunta_opcao():
    escolha = (input("Escolha sua ação:"))
    try:
        return int(escolha)
    except ValueError as err:
        print('Você digitou uma letra! DIGITE UM NÚMERO!')
    return pergunta_opcao()

distancia = Distancia()
personagem = Personagem()
itens = Itens()

objetosPersonagem = {'Kit de primeiros socorros' : 1, 'barrinhas de cereal' : 3, 'Cantil' : 1}