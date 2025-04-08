import serial
import time
from banco import Banco
PORTA = "COM3"
ARDUINO = serial.Serial(PORTA, 9600, timeout=1)
time.sleep(2)

ALUNO = "Rafael 2"
LED = 1
banco = Banco()
banco.criar_tabela()

while True:
    
    estado = banco.ler_estado(ALUNO)
    if estado.upper() == "LIGADO":
        ARDUINO.write(b'1')
    else:
        ARDUINO.write(b'0')
        
    print(f"Esse é o estado do meu led: {estado}")
    comando = input("Digite 1 para Ligar o LED e 0 Para desligar ou Sair para encerrar o programa! ").upper()
    match comando:
        case "1":
            estado = "Ligado"
            banco.inserir_ou_atualizar_estado(ALUNO,LED,estado)
            print("O LED está ligado!")
        case "0":
            estado = "Desligado"
            banco.inserir_ou_atualizar_estado(ALUNO,LED,estado)
            print("o LED está desligado!")
        case "2":
            banco.listar_estados()
        case "SAIR":
            print("Saindo do Programa! ")
            break
            