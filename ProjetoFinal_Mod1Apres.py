from modulosProjeto import *

if(__name__ == "__main__"):
    Fase0 = input('Deseja iniciar o jogo mais emocionante de sua vida? [Sim/Não] ').title().replace('a', 'ã')
    print()
    if Fase0 not in 'SimNão':
        Fase0 = input('RESPOSTA INVÁLIDA! Deseja iniciar o jogo mais emocionante de sua vida? [Sim/Não] ').title().replace('a', 'ã')
    if Fase0 == "Sim":
        print("---")
        print('... "O HELICÓPTERO EM QUE VOCÊ ESTAVA CAIU. \nOS EQUIPAMENTOS ELETRÔNICOS ESTÃO INUTILIZÁVEIS. \nA ÚLTIMA CIDADE QUE VOCÊ AVISTOU SE ENCONTRA A 120KM AO NORTE."...')
        print()
        print("Você acorda em um descampado, com pedaços de metal e objetos caídos a sua volta.\n Você olha ao redor e encontra alguns itens úteis:")
        print()
        while objetosPersonagem['Kit de primeiros socorros'] != 0:
            print(f'''Você possui os seguintes itens:
            {objetosPersonagem['Kit de primeiros socorros']} - Kit de primeiros socorros
            {objetosPersonagem['barrinhas de cereal']} - Barrinhas de cereal
            {objetosPersonagem['Cantil']} - Cantil
            ''')
            print()
            print(personagem)
            print()
            print("Ações:")
            print("1 - Usar o Kit de primeiros socorros")
            print("2 - Comer uma barrinha de cereal")
            print("3 - Vereficar se o cantil contém algo")
            print("4 - Gritar por socorro!")
            print("5 - Vasculhar o helicóptero")
            print("0 - Sair do jogo")
            opcao = pergunta_opcao()
            print()
            if opcao == 1:
                itens.Primeiros_Socorros()
                print('Você utilizou o Kit de Primeiros socorros e não está mais machucado!')
                objetosPersonagem['Kit de primeiros socorros'] -=1
                print()
                print('***Comece a andar! A cidade mais próxima fica a 120 km.***')
                print()
            elif opcao == 2:
                print(itens.Barrinha())
                print()
            elif opcao == 3:
                if itens.cantil == 2:
                    print('Você achou água!')
                    beber = input('Deseja bebê-la? [S/N]').upper()
                    if beber == 'S':
                        personagem.Beber()
                print()
                print('***Comece a andar! A cidade mais próxima fica a 120 km.***')
                print()
            elif opcao == 4:
                if personagem.gritos > 0:  
                    print(personagem.jaGritou())
                else:
                    print('Você grita desesperadamente por socorro, mas não ouve nada além do som dos pássaros a sua volta!')
                    personagem.jaGritou()
                print()
                print('***Comece a andar! A cidade mais próxima fica a 120 km.***')
                print()
            elif opcao == 5:
                print('Você acha a carcaça do helicóptero mas não encontra nada além do corpo do piloto e de seu amigo. FeelsBad\n Você olha para o lado e encontra mais uma barrinha de cereal.  ' )
                objetosPersonagem['barrinhas de cereal'] += 1
                itens.barrinha += 1
                print()
                print('***Comece a andar! A cidade mais próxima fica a 120 km.***')
                print()
            elif opcao == 0:
                break
            else:
                print("Opção inválida!")
    print()
    print('Você está perdido! Seu senso de direção te diz que o caminho mais seguro a percorrer é seguindo o curso do rio.')
    print()
    while distancia.km > 0:
        print()
        print(f'''Você possui os seguintes itens:
        {objetosPersonagem['barrinhas de cereal']} - Barrinhas de cereal
        {objetosPersonagem['Cantil']} - Cantil
        ''')
        print(personagem)
        print()
        print("Ações:")
        print("1 - Seguir o curso do rio em busca da cidade")
        print("2 - Comer uma barrinha de cereal")
        print("3 - Beber água")
        print("4 - Gritar por socorro!")
        print("5 - Pegar água do rio")
        print("6 - Montar acampamento e descansar")
        print("0 - Sair do jogo")
        print()
        opcao = pergunta_opcao()
        print()
        if opcao == 1:
            print(distancia.Avanca_Distancia())
        elif opcao == 2:
            print(itens.Barrinha())
            print()             
        elif opcao == 3:
            personagem.Beber()
            if itens.cantil == 0:
                print('Sua água chegou ao fim! Encontre mais água!!!')
                print()
            else:
                print('Glub, glub, glub ...')
                print()
        elif opcao == 4:
            if personagem.gritos > 0:  
                print(personagem.jaGritou())
                print()
            else:
                print('Você grita desesperadamente por socorro, mas não ouve nada além do som dos pássaros a sua volta!')
                personagem.jaGritou()
                
        elif opcao == 5:
            if itens.cantil == 2:
                print('Você não tem espaço para armazenar a água. SEU CANTIL ESTÁ CHEIO! ')
            elif itens.cantil == 1:
                print('Você coletou apenas 1L de água do rio, pois seu cantil estava pela metade.')
                itens.cantil += 1
                escolha = input('Você pisou em algo estranho! Gostaria de conferir o que é? [S/N]').upper()
                if escolha == 'S':
                    print('OLHA QUE SORTE! Você encontrou mais uma barrinha de cereal!')
                    itens.barrinha += 1
                    objetosPersonagem['barrinhas de cereal'] += 1
            else:
                print('Você coletou 2L de água do rio.')               
                itens.cantil += 2
                escolha = input('Você pisou em algo estranho! Gostaria de conferir o que é? [S/N]').upper()
                if escolha == 'S':
                    print('OLHA QUE SORTE! Você encontrou mais uma barrinha de cereal!')
                    itens.barrinha += 1  
                    objetosPersonagem['barrinhas de cereal'] += 1              
        elif opcao == 6:
            print()
            print(personagem.Dormir())
        elif opcao == 0:
            break
        else:
            print("Opção inválida!")
            