vagas = {
    "Vaga 1": ["Python", "Programação", "Desenvolvimento"],
    "Vaga 2": ["Análise de dados", "Dados", "SQL"]
}

inscritos = {vaga: 0 for vaga in vagas}
validos = {vaga: 0 for vaga in vagas}

while True:
    vaga_escolhida = input("Para qual vaga você se inscreveu? (Digite o número da vaga 1 ou 2, ou 0 para sair): ")

    if vaga_escolhida == '0':
        break

    if vaga_escolhida not in ('1', '2'):
        print("Vaga inválida. Tente novamente.")
        continue

    vaga = f"Vaga {vaga_escolhida}"

    resumo = input("Por favor, insira um resumo do seu currículo: ")
    palavras_chave = resumo.split()

    if any(palavra in palavras_chave for palavra in vagas[vaga]):
        validos[vaga] += 1

    inscritos[vaga] += 1

print("\nResumo da inscrição:\n")
for vaga, total_inscritos in inscritos.items():
    total_validos = validos[vaga]
    print(f"{vaga}:")
    print(f"Total de inscritos: {total_inscritos}")
    print(f"Total de candidatos válidos: {total_validos}\n")
