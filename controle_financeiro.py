"""Controle financeiro simples em Python, com valores monetários precisos."""

from decimal import Decimal, InvalidOperation


def converter_valor(texto):
    """Converte '125,50' ou '125.50' para Decimal positivo."""
    try:
        valor = Decimal(texto.strip().replace(",", "."))
    except (InvalidOperation, AttributeError):
        raise ValueError("Digite um valor válido, como 125,50.") from None

    if not valor.is_finite() or valor <= 0:
        raise ValueError("O valor precisa ser maior que zero.")
    if valor.as_tuple().exponent < -2:
        raise ValueError("Use no máximo duas casas decimais.")
    return valor


def registrar_lancamento(lancamentos, tipo, descricao, valor):
    """Registra uma receita ou despesa após validar os dados."""
    if tipo not in ("receita", "despesa"):
        raise ValueError("O tipo deve ser 'receita' ou 'despesa'.")
    descricao = descricao.strip()
    if not descricao:
        raise ValueError("A descrição não pode ficar vazia.")
    if not isinstance(valor, Decimal) or not valor.is_finite() or valor <= 0:
        raise ValueError("O valor deve ser um Decimal positivo.")
    lancamentos.append({"tipo": tipo, "descricao": descricao, "valor": valor})


def calcular_saldo(lancamentos):
    """Soma receitas e subtrai despesas."""
    saldo = Decimal("0.00")
    for item in lancamentos:
        if item["tipo"] == "receita":
            saldo += item["valor"]
        else:
            saldo -= item["valor"]
    return saldo


def formatar_reais(valor):
    """Exibe um valor em reais, usando vírgula como separador decimal."""
    sinal = "-" if valor < 0 else ""
    numero = f"{abs(valor):,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
    return f"{sinal}R$ {numero}"


def exibir_relatorio(lancamentos):
    if not lancamentos:
        print("\nNenhuma movimentação cadastrada.")
    else:
        print("\n--- Movimentações ---")
        for numero, item in enumerate(lancamentos, start=1):
            print(f"{numero}. {item['tipo'].capitalize()}: {item['descricao']} — {formatar_reais(item['valor'])}")
    print(f"Saldo atual: {formatar_reais(calcular_saldo(lancamentos))}")


def main():
    lancamentos = []
    while True:
        print("\n=== Controle Financeiro ===")
        print("1 - Cadastrar receita")
        print("2 - Cadastrar despesa")
        print("3 - Ver relatório e saldo")
        print("0 - Sair")
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "0":
            print("Até a próxima!")
            break
        if opcao == "3":
            exibir_relatorio(lancamentos)
            continue
        if opcao in ("1", "2"):
            tipo = "receita" if opcao == "1" else "despesa"
            descricao = input("Descrição: ")
            entrada = input("Valor (ex.: 125,50): ")
            try:
                valor = converter_valor(entrada)
                registrar_lancamento(lancamentos, tipo, descricao, valor)
            except ValueError as erro:
                print(f"Erro: {erro}")
            else:
                print("Movimentação cadastrada com sucesso!")
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()
