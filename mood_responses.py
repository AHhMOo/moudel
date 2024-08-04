
def mood_response(mood):
    mood = mood.lower()
    responses = {
        "happy": "That's great to hear! Keep smiling and enjoy your day!",
        "sad": "I'm sorry to hear that. I hope things get better soon.",
        "excited": "Awesome! It sounds like something fun is coming up.",
        "angry": "It can be tough to deal with anger. Try to take some deep breaths.",
        "bored": "Sometimes boredom can be a chance to explore new interests!",
    }

    return responses.get(mood, "Hmm, I don't recognize that mood. But I hope you're doing well!")
