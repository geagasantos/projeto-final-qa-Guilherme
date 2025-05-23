📚Teste Regressão Tema: Sistema de Biblioteca
class Biblioteca:
    def __init__(self):
        self.livros = {}
        self.emprestimos = []
    
    def cadastrar_livro(self, id, titulo, autor):
        if id in self.livros:
            raise ValueError("ID já existente")
        self.livros[id] = {"titulo": titulo, "autor": autor, "disponivel": True}
    
    def emprestar_livro(self, id_livro, usuario):
        if id_livro not in self.livros:
            raise ValueError("Livro não encontrado")
        if not self.livros[id_livro]["disponivel"]:
            raise ValueError("Livro já emprestado")
        
        self.livros[id_livro]["disponivel"] = False
        self.emprestimos.append({"livro": id_livro, "usuario": usuario, "devolvido": False})
        return True
    
    def devolver_livro(self, id_livro):
        for emprestimo in self.emprestimos:
            if emprestimo["livro"] == id_livro and not emprestimo["devolvido"]:
                emprestimo["devolvido"] = True
                self.livros[id_livro]["disponivel"] = True
                return True
        raise ValueError("Livro não consta como emprestado")
    
    def buscar_livros_por_autor(self, autor):
        return [livro for livro in self.livros.values() if livro["autor"] == autor]

  import unittest

class Biblioteca:
    def __init__(self):
        self.livros = {}
        self.emprestimos = []
    
    def cadastrar_livro(self, id, titulo, autor):
        if id in self.livros:
            raise ValueError("ID já existente")
        self.livros[id] = {"titulo": titulo, "autor": autor, "disponivel": True}
    
    def emprestar_livro(self, id_livro, usuario):
        if id_livro not in self.livros:
            raise ValueError("Livro não encontrado")
        if not self.livros[id_livro]["disponivel"]:
            raise ValueError("Livro já emprestado")
        
        self.livros[id_livro]["disponivel"] = False
        self.emprestimos.append({"livro": id_livro, "usuario": usuario, "devolvido": False})
        return True
    
    def devolver_livro(self, id_livro):
        for emprestimo in self.emprestimos:
            if emprestimo["livro"] == id_livro and not emprestimo["devolvido"]:
                emprestimo["devolvido"] = True
                self.livros[id_livro]["disponivel"] = True
                return True
        raise ValueError("Livro não consta como emprestado")
    
    def buscar_livros_por_autor(self, autor):
        return [livro for livro in self.livros.values() if livro["autor"] == autor]

class TestBibliotecaRegression(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """Configuração inicial PARA TODOS OS TESTES"""
        cls.bib = Biblioteca()
        # Dados de teste compartilhados
        cls.bib.cadastrar_livro(1, "Python Essentials", "John Doe")
        cls.bib.cadastrar_livro(2, "Advanced Python", "Jane Smith")
    
    def setUp(self):
        """Executado antes de CADA teste"""
        # Reinicia o estado do empréstimo para cada teste
        if 1 in self.bib.livros and not self.bib.livros[1]["disponivel"]:
            self.bib.devolver_livro(1)
        self.bib.emprestar_livro(1, "maria@email.com")
    
    # ---- TESTES DE REGRESSÃO ----
    def test_regressao_cadastro(self):
        """Verifica se o cadastro continua funcionando"""
        self.assertIn(1, self.bib.livros)
        with self.assertRaises(ValueError):
            self.bib.cadastrar_livro(1, "Título Novo", "Autor")
    
    def test_regressao_emprestimo(self):
        """Verifica fluxo básico de empréstimo"""
        self.assertFalse(self.bib.livros[1]["disponivel"])
        self.assertTrue(self.bib.emprestar_livro(2, "joao@email.com"))
    
    def test_regressao_devolucao(self):
        """Verifica se devolução não quebrou"""
        self.assertTrue(self.bib.devolver_livro(1))
        self.assertTrue(self.bib.livros[1]["disponivel"])
        with self.assertRaises(ValueError):
            self.bib.devolver_livro(1)  # Tentativa de devolução duplicada
    
    def test_regressao_busca(self):
        """Verifica busca por autor"""
        resultados = self.bib.buscar_livros_por_autor("Jane Smith")
        self.assertEqual(len(resultados), 1)
        self.assertEqual(resultados[0]["titulo"], "Advanced Python")

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
