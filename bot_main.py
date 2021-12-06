from bot_delete_github import delete


def main():
    username = input("Insira o seu username do github: ")
    password = input("Insira a sua senha do github: ")

    exceptions = input(
        "Quais repositorios você deseja manter? (separe por espaço, diferencie entre letras maiuscula e minuscula):").split()
    print("#" * 8)
    print("Apenas estes repositorios não serão excluidos:" + ','.join(exceptions))

    confirm = input("Deseja continuar? [Y/N] ").lower()

    delete(username, password, exceptions) if confirm == 'y' else print("Operação Negada")

if __name__ == '__main__':
    main()