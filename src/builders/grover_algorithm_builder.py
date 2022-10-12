import os
from qiskit import QuantumCircuit
from qiskit.circuit.library import PhaseOracle, GroverOperator


class GroverAlgorithmBuilder:
    def __init__(self):
        self.number_of_qubits = None

        self.oracle = None
        self.grover_quantum_circuit = None

    def oracle_builder(self):
        project_directory = os.getcwd()
        self.oracle = PhaseOracle.from_dimacs_file(project_directory + '/files/search.dimacs')
        self.number_of_qubits = self.oracle.num_qubits

    def grover_quantum_circuit_builder(self):
        self.grover_quantum_circuit = QuantumCircuit(self.number_of_qubits)
        self.grover_quantum_circuit.h([index for index in range(self.number_of_qubits)])
        grover_operator = GroverOperator(self.oracle)
        self.grover_quantum_circuit = self.grover_quantum_circuit.compose(grover_operator)
        self.grover_quantum_circuit.measure_all()
