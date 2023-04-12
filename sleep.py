import os
import platform


def main():
    while True:
        try:
            tempo = int(input("Quanto tempo para desligar o PC?\nEscreva em horas\n->"))
            break  # sai do loop se a conversão para int funcionar
        except ValueError:
            print("Por favor, digite um número válido.")
    while True:
        querDesligar = input(f"Tem certeza que quer desligar o PC em {tempo} hora(s)\n s/n: ").strip().lower()
        if querDesligar in ['s', 'n']:
            break
        print("Por favor, insira 's' ou 'n'.")
    if querDesligar == 's':
        tempo = tempo * 3600
        tempoStr = str(tempo)
        system_name = platform.system()
        if system_name == 'Windows':
            comando = "shutdown /s /t " + tempoStr
        elif system_name == 'Linux':
            comando = "shutdown -h " + tempoStr
        elif system_name == 'Darwin':
            comando = "sudo shutdown -h +" + tempoStr
        else:
            print("Sistema operacional não suportado.")
            exit()
        os.system(comando)
    else:
        print("Obrigado, o programa vai fechar!!!")
        input("Pressione enter para fechar o programa...")

if __name__ == "__main__":
    main()
