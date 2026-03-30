from datetime import date
import sys
import inflect
p = inflect.engine()

def main():
    s = input("Date of Birth: ")
    minutes = get_minutes(s)
    print(minutes_to_words(minutes))

def get_minutes(s):
    try:
        birth=date.fromisoformat(s)
    except ValueError:
        sys.exit("Invalid date")
    today=date.today()
    delta=today-birth
    return delta.days*24*60
    

def minutes_to_words(minutes):
    return p.number_to_words(minutes, andword="").capitalize() + " minutes"

if __name__ == "__main__":
    main()