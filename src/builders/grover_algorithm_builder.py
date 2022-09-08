from qiskit import QuantumCircuit


class GroverAlgorithmBuilder:
    def __init__(self):
        self.oracle_quantum_circuit = None
        self.grover_quantum_circuit = None
        self.reflection_quantum_circuit = None

    def two_qubits_oracle_builder(self):
        number_of_qubits = 2
        quantum_circuit = QuantumCircuit(number_of_qubits, name='oracle')
        quantum_circuit.cz(0, 1)
        quantum_circuit.to_gate()
        self.oracle_quantum_circuit = quantum_circuit

    def two_qubits_reflection_builder(self):
        number_of_qubits = 2
        quantum_circuit = QuantumCircuit(number_of_qubits, name='reflection')
        quantum_circuit.h([0, 1])
        quantum_circuit.z([0, 1])
        quantum_circuit.cz(0, 1)
        quantum_circuit.h([0, 1])
        quantum_circuit.to_gate()
        self.reflection_quantum_circuit = quantum_circuit

    def two_qubits_grover_circuit_builder(self):
        number_of_qubits = 2
        number_of_bits = 2
        self.two_qubits_oracle_builder()
        self.two_qubits_reflection_builder()
        quantum_circuit = QuantumCircuit(number_of_qubits, number_of_bits, name='grover')
        quantum_circuit.h([0, 1])
        quantum_circuit.append(self.oracle_quantum_circuit, [0, 1])
        quantum_circuit.append(self.reflection_quantum_circuit, [0, 1])
        quantum_circuit.measure([0, 1], [0, 1])
        self.grover_quantum_circuit = quantum_circuit
