from services.connection_manager import account_initialization_manager, ConnectionManager
from qiskit import QuantumCircuit

if __name__ == '__main__':
    account_initialization_manager()

    quantum_circuit = QuantumCircuit(3)
    quantum_circuit.h(0)
    quantum_circuit.cx(0, [1, 2])
    quantum_circuit.measure_all()
    print('Quantum circuit ready.')

    connection_manager = ConnectionManager(real_machine=True)
    connection_manager.get_least_busy_quantum_computer()
    quantum_computer = connection_manager.quantum_computer
    print('Connected to quantum computer:')
    print(quantum_computer)

    job = connection_manager.run_quantum_circuit(quantum_circuit=quantum_circuit)
    print(job.result().get_counts())
