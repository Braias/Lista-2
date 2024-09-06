import modulo
import json
import pprint

def exercicio3():
    while True:
        arquivo = input("insira o nome do arquivo aqui")
        try:
            return modulo.carrega_conteudos_json(arquivo)
        except(FileNotFoundError, InterruptedError, IsADirectoryError, PermissionError, OSError, json.JSONDecodeError) as error:
            match error:
                case FileNotFoundError():
                    print(f"O arquivo inserido não foi encontrado: {arquivo}")
                case InterruptedError():
                    print(f"Você interrompeu a execução do programa, byebye :)")
                    return
                case IsADirectoryError():
                    print("O arquivo passado é um diretório, insira apenas arquivos txt")
                case PermissionError():
                    print("Não tenho acesso ao arquivo desejado")
                case OSError():
                    print("Oh não! Ocorreu um erro de sistema durante a execução do programa")
                case json.JSONDecodeError():
                    print("O arquivo passado não tem uma estrutura JSON dentro dele :(")
