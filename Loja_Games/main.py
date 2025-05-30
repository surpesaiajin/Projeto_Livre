from controllers.apploja import LojaGUI
from controllers.bancoSqlite import BancoDeDados
from controllers.loja import Loja

def main():
    loja = Loja('games.db')

    interface = LojaGUI(loja)
    interface.run()

if __name__ == '__main__':
    main()