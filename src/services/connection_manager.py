from qiskit import IBMQ, BasicAer
from qiskit.providers.ibmq import least_busy
import os
from dotenv import load_dotenv


def account_initialization_manager():
    if IBMQ.stored_account() == {}:
        load_dotenv()
        api_key = os.getenv('IBM_API_KEY')
        IBMQ.save_account(api_key)
    IBMQ.load_account()


class ConnectionManager:
    def __init__(self, real_machine=True):
        self.backend = None
        self.real_machine = real_machine

    def get_to_least_busy_quantum_computer(self):
        if self.real_machine:
            try:
                provider = IBMQ.get_provider(
                    hub='ibm-q', group='open', project='main'
                )
                self.backend = least_busy(
                    provider.backends(
                        filters=lambda device: not device.configuration().simulator
                    )
                )
            except Exception:
                print('Impossible to connect to a quantum computer')
        else:
            self.backend = BasicAer.get_backend('qasm_simulator')
        return self.backend
