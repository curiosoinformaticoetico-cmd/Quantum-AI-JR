import json
import os
from datetime import datetime

# 📂 Ruta en Google Drive (memoria persistente)
PROFILE_FILE = "/content/drive/MyDrive/Quantum_AI_JR/jr_profile.json"

# 🧠 Perfil inicial del sistema
DEFAULT_PROFILE = {
    "name": "JR",
    "interaction_count": 0,
    "leadership_count": 0,
    "strategy_count": 0,
    "preferences": {
        "decision_style": "balanced",
        "ethics_mode": "strict"
    },
    "history": []
}

# 📥 Cargar perfil
def load_profile():
    os.makedirs(os.path.dirname(PROFILE_FILE), exist_ok=True)

    if os.path.exists(PROFILE_FILE):
        with open(PROFILE_FILE, "r") as f:
            return json.load(f)

    return DEFAULT_PROFILE.copy()

# 💾 Guardar perfil
def save_profile(profile):
    with open(PROFILE_FILE, "w") as f:
        json.dump(profile, f, indent=2)

# 🔄 Actualizar perfil
def update_profile(decision: str, result: dict):
    profile = load_profile()

    profile["interaction_count"] += 1

    if "liderazgo activo" in decision.lower():
        profile["leadership_count"] += 1

    if "evolución estratégica" in decision.lower():
        profile["strategy_count"] += 1

    profile["history"].append({
        "timestamp": datetime.utcnow().isoformat(),
        "result": result,
        "decision": decision
    })

    save_profile(profile)
    return profile

# 🤖 Modo autónomo
def autonomous_mode(profile):
    total = profile["interaction_count"]
    leadership = profile["leadership_count"]
    strategy = profile["strategy_count"]

    if total <= 5:
        return "Modo autónomo inicial: aprendizaje y observación."

    if leadership > strategy:
        return "Modo autónomo JR: liderazgo decisivo ⚡"

    if strategy > leadership:
        return "Modo autónomo JR: análisis estratégico 🧠"

    return "Modo autónomo JR: equilibrio total ⚖️"
