"""Testes automatizados com a biblioteca padrão unittest."""

import unittest
from decimal import Decimal

from controle_financeiro import (
    calcular_saldo,
    converter_valor,
    formatar_reais,
    registrar_lancamento,
)


class TesteControleFinanceiro(unittest.TestCase):
    def setUp(self):
        self.lancamentos = []

    def test_converte_valor_com_virgula(self):
        self.assertEqual(converter_valor("125,50"), Decimal("125.50"))

    def test_rejeita_valor_invalido(self):
        for texto in ("abc", "-5", "0", "NaN", "1,999"):
            with self.subTest(texto=texto):
                with self.assertRaises(ValueError):
                    converter_valor(texto)

    def test_registra_receita(self):
        registrar_lancamento(self.lancamentos, "receita", "Salário", Decimal("2500.00"))
        self.assertEqual(calcular_saldo(self.lancamentos), Decimal("2500.00"))

    def test_desconta_despesa(self):
        registrar_lancamento(self.lancamentos, "receita", "Salário", Decimal("2500.00"))
        registrar_lancamento(self.lancamentos, "despesa", "Mercado", Decimal("199.90"))
        self.assertEqual(calcular_saldo(self.lancamentos), Decimal("2300.10"))

    def test_saldo_inicial_zero(self):
        self.assertEqual(calcular_saldo(self.lancamentos), Decimal("0.00"))

    def test_rejeita_descricao_vazia(self):
        with self.assertRaises(ValueError):
            registrar_lancamento(self.lancamentos, "receita", "   ", Decimal("10.00"))

    def test_rejeita_tipo_invalido(self):
        with self.assertRaises(ValueError):
            registrar_lancamento(self.lancamentos, "transferencia", "PIX", Decimal("10.00"))

    def test_formata_reais(self):
        self.assertEqual(formatar_reais(Decimal("1234.50")), "R$ 1.234,50")
        self.assertEqual(formatar_reais(Decimal("-15.50")), "-R$ 15,50")


if __name__ == "__main__":
    unittest.main()
