import random
from testar_metodos import testar_metodos

def main():
    random.seed(0)  # Para reprodução
    testar_metodos(n=4)
    testar_metodos(n=6)
    testar_metodos(n=10)
    testar_metodos(n=15)

if __name__ == "__main__":
    main()
