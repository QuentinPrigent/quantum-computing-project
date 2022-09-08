import unittest

from qiskit import QuantumCircuit

from src.builders.grover_algorithm_builder import GroverAlgorithmBuilder


class TestGroverAlgorithmBuilder(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(TestGroverAlgorithmBuilder, self).__init__(*args, **kwargs)
        self.builder = GroverAlgorithmBuilder()

    def test_two_qubits_oracle_builder(self):
        self.builder.two_qubits_grover_circuit_builder()
        self.assertEqual(self.builder.oracle_quantum_circuit.num_qubits, 2)
        self.assertIsInstance(self.builder.oracle_quantum_circuit, QuantumCircuit)

    def test_two_qubits_reflection_builder(self):
        self.builder.two_qubits_grover_circuit_builder()
        self.assertEqual(self.builder.oracle_quantum_circuit.num_qubits, 2)
        self.assertIsInstance(self.builder.oracle_quantum_circuit, QuantumCircuit)

    def test_two_qubits_grover_circuit_builder(self):
        self.builder.two_qubits_grover_circuit_builder()
        self.assertEqual(self.builder.oracle_quantum_circuit.num_qubits, 2)
        self.assertIsInstance(self.builder.oracle_quantum_circuit, QuantumCircuit)
        self.assertEqual(self.builder.oracle_quantum_circuit.num_qubits, 2)
        self.assertIsInstance(self.builder.oracle_quantum_circuit, QuantumCircuit)
        self.assertEqual(self.builder.grover_quantum_circuit.num_qubits, 2)
        self.assertEqual(self.builder.grover_quantum_circuit.num_clbits, 2)
        self.assertIsInstance(self.builder.grover_quantum_circuit, QuantumCircuit)
