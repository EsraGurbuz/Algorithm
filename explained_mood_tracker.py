import datetime  # Importing the datetime module to work with dates

# Class to represent a single mood entry
class MoodEntry:
    def __init__(self, colour, note=""):
        self.date = datetime.date.today()  # Store today's date
        self.colour = colour  # Store the mood color
        self.note = note  # Optional note for the mood

    def __str__(self):
        # String representation of the mood entry
        return f"{self.date} - Colour: {self.colour}, Note: {self.note}"
    

# Class to track mood entries
class MoodTracker:
    def __init__(self):
        self.entries = []  # List to store all mood entries
        self.allowed_colours = {  # Predefined mood colors and their meanings
            "blue": "Calm, peaceful, relaxed",
            "yellow": "Happy, energetic, optimistic",
            "red": "Angry, passionate, intense",
            "black": "Sad, stressed, tired",
            "green": "Hopeful, balanced, natural",
            "purple": "Creative, imaginative, mysterious",
            "orange": "Sociable, excited, motivated",
            "white": "Clear, pure, refreshed",
            "other": "Custom mood (you define it)"
        }

    # Method to add a mood entry
    def add_entry(self, colour, note=""):
        colour = colour.lower()  # Convert input color to lowercase
        if colour not in self.allowed_colours:
            # If color is not valid, show an error and stop
            print("Invalid input. Use a color from the guide or type 'other'.")
            return
        if colour == "other":
            # If user chooses 'other', ask for a custom mood description
            custom_colour = input("Please describe your mood or custom colour:")
            entry = MoodEntry(f"Other - {custom_colour}", note)
        else:
            # Otherwise, create a regular mood entry
            entry = MoodEntry(colour, note)
        self.entries.append(entry)  # Add the entry to the list
        print("Mood entry saved. \n")

    # Method to list all mood entries
    def list_entries(self):
        if not self.entries:
            print("No entries yet.\n")  # If no entries exist
            return
        print("Mood history")
        
        # Use enumerate to loop through all mood entries with an index starting from 1 (for user-friendly numbering)
        for i, entry in enumerate(self.entries, 1):
            print(f"{i}. {entry}")  # Print the entry with its corresponding number
        print()
    
    # Method to show the mood color guide
    def show_color_guide(self):
        print("🎨 Color Guide:")
        
        # Loop through each color and its meaning from the dictionary
        # Use color.capitalize() to make the first letter uppercase (for presentation)
        # The format specifier :<8 ensures each color label is left-aligned in an 8-character field
        # This keeps the output neatly aligned in a column
        for color, meaning in self.allowed_colours.items():
            print(f"{color.capitalize():<8}: {meaning}")
        print()


# Main function for the application
def main():
    tracker = MoodTracker()  # Create a new mood tracker instance

    while True:
        # Display menu options
        print("🎨 COLOR MOOD TRACKER")
        print("1. Add mood for today")
        print("2. Show mood history")
        print("3. Show color guide")
        print("4. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            # Option 1: Add a new mood entry
            color = input("Enter your mood color (use the guide or type 'other'): ")
            note = input("Optional note: ")
            tracker.add_entry(color, note)
        elif choice == "2":
            # Option 2: Show all mood history
            tracker.list_entries()
        elif choice == "3":
            # Option 3: Show the color guide
            tracker.show_color_guide()
        elif choice == "4":
            # Option 4: Exit the application
            print("👋 Goodbye!")
            break
        else:
            # Invalid input handling
            print("⚠️ Invalid selection. Please try again.\n")


# Entry point of the program
if __name__ == "__main__":
    main()
