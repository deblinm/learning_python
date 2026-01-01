import  random

Character = ["Alex", "Darcy", "Elara", "Finn",
             "Harper", "Orion", "Piper", "Rowan",
             "Silas", "Willow"]
Action = ["Tapping fingers impatiently", "Fiddling with a necklace",
          "Sharpening a knife or tool", "Brushing hair back from face",
          "Adjusting glasses", "Pacing back and forth", "Polishing a medal/object",
          "Staring out a window", "Counting change", "Checking a watch", "Deep sighing",
          "Shivering (even indoors)", "Flinching at loud noises", "Running hands through hair",
          "Humming a tune", "Emotional & Reactive Actions", "Slamming a door",
          "Hiding a smile", "Clenching fists", "Turning away suddenly",
          "Widening eyes in surprise", "Covering mouth to stifle a gasp",
          "Shaking head in disbelief", "Wringing hands", "Blushing deeply",
          "Frowning intensely", "Dropping something in shock", "Stiffening posture",
          "Looking over shoulder nervously", "Burying face in hands",
          "Letting out a nervous laugh ", "Social & Interpersonal Actions",
          "Offering a warm hug", "Patting someone on the back", "Avoiding eye contact",
          "Offering a cup of tea/coffee", "Giving a subtle nod", "Ignoring someone completely",
          "Sharing a secret glance", "Helping with a heavy bag", "Lecturing/scolding someone",
          "Offering a genuine compliment", "Goal-Oriented & Creative Actions",
          "Sketching in a notebook", "Studying a map", "Packing a bag", "Digging in a garden",
          "Building a fire", "Fixing a broken item", "Mending clothes", "Writing a letter",
          "Practicing a skill (music, sport)", "Organizing a desk/space"]

while True:
    user_answer = input("Would you like to generate a random sentence(yes/no)? ").strip().lower()
    if user_answer == "yes":
        final_action = random.choice(Character) + ' is ' + random.choice(Action)
        print(final_action)
        continue
    elif user_answer == "no":
        print("Thank You!!!!")
        break
    else:
        print("please answer only by typing yes or no")
        continue
