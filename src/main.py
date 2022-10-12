from services.connection_manager import account_initialization_manager, ConnectionManager
from builders.grover_algorithm_builder import GroverAlgorithmBuilder

if __name__ == '__main__':
    account_initialization_manager()

    algorithm_builder = GroverAlgorithmBuilder()
    algorithm_builder.oracle_quantum_circuit_builder()
    algorithm_builder.grover_algorithm_quantum_circuit_builder()
    quantum_circuit = algorithm_builder.grover_algorithm_quantum_circuit
    print('Quantum circuit ready.')

    connection_manager = ConnectionManager(real_machine=False)
    connection_manager.get_least_busy_quantum_computer()
    quantum_computer = connection_manager.quantum_computer
    print('Connected to quantum computer:')
    print(quantum_computer)

    job = connection_manager.run_quantum_circuit(quantum_circuit=quantum_circuit, number_of_shots=1024)
    print(job.result().get_counts())
