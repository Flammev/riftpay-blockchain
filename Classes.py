class user:
    def __init__(self, name,prenom, id, phone, account_num,email):
        self.name = name
        self.prenom = prenom
        self.id = id
        self.phone = phone
        self.account_num = account_num
        self.email = email

    def display_info(self):
        print(f"Name: {self.name}, Prenom: {self.prenom}, ID: {self.id}, Phone: {self.phone}, Account Number: {self.account_num}, Email: {self.email}")

class admin(user):
    def __init__(self, name, prenom, id, phone, account_num, email, access_level):
        super().__init__(name, prenom, id, phone, account_num, email)
        self.access_level = access_level
    def display_info(self):        
        super().display_info()
        print(f"Access Level: {self.access_level}")

class merchant(user):
    def __init__(self, name, prenom, id, phone, account_num, email, business_name):
        super().__init__(name, prenom, id, phone, account_num, email)
        self.business_name = business_name
    def display_info(self):        
        super().display_info()
        print(f"Business Name: {self.business_name}")

class customer(user):
    def __init__(self, name, prenom, id, phone, account_num, email, loyalty_points):
        super().__init__(name, prenom, id, phone, account_num, email)
        self.loyalty_points = loyalty_points
    def display_info(self):        
        super().display_info()
        print(f"Loyalty Points: {self.loyalty_points}")

class account: 
    state = ['active', 'inactive', 'suspended']
    def __init__(self, balance, account_num, account_type, user_id, card_num,transaction_history):
        self.balance = balance
        self.account_num = account_num
        self.account_type = account_type
        self.user_id = user_id
        self.card_num = card_num
        self.transaction_history = transaction_history
    def display_info(self):
        print(f"Balance: {self.balance}, Account Number: {self.account_num}, Account Type: {self.account_type}, User ID: {self.user_id}, Card Number: {self.card_num}, Transaction History: {self.transaction_history}")

class card:
    state = ['active', 'inactive', 'suspended']
    def __init__(self, card_num, card_type, expiry_date, cvv, account_num, user_id):
        self.card_num = card_num
        self.card_type = card_type
        self.expiry_date = expiry_date
        self.cvv = cvv
        self.account_num = account_num
        self.user_id = user_id
    def display_info(self):
        print(f"Card Number: {self.card_num}, Card Type: {self.card_type}, Expiry Date: {self.expiry_date}, CVV: {self.cvv}, Account Number: {self.account_num}, User ID: {self.user_id}")

class transaction:
    state = ['pending', 'completed', 'failed']
    def __init__(self, transaction_id, amount, transaction_type, timestamp, sender, receiver=None):
        self.transaction_id = transaction_id
        self.amount = amount
        self.transaction_type = transaction_type
        self.timestamp = timestamp
        self.sender = sender
        self.receiver = receiver
    def display_info(self):
        print(f"Transaction ID: {self.transaction_id}, Amount: {self.amount}, Transaction Type: {self.transaction_type}, Timestamp: {self.timestamp}, Sender: {self.sender}, Receiver: {self.receiver}")


class audit_Log:
    def __init__(self, log_id, user_id, action, timestamp):
        self.log_id = log_id
        self.user_id = user_id
        self.action = action
        self.timestamp = timestamp
    def display_info(self):
        print(f"Log ID: {self.log_id}, User ID: {self.user_id}, Action: {self.action}, Timestamp: {self.timestamp}")

class KYC:
    def __init__(self, user_id, document_type, document_number, expiry_date):
        self.user_id = user_id
        self.document_type = document_type
        self.document_number = document_number
        self.expiry_date = expiry_date
    def display_info(self):
        print(f"User ID: {self.user_id}, Document Type: {self.document_type}, Document Number: {self.document_number}, Expiry Date: {self.expiry_date}")

class API_key:
    def __init__(self, key_id, user_id, key_value, permissions):
        self.key_id = key_id
        self.user_id = user_id
        self.key_value = key_value
        self.permissions = permissions
    def display_info(self):
        print(f"Key ID: {self.key_id}, User ID: {self.user_id}, Key Value: {self.key_value}, Permissions: {self.permissions}")

class notification:
    def __init__(self, notification_id, user_id, message, timestamp):
        self.notification_id = notification_id
        self.user_id = user_id
        self.message = message
        self.timestamp = timestamp
    def display_info(self):
        print(f"Notification ID: {self.notification_id}, User ID: {self.user_id}, Message: {self.message}, Timestamp: {self.timestamp}")

class session:
    def __init__(self, session_id, user_id, login_time, logout_time=None):
        self.session_id = session_id
        self.user_id = user_id
        self.login_time = login_time
        self.logout_time = logout_time
    def display_info(self):
        print(f"Session ID: {self.session_id}, User ID: {self.user_id}, Login Time: {self.login_time}, Logout Time: {self.logout_time}")

class device:
    def __init__(self, device_id, user_id, device_type, last_used):
        self.device_id = device_id
        self.user_id = user_id
        self.device_type = device_type
        self.last_used = last_used
    def display_info(self):
        print(f"Device ID: {self.device_id}, User ID: {self.user_id}, Device Type: {self.device_type}, Last Used: {self.last_used}")

class location:
    def __init__(self, location_id, user_id, latitude, longitude, timestamp):
        self.location_id = location_id
        self.user_id = user_id
        self.latitude = latitude
        self.longitude = longitude
        self.timestamp = timestamp
    def display_info(self):
        print(f"Location ID: {self.location_id}, User ID: {self.user_id}, Latitude: {self.latitude}, Longitude: {self.longitude}, Timestamp: {self.timestamp}")

class risk_score:
    def __init__(self, user_id, score, factors):
        self.user_id = user_id
        self.score = score
        self.factors = factors
    def display_info(self):
        print(f"User ID: {self.user_id}, Risk Score: {self.score}, Factors: {self.factors}")

class fraud_alert:
    def __init__(self, alert_id, user_id, transaction_id, alert_type, timestamp):
        self.alert_id = alert_id
        self.user_id = user_id
        self.transaction_id = transaction_id
        self.alert_type = alert_type
        self.timestamp = timestamp
    def display_info(self):
        print(f"Alert ID: {self.alert_id}, User ID: {self.user_id}, Transaction ID: {self.transaction_id}, Alert Type: {self.alert_type}, Timestamp: {self.timestamp}")

class report:
    def __init__(self, report_id, user_id, report_type, description, timestamp):
        self.report_id = report_id
        self.user_id = user_id
        self.report_type = report_type
        self.description = description
        self.timestamp = timestamp
    def display_info(self):
        print(f"Report ID: {self.report_id}, User ID: {self.user_id}, Report Type: {self.report_type}, Description: {self.description}, Timestamp: {self.timestamp}")



#class fraud_detection:
