import pymongo

# Connect to MongoDB
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["mydatabase"]  # Change to your database name

def create_document(collection_name, document):
	collection = db[collection_name]
	result = collection.insert_one(document)
	return result.inserted_id

def read_documents(collection_name, query={}):
	collection = db[collection_name]
	return list(collection.find(query))

def update_document(collection_name, query, new_values):
	collection = db[collection_name]
	result = collection.update_one(query, {"$set": new_values["$set"]})
	return result.modified_count

def delete_document(collection_name, query):
	collection = db[collection_name]
	result = collection.delete_one(query)
	return result.deleted_count

def display_menu():
	print("\nMenu:")
	print("1. Create a document")
	print("2. Read documents")
	print("3. Update a document")
	print("4. Delete a document")
	print("5. Exit")

while True:
	display_menu()
	choice = input("Enter your choice: ")

	if choice == "1":
		name = input("Enter name: ")
		age = int(input("Enter age: "))
		new_document = {"name": name, "age": age}
		created_id = create_document("users", new_document)
		print(f"Created document with ID: {created_id}")

	elif choice == "2":
		users = read_documents("users")
		print("All users:")
		for user in users:
			print(user)

	elif choice == "3":
		name = input("Enter name to update: ")
		age = int(input("Enter new age: "))
		update_query = {"name": name}
		update_values = {"$set": {"age": age}}
		modified_count = update_document("users", update_query, update_values)
	#	print(f"Modified {modified_count} document(s)")
		if modified_count > 0:
			print(f"Modified {modified_count} document(s)")
		else:
			print("No documents were modified.")
	elif choice == "4":
		name = input("Enter name to delete: ")
		delete_query = {"name": name}
		deleted_count = delete_document("users", delete_query)
		print(f"Deleted {deleted_count} document(s)")
	elif choice == "5":
		print("Exiting program.")
		break
	else:
		print("Invalid choice. Please enter a valid option.")
