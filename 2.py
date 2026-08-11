import sys
import time
lyrics = [
    ("khud se jo thay waaday", 0.8),
    ("Ke ab yeh ishq nibhaana nahi?", 1.2),
    ("Mein morrun tum se jo yeh chehra", 1.0),
    ("Dobara nazar milana nahi", 1.1),
    ("Yeh duniya jaanay mera dard", 0.9),
    ("Tujhe yeh nazar kyun aata nahi?", 1.3),
    ("Sohneya, yoon tera sharmana", 0.8),
    ("meri jaan naa lele", 1.0),
    ("Kaan ke peeche zulf chhupana,", 0.9),
    ("meri jaan, kya kehne", 1.2),
]
def print_typewriter(text, char_delay=0.035):
   
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(char_delay)
    print()
def play_synced_lyrics():
    print("When some lyrics hit different...🌹😌\n")
    time.sleep(0.5)  
    for line, pause in lyrics:
        print_typewriter(line)
        time.sleep(pause)
if __name__ == "__main__":
    play_synced_lyrics()