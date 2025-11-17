# Repeat asking for numbers until user types "exit", print positive, negative, or zero for each number

while True:
    user_input = input("Enter a number (or 'exit' to quit): ")

    if user_input.lower() == "exit":
        print("Goodbye!")
        break

   
    num = int(user_input)

   
    if num > 0:
        print("Positive\n")
    elif num < 0:
        print("Negative\n")
    else:
        print("Zero\n")