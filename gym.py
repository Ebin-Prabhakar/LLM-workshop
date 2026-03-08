import os
import google.generativeai as genai
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

API_KEY = os.getenv("GOOGLE_API_KEY")

# Configure Gemini
genai.configure(api_key=API_KEY)

model = genai.GenerativeModel("gemini-3-flash-preview")

SYSTEM_PROMPT = """
You are an expert fitness trainer, strength and conditioning coach, and sports science advisor.

Your role is to provide accurate, practical, and safe advice related to physical fitness and human performance.

You are allowed to answer questions related to:

• Gym workouts
• Strength training
• Bodybuilding
• Muscle gain and hypertrophy
• Weight loss and fat loss
• Cardio training
• Endurance training
• Running and jogging
• Cycling and biking
• Swimming and other cardio activities
• Athletic performance
• Sports training
• Calisthenics and bodyweight training
• Functional fitness
• CrossFit and HIIT
• Mobility and flexibility training
• Stretching and warm-ups
• Injury prevention
• Recovery and rest
• Sleep and physical recovery
• Nutrition for athletes
• Diet planning for fitness goals
• Supplements used in sports nutrition
• Body composition
• Strength and conditioning
• Exercise technique and form
• Gym equipment usage
• Home workouts
• Outdoor physical activities
• General health related to physical activity

Guidelines:

1. Provide clear and practical answers.
2. If appropriate, suggest exercises, training methods, or routines.
3. Keep explanations simple and useful.
4. Encourage safe training practices.
5. Do not give medical diagnoses.

Restriction:

If a question is NOT related to fitness, gym training, sports performance, exercise, nutrition for athletes, recovery, sleep, or physical health,

respond ONLY with:

"I can only answer questions related to fitness, gym training, sports, and physical health."
"""

GYM_KEYWORDS = [
" gym ", " fitness ", " exercise ", " workout ", " training ",
" cardio ", " running ", " cycling ", " swimming ",
" squat ", " deadlift ", " bench press ", " push up ", " pull up ",
" shoulder press ", " bicep curl ", " tricep ",
" chest ", " back ", " legs ", " abs ", " muscle ",
" protein ", " diet ", " calories ",
" creatine ", " whey protein ",
" stretching ", " recovery ", " sleep "
]


def is_gym_related(query: str):

    query = " " + query.lower() + " "

    for word in GYM_KEYWORDS:
        if word in query:
            return True

    return False


def ask_gym_assistant(user_query):

    if not is_gym_related(user_query):
        return "I can only answer questions related to fitness, gym training, sports, and physical health."

    prompt = SYSTEM_PROMPT + "\n\nUser Question:\n" + user_query

    try:
        response = model.generate_content(prompt)
        return response.text

    except Exception as e:
        return f"Error contacting Gemini API: {e}"


def main():

    print("\n🏋️ Fitness AI Assistant Ready")
    print("Type 'exit' to quit\n")

    while True:

        user_input = input("You: ")

        if user_input.lower() == "exit":
            break

        answer = ask_gym_assistant(user_input)

        print("\nTrainer:", answer)
        print()


if __name__ == "__main__":
    main()