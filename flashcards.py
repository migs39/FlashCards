import os
import subprocess
from random import shuffle as r
import datetime
tday = datetime.date.today()
pasta = r'C:\Users\monke\OneDrive\Área de Trabalho\Migs\flashcards'

def encontrar_materia(materia):
    caminho_materia = os.path.join(pasta, materia)
    
    if not os.path.exists(caminho_materia):
        os.makedirs(caminho_materia)
    return caminho_materia

def definir_local(materia):
    i = 1
    nome_arquivo = f"card{i}.txt"
    caminho_arquivo = os.path.join(materia, nome_arquivo)
    
    while os.path.exists(caminho_arquivo):
        i += 1
        nome_arquivo = f"card{i}.txt"
        caminho_arquivo = os.path.join(materia, nome_arquivo)
    with open(caminho_arquivo, 'w') as arquivo:
        pass
    
    return caminho_arquivo


class Cards:
    def __init__(self, pergunta, resposta, ultimoAcesso, local, streak):
        self.pergunta = pergunta
        self.resposta = resposta
        self.ultimoAcesso = ultimoAcesso #ultima vez que foi revisado
        self.local = local #local onde esta salvo
        self.streak = streak #quantidades de acertos seguidos atualmente

    def save(self):
        with open(self.local, 'w') as arquivo:
            arquivo.write(f"{self.pergunta}\n{self.resposta}\n{self.ultimoAcesso}\n{self.streak}")

    def force_review(self): #revisa mesmo se não for necssário. Não aumenta a streak
        revisou = self.revisar()
        if not revisou:
            print(self.pergunta)
            print('digite qualquer coisa para ver a resposta')
            macacosmemordam = input()
            print(self.resposta)
            acertou = 0
            while (acertou != '1') and (acertou != '2'):
                print('Digite 1 se acertou e 2 se errou')
                acertou = input()
                if acertou == 'getCard':
                    print(self.local)
            acertou = not (int(acertou)-1)
            if not acertou:
                self.streak = 0
            self.ultimoAcesso = tday
            self.save()

    def revisar(self):
        t = (tday - datetime.datetime.strptime(self.ultimoAcesso, "%Y-%m-%d").date()).days
        streak = self.streak
        #precisa vale True a depender da streak atual e de quanto tempo faz desde a ultima revisão
        precisa = (streak == 0 or streak == 1) and t>0
        precisa = precisa or (streak == 2 and t>1)
        precisa = precisa or (streak == 3 and t>3)
        precisa = precisa or ((streak == 4 or streak == 5) and t>6)
        precisa = precisa or ((streak == 6 or streak == 7 or streak == 8) and t>30)
        precisa = precisa or t>185
        #se precisa for True, revisa o flashcard
        if precisa:
            print(self.pergunta)
            print('digite qualquer coisa para ver a resposta')
            macacosmemordam = input()
            print(self.resposta)
            acertou = 0
            while (acertou != '1') and (acertou != '2'):
                print('Digite 1 se acertou e 2 se errou')
                acertou = input()
                if acertou == 'getCard':
                    print(self.local)
            acertou = not (int(acertou)-1)
            if acertou:
                self.streak +=1
            if not acertou:
                self.streak = 0
            self.ultimoAcesso = tday
            self.save()
        return precisa #retorna True se o flashcard foi revisado e False se não foi


def revisar_materia(materia): #revisa forçadamente (independente de streak e tempo de acesso) todos os cards de uma matéria
    cards = (os.listdir(materia))
    r(cards)
    for i in cards:
        c = import_card(os.path.join(materia, i))
        c.force_review()
    print('Foi revisado tudo que era necessário')



    
def newCard(pergunta, resposta, materia):
    materia = encontrar_materia(materia)
    local = definir_local(materia)
    card = Cards(pergunta, resposta, tday, local, 0)
    card.save()
    return card

def import_card(local): #cria um objeto da classe Cards baseado no arquivo salvo
    with open(local, 'r') as arquivo:
        linhas = arquivo.readlines()
        
        pergunta = linhas[0].strip()
        resposta = linhas[1].strip()
        ultimo_acesso = linhas[2].strip()
        streak = int(linhas[3].strip())
        
        card = Cards(pergunta, resposta, ultimo_acesso, local, streak)
        
        return card

def main():
    materias = os.listdir(pasta)
    print('\n\n-----------------------------------------------------------------------------------------------------------------------\nO que você deseja fazer?\n1) Revisar tudo')
    print('2) Revisar alguma matéria específica\n3) Criar um card novo')
    print('4) Sair')
    i=input()
    if i =='0':
        print('Lista de comandos adicionais:')
        print('0 para ver a lista de comandos adicionais')
        print('getFile para abrir a pasta com os flashcards salvos')
        print("getCard durante o comando 'digite 1 se arcertou e 2 se errou' para receber o local do card")
    if i == '1':
        allc = []
        for i in materias:
            m = os.path.join(pasta, i)
            ms = os.listdir(m)
            for j in ms:
                allc.append(os.path.join(m, j))
            r(allc)
            for i in allc:
                c = import_card(i)
                c.revisar()
        print('Foi revisado tudo que era necessário')
        main()
        return
    if i == '2':
        print("Qual matéria deseja revisar?")
        for i in range(len(materias)):
            print(f'{i+1}) {materias[i]}')
        i = input()
        try:
            revisar_materia(os.path.join(pasta, materias[int(i)-1]))
        except:
            print("valor invalido")
            main()
            return
        main()
        return
    if i == '3':
        print('A qual matéria você deseja adicionar o card?')
        for i in range(len(materias)):
            print(f'{i+1}) {materias[i]}')
        print(f'{len(materias)+1}) Criar uma nova')
        i = input()
        try:
            if int(i) == len(materias)+1:
                print("Pergunta:")
                pergunta = input()
                print("Resposta:")
                resposta = input()
                print("Materia")
                newCard(pergunta, resposta, os.path.join(pasta, input()))
            else:
                print("Pergunta:")
                pergunta = input()
                print("Resposta:")
                resposta = input()
                newCard(pergunta, resposta, os.path.join(pasta, materias[int(i)-1]))
            main()
            return
        except:
            print("valor invalido")
            main()
            return
    if i == '4':
        return
    if i == 'getFile':
        print(pasta)
        main()
        return
    print('valor invalido')
    main()
    return
        
main()
