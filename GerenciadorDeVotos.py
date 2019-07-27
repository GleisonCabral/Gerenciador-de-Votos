#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 24 19:03:25 2019

@author: Gleison Alves
"""
import os
import time

class candidato():
    
    def __init__(self, codCan, nome, cargo, regiao, qtdVot):
        self.codCan = codCan
        self.nome = nome
        self.cargo = cargo
        self.regiao = regiao
        self.qtdVot = qtdVot
        
    def __str__(self):
        return '{} {} {} {} {}'.format(self.codCan,self.nome,
                self.cargo,self.regiao,self.qtdVot)



c1 = candidato('01', 'Francisco' , 'Vereador', 'Sul', 40)
c2 = candidato('02', 'Joao' , 'Vereador', 'Norte', 10)
c3 = candidato('03', 'Maria' , 'Vereador', 'Norte', 13)
c4 = candidato('04', 'Joana' , 'Vereador', 'sul', 15)
c5 = candidato('05', 'Lucia' , 'Vereador', 'Norte', 21)
c6 = candidato('06', 'Jorge' , 'Vereador', 'sul', 42)
c7 = candidato('07', 'Luiz' , 'Vereador', 'sul', 41)
c8 = candidato('08', 'jose' , 'Vereador', 'sul', 19)
c9 = candidato('09', 'Pedro' , 'Vereador', 'leste', 22)
c10 = candidato('10', 'Manoel' , 'Vereador', 'leste', 10)
c11 = candidato('11', 'Miguel' , 'Vereador', 'leste', 7)
c12 = candidato('12', 'Paulo' , 'Vereador', 'Norte', 7)
c13 = candidato('13', 'Tereza' , 'Vereador', 'Oeste', 2)
c14 = candidato('14', 'Helena' , 'Vereador', 'Oeste', 50)
c15 = candidato('15', 'Gloria' , 'Vereador', 'Norte', 42)
c16 = candidato('16', 'Geraldo' , 'Vereador', 'Norte', 30)
c17 = candidato('17', 'Marta' , 'Vereador', 'Leste', 30)
c18 = candidato('18', 'Marcia' , 'Vereador', 'Sul', 30)
c19 = candidato('19', 'Julia' , 'Vereador', 'Sul', 28)
c20 = candidato('20', 'Sebastiao' , 'Vereador', 'Norte', 19)     

arquivo = []

arquivo.append(c1)
arquivo.append(c2)
arquivo.append(c3)
arquivo.append(c4)
arquivo.append(c5)
arquivo.append(c6)
arquivo.append(c7)
arquivo.append(c8)
arquivo.append(c9)
arquivo.append(c10)
arquivo.append(c11)
arquivo.append(c12)
arquivo.append(c13)
arquivo.append(c14)
arquivo.append(c15)
arquivo.append(c16)
arquivo.append(c17)
arquivo.append(c18)
arquivo.append(c19)
arquivo.append(c20)




def listarCandidatos(dadosControle):
    print(f'\033[33m{"Lista de Candidatos": ^80}\033[m\n\n')
    print('Codigo - Nome\n')
    for i in range(0,len(dadosControle)):
        aux = dadosControle[i].split()
        print(aux[0]+ ' - ' + aux[1])


def votosPorCandidatos(dadosControle):
    print(f'\033[33m{"Relação de Votos por Candidatos": ^80}\033[m\n\n')
    print('Cadastro - Nome - Votos\n\n')
    for i in range(0,len(dadosControle)):
        aux = dadosControle[i].split()
        print('Candidato: {} - {} ----------  Votos: {} '.format(aux[0],aux[1],aux[4]))

def votosPorCandidatoRegiao(dadosControle):
    print(f'\033[33m{"Votos por candidatos e região": ^80}\033[m\n\n')
    rNorte = []
    rSul = []
    rLeste = []
    rOeste = []
    tvNorte = 0
    tvSul = 0
    tvLeste = 0
    tvOeste = 0
    
    for i in range(0,len(dadosControle)):
        aux = dadosControle[i].split()
        if aux[3] == 'Norte' or aux[3] == 'norte':
            rNorte.append('Candidato: {} - {} ------ Votos: {}'.format(aux[0], aux[1],aux[4]))
            tvNorte += int(aux[4])
        elif aux[3] == 'Sul' or aux[3] == 'sul':
            rSul.append('Candidato: {} - {} ------ Votos: {}'.format(aux[0], aux[1],aux[4]))
            tvSul += int(aux[4])
        elif aux[3] == 'Leste' or aux[3] == 'leste':
            rLeste.append('Candidato: {} - {} ------ Votos: {}'.format(aux[0], aux[1],aux[4]))
            tvLeste += int(aux[4])
        elif aux[3] == 'Oeste' or aux[3] == 'oeste':
            rOeste.append('Candidato: {} - {} ------ Votos: {}'.format(aux[0], aux[1],aux[4]))
            tvOeste += int(aux[4])
    
    print('Candidatos da região NORTE')
    ordernar = sorted(rNorte)       
    for x in ordernar:
        print(str(x))
    print('\nTotal de votos: {}\n\n'.format(tvNorte))
    
    print('\n\nCandidatos da região SUL')
    ordernar = sorted(rSul)       
    for x in ordernar:
        print(str(x))
    print('\nTotal de votos: {}'.format(tvSul))
    
    print('\n\nCandidatos da região LESTE')
    ordernar = sorted(rLeste)       
    for x in ordernar:
        print(str(x))
    print('\nTotal de votos: {}'.format(tvLeste))
    
    print('\n\nCandidatos da região OESTE')
    ordernar = sorted(rOeste)       
    for x in ordernar:
        print(str(x))
    print('\nTotal de votos: {}'.format(tvOeste))


def cabecalho():
    os.system('cls||clear')   
    print(f'{"*" * 80}\n') 
    print(f'\033[32m{"Controle de Votos": ^80}\033[m\n\n')
    print(f'{"*" * 80}\n')


cabecalho()
try:
    arq = open('controleVotos.dat','r')
    txt = arq.readlines()
    arq.close()
    print(f'\033[36m{":) Dados Carregados com sucesso !": ^80}\033[m\n\n')
except:
    arq = open('controleVotos.dat','w')
    print(f'\033[31m{":( Dados Não Existem !": ^80}\033[m\n\n')
    for c in arquivo:
        arq.write(str(c)+'\n')
    arq.close()
    print(f'\033[34m{"Criando dados de teste. AGUARDE..." : ^80}\033[m\n\n')
    time.sleep(3)
    arq = open('controleVotos.dat','r')
    txt = arq.readlines()
    arq.close()
    print(f'\033[36m{" :) Dados Criados e carregados com sucesso": ^80}\033[m\n\n')
    

time.sleep(2)

while(True):

    cabecalho()
    print('\n\nMENU \n\n(1)-Listar Candidatos\n(2)-Listar Candidatos e votos\n(3)-Listar Votos Por Regiao\n(4)-Sair')
    op = input('\nEscolha uma opção: ')

    if(op == '1'):
        cabecalho()
        listarCandidatos(txt)
        print('\n\nFINALIZADO.\n')
        op2 = input('Precione ENTER para voltar ou digite (s) para SAIR: ')

        if op2 == 's' or op2 == 'S':
            break
        
    elif(op == '2'):
        cabecalho()
        votosPorCandidatos(txt)
        print('\n\nFINALIZADO.\n')
        op2 = input('Precione ENTER para voltar ou digite (s) para SAIR: ')

        if op2 == 's' or op2 == 'S':
            break
        
    elif(op == '3'):
        cabecalho()
        votosPorCandidatoRegiao(txt)
        print('\n\nFINALIZADO.\n')
        op2 = input('Precione ENTER para voltar ou digite (s) para SAIR: ')

        if op2 == 's' or op2 == 'S':
            break
        
    elif(op == '4'):
       break
   
    else:
        cabecalho()
        print('\n\n')
        print(f'\033[31m{":( Opçao não existe !": ^80}\033[m]\n\n')
        op2 = input('Precione ENTER para voltar ou digite (s) para SAIR: ')

        if op2 == 's' or op2 == 'S':
            break