def generate_training_prompt(age, gender, mileage, race_goal, goal_time, fitness_level):
    """
    Builds the AI prompt for generating a weekly training plan.
    """
    return f"""
    Create a 1-week running training plan for a {age}-year-old {gender}.
    Current weekly mileage: {mileage} miles.
    Race goal: {race_goal}.
    Target goal time: {goal_time if goal_time else "Not specified"}.
    Current condition: {fitness_level}.

    Requirements:
    - Provide 7 days of training (Mon–Sun).
    - Include mileage or duration for each day.
    - Specify type of workout (easy run, tempo, intervals, long run, rest, cross-training).
    - Adapt intensity based on how the runner feels today ("{fitness_level}").
    - Add a short 1–2 sentence explanation for each day, grounded in running science.
    - Keep it beginner-friendly and safe.
    """
