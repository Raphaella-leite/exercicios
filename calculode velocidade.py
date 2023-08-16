print("Limite de velocidade: 70 km/h")

print ("Valor aplicado por km/h acima do limite: R$0.90")

 
vel_Louzada = 85
limite_velo = 70

limite_ultrapassado = (vel_Louzada - limite_velo)

multa = (limite_ultrapassado * 0.9)

print(f"O professor estava acima do limite! Iremos emitir uma multa!")

print(f'Velocidade acima do limite: {vel_Louzada} km/h.') 

print(f'Multa aplicada R$:{multa}')