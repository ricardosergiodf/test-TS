def calcular_percentuais(faturamentos):
    total = sum(faturamentos.values())
    percentuais = {}

    for estado, valor in faturamentos.items():
        percentual = (valor / total) * 100
        percentuais[estado] = percentual

    return percentuais

faturamentos = {
    "SP": 67836.43,
    "RJ": 36678.66,
    "MG": 29229.88,
    "ES": 27165.48,
    "Outros": 19849.53
}

percentuais = calcular_percentuais(faturamentos)

for estado, percentual in percentuais.items():
    print(f"{estado}: {percentual:.2f}%")

