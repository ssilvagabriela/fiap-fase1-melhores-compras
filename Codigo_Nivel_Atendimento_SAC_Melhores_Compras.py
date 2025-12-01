# Solicita o RM do aluno
rm = input("Insira seu RM: ")

# Solicita a nota de satisfação
nota = float(input("Digite a nota de satisfação (0 a 100): "))

# Verifica se a nota é válida
if nota < 0 or nota > 100:
    print("Nota inválida. A nota deve estar entre 0 e 100.")
else:
    # Classifica o atendimento com base na nota
    if nota >= 90:
        print(
            f"Aluno de RM {rm}, o atendimento foi classificado como: Atendimento de qualidade."
        )
    elif nota >= 70:
        print(
            f"Aluno de RM {rm}, o atendimento foi classificado como: Atendimento neutro."
        )
    else:
        print(
            f"Aluno de RM {rm}, o atendimento foi classificado como: Atendimento insatisfatório."
        )