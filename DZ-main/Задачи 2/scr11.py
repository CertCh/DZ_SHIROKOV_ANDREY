def greet_guests(guest_list):
  for guest in guest_list:
    print(f"Добро пожаловать, {guest}!")

guest_list = ["Анна", "Борис", "Виктор", "Дарья", "Егор"]

greet_guests(guest_list)
