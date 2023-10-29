import openai
import time

# Your OpenAI API key
api_key = "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"

cal_count = {
    "b1": 300, "b2": 250, "b3": 220,
    "l1": 350, "l2": 400, "l3": 280,
    "d1": 380, "d2": 250, "d3": 320,
    "s1": 200, "s2": 150, "s3": 180,
    "v1": 570, "v2": 300, "v3": 290
}
meal_choice = []
calories = 0  # Initialize calories as 0

# Function to interact with ChatGPT model via API with rate limiting
def chat_with_gpt(prompt):
    response = openai.Completion.create(
        engine="davinci",
        prompt=prompt,
        max_tokens=50,
        api_key=api_key
    )
    return response.choices[0].text

# Define a function to interact with the chatbot
def healthy_cooking_chatbot(user_input, user_info):
    global calories  # Declare calories as a global variable
    response = ""  # Initialize response

    if "breakfast" in user_input:
        response = "Sure, here are some breakfast ideas:\n1. Classic oatmeal with fruits and nuts (Calories: 300 per serving)\n2. Yogurt parfait with granola and berries (Calories: 250 per serving)\n3. Scrambled eggs with spinach and tomatoes (Calories: 220 per serving)\nIf you'd like more details or have other questions, feel free to ask."

    elif "lunch" in user_input:
        response = "For a healthy lunch, you can consider options like:\n1. Salad with grilled chicken (Calories: 350 per serving)\n2. Quinoa bowl (Calories: 400 per serving)\n3. Vegetable stir-fry (Calories: 280 per serving). \nWould you like more information on any of these or something else?"

    elif "dinner" in user_input:
        response = "Dinner options include:\n1. Baked salmon with vegetables (Calories: 380 per serving)\n2. Lentil soup (Calories: 250 per serving)\n3. Quinoa and vegetable stir-fry (Calories: 320 per serving). \nIf you'd like more details or have other questions, feel free to ask."

    elif "snack" in user_input:
        response = "For healthy snacks, you can have options like:\n1. Mixed nuts (Calories: 200 per serving)\n2. Greek yogurt with honey (Calories: 150 per serving)\n3. Sliced apple with peanut butter (Calories: 180 per serving). \nWould you like more information on any of these or have other questions?"

    elif "calories" in user_input or "calorie" in user_input:
        response = "The average calorie requirement per day is 2000 kcal.\n You have consumed " + str(calories) + " kcal"

    elif "vegan" in user_input.lower():
        response = "Vegan options include:\n1.) Lentil Bolognese with green salad (Calories: 570 per serving)\n2.) Coconut rice bowl (300 Calories per serving)\n3.) Vegan Alfredo (290 Calories per serving)\nWould you like more information on any of these or have any other questions?"

    elif "quit" in user_input.lower():
        print("Your meal choice for the day: ", meal_choice)
        if calories > 2000 and calories <= 2500:
            print("Good job! Optimum calorie intake secured. Total calories = ", calories)
        elif calories < 2000:
            print("Calorie intake must be increased. Total calories = ", calories)
        elif calories > 2500:
            print("Calorie intake must be decreased. Total calories = ", calories)
        print("ChatGPT: Goodbye, {}! Have a great day.".format(user_info['name']))
        return None
    else:
        response = "Please ask me any questions regarding healthy meal choices for any time of the day and your calorie requirements."

    print("ChatGPT:", response)  # Display ChatGPT response

    if "breakfast" in user_input or "lunch" in user_input or "dinner" in user_input or "snack" in user_input or "vegan" in user_input.lower():
        b = int(input("Enter choice: 1/2/3: "))
        if "breakfast" in user_input:
            if b == 1:
                meal_choice.append("Oatmeal with fruits and nuts")
                calories += cal_count["b1"]
            elif b == 2:
                meal_choice.append("Yogurt parfait with granola and berries")
                calories += cal_count["b2"]
            elif b == 3:
                meal_choice.append("Scrambled eggs with spinach and tomatoes.")
                calories += cal_count["b3"]
        elif "lunch" in user_input:
            if b == 1:
                meal_choice.append("Salad with grilled chicken")
                calories += cal_count["l1"]
            elif b == 2:
                meal_choice.append("Quinoa bowl")
                calories += cal_count["l2"]
            elif b == 3:
                meal_choice.append("Vegetable stir fry")
                calories += cal_count["l3"]
        elif "dinner" in user_input:
            if b == 1:
                meal_choice.append("Baked salmon with vegetables.")
                calories += cal_count["d1"]
            elif b == 2:
                meal_choice.append("Lentil soup.")
                calories += cal_count["d2"]
            elif b == 3:
                meal_choice.append("Quinoa and Vegetable stir fry")
                calories += cal_count["d3"]
        elif "snack" in user_input:
            if b == 1:
                meal_choice.append("Mixed nuts")
                calories += cal_count["s1"]
            elif b == 2:
                meal_choice.append("Greek Yogurt with honey")
                calories += cal_count["s2"]
            elif b == 3:
                meal_choice.append("Sliced apple with peanut butter")
                calories += cal_count["s3"]
        elif "vegan" in user_input.lower():
            if b == 1:
                meal_choice.append("Lentil Bolognese with green salad")
                calories += cal_count["v1"]
            elif b == 2:
                meal_choice.append("Coconut rice bowl")
                calories += cal_count["v2"]
            elif b == 3:
                meal_choice.append("Vegan Alfredo")
                calories += cal_count["v3"]
        print("Your meal choice:", meal_choice)
        print("Calorie intake = ", calories)

    # Introduce rate limiting here to avoid exceeding API rate limits
    time.sleep(2)  # 2-second rate limiting

    return response

# Initial greeting and user information collection
print("ChatGPT: Hello! I'm your Healthy Cooking Assistant.")
user_info = {}
user_info['name'] = input("What's your name? ")
user_info['age'] = input("How old are you? ")
user_info['gender'] = input("What's your gender? ")
user_info['weight'] = input("What's your weight in kilograms? ")
user_info['profession'] = input("What's your profession? ")

print("ChatGPT: Nice to meet you, {}! How can I assist you today?".format(user_info['name']))

# Start a conversation with the user
while True:
    user_input = input("{}: ".format(user_info['name']))
    response = healthy_cooking_chatbot(user_input, user_info)
    if response is None:
        break  # End the conversation if the user chooses to quit
