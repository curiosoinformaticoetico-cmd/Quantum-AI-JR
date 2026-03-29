def analyze_quantum_result(resultado):
    total = sum(resultado.values())

    prob_00 = resultado.get('00', 0) / total
    prob_11 = resultado.get('11', 0) / total

    print("Análisis de IA:")
    print(f"Probabilidad estado 00: {prob_00:.2f}")
    print(f"Probabilidad estado 11: {prob_11:.2f}")

    # Identidad JR
    if prob_11 > 0.5:
        return "JR detectado: liderazgo activo ⚡"
    else:
        return "JR en análisis: equilibrio estratégico 🧠"
