import os


def carregarArquivo(nomeArquivo):
    if not os.path.exists(nomeArquivo):
        with open(nomeArquivo, "w", encoding="utf-8") as f:
            pass
        return []
    with open(nomeArquivo, "r", encoding="utf-8") as f:
        linhas_limpas = []
        for linha in f.readlines():
            linhas_limpas.append(linha.rstrip("\n"))
        return linhas_limpas


def salvarArquivo(nomeArquivo, linhas):
    with open(nomeArquivo, "w", encoding="utf-8") as f:
        for linha in linhas:
            f.write(linha + "\n")
    print(f"\n[OK] Arquivo '{nomeArquivo}' salvo no disco com sucesso!")


def menuEdicao(nomeArquivo):
    linhas = carregarArquivo(nomeArquivo)

    while True:
        print(f"\n--- EDITANDO: {nomeArquivo} ---")
        if not linhas:
            print("(Arquivo vazio)")
        else:
            for i, linha in enumerate(linhas):
                print(f"{i + 1}: {linha}")

        print("\nOpções de Edição:")
        print("1. Adicionar linha")
        print("2. Editar linha existente")
        print("3. Remover linha")
        print("4. Salvar alterações no disco")
        print("5. Voltar ao menu principal (sem salvar)")

        opcao = input("Escolha: ")

        if opcao == "1":
            novaLinha = input("Digite o texto da nova linha: ")
            linhas.append(novaLinha)
            print("-> Linha adicionada na lista (memória RAM).")

        elif opcao == "2":
            try:
                num = int(input("Número da linha para editar: ")) - 1
                if 0 <= num < len(linhas):
                    novoTexto = input(f"Novo texto para a linha {num + 1}: ")
                    linhas[num] = novoTexto
                    print("-> Linha alterada na lista (memória RAM).")
                else:
                    print("Linha inválida.")
            except ValueError:
                print("Digite um número válido.")

        elif opcao == "3":
            try:
                num = int(input("Número da linha para remover: ")) - 1
                if 0 <= num < len(linhas):
                    linhas.pop(num)
                    print("-> Linha removida da lista (memória RAM).")
                else:
                    print("Linha inválida.")
            except ValueError:
                print("Digite um número válido.")

        elif opcao == "4":
            salvarArquivo(nomeArquivo, linhas)

        elif opcao == "5":
            break
        else:
            print("Opção inválida!")


def main():
    while True:
        print("\n=== EDITOR DE TEXTO PYTHON ===")
        print("1. Abrir / Criar arquivo .txt")
        print("2. Excluir arquivo .txt do disco")
        print("3. Sair")

        opcao = input("Escolha: ")

        if opcao == "1":
            nome = input("Nome do arquivo (ex: notas.txt): ").strip()
            if not nome.endswith(".txt"):
                nome += ".txt"
            menuEdicao(nome)

        elif opcao == "2":
            nome = input("Nome do arquivo para EXCLUIR: ").strip()
            if not nome.endswith(".txt"):
                nome += ".txt"
            if os.path.exists(nome):
                confirmacao = input(
                    f"Tem certeza que deseja apagar '{nome}' permanentemente? (s/n): "
                )
                if confirmacao.lower() == "s":
                    os.remove(nome)
                    print(f"[!] Arquivo '{nome}' excluído do disco.")
            else:
                print("Arquivo não encontrado.")

        elif opcao == "3":
            print("Encerrando o programa...")
            break
        else:
            print("Opção inválida!")


if __name__ == "__main__":
    main()