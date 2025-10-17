# ==========================================
# SISTEMA CLÍNICA VIDA+
# Projeto Integrado - Cadastro de Pacientes
# ==========================================

def exibir_menu():
    print("\n=== SISTEMA CLÍNICA VIDA+ ===")
    print("1. Cadastrar paciente")
    print("2. Ver estatísticas")
    print("3. Buscar paciente")
    print("4. Listar todos os pacientes")
    print("5. Sair")

def cadastrar_paciente(pacientes):
    nome = input("Nome do paciente: ").strip()
    if not nome:
        print("❌ Nome não pode ser vazio!")
        return

    try:
        idade = int(input("Idade: "))
    except ValueError:
        print("❌ Idade inválida! Digite apenas números.")
        return

    telefone = input("Telefone: ").strip()
    pacientes.append({"nome": nome, "idade": idade, "telefone": telefone})
    print("✅ Paciente cadastrado com sucesso!")

def ver_estatisticas(pacientes):
    if not pacientes:
        print("⚠️ Nenhum paciente cadastrado ainda.")
        return

    total = len(pacientes)
    idade_media = sum(p["idade"] for p in pacientes) / total
    paciente_mais_novo = min(pacientes, key=lambda x: x["idade"])
    paciente_mais_velho = max(pacientes, key=lambda x: x["idade"])

    print("\n=== ESTATÍSTICAS ===")
    print(f"📋 Total de pacientes: {total}")
    print(f"📊 Idade média: {idade_media:.1f} anos")
    print(f"🧒 Paciente mais novo: {paciente_mais_novo['nome']} ({paciente_mais_novo['idade']} anos)")
    print(f"👴 Paciente mais velho: {paciente_mais_velho['nome']} ({paciente_mais_velho['idade']} anos)")

def buscar_paciente(pacientes):
    nome_busca = input("Digite o nome do paciente para buscar: ").strip().lower()
    resultados = [p for p in pacientes if nome_busca in p["nome"].lower()]

    if resultados:
        print("\n=== RESULTADOS DA BUSCA ===")
        for p in resultados:
            print(f"👤 Nome: {p['nome']} | Idade: {p['idade']} | Telefone: {p['telefone']}")
    else:
        print("❌ Nenhum paciente encontrado com esse nome.")

def listar_pacientes(pacientes):
    if not pacientes:
        print("⚠️ Nenhum paciente cadastrado ainda.")
        return

    print("\n=== LISTA DE PACIENTES ===")
    for i, p in enumerate(pacientes, start=1):
        print(f"{i}. Nome: {p['nome']} | Idade: {p['idade']} | Telefone: {p['telefone']}")

def main():
    pacientes = []
    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_paciente(pacientes)
        elif opcao == "2":
            ver_estatisticas(pacientes)
        elif opcao == "3":
            buscar_paciente(pacientes)
        elif opcao == "4":
            listar_pacientes(pacientes)
        elif opcao == "5":
            print("👋 Saindo do sistema... Até logo!")
            break
        else:
            print("❌ Opção inválida! Tente novamente.")

# Execução principal
if __name__ == "__main__":
    main()
