from services.connection_manager import account_initialization_manager, ConnectionManager

if __name__ == '__main__':
    account_initialization_manager()
    connection_manager = ConnectionManager()
    print(connection_manager.get_to_least_busy_quantum_computer())
