from qiskit import QuantumCircuit, execute, Aer

# Create a quantum circuit with 2 qubits
qc = QuantumCircuit(2, 2)

# Apply a Hadamard gate to the first qubit
qc.h(0)

# Apply a CNOT with the first qubit as control and second as target
qc.cx(0, 1)

# Measure both qubits
qc.measure([0,1], [0,1])

# Use Aer's qasm_simulator
simulator = Aer.get_backend('qasm_simulator')

# Execute the circuit on the qasm simulator
job = execute(qc, simulator, shots=1000)

# Grab results from the job
result = job.result()

# Returns counts
counts = result.get_counts(qc)
print("\nTotal count for 00 and 11 are:",counts)