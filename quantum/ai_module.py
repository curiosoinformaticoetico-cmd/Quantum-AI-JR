import json
import os

MEMORY_FILE = "memory.json"

def load_memory():
    if os.path.exists(MEMORY_FILE):
        with open(MEMORY_FILE, "r") as f:
            return json.load(f)
    return {"interactions": 0}

def save_memory(memory):
    with open(MEMORY_FILE, "w") as f:
        json.dump(memory, f)

def analyze_quantum_result(resultado):
    total = sum(resultado.values())

    prob_00 = resultado.get('00', 0) / total
    prob_11 = resultado.get('11', 0) / total

    print("Análisis de IA:")
    print(f"Probabilidad estado 00: {prob_00:.2f}")
    print(f"Probabilidad estado 11: {prob_11:.2f}")

    # 🔹 Cargar memoria
    memory = load_memory()
    memory["interactions"] += 1

    print(f"Memoria IA - Interacciones: {memory['interactions']}")

    # 🔹 Guardar memoria
    save_memory(memory)

    # 🔹 Identidad JR
    if prob_11 > 0.5:
        return f"JR detectado: liderazgo activo ⚡ | Nivel: {memory['interactions']}"
    else:
        return f"JR en análisis: evolución estratégica 🧠 | Nivel: {memory['interactions']}"
