Definição: Um programa para criar uma interface simples, com banco de dados, que permite administrar o estoque de uma loja de games. Permitindo adicionar e excluir produtos do tipo Console, Jogo e Controle, assim como visualiza-los de maneira separada.

Utiliza python como linguagem principal. Sqlite para o banco de dados. Tkinter para a interface gráfica.

Como executar:
- Clone o repositório: git clone https://github.com/seuusuario/Loja_Games.git
cd Loja_Games
- Execute o sistema com o comando: python3 -m main.py

Casos de Uso:
1. Adicionar Produto

    Ator principal: Usuário

    Descrição: O usuário adiciona um novo produto do tipo Console, Controle ou Jogo.

    Pré-condições: A aplicação deve estar em execução.

    Fluxo principal:

        O usuário clica em "Adicionar Produto".

        O sistema solicita o tipo do produto (Console / Controle / Jogo).

        O usuário informa o tipo.

        O sistema solicita os dados comuns (nome, preço).

        O sistema solicita os dados específicos de acordo com o tipo:

            Console → armazenamento

            Controle → compatibilidade

            Jogo → plataforma

        O sistema valida os dados.

        O sistema salva o produto no banco de dados.

        O sistema informa sucesso.

    Fluxos alternativos:

        5a. Usuário informa tipo inválido → sistema exibe erro.

        6a. Algum campo obrigatório está vazio ou inválido → exibe erro e retorna ao passo 3.

    Pós-condição: Produto armazenado no banco.
    
2. Visualizar Produtos por Tipo

    Ator principal: Usuário

    Descrição: Exibe os produtos cadastrados no banco, filtrando por tipo.

    Pré-condições: Deve haver produtos cadastrados.

    Fluxo principal:

        O usuário clica em "Visualizar Produtos".

        O sistema solicita o tipo desejado.

        O usuário informa (Console / Controle / Jogo).

        O sistema busca os produtos no banco.

        O sistema exibe os produtos encontrados.

    Fluxo alternativo:

        3a. Tipo inválido → sistema exibe erro.

        4a. Nenhum produto encontrado → sistema avisa usuário.

    Pós-condição: Produtos exibidos.
   
3. Excluir Produto por Nome

    Ator principal: Usuário

    Descrição: Remove um produto pelo nome.

    Pré-condições: Deve haver ao menos um produto com o nome informado.

    Fluxo principal:

        O usuário clica em "Excluir Produto".

        O sistema solicita o nome do produto.

        O usuário informa o nome.

        O sistema busca e remove o produto no banco.

        O sistema informa se foi removido com sucesso.

    Fluxo alternativo:

        3a. Nome vazio → sistema exibe erro.

        4a. Produto não encontrado → sistema exibe erro.

    Pós-condição: Produto removido do banco (se encontrado).
