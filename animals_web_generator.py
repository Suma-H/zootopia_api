from data_fetcher import fetch_data

def main():
    animal_name = input("Enter the name of an animal: ").strip()
    if not animal_name:
        print("Please enter an animal name")
        return

    print(f"Fetching information about '{animal_name}'...")
    animal_info = fetch_data(animal_name)

    if animal_info:
        for i, animal in enumerate(animal_info, start=1):
            print(f"\nAnimal {i}:")
            for key, value in animal.items():
                print(f"{key.capitalize()}: {value}")
    else:
        print(f"No information found for the animal '{animal_name}'.")

if __name__ == "__main__":
    main()
