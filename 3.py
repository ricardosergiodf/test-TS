import json

with open('dados.json', 'r') as f:
    dados = json.load(f)

faturamento = [dia['valor'] for dia in dados if dia['valor'] > 0]
print(faturamento)

media_faturamento = 0

for valor in faturamento:
    media_faturamento += valor

maior_faturamento = max(faturamento)
menor_faturamento = min(faturamento)
media_faturamento = media_faturamento / len(faturamento)

dias_acima_media = sum(1 for v in faturamento if v > media_faturamento)

print(f'Maior faturamento: {maior_faturamento}\nMenor faturamento: {menor_faturamento}\nMedia faturamento: {media_faturamento}\nDias acima da media: {dias_acima_media}')