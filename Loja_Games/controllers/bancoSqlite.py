from modelos.console import Console
from modelos.jogo import Jogo
from modelos.controle import Controle


import sqlite3

class BancoDeDados:
    def __init__(self, nome_banco='produtos.db'):
        self.nome_banco = nome_banco
        self._criar_tabela()

    def _conectar(self):
        return sqlite3.connect(self.nome_banco)
    
    def _criar_tabela(self):
        conn = self._conectar()
        cursor = conn.cursor()
        cursor.execute(''' 
            CREATE TABLE IF NOT EXISTS produtos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT,
                tipo TEXT,
                preco REAL,
                armazenamento INTEGER,
                plataforma TEXT,
                compatibilidade TEXT
            )
        ''')
        conn.commit()
        conn.close()

    def inserir_produto(self, produto):
        conn = self._conectar()
        cursor = conn.cursor()

        if isinstance(produto, Console):
            tipo = 'Console'
            cursor.execute('''
                INSERT INTO produtos (nome, tipo, preco, armazenamento)
                VALUES (?, ?, ?, ?)  
            ''', (produto.nome, tipo, produto.preco, produto.armazenamento))
        
        elif isinstance(produto, Jogo):
            tipo = 'Jogo'
            cursor.execute('''
                INSERT INTO produtos (nome, tipo, preco, plataforma)
                VALUES (?, ?, ?, ?)  
            ''', (produto.nome, tipo, produto.preco, produto.plataforma))

        elif isinstance(produto, Controle):
            tipo = 'Controle'
            cursor.execute('''
                INSERT INTO produtos (nome, tipo, preco, compatibilidade)
                VALUES (?, ?, ?, ?)  
            ''', (produto.nome, tipo, produto.preco, produto.compatibilidade))

        else:
            tipo = 'Produto'
            cursor.execute('''
                INSERT INTO produtos (nome, tipo, preco)
                VALUES (?, ?, ?)  
            ''', (produto.nome, tipo, produto.preco))

        conn.commit()
        conn.close()

    def listar_formatado_por_tipo(self, tipo):
        conn = self._conectar()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM produtos WHERE tipo = ?', (tipo,))
        resultados = cursor.fetchall()
        conn.close()

        campos = ['ID', 'Nome', 'Tipo', 'Preço', 'Armazenamento', 'Plataforma', 'Compatibilidade']

        produtos_formatados = []
        for linha in resultados:
            detalhes = [f"{campo}: {valor}" for campo, valor in zip(campos, linha) if valor is not None]
            produtos_formatados.append(" | ".join(detalhes))

        return produtos_formatados

    def buscar_por_nome(self, termo_busca):
        conn = self._conectar()
        cursor = conn.cursor()
        
        cursor.execute('''
            SELECT * FROM produtos WHERE nome LIKE ?
        ''', (f"%{termo_busca}%",))
        
        resultados = cursor.fetchall()
        conn.close()

        campos = ['ID', 'Nome', 'Tipo', 'Preço', 'Armazenamento', 'Plataforma', 'Compatibilidade']
        
        produtos_formatados = []
        for linha in resultados:
            detalhes = [f"{campo}: {valor}" for campo, valor in zip(campos, linha) if valor is not None]
            produtos_formatados.append(" | ".join(detalhes))

        return produtos_formatados

    def excluir_por_nome(self, nome):
        conn = self._conectar()
        cursor = conn.cursor()

        cursor.execute('DELETE FROM produtos WHERE nome = ?', (nome,))
        conn.commit()
        excluiu = cursor.rowcount > 0  # True se algum registro foi excluído

        conn.close()
        return excluiu
