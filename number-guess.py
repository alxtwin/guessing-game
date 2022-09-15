from multiprocessing.sharedctypes import Value
from random import randint, choice

#code
#Armazena o número de tentativas; precisa ser otimizada para abarcar outros jogadores
tentativas = []
global tentativa
tentativa = 0


#Essa função armazena "ofensas" do desafiante Billy the Kid ao jogador cada vez que ele erra 
ofensas = ['Seus olhos estão cansados, caubói?! Você errou!',
           'Há! Minha vó atira melhor que você. Tente outra vez!',
           'Vou te dar uma colher de chá, caubói. Tente novamente!',
           'Tente outra vez, pistoleiro míope!',
           ]

#Essa função checa o placar. Precisa ser otimizada para abarcar outros jogadores
def check_placar():
    if len(tentativas) <= 0:
        print("Você não teve nenhuma tentativa. :(")
    else:
        # print("Você tem {} tentativas no placar.".format(len(tentativas)))
        # print("O gatilho mais rápido é de {} tentativas.".format(min(tentativas)))
        # print(f'Você acertou em {.format(tentativas.')
        print()
        print("a rapidez do seu gatilho é de {} tentativas.".format(len(tentativas)))
        print()
    
#Essa função guarda o texto de apresentação do jogo
def apresentacao():
    print()
    print("Bem vindo ao jogo de adivinhação, forasteiro.")
    print('Meu nome é Billy the Kid e eu sou o pistoleiro mais rápido do oeste.')
    print()
    print("Eu estou pensando em um número entre 1 e 10, e os alvos estão à sua frente.")
    print("Para ganhar, você deve atirar no número que estou pensando.")
    print()
    nome_jogador = input('Qual é o seu nome?: ')
    print()
    print(f"Bem vindo à cidade, caubói {nome_jogador}. Gostaria de me desafiar?")
    print()

def fora_do_alvo():
    print("(você não pode atirar fora do alvo)")
    print()
    
def acertou():
    print("Na mosca, caubói!")
    global tentativa
    tentativa+=1
    tentativas.append(tentativa)
    # print(f'Você acertou em {tentativa} tentativas.')
    
def mais_baixo():
    print(choice(ofensas),"Mire mais baixo!")
    print()
    global tentativa
    tentativa+=1
    tentativas.append(tentativa)
    
def mais_alto():
    print(choice(ofensas),"Mire mais alto!")
    print()
    global tentativa

    tentativa+=1
    tentativas.append(tentativa)

#Nessa função estão contidos todos os comandos do jogo 
def start_jogo():
    numero_gerado = randint(1, 10)    
    print("(digite sim ou não)")
    escolha = input()
   
    while escolha.lower() == 'sim':
        print()
        print("Atire no número que eu estou pensando!")
        print('(digite um número de 1 a 10)')
        try:
          
            tiro = int(input())
            
            # if tiro != numero_gerado:
            #     print(choice(ofensas))
            #     tentativa +=1
            #     print()
            
            if tiro < 1 or tiro > 10:
                # print("Você não pode atirar fora do alvo!")
                fora_do_alvo()
                
            if int(tiro) == numero_gerado:
                acertou()     
                # print("Na mosca, caubói!")
                # tentativa+=1
                # tentativas.append(tentativa)
                # print(f'Você acertou em {tentativa} tentativas.')
                break
            
            elif tiro > numero_gerado:
               mais_baixo()
                
            elif tiro < numero_gerado:
                mais_alto()
                # print(choice(ofensas),"Mire mais alto!")
                # print()
                # tentativa+=1
                # tentativas.append(tentativa)
                
        except ValueError:
            print("(você não pode atirar fora do alvo)")
            print()
            continue
    if escolha.lower() != 'sim' and escolha.lower() != 'não' and escolha.lower() != 'nao':
        print()
        print('Não entendi porcaria nenhuma!')
        start_jogo()
    else:
        print()
        print("Eu sabia que essa cidade era pequena demais para nós dois...")
        check_placar()
        print()
        quit()
        
    check_placar()
    try:
        print("Gostaria de jogar novamente?")
        start_jogo()
    except ValueError:
        print("Até a próxima!")


if __name__ == '__main__':

    apresentacao()
    start_jogo()

            
    
        
