import cirq

# Create a qubit
qubit = cirq.LineQubit(0)

# Create a Circuit
circuit = cirq.Circuit(
    cirq.H(qubit),  # Apply Hadamard gate to put qubit in superposition
    cirq.measure(qubit, key='m')  # Measure the qubit
)

# Display the circuit
print("Quantum Circuit:")
print(circuit)

# Simulate the circuit
simulator = cirq.Simulator()
result = simulator.run(circuit, repetitions=1000)

# Print the results
print("\nMeasurement Results:")
print(result.histogram(key='m'))