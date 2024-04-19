import math

def Calculo_Circunferencia(radio):
    pi = round(math.pi, 6)
    circunferencia = 2 * pi * radio
    return circunferencia

def main():
    radios = [3, 8, 10]
    for radio in radios:
        Circunferencia = Calculo_Circunferencia(radio)
        print(f"Para un radio de {radio}, la circunferencia es: {Circunferencia}")

if __name__ == "__main__":
    main()
