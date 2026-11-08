#Warmup 3: Linear Search
names = ["John", "Doe", "Sara", "Steve", "Zara"]

search_name = input("Enter a name to search for: ")

found = False

for i in range(len(names)):
    if names[i].lower() == search_name.lower():
        print(f'"{search_name}" was found at index {i}.')
        found = True
        break
else:
        print(f'"{search_name}" was not found in the list.')

