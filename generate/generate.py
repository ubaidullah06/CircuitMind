def generate_circuit(user_prompt: str) -> dict:
    
    prompt = user_prompt.lower()

    if "led" in prompt or "light" in prompt:
        return {
            "components": ["battery", "resistor", "led"],
            "connections": ["battery -> resistor -> led"]
        }
    elif "motor" in prompt:
        return {
            "components": ["battery", "switch", "motor"],
            "connections": ["battery -> switch -> motor"]
        }
    elif "buzzer" in prompt:
        return {
            "components": ["battery", "resistor", "buzzer"],
            "connections": ["battery -> resistor -> buzzer"]
        }
    else:
        return {
            "components": ["battery"],
            "connections": [],
            "note": "Circuit not recognized, add more keywords"
        }