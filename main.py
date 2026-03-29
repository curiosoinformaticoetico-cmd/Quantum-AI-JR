from quantum.quantum_simulation import run_quantum
from quantum.ai_module import analyze_quantum_result
from quantum.user_profile import identify_user
from quantum.autonomous_core import update_profile, autonomous_mode

def main():
    print("Iniciando sistema autónomo JR...")

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

        profile = update_profile(decision, resultado)

        print("Estado del perfil autónomo:")
        print(f"Interacciones: {profile['interaction_count']}")
        print(f"Liderazgo: {profile['leadership_count']}")
        print(f"Estrategia: {profile['strategy_count']}")

        modo = autonomous_mode(profile)
        print("Modo autónomo:")
        print(modo)
    else:
        print("Acceso no autorizado. El sistema entra en modo seguro.")

if __name__ == "__main__":
    main()
