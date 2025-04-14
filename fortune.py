import random

def main():
    print("🔮 Welcome to Adesh Sinha's Fortune Teller (21JE0036) 🔮")
    
    mood = input("How are you feeling today? (happy/sad/neutral): ").lower()
    
    happy_fortunes = [
        "✨ Your fortune: Great things await you, Adesh Sinha! Keep smiling. ✨",
        "✨ Your fortune: Your positive energy will lead to wonderful opportunities today! ✨",
        "✨ Your fortune: The sun shines brighter because of your happiness! ✨"
    ]
    
    sad_fortunes = [
        "✨ Your fortune: Better days are coming. Tomorrow will bring you joy. ✨",
        "✨ Your fortune: Even in darkness, Adesh Sinha, you'll find your inner light. ✨",
        "✨ Your fortune: This feeling is temporary. Happiness awaits around the corner. ✨"
    ]
    
    neutral_fortunes = [
        "✨ Your fortune: Balance in all things will lead you to success. ✨", 
        "✨ Your fortune: Adesh Sinha, your calm demeanor will help solve a mystery today. ✨",
        "✨ Your fortune: Neither too high nor too low - you're on the perfect path. ✨"
    ]
    
    if mood == "happy":
        print(random.choice(happy_fortunes))
    elif mood == "sad":
        print(random.choice(sad_fortunes))
    elif mood == "neutral":
        print(random.choice(neutral_fortunes))
    else:
        print("✨ Your fortune: I cannot read your mood, but Adesh Sinha's destiny is still bright! ✨")

if __name__ == "__main__":
    main()
