📦 1. Classe Produto (Tema: E-commerce)
class Produto:
    def __init__(self, nome, preco, estoque):
        self.nome = nome
        self.preco = preco
        self.estoque = estoque
    
    def aplicar_desconto(self, percentual):
        if percentual < 0 or percentual > 100:
            raise ValueError("Desconto inválido (0-100%)")
        self.preco *= (1 - percentual/100)
    
    def vender(self, quantidade):
        if quantidade <= 0:
            raise ValueError("Quantidade deve ser positiva")
        if self.estoque < quantidade:
            raise ValueError("Estoque insuficiente")
        self.estoque -= quantidade
        return quantidade * self.preco

import unittest

class TestProduto(unittest.TestCase):
    def setUp(self):
        """Executado antes de cada teste"""
        self.produto = Produto("Smartphone", 2000.00, 10)
    
    # ---- Testes de Inicialização ----
    def test_criacao_produto(self):
        self.assertEqual(self.produto.nome, "Smartphone")
        self.assertEqual(self.produto.preco, 2000.00)
        self.assertEqual(self.produto.estoque, 10)
    
    # ---- Testes de Desconto ----
    def test_desconto_valido(self):
        self.produto.aplicar_desconto(10)
        self.assertAlmostEqual(self.produto.preco, 1800.00)
    
    def test_desconto_invalido(self):
        with self.assertRaises(ValueError):
            self.produto.aplicar_desconto(110)  # >100%
        with self.assertRaises(ValueError):
            self.produto.aplicar_desconto(-5)   # <0
    
    # ---- Testes de Venda ----
    def test_venda_bem_sucedida(self):
        total = self.produto.vender(2)
        self.assertEqual(total, 4000.00)
        self.assertEqual(self.produto.estoque, 8)
    
    def test_venda_estoque_insuficiente(self):
        with self.assertRaises(ValueError):
            self.produto.vender(15)  # Estoque=10
    
    def test_venda_quantidade_invalida(self):
        with self.assertRaises(ValueError):
            self.produto.vender(-1)  # Negativo

# Configuração especial para o Colab
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
