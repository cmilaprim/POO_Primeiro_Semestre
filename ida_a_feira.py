ida_a_feira = int(input())
for _ in range(ida_a_feira):
    produtos = dict()
    qtd_disponivel = int(input())
    for _ in range(qtd_disponivel):
        fruta, preço = input().split()
        produtos[fruta] = float(preço)
            
    num_compra = int(input())
    quantidade = 0.0
    for _ in range(num_compra):
        fruta, unidade = input().split()
    
        quantidade += int(unidade) * produtos[fruta]
    print(f'R${quantidade:.2f}')