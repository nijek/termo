import numpy as np
from unidecode import unidecode
from dicionario import dicionario

NUM_TENTATIVAS = 7
PALAVRAS = ["exemplo", "teste", "idoso"]

def para_string (lista):
    s = " "
    lista.sort()
    
    return s.join(lista) 

def printa_certas (letras, listaCertas, contaTentativas):
    if(contaTentativas == 0):
        palavra = "\n> "
    else:
        palavra = "\n  "

    for j in range (NUM_TENTATIVAS):
        for i in range (len(letras)):
            if listaCertas[j][i] == True: 
                palavra += letras[i]
            else: palavra += "*"
        if (j == contaTentativas - 1):
            palavra = palavra + "\n> "
        else:
            palavra = palavra + "\n  "
                
    return palavra

def lê_tentativa(palavra):
    def lê():
        return (unidecode(input("Palavra de " + str(tam) + " letras: (? para dica) "))).lower()
    while True:
        tentativa = lê()
        conta_dica = 0
        while '?' in tentativa:
           dica(palavra, conta_dica)
           tentativa = lê()
           conta_dica += 1
            
        if len(tentativa) != tam:
            print ("Chute uma palavra com o número de letras correto!!!")
            continue
        if tentativa not in dicionario:
            print ("Chute uma palavra que exista na língua portuguesa!!!")
            continue
        else:
            return tentativa

def dica(palavra, conta_dica):
    if conta_dica >= len(palavra):
        print("Você já sabe todas as letras!!!")
    else:
        print ("A " + str(conta_dica + 1) + "ª letra é " + palavra[conta_dica])
    


conta = 0
letrasErradas = []
letrasPosErrada = []
letrasPosCerta = []

for palavra in PALAVRAS:
    
    tam = len(palavra)
    letrasPosCerta = list(palavra)
    flagsPosCerta = np.full((NUM_TENTATIVAS, tam), False)
    contaTentativas = 0
    
    tentativa = lê_tentativa(palavra)

    while (tentativa != palavra):
        palavraLista = list(palavra)
        tentativaLista = list(tentativa)
        
        for i in range(len(palavraLista)):
            flagCerta = False
            if palavraLista[i] == tentativaLista[i] and flagsPosCerta[contaTentativas][i] == False:
                letrasPosCerta[i] = tentativaLista[i]
                flagsPosCerta[contaTentativas][i] = True
                flagCerta = True
                
            elif palavra.find(tentativaLista[i]) == -1:
                letrasErradas.append(tentativaLista[i])
            
            else: 
                letrasPosErrada.append(tentativaLista[i])

            if flagCerta and (tentativaLista[i] in letrasPosErrada):
                letrasPosErrada.remove(tentativaLista[i])    
                
        #elimina duplicadas
        letrasErradas = list(dict.fromkeys(letrasErradas))
        letrasPosErrada = list(dict.fromkeys(letrasPosErrada))
        
        print("Letras certas na posição certa: " + printa_certas(letrasPosCerta, flagsPosCerta, contaTentativas))
        print("Letras erradas: " + para_string(letrasErradas))
        print("Letras certas, mas na posição errada: " + para_string(letrasPosErrada))    
        
        contaTentativas += 1
        if (contaTentativas == NUM_TENTATIVAS):
            print("Perdeu pleyba HAHAHAH")
            quit()
        
        tentativa = lê_tentativa(palavra)      
        
    print("Parabéns, acertou a " + str((conta + 1)) + "ª palavra!!")
    
    letrasErradas.clear()
    letrasPosErrada.clear()
    letrasPosCerta.clear()
    conta += 1
print("\n\n\n\n!!!\nE aí, qual sua resposta :) :) :)\n!!!")
        
        
    
    
    
     
