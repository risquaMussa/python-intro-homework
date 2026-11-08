#mini project
numbers = [42, 17, 83, 5, 61, 29, 74, 8, 55, 93, 31,
            66, 14, 47, 78, 3, 59, 22, 86, 40]

while True:
    print("=== Number Cruncher ===")
    print("1. Find minimum")
    print("2. Find maximum")
    print("3. Search for a number")
    print("4. Sort the list")
    print("5. Quit")  

    choice = input("Choose an option (1-5): ")

    if choice == "1": 
        smallest = numbers[0]

        for number in numbers:
            if number < smallest:
                smallest = number
        print(f'"Minimum number:", {smallest}')

    elif choice == "2":
        largest = numbers[0]
        for number in numbers:
            if number > largest:
                largest = number        
        print(f'"Maximum number is:", {largest}')

#lineary search
    elif choice == "3":
        search_number = int(input("Enter a number to search for: "))

        found = False
        for i in range(len(numbers)):
            if numbers[i] == search_number:
                print(f"Found {search_number} at index {i}.")
                found = True
                break

        if not found:
            print(f"{search_number} was not found in the list.")
               ######-------------########

    elif choice == "4":
        sorted = True

        while sorted:
            sorted = False

            for i in range(len(numbers) - 1):
                if numbers[i] > numbers[i + 1]:
                    #swapp
                    numbers[i], numbers[i + 1] = numbers[i + 1], numbers[i] 
                    sorted = True
        print("Sort the list:", numbers)
    elif choice == "5":
        print("Good bye")
        break


    else:
        print("Invalid option. Please choose 1-5.")




