#Part 2: Mini-Project — Refactor the Number Cruncher
numbers = [42, 17, 83, 5, 61, 29, 74, 8, 55, 93, 31,
            66, 14, 47, 78, 3, 59, 22, 86, 40]

#find minimum
def find_min(number):
    smallest = numbers[0]

    for number in numbers:
        if number < smallest:
            smallest = number
    return smallest

#find max
def find_max(number):
    largest = numbers[0]

    for number in numbers:
        if number > largest:
            largest = number
    return largest

# Search for a number and return its index
def search(numbers, target):
    for i in range(len(numbers)):
        if numbers[i] == target:
            return i

    return -1

#bubble_sort(numbers)
def bubble_sort(numbers):
    sorted_numbers = numbers.copy()

    swapped = True

    while swapped:
        swapped = False

        for i in range(len(sorted_numbers) - 1):
            if sorted_numbers[i] > sorted_numbers[i + 1]:
                sorted_numbers[i], sorted_numbers[i + 1] = (
                    sorted_numbers[i + 1],
                    sorted_numbers[i]
                )
                swapped = True
#return outside while return after sorting is finished
    return sorted_numbers

def show_menu():
    print("\n=== Number Cruncher ===")
    print("1. Find minimum")
    print("2. Find maximum")
    print("3. Search for a number")
    print("4. Sort the list")
    print("5. Quit")

    choice = input("Choose an option (1-5): ")

    return choice

# Main 
def main():
    while True:
        choice = show_menu()

        if choice == "1":
            smallest = find_min(numbers)
            print(f"Minimum number: {smallest}")

        elif choice == "2":
            largest = find_max(numbers)
            print(f"Maximum number: {largest}")

        elif choice == "3":
            search_number = int(input("Enter a number to search for: "))

            index = search(numbers, search_number)

            if index != -1:
                print(f"Found at index {index}")
            else:
                print("Not found")

        elif choice == "4":
            sorted_numbers = bubble_sort(numbers)
            print("Sorted list:", sorted_numbers)

        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print("Invalid option. Please choose 1-5.")



main()


