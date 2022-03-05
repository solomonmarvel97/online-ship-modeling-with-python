from dataclasses import dataclass

@dataclass
class Customer:
	id: int
	email: str
	username: str
	password: str

	def create(self):
		print("customer created successfully")

	def delete(self):
		return "customer deleted successfully"

	def __repr__(self):
		return 'This object represents {}'.format(self.username)

base_user = {"id":1, "email": 'solomonmarvel@hotmail.com', 
				"username": 'solomon', "password": 'abcd12345'}

marv = Customer(base_user['id'], base_user['email'], 
	base_user['username'], base_user['password'])
