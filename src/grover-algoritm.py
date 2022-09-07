from qiskit import QuantumCircuit


class GroverAlgorithm:
    def __init__(self):
        self.oracle_quantum_circuit = None
        self.grover_quantum_circuit = None
        pass

    def two_qubits_oracle_builder(self):
        number_of_qubits = 2
        number_of_bits = 2
        quantum_circuit = QuantumCircuit(number_of_qubits, number_of_bits)
        quantum_circuit.cz(0, 1)
        self.oracle_quantum_circuit = quantum_circuit

    def two_qubits_grover_circuit_builder(self):
        number_of_qubits = 2
        number_of_bits = 2
        quantum_circuit = QuantumCircuit(number_of_qubits, number_of_bits)
        quantum_circuit.h([0, 1])
        quantum_circuit.append(self.oracle_quantum_circuit, [0, 1])
        self.grover_quantum_circuit = quantum_circuit
