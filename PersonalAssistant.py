class PersonalAssistant:
  def __init__(self, todos):
    self.contacts = {
      "Ann": "Marketing Coordinator",
      "Chelsea": "Software Developer",
      "Nichole": "Sales Representative",
    }
    self.birthdays = {
      "Ann": "04/15/92",
      "Chelsie": "07/12/98",
      "Nichole": "02/31/85",
    }
    self.todos = todos
# --- contacts ---
  def get_contact(self, name):
    if name in self.contacts:
      return self.contacts[name]
    else:
      return "Not a contact."

  def add_contact(self, name, position):
    if name in self.contacts:
      return "Contact already exists."
    else:
      self.contacts[name] = position

  def remove_contact(self, name):
    if name in self.contacts:
      self.contacts.pop(name, None)
    else:
      return "That contact isn't saved."
# --- todos ---
  def add_todo(self, new_item):
    self.todos.append(new_item)

  def remove_todo(self, todo_item):
    # Checks if todo_item is in todos list
    if todo_item in self.todos:
      # Gets the todo_item index in list
      index = self.todos.index(todo_item)
      # pop the index for todo_item in todos list
      self.todos.pop(index)
    else:
      return "To-do is not in list."

  def get_todo(self):
    return self.todos

# --- birthdays ---
  def get_birthday(self, name):
    if name in self.birthdays:
      return self.birthdays[name]
    else:
      return "not saved!"

  def add_birthday(self, name, birthday):
    if name in self.birthdays:
      return "A birthday is already saved for this person."
    else:
      self.birthdays[name] = birthday

  def remove_birthday(self, name):
    if name in self.birthdays:
      self.birthdays.pop(name)
    else:
      return "No birthday is saved for this person."
