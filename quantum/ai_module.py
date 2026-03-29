def analyze_quantum_result(counts):
    total = sum(counts.values())

    prob_00 = counts.get('00', 0) / total
    prob_11 = counts.get('11', 0) / total

    print("Análisis de IA:")
    print(f"Probabilidad estado 00: {prob_00:.2f}")
    print(f"Probabilidad estado 11: {prob_11:.2f}")

    if prob_11 > 0.5:
        return "Sistema estable y sincronizado"
    else:
        return "Sistema requiere ajuste"
