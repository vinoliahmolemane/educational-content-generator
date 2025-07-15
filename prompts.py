def get_prompt_templates(content_type, subject, level):
    level_text = level.lower()

    if content_type == "Lesson Summary":
        return f"Write a clear and concise {level_text}-level lesson summary about {subject}."

    elif content_type == "Quiz Questions":
        return (
            f"Generate 5 {level_text}-level quiz questions with answers about {subject}. "
            "Make questions varied and educational."
        )

    elif content_type == "Concept Explanation":
        return (
            f"Explain the concept of {subject} in a detailed and easy-to-understand way suitable for a "
            f"{level_text}-level learner."
        )

    elif content_type == "Flashcards":
        return (
            f"Create 5 flashcards for studying the topic {subject} at a {level_text} difficulty level. "
            "Each flashcard should have a question and a concise answer."
        )

    elif content_type == "Study Tips":
        return (
            f"Provide useful {level_text}-level study tips and strategies for learning about {subject}."
        )

    else:
        return f"Write about {subject}."
