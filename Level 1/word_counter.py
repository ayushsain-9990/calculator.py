import os

def count_words_in_file():
    print("===== WORD COUNTER =====")
    filename = input("Kripya text file ka naam ya path enter karein (e.g., sample.txt): ")

    try:
        # File read karna
        with open(filename, 'r', encoding='utf-8') as file:
            content = file.read()
            
            # Content ko words me split karke count karna
            words = content.split()
            word_count = len(words)
            
            print(f"\n✅ File successfully read ho gayi!")
            print(f"📊 Total words count: {word_count}")

    # Exception handling: File nahi milne par
    except FileNotFoundError:
        print(f"\n❌ Error: '{filename}' naam ki file nahi mili. Kripya file path check karein.")
    
    # Dusre tarah ke errors handle karne ke liye
    except Exception as e:
        print(f"\n❌ Ek error aaya: {e}")

if __name__ == "__main__":
    count_words_in_file()