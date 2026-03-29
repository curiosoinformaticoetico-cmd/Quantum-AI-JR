from quantum.quantum_simulation import run_quantum
from quantum.ai_module import analyze_quantum_result
from quantum.user_profile import identify_user

def main():
    print("Iniciando sistema de IA cuántica JR...")

    nombre_usuario = "JR"
    identidad = identify_user(nombre_usuario)

    print(identidad["message"])

    if identidad["recognized"]:
        resultado = run_quantum()

        print("Resultado del sistema cuántico:")
        print(resultado)

        decision = analyze_quantum_result(resultado)

        print("Decisión de la IA:")
        print(decision)
    else:
        print("El sistema no ejecutará funciones avanzadas.")

if __name__ == "__main__":
    main()
