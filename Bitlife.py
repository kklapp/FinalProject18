import random
   
happiness = random.randint(1,101)
health = random.randint(1,101)
smarts = random.randint(1,101)
looks = random.randint(1,101)
death_chance= 50
possible_genders = ["male","female", "alien"]
gender= random.choice(possible_genders)
completed_scenarios = []
times_studied = []
times_workedout = []

class Person:
  def __init__(self,name,status,month_display,month_total,grade,gender,popularity,happiness,health,smarts,looks):
    self.name = name
    self.status = status
    self.month_display = month_display
    self.month_total = month_total
    self.grade= grade
    self.gender = gender
    self.popularity = popularity
    self.happiness = happiness
    self.health = health
    self.smarts = smarts 
    self.looks = looks
    
  def introduce(self):
    print(f"Welcome {self.name} to your first day of 9th grade. You were born {self.gender}.")

  def stats(self):
      print(f"Grade: {self.grade} \nMonth: {self.month_display} \n\n Stats:\n Popularity: {self.popularity} \n Happiness: {self.happiness} \n Health: {self.health} \n Smarts: {self.smarts} \n Looks: {self.looks} \n")
  
  def month_up(self):
    self.month_display += 1
    self.month_total += 1
    print(f'It is the next month')

  def school_scenarios(self):
    global completed_scenarios
    
    if self.grade == 9:
      scenario = random.randint(1,3)
      if scenario == 1:
        if 1 not in completed_scenarios:
          completed_scenarios.append(1)
          while True:
            x = input("A bully wants to take your lunch. \n What will you do? \n \n a= punch the bully \n b= give the bully your lunch \n c = run away \n")
            if x == 'a':
              fight = random.randint(1,2)
              if fight == 1:
                print("You got beat up")
                self.health -= 10
                print("OOF that one hurt. Your health just went down ten points")
                break
              if fight == 2:
                print("You won")
                self.happiness += 10
                print("Congrats you surprisingly won! Your happiness went up 10 points")
                break
            elif x == 'b':
              self.happiness -= 10
              print("That one was a blow to your self esteem. Your happiness went down 10 points")
              break
            elif x == 'c':
              self.smarts += 5
              print("Finally, you did something intelligent. Your smarts went up 5 points")
              break
            else:
              print("Error")
              
      elif scenario == 2:
        if 2 not in completed_scenarios:
          completed_scenarios.append(2)
          while True:
            x = input("You are assigned a group project from your freshman technology teacher. What are you going to do? \n \n a= do all the work \n b= do none of the work \n c= split up the work evenly \n")
            if x == 'a':
              self.smarts += 10
              print("Congrats try hard. Your now THAT kid, but hey your smarts went up 10 points")
              break
            elif x == 'b':
              self.popularity -= 10
              print("Ew. Now your THAT kid. No one likes you so you lost 10 popularity points")
              break
            elif x == 'c':
              self.popularity += 5
              print("Your chill with your groupmates now. You gained 5 popularity points")
              break
            else:
              print("Error")
              
      elif scenario == 3:
        if 3 not in completed_scenarios:
          completed_scenarios.append(3)
          while True:
            x = input("Your mom is yelling at you for getting a bad grade in Dr. Gupta's freshman biology class. What is your next move? \n \n a= give up and cry \n b= study harder \n c= bribe the teacher \n")
            if x == 'a':
              self.happiness -= 10
              print("Since you are a sad, depressed, loser your happiness went down ten points")
              break
            elif x == 'b':
              self.smarts += 10
              print("Wow! Good job! You actually made a good decision. Your smarts went up 10 points")
              break
            elif x == 'c':
              self.smarts -= 10
              print("Nice try! But she failed you and gave you a fat 0. Your smarts went down 10 points.")
              break
            else:
              print("Error")
              
  def study(self):
    if self.month_total in times_studied:
      print("We all know you aint studying more than once a month. Nice try")
    else:
      times_studied.append(self.month_total)
      print('You went to the library to study like a good boy. Your smarts went up 10 points.')
      self.smarts += 5
      
  def workout(self):
    if self.month_total in times_workedout:
      print("You got your swole on so hard you broke the gym. Come back at a later time.")
    else:
      times_workedout.append(self.month_total)
      while True:
        x = input("What are you working on? \n c = cardio \n f = flexibility \n w = weights \n p = pretend to do something \n")
        y = random.randint(1,10)
        if y == 1:
          print("Nice job bozo. You injured yourself at the gym. Your health is now down 10 points.")
          self.health -= 10
        elif x == 'c':
          print("The only other time I have you seen you ran that fast is into Wendy's when you heard they were having a deal. But hey your looks and health went up 5 points")
          self.looks += 5
          self.health += 5
          break
        elif x == 'f':
          print("Maybe next time youll actually be able to touch your toes but at least you put in some effort. Your health went up 5 points")
          self.health += 5
          break
        elif x== 'w':
          print("Damn the grind really is real. You actually broke a sweat. Not gonna lie im surprised. Your looks went up 10 points")
          self.looks += 10
          break
        elif x== 'p':
          print("This is lowkey sad but hey what works for you works for me so your happiness went up 5 points.")
          self.happiness += 5
          break
        else:
          print("Error")
              
character = Person(input("What is your name"),"alive",0,0,9,gender,50,happiness,health,smarts,looks)

character.introduce()

if character.gender == "alien":
  print("⏁⊑⟒ ☌⟟⍀⌰ ⏃⏁ ⏁⊑⟒ ⏚⍜⍜⏁⊑ ⌇⍜⌰⎅ ⎎⟟⎎⏁⊬ ⏚⍜⋏⎅⌇. ⌰⍜⍜☍ ⟟⋏ ⏁⊑⟒ ☊⍜⍀⋏⟒⍀ ⏁⍜ ⎎⟟⋏⎅ ⏁⊑⟒ ⏁⏃⋏ ⌇⊑⟟⍀⏁.⏁⊑⟒ ☌⍀⟒⏃⏁ ⏃⋏⏁⟟⍾⎍⟟⏁⊬ ⍜⎎ ⋏⍜⏁⊑⟟⋏☌ ⟟⌇ ⏃⌿⌿⏃⍀⟒⋏⏁ ⎎⍀⍜⋔ ⟟⏁⌇ ⏚⟒⟟⋏☌ ⌇⍜ ⎐⟟⌇⟟⏚⌰⟒ ⟟⋏ ⏁⊑⟒ ⏃☊☊⍜⎍⋏⏁⌇ ⍙⟒ ⊑⏃⎐⟒ ⍜⎎ ⏁⊑⟒ ⏚⟒☌⟟⋏⋏⟟⋏☌ ⍜⎎ ⟒⎐⟒⍀⊬ ⋏⏃⏁⟟⍜⋏. ⏁⊑⟟⌇ ⟟⌇ ⎐⟒⍀⊬ ⌿⌰⏃⟟⋏⌰⊬ ⏁⍜ ⏚⟒ ⎅⟟⌇☊⍜⎐⟒⍀⟒⎅ ⟟⋏ ⏁⊑⟒ ⎎⟟⍀⌇⏁ ⌿⏃☌⟒⌇, ⏃⋏⎅ ⌇⍜⋔⟒⏁⟟⋔⟒⌇")
  character.status = 'ded'
  print('the fbi found you')
  
while character.status == "alive":
  if character.month_display == 7:
    character.month_display = 0
    character.grade += 1
    
  if character.health < 0:
    character.health = 0
  if character.health > 100:
    character.health = 100
  if character.happiness < 0:
    character.happiness = 0
  if character.happiness > 100:
    character.happiness = 100
  if character.smarts < 0:
    character.smarts = 0
  if character.smarts > 100:
    character.smarts = 100
  if character.looks < 0:
    character.looks = 0
  if character.looks > 100:
    character.looks = 100
    
  character.stats()
  death_number = random.randint(1,death_chance)
  kill_number = random.randint(1,death_chance)
  if death_number == kill_number:
    character.staus = "dead"
    x = random.randint(1,2)
    if x == 1:
        print("You died of an advil overdose")
    if x == 2:
        print("You tripped and fell and drowned in the toilet. There was no poop in it though so you are all good")
    break
  character.school_scenarios()
  print("\n Moves: \n a = advance a month \n s = go study at the library \n w = go workout")
  while True:
    move = input("What is your next move \n")
    if move == 'a':
      print("\n \n \n \n \n \n \n \n \n \n \n")
      character.month_up()
      break
    elif move == 's':
      character.study()
    elif move == 'w':
      character.workout()
    else:
      print("Error")
