import psycopg2
connection = psycopg2.connect(
   host="localhost",
   database="dict",
   user="dict",
   password="abc123"
)
# read_dict: returns the list of all dictionary entries:
# argument: connection - the database connection.
def read_dict(connection):
    cur = connection.cursor()
    cur.execute("SELECT id, word, translation FROM dictionary;")
    rows = cur.fetchall()
    cur.close()
    return rows
# add_word add new word and translation into the list
def add_word(connection, word, translation):
    cur = connection.cursor()
    cur.execute(f"INSERT INTO dictionary (word, translation) VALUES ('{word}', '{translation}');")
    cur.close()
# delete_word delete from dictionary    
def delete_word(connection, ID):
    cur = connection.cursor()
    cur.execute(f"DELETE FROM dictionary WHERE id = '{ID}';")
    cur.close()
# save_dict save word into the dictionary    
def save_dict(connection):
    cur = connection.cursor()
    cur.execute("COMMIT;")
    cur.close()
# print_help show help for application
def  print_help():
    print("""Hello and welcome to the dictionary list, available commands:
 add - add a new word
 delete - delete from list
 help - print the help
 list - list dictinary
 quit - quit the program
 """)
    
def main():
    while True: ## REPL - Read Execute Program Loop
        cmd = input("Command: ")
        if cmd == "list":
            for i, wd, trans in read_dict(connection):
                print(f"{i}: {wd} - {trans}")
        elif cmd == "add":
            word = input("  Word: ")
            translation = input("  Translation: ")
            add_word(connection, word, translation)
            print(f" Added word {word}")
            print(f" Added translation {translation}")
        elif cmd == "delete":
            ID = input("  ID: ")
            delete_word(connection, ID)
            print(f" You have deleted the {ID}")
        elif cmd == "help":
            print_help()
        elif cmd == "quit":
            print(f" You have quit now!Thank you and Godbye!")
            save_dict(connection)
            exit()
            
if __name__ == "__main__":
    main()
