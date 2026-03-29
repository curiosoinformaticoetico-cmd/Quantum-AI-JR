from quantum.quantum_simulation import run_quantum
from quantum.ai_module import analyze_quantum_result

def main():
    print("Iniciando sistema de IA cuántica JR...")

    resultado = run_quantum()

    print("Resultado del sistema cuántico:")
    print(resultado)

    decision = analyze_quantum_result(resultado)

    print("Decisión de la IA:")
    print(decision)

if __name__ == "__main__":
    main()
