from datetime import timedelta
from random import randint
import time

#Horário da chegada da Van
chegada = (timedelta(hours=20))
print ("Chegada da Van ás",chegada)
print ("Das 20:00 ás 20:10:\n")

#Número de pessoas na fila ás 20:00hs (aleatório max= 15)
tamanhoDaFila = (randint(5,15))
print ("Chegaram na fila:",tamanhoDaFila, "pessoas")

#Criar a fila de acordo com o número aleatório e adicionar 10 minutos ao tempo de espera dos primeiros moradores
fila = []
tempoDeEspera = []
while tamanhoDaFila != 0:
    fila.append(1)
    tempoDeEspera.append(10)
    tamanhoDaFila -= 1

#Limite de inicio da entrega da comida
limite = (timedelta(hours=20,minutes=10))

#controle de minutos
contadorDeMinutos = 2
#Das 20:00 ás 20:10 (a cada 2 minutos 1 pessoa chega na fila e limite máximo da fila 15 pessoas)
while (len(fila)) <= 15 and chegada != limite:
    time.sleep(1.5)
    chegada = chegada + (timedelta(minutes=1))
    print ("Ás",chegada)
    print ("O tamanho da fila é:",len(fila),"\n")
    if contadorDeMinutos % 2 == 0:
        fila.append(1)
        tempoDeEspera.append(contadorDeMinutos + 10)
    contadorDeMinutos += 1

#Tempo em minutos é o resultado de X=resto da divisão dos últimos 2 dígitos do seu RM por 3 somado a 1 (RM88059)
tempoDeServirSopa = 59 % 3 + 1

#Sobra pra acrescentar ao tempo de espera aos próximo moradores que chegarem na fila
sobraDeTempo = contadorDeMinutos

#controle de minutos
contadorDeMinutos = 0

#Começar a servir a sopa
chegada = timedelta(hours=20,minutes=10)
print("Às",chegada,"Começa a servir a sopa\n")

#Servindo as sopas
while len(fila) > 0:
    time.sleep(1.5)
    chegada = chegada + (timedelta(minutes=1))
    contadorDeMinutos += 1
    
    #A cada 2 minutos 1 morador chega na fila
    if contadorDeMinutos %2 == 0 and len(fila) <= 15:
        fila.append(1)
        tempoDeEspera.append(sobraDeTempo + contadorDeMinutos)
        print("Ás",chegada)
        print("Chegou +1 morador de rua, total na fila:",len(fila),"\n")

    #A cada 3 minutos 3 pratos são servidos (fórmula RM)    
    if contadorDeMinutos % tempoDeServirSopa == 0:
        if len(fila) > 3:
            fila.pop()
            fila.pop()
            fila.pop()
            print("Ás",chegada)
            print("3 pratos servidos, na fila ainda:",len(fila),"\n")

        #Se o serviço durar mais de 30 minutos um ajudante voluntário também servirá 3 sopas a cada 3 minutos
        if contadorDeMinutos >= 30:
            print("Ás",chegada)
            print("Ajudante voluntário precisou ajudar")
            if len(fila) > 3:
                fila.pop()
                fila.pop()
                fila.pop()           
                print("3 pratos servidos pelo ajudante, na fila ainda:",len(fila),"\n")

    #Quando houver 3 ou menos moradores, haverá a última rodada de sopa para servir
    if len(fila) <= 3:
        fila = [] 
        print("Ás",chegada)
        print("Todos foram servidos, não há mais ninguém na fila")

        print("O tempo de espera respectivamente para cada morador foi:",tempoDeEspera)