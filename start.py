import os

system = "linux"
env = None


def createEnv():
    if not os.path.exists('./venv'):
        print("\n > Criando ambiente virtual...\n")
        os.system("virtualenv --python='/usr/bin/python3.7' venv")

    print("\n > Ambiente virtual já criado!\n")


def initEnv():
    print("\n > Iniciando ambiente virtual!\n")

    if system == 'linux':
        return os.system("source venv/bin/activate")
    else:
        return os.system("venv\bin\activate")

    print("\n > Ambiente virtual pronto!\n ")


def installPackages():
    print("\n > Preparando para instalar pacotes!\n")
    return os.system("pip install -r requirements.txt")


def initNadja():
    if not os.path.exists('./db.sqlite3'):
        print("\n > Preparando para rodar o banco de dados")
        os.system("python manage.py makemigrations core accounts")
        os.system("python manage.py migrate")


def startNadja():
    return os.system("python manage.py runserver")


if __name__ == "__main__":
    createEnv()
    initEnv()
    installPackages()
    initNadja()
    startNadja()
