from Classes import *

# Module-level objects available for import
admin1 = admin("John", "Doe", "12345", "555-1234", "ACC-001", "admin", "superuser")
merchant1 = merchant("Jane", "Smith", "67890", "555-5678", "ACC-002", "merchant", "Jane's Store")
customer1 = customer("Alice", "Johnson", "54321", "555-9876", "ACC-003", "customer", 100)
transfert = transaction("TX-001", 500, "payment", "2024-06-01", "CCB-123", "CCB-789")



if __name__ == "__main__":
    admin1.display_info()
    print("\n")
    merchant1.display_info()
    print("\n") 
    customer1.display_info()    
    print("\n")
    transfert.display_info()    
    print(transfert.transaction_id)
    print(transfert.amount)
    print(transfert.timestamp)
    print(transfert.transaction_type)
    print(transfert.timestamp)
    print (transfert.sender)
    print(transfert.receiver)