from generate import generate_circuit

print("Test 1: LED circuit")
print(generate_circuit("make me a LED circuit"))

print("Test 2: Motor circuit")
print(generate_circuit("make me a motor circuit"))

print("Test 3: Buzzer circuit")
print(generate_circuit("make me a buzzer circuit"))

print("Test 4: Unknown")
print(generate_circuit("make me a robot"))