
qtd_armas = int(input())
qtd = 0 
armas = {'HANDGUN':2, 'RED9':3.5,'BLACKTAIL':3.5,'MATILDA':2,'HANDCANNON':60,'STRIKER':12,'TMP':1.5,'RIFLE':12}
monstros = {'GANADOS' :40, 'COBRAS':50 ,'ZEALOT':75, 'COLMILLOS':60, 'GARRADOR':125, 'LASPLAGAS':100, 'GATLINGMAN':150, 'REGENERATOR':250, 'ELGIGANTE':500, 'DR.SALVADOR':350}

balas_utilizadas = 0
dano_causado = 0
qtd = 0 

while qtd != qtd_armas:
    entrada = input().split(' ')
    balas_utilizadas += int(entrada[1])
    dano_causado += int(entrada[1])*armas[entrada[0]]
    qtd +=1

vida_monstros = 0 
qtd_monstros = int(input())
qtd = 0 
while qtd != qtd_monstros:
    entrada_monstro = input().split(' ')
    vida_monstros += int(entrada_monstro[1])*monstros[entrada_monstro[0]]
    qtd +=1

qtd_balas = int(input())

print()
if qtd_balas > balas_utilizadas and vida_monstros <= dano_causado:
    print('Missao completada com sucesso')
else:
    print('You Are Dead')
print()

