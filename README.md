
# 💰 Controle Financeiro em Python

Sistema de controle financeiro desenvolvido em Python como projeto prático de aprendizagem e portfólio profissional.

O objetivo é aplicar conceitos de programação, lógica, organização de código e testes automatizados.

## 🚀 Funcionalidades

- Cadastro de receitas.
- Cadastro de despesas.
- Cálculo automático do saldo financeiro.
- Relatório de movimentações.
- Formatação de valores em reais (R$).
- Validação de valores inválidos.
- Aceita valores com vírgula ou ponto decimal.
- Testes automatizados com unittest.

## 🛠️ Tecnologias utilizadas

- Python 3
- Biblioteca decimal
- Biblioteca unittest
- Git e GitHub

O projeto utiliza apenas bibliotecas padrão do Python.

## 💻 Como executar

Baixe ou clone o repositório e abra o Terminal na pasta do projeto.

Execute:

```bash
python3 controle_financeiro.py
```

O sistema apresenta um menu interativo:

```text
=== Controle Financeiro ===
1 - Cadastrar receita
2 - Cadastrar despesa
3 - Ver relatório e saldo
0 - Sair
```

## 📊 Exemplo de utilização

Receita cadastrada: Salário — R$ 2.500,00

Despesa cadastrada: Mercado — R$ 199,90

Resultado:

```text
--- Movimentações ---
1. Receita: Salário — R$ 2.500,00
2. Despesa: Mercado — R$ 199,90

Saldo atual: R$ 2.300,10
```

## 🧪 Testes automatizados

O projeto contém oito testes automatizados que verificam:

- Conversão de valores monetários.
- Rejeição de valores inválidos.
- Cadastro de receitas.
- Desconto de despesas.
- Saldo inicial zerado.
- Validação de descrições.
- Rejeição de tipos inválidos.
- Formatação de valores em reais.

Para executar os testes:

```bash
python3 -m unittest discover -s . -p 'test_*.py' -v
```

Resultado obtido durante os testes:

```text
Ran 8 tests

OK
```

Os oito testes foram executados com sucesso em um MacBook utilizando Python 3.8.2.

## 📁 Estrutura do projeto

```text
controle-financeiro-python/
├── controle_financeiro.py
├── test_controle_financeiro.py
├── README.md
├── .gitignore
└── LICENSE
```

## 🔄 Melhorias futuras

- Salvamento permanente das movimentações.
- Edição e exclusão de lançamentos.
- Relatórios mensais.
- Exportação de dados para CSV.
- Interface gráfica.
- Ampliação da cobertura dos testes.

Atualmente, os lançamentos ficam armazenados apenas enquanto o programa está em execução.

## 👨‍💻 Sobre o projeto

Projeto educacional de Valdir Barbosa, estudante de Análise e Desenvolvimento de Sistemas na Anhanguera Educacional, em transição de carreira para Tecnologia da Informação.

Desenvolvido com apoio de IA e acompanhado de testes práticos, com foco no aprendizado de Python, desenvolvimento de software e Quality Assurance (QA).

**Áreas de interesse:** Python | Desenvolvimento de Software | QA | Testes Automatizados

## 📄 Licença

Este projeto está disponibilizado sob a licença MIT.
