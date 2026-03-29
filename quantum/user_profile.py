USER_PROFILE = {
    "name": "JR",
    "role": "Founder",
    "project": "Quantum-AI-JR",
    "access_level": "master"
}

def identify_user(input_name: str):
    if input_name.strip().lower() == USER_PROFILE["name"].lower():
        return {
            "recognized": True,
            "message": f"Bienvenido, {USER_PROFILE['name']}. Acceso concedido.",
            "profile": USER_PROFILE
        }
    else:
        return {
            "recognized": False,
            "message": "Usuario no reconocido. Acceso limitado.",
            "profile": None
        }
