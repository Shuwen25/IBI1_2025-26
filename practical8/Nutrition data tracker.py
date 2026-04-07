class FoodItem:
    def __init__(self,name,calories,protein,carbs,fat):
        self.name=name
        self.calories=calories
        self.protein=protein
        self.carbs=carbs
        self.fat=fat

def nutrition(food_list):
    total_calories=0
    total_protein=0
    total_carbs=0
    total_fat=0

    for food in food_list:
        total_calories+=food.calories
        total_protein+=food.protein
        total_carbs+=food.carbs
        total_fat+=food.fat
    
    print(f"Total calories: {total_calories} kcal")
    print(f"Total protein: {total_protein} g")
    print(f"Total carbohydrates: {total_carbs} g")
    print(f"Total fat: {total_fat} g")

    if total_calories>2500 or total_fat>90:
        print(f"Warning: You have taken in excessive calories or fat today!")
    else:
        print("nutrition levels are within the standard range.")
    
apple=FoodItem("Apple",60,0.3,15,0.5)
burger=FoodItem("Burger",800,30,40,50)
salad =FoodItem("Salad",200,10,15,10)
daily_diet=[apple,burger,salad]
nutrition(daily_diet)
