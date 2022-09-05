import unittest
from unittest.mock import MagicMock
from qiskit import IBMQ
from qiskit import QuantumCircuit, BasicAer

from src.services.connection_manager import account_initialization_manager, ConnectionManager


class TestAccountInitializationManager(unittest.TestCase):
    def test_account_initialization_manager_with_no_key(self):
        IBMQ.save_account = MagicMock()
        IBMQ.load_account = MagicMock()
        IBMQ.stored_account = MagicMock(return_value={})
        account_initialization_manager()
        self.assertTrue(IBMQ.save_account.called)
        self.assertTrue(IBMQ.load_account.called)

    def test_account_initialization_manager_with_a_key(self):
        IBMQ.save_account = MagicMock()
        IBMQ.load_account = MagicMock()
        IBMQ.stored_account = MagicMock(return_value={"token": "api-token"})
        account_initialization_manager()
        self.assertFalse(IBMQ.save_account.called)
        self.assertTrue(IBMQ.load_account.called)


if __name__ == '__main__':
    unittest.main()
