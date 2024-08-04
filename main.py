

import mood_responses

def main():
    mood = input("How are you feeling today? ").strip()
    response = mood_responses.mood_response(mood)
    print(response)

main()
