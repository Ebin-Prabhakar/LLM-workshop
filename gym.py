import os
from dotenv import load_dotenv
from mistralai import Mistral

# =========================
# Load API Key
# =========================
load_dotenv()

API_KEY = os.getenv("MISTRAL_API_KEY")

if not API_KEY:
    print("❌ MISTRAL_API_KEY not found in .env file")
    exit()

# =========================
# Initialize Mistral Client
# =========================
client = Mistral(api_key=API_KEY)

MODEL = "mistral-small-latest"

# =========================
# System Prompt
# =========================
SYSTEM_PROMPT = """
You are a professional gym trainer and fitness coach.

You ONLY answer questions related to:
- gym workouts
- bodybuilding
- strength training
- muscle gain
- weight loss
- exercise techniques
- workout routines
- fitness nutrition
- gym equipment
- recovery and rest

Rules:
1. If the question is gym/fitness related → answer clearly.
2. If the question is unrelated → respond ONLY with:
"I can only answer gym and fitness related questions."
3. Keep answers helpful and practical.
"""

# =========================
# Gym Query Filter
# =========================
GYM_KEYWORDS = [

# General fitness
"gym","fitness","exercise","workout","training","strength","conditioning",
"physical training","resistance training","weight training","functional training",
"athletic training","fitness routine","fitness program",

# Body parts / anatomy
"muscle","muscles","skeletal muscle","muscle fibers","muscle fibre",
"biceps","triceps","forearms","shoulders","deltoids","rear delts","front delts",
"chest","pectorals","upper chest","lower chest",
"back","lats","latissimus dorsi","traps","trapezius","rhomboids",
"spine","erector spinae",
"core","abs","abdominals","obliques","rectus abdominis","transverse abdominis",
"legs","quads","quadriceps","hamstrings","glutes","gluteus maximus",
"calves","soleus","gastrocnemius",
"hip flexors","adductors","abductors",
"joints","ligaments","tendons","cartilage",

# Exercises
"bench press","incline bench","decline bench",
"push up","pushups","dips",
"squat","back squat","front squat","hack squat",
"deadlift","romanian deadlift","sumo deadlift",
"pull up","chin up","lat pulldown",
"barbell row","seated row","t bar row",
"shoulder press","military press","overhead press",
"lateral raise","rear delt fly",
"bicep curl","barbell curl","hammer curl","preacher curl",
"tricep pushdown","skull crushers","close grip bench",
"leg press","leg extension","leg curl",
"calf raises","seated calf raise",
"plank","crunch","leg raise","russian twist",

# Training methods
"hypertrophy","progressive overload","time under tension",
"eccentric","concentric","isometric",
"compound exercise","isolation exercise",
"volume","intensity","frequency",
"drop set","superset","giant set",
"pyramid set","failure training",
"strength training","power training",
"endurance training","hiit","interval training",
"cross training","circuit training",

# Physiology / biology
"metabolism","metabolic rate","energy systems",
"ATP","ATP-PC system","glycolysis",
"aerobic respiration","anaerobic respiration",
"lactic acid","oxygen consumption","VO2 max",
"muscle fatigue","muscle recovery",
"neural adaptation","motor unit recruitment",

# Physics / biomechanics
"biomechanics","force","torque","leverage",
"moment arm","mechanical tension",
"range of motion","kinetics","kinematics",
"gravity","resistance","load","momentum",
"stability","balance","center of mass",

# Nutrition
"diet","nutrition","macronutrients","micronutrients",
"calories","calorie deficit","calorie surplus",
"protein","carbohydrates","carbs","fats",
"fiber","vitamins","minerals","electrolytes",
"hydration","water intake",

# Muscle building nutrition
"bulking","cutting","lean bulk",
"muscle gain","fat loss","body recomposition",
"meal plan","pre workout meal","post workout meal",

# Supplements
"whey protein","casein protein","protein powder",
"creatine","creatine monohydrate",
"bcaa","eaas",
"beta alanine",
"pre workout","caffeine",
"multivitamin","omega 3","fish oil",

# Recovery
"recovery","muscle recovery","active recovery",
"rest day","deload",
"foam rolling","stretching","mobility",
"flexibility","warm up","cool down",

# Sleep
"sleep","deep sleep","rem sleep",
"sleep recovery","sleep quality",
"circadian rhythm",

# Hormones
"testosterone","growth hormone",
"insulin","cortisol",
"anabolism","catabolism",

# Body composition
"body fat","body fat percentage",
"lean mass","fat mass",
"bmi","body composition",

# Injuries
"injury","muscle strain","sprain",
"tendonitis","overtraining",
"joint pain","knee pain","shoulder pain",
"lower back pain","rehabilitation",

# Modern fitness trends
"crossfit","powerlifting","bodybuilding",
"calisthenics","street workout",
"functional fitness","mobility training",
"plyometrics","explosive training",

# Gym equipment
"dumbbells","barbell","kettlebell",
"resistance bands","smith machine",
"cable machine","leg press machine",
"pull up bar","squat rack",

# Health and wellness
"fitness lifestyle","physical health",
"athletic performance","sports performance",
"endurance","stamina","agility"
]


def is_gym_related(query: str) -> bool:
    query = query.lower()
    for word in GYM_KEYWORDS:
        if word in query:
            return True
    return False


# =========================
# Ask Mistral
# =========================
def ask_gym_assistant(question):

    if not is_gym_related(question):
        return "I can only answer gym and fitness related questions."

    try:
        response = client.chat.complete(
            model=MODEL,
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": question}
            ],
            temperature=0.4
        )

        return response.choices[0].message.content

    except Exception as e:
        return f"⚠️ Error contacting Mistral API: {e}"


# =========================
# CLI Chat Loop
# =========================
def main():

    print("\n💪 Gym AI Assistant")
    print("Ask any gym or fitness question")
    print("Type 'exit' to quit\n")

    while True:

        try:
            user_input = input("You: ")

            if user_input.lower() in ["exit", "quit"]:
                print("Assistant: Stay strong 💪")
                break

            if not user_input.strip():
                print("Assistant: Please ask a question.")
                continue

            answer = ask_gym_assistant(user_input)

            print("\nAssistant:", answer)
            print()

        except KeyboardInterrupt:
            print("\nAssistant: Goodbye! Keep training 💪")
            break


# =========================
# Run Program
# =========================
if __name__ == "__main__":
    main()