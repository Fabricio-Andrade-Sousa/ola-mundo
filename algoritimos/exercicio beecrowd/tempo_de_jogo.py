tempo = input('').split(' ')
inicio = int(tempo[0])
fim = int(tempo[1])
if inicio >= fim : 
    tempo_jogado = 24 - inicio  + fim
else:
    tempo_jogado = fim - inicio 

print(f'O JOGO DUROU {tempo_jogado} HORA(S)')