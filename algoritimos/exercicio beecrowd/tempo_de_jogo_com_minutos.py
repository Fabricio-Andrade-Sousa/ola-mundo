



hora_inicial, minuto_inicial, hora_final, minuto_final= input('').split()


hora_inicial = int(hora_inicial)
hora_final = int(hora_final)
minuto_inicial = int(minuto_inicial)
minuto_final = int(minuto_final)

    


if minuto_inicial <= minuto_final:
    minuto_jogado = minuto_final - minuto_inicial

else:
    minuto_jogado = 60 - minuto_inicial + minuto_final

if hora_inicial >= hora_final: 

    tempo_jogado = 24 - hora_inicial  + hora_final
    if tempo_jogado == 24 and minuto_inicial < minuto_final:
        tempo_jogado  = 0 
else:
    tempo_jogado = hora_final - hora_inicial

if minuto_final < minuto_inicial:
    tempo_jogado -= 1
print(f'O JOGO DUROU {tempo_jogado} HORA(S) E {minuto_jogado} MINUTO(S)')