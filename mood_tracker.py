import datetime

class MoodEntry:
    def __init__(self, colour, note=""):
        self.date = datetime.date.today()
        self.colour = colour
        self.note = note

    def __str__(self):
        return f"{self.date} - Colour: {self.colour}, Note: {self.note}"
    

class MoodTracker:
    def __init__(self):
        self.entries = []
        self.allowed_colours = {
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

    def add_entry(self, colour, note=""):
        colour = colour.lower()
        if colour not in self.allowed_colours:
            print("Invalid input. Use a color from the guide or type 'other'.")
            return
        if colour == "other":
            custom_colour = input("Please describe your mood or custom colour:")
            entry = MoodEntry(f"Other - {custom_colour}", note)
        else:
            entry = MoodEntry(colour, note)
        self.entries.append(entry)
        print("Mood entry saved. \n")

    def list_entries(self):
        if not self.entries:
            print("No entries yet.\n")
            return
        print("Mood history")
        for i, entry in enumerate(self.entries, 1):
            print(f"{i}. {entry}")
        print()
    
    def show_color_guide(self):
        print("🎨 Color Guide:")
        for color, meaning in self.allowed_colours.items():
            print(f"{color.capitalize():<8}: {meaning}")
        print()

def main():
    tracker = MoodTracker()

    while True:
        print("🎨 COLOR MOOD TRACKER")
        print("1. Add mood for today")
        print("2. Show mood history")
        print("3. Show color guide")
        print("4. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            color = input("Enter your mood color (use the guide or type 'other'): ")
            note = input("Optional note: ")
            tracker.add_entry(color, note)
        elif choice == "2":
            tracker.list_entries()
        elif choice == "3":
            tracker.show_color_guide()
        elif choice == "4":
            print("👋 Goodbye!")
            break
        else:
            print("⚠️ Invalid selection. Please try again.\n")

if __name__ == "__main__":
    main()
