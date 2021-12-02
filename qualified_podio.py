tempo_chegada1 = 120
tempo_chegada2 = 90
tempo_chegada3 = 110

def podio_olimpico(tempo_chegada1, tempo_chegada2, tempo_chegada3):
 
    tempo = sorted([tempo_chegada1, tempo_chegada2, tempo_chegada3])
    return (f'1 - {tempo[0]} minutos\n2 - {tempo[1]} minutos\n3 - {tempo[2]} minutos\n')
  
print(podio_olimpico(tempo_chegada1, tempo_chegada2, tempo_chegada3))