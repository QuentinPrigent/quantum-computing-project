import unittest

from qiskit import QuantumCircuit

from src.builders.grover_algorithm_builder import GroverAlgorithmBuilder


class TestGroverAlgorithmBuilder(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(TestGroverAlgorithmBuilder, self).__init__(*args, **kwargs)
        self.builder = GroverAlgorithmBuilder()

    def test_oracle_builder(self):
        self.builder.oracle_quantum_circuit_builder()
        self.assertIsInstance(self.builder.oracle_quantum_circuit, QuantumCircuit)
        self.assertEqual(self.builder.number_of_qubits, self.builder.oracle_quantum_circuit.num_qubits)

    def test_grover_algorithm_quantum_circuit_builder(self):
        self.builder.oracle_quantum_circuit_builder()
        self.builder.grover_algorithm_quantum_circuit_builder()
        self.assertIsInstance(self.builder.grover_algorithm_quantum_circuit, QuantumCircuit)
        self.assertEqual(self.builder.number_of_qubits, self.builder.grover_algorithm_quantum_circuit.num_qubits)
