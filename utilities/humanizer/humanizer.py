import random

def humanize(text):
    # Mapping of formal words to casual/human-like synonyms
    replacements = {
        "utilize": ["use", "go with"],
        "commence": ["start", "get going"],
        "terminate": ["end", "stop", "finish"],
        "subsequent": ["next", "later"],
        "furthermore": ["also", "plus"],
        "however": ["but", "though"],
        "assistance": ["help"],
        "therefore": ["so"],
        "demonstrate": ["show"],
        "sufficient": ["enough"],
        "requires": ["needs"],
        "provide": ["give"]
    }
    
    words = text.split()
    humanized_words = []
    
    for word in words:
        clean_word = word.lower().strip(".,!?;:")
        suffix = word[len(clean_word):] # preserve punctuation
        
        if clean_word in replacements:
            new_word = random.choice(replacements[clean_word])
            # Try to match capitalization
            if word[0].isupper():
                new_word = new_word.capitalize()
            humanized_words.append(new_word + suffix)
        else:
            humanized_words.append(word)
            
    # Add some human "filler" if it's too short
    if len(humanized_words) > 5 and random.random() > 0.7:
        insertion_point = random.randint(1, len(humanized_words)-1)
        fillers = ["you know,", "honestly,", "basically,", "actually,"]
        humanized_words.insert(insertion_point, random.choice(fillers))

    return " ".join(humanized_words)

def main():
    print("Welcome to the Text Humanizer!")
    print("Paste your formal/AI text and I will try to make it sound more natural.")
    
    while True:
        text = input("\nEnter text (or type 'quit' to exit): ")
        if text.lower() == 'quit':
            break
            
        if not text.strip():
            continue
            
        result = humanize(text)
        print("\n--- Humanized Text ---")
        print(result)

if __name__ == "__main__":
    main()
