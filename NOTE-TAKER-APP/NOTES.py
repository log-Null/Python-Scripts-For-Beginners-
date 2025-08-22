from colorama import Fore,Style
notes=[]
def add():
    user=input("enter the note")
    notes.append(user)
    print("Note added successfully!")
def view():
    print("Your notes:")
    for index,note in enumerate(notes):
        print(f"{index} : {note}")
def delete():
    print(notes)
    users=int(input(("enter the index of note you want to remove:")))
    notes.remove(notes[users])
def main():
    print(Fore.GREEN+"Welcome to the Note Taker App!"+Style.RESET_ALL)
    while True:
        user=int(input(f"choose the operation you want to perform\n1.Add Note\n2.View Notes\n3.Delete Note\n4.Exit\n"))
        if user==1:
            add()
        elif user==2:
            view()
        elif user==3:
            delete()
        elif user==4:
            print(Fore.GREEN+"Thank you for using the Note Taker App!"+Style.RESET_ALL)
            quit()
        else:
            print(Fore.RED+"Invalid choice. Please try again."+Style.RESET_ALL)
            continue
main()        
