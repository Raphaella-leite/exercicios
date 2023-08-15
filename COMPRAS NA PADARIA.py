preco_pa= float(input("Qual preço de um único pão francês? "))
preco_banana= float(input("Qual preço de uma única banana? "))

preco_total_paes = (preco_pa * 5)
preco_total_bananas =(preco_banana *5)
preco_total_compra =(preco_total_paes + preco_total_bananas)

print(f'O preço total dos pães é RS: {preco_total_paes}')
print(f'O preço total das bananas é RS: {preco_total_bananas}')
print(f'O preço total da compra é RS: {preco_total_compra}')