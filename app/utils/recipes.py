from langchain_core.documents import Document

RECIPES_DOCUMENT = [

    Document(
        page_content="""
Recipe: Veg Cutlet
Ingredients: potato, carrot, peas, breadcrumbs
Taste: crispy and savory
Process: Boil and mash vegetables. Shape into patties and shallow fry until golden.
Nutrients: fiber-rich
""",
        metadata={
            "name": "Veg Cutlet",
            "type": "veg",
            "ingredients": ["potato", "carrot", "peas", "breadcrumbs"],
            "taste": "crispy",
            "nutrient": "fiber-rich",
            "meal_type": "snack"
        },
    ),

    Document(
        page_content="""
Recipe: Paneer Butter Masala
Ingredients: paneer, tomato, butter, cream
Taste: creamy and mildly spicy
Process: Cook tomato gravy with butter and spices. Add paneer and simmer with cream.
Nutrients: protein-rich
""",
        metadata={
            "name": "Paneer Butter Masala",
            "type": "veg",
            "ingredients": ["paneer", "tomato", "butter", "cream"],
            "taste": "creamy",
            "nutrient": "protein-rich",
            "meal_type": "lunch"
        },
    ),

    Document(
        page_content="""
Recipe: Egg Fried Rice
Ingredients: rice, egg, soy sauce, vegetables
Taste: savory and umami
Process: Scramble eggs and sauté vegetables. Mix cooked rice with soy sauce and eggs.
Nutrients: protein-rich
""",
        metadata={
            "name": "Egg Fried Rice",
            "type": "non-veg",
            "ingredients": ["rice", "egg", "soy sauce", "vegetables"],
            "taste": "savory",
            "nutrient": "protein-rich",
            "meal_type": "dinner"
        },
    ),

    Document(
        page_content="""
Recipe: Chicken Curry
Ingredients: chicken, onion, tomato, spices
Taste: spicy and flavorful
Process: Cook onions with spices and tomatoes. Add chicken and simmer until tender.
Nutrients: protein-rich
""",
        metadata={
            "name": "Chicken Curry",
            "type": "non-veg",
            "ingredients": ["chicken", "onion", "tomato", "spices"],
            "taste": "spicy",
            "nutrient": "protein-rich",
            "meal_type": "lunch"
        },
    ),

    Document(
        page_content="""
Recipe: Tomato Soup
Ingredients: tomato, garlic, butter
Taste: tangy and smooth
Process: Cook tomatoes with garlic. Blend and simmer with butter.
Nutrients: vitamin-rich
""",
        metadata={
            "name": "Tomato Soup",
            "type": "veg",
            "ingredients": ["tomato", "garlic", "butter"],
            "taste": "tangy",
            "nutrient": "vitamin-rich",
            "meal_type": "starter"
        },
    ),

    Document(
        page_content="""
Recipe: Grilled Fish
Ingredients: fish, lemon, spices
Taste: smoky and tangy
Process: Marinate fish with spices and lemon. Grill until cooked and slightly charred.
Nutrients: omega-3-rich
""",
        metadata={
            "name": "Grilled Fish",
            "type": "non-veg",
            "ingredients": ["fish", "lemon", "spices"],
            "taste": "smoky",
            "nutrient": "omega-3-rich",
            "meal_type": "dinner"
        },
    ),

    Document(
        page_content="""
Recipe: Vegetable Upma
Ingredients: rava, vegetables, mustard seeds
Taste: light and savory
Process: Roast rava and sauté vegetables. Cook together with water until soft.
Nutrients: carb-rich
""",
        metadata={
            "name": "Vegetable Upma",
            "type": "veg",
            "ingredients": ["rava", "vegetables", "mustard seeds"],
            "taste": "savory",
            "nutrient": "carb-rich",
            "meal_type": "breakfast"
        },
    ),

    Document(
        page_content="""
Recipe: Masala Dosa
Ingredients: rice batter, potato, spices
Taste: crispy and spicy
Process: Spread batter thin on pan. Fill with spiced potato mixture and cook crisp.
Nutrients: carb-rich
""",
        metadata={
            "name": "Masala Dosa",
            "type": "veg",
            "ingredients": ["rice batter", "potato", "spices"],
            "taste": "crispy",
            "nutrient": "carb-rich",
            "meal_type": "breakfast"
        },
    ),

    Document(
        page_content="""
Recipe: Paneer Sandwich
Ingredients: bread, paneer, mayonnaise
Taste: creamy and savory
Process: Mix paneer with mayonnaise. Spread on bread and toast lightly.
Nutrients: protein-rich
""",
        metadata={
            "name": "Paneer Sandwich",
            "type": "veg",
            "ingredients": ["bread", "paneer", "mayonnaise"],
            "taste": "creamy",
            "nutrient": "protein-rich",
            "meal_type": "snack"
        },
    ),

    Document(
        page_content="""
Recipe: Fruit Salad
Ingredients: apple, banana, orange, honey
Taste: sweet and fresh
Process: Chop fruits evenly. Mix with honey and chill before serving.
Nutrients: vitamin-rich
""",
        metadata={
            "name": "Fruit Salad",
            "type": "veg",
            "ingredients": ["apple", "banana", "orange", "honey"],
            "taste": "sweet",
            "nutrient": "vitamin-rich",
            "meal_type": "snack"
        },
    ),

    # --- Remaining 20 (shortened but same structure) ---

    Document(
        page_content="Recipe: Dal Tadka\nIngredients: lentils, garlic, spices\nTaste: spicy\nProcess: Cook lentils. Add tempered garlic and spices.\nNutrients: protein-rich",
        metadata={"name":"Dal Tadka","type":"veg","ingredients":["lentils","garlic","spices"],"taste":"spicy","nutrient":"protein-rich","meal_type":"lunch"},
    ),

    Document(
        page_content="Recipe: Omelette\nIngredients: eggs, onion, chili\nTaste: savory\nProcess: Beat eggs with onion and chili. Cook on pan until fluffy.\nNutrients: protein-rich",
        metadata={"name":"Omelette","type":"non-veg","ingredients":["eggs","onion","chili"],"taste":"savory","nutrient":"protein-rich","meal_type":"breakfast"},
    ),

    Document(
        page_content="Recipe: Vegetable Pulao\nIngredients: rice, vegetables, spices\nTaste: aromatic\nProcess: Sauté veggies and spices. Cook with rice.\nNutrients: carb-rich",
        metadata={"name":"Vegetable Pulao","type":"veg","ingredients":["rice","vegetables","spices"],"taste":"aromatic","nutrient":"carb-rich","meal_type":"lunch"},
    ),

    Document(
        page_content="Recipe: Fish Fry\nIngredients: fish, chili powder, turmeric\nTaste: spicy\nProcess: Marinate fish. Fry until crispy.\nNutrients: protein-rich",
        metadata={"name":"Fish Fry","type":"non-veg","ingredients":["fish","chili powder","turmeric"],"taste":"spicy","nutrient":"protein-rich","meal_type":"dinner"},
    ),

    Document(
        page_content="Recipe: Chana Masala\nIngredients: chickpeas, tomato, spices\nTaste: tangy\nProcess: Cook chickpeas in tomato gravy.\nNutrients: protein-rich",
        metadata={"name":"Chana Masala","type":"veg","ingredients":["chickpeas","tomato","spices"],"taste":"tangy","nutrient":"protein-rich","meal_type":"lunch"},
    ),

   

    Document(
        page_content="Recipe: Vegetable Soup\nIngredients: vegetables, pepper\nTaste: light\nProcess: Boil vegetables. Season and simmer.\nNutrients: vitamin-rich",
        metadata={"name":"Vegetable Soup","type":"veg","ingredients":["vegetables","pepper"],"taste":"light","nutrient":"vitamin-rich","meal_type":"starter"},
    ),

    Document(
        page_content="Recipe: Chicken Biryani\nIngredients: chicken, rice, spices\nTaste: spicy\nProcess: Layer rice and chicken. Cook on dum.\nNutrients: protein-rich",
        metadata={"name":"Chicken Biryani","type":"non-veg","ingredients":["chicken","rice","spices"],"taste":"spicy","nutrient":"protein-rich","meal_type":"lunch"},
    ),

    Document(
        page_content="Recipe: Idli\nIngredients: rice batter, urad dal\nTaste: mild\nProcess: Ferment batter. Steam until fluffy.\nNutrients: carb-rich",
        metadata={"name":"Idli","type":"veg","ingredients":["rice batter","urad dal"],"taste":"mild","nutrient":"carb-rich","meal_type":"breakfast"},
    ),

    Document(
        page_content="Recipe: Sambar\nIngredients: lentils, vegetables, tamarind\nTaste: tangy\nProcess: Cook dal with veggies. Add tamarind.\nNutrients: fiber-rich",
        metadata={"name":"Sambar","type":"veg","ingredients":["lentils","vegetables","tamarind"],"taste":"tangy","nutrient":"fiber-rich","meal_type":"lunch"},
    ),

    Document(
        page_content="Recipe: Bread Omelette\nIngredients: bread, eggs, spices\nTaste: savory\nProcess: Dip bread in egg mix. Cook on pan.\nNutrients: protein-rich",
        metadata={"name":"Bread Omelette","type":"non-veg","ingredients":["bread","eggs","spices"],"taste":"savory","nutrient":"protein-rich","meal_type":"snack"},
    ),

    Document(
        page_content="Recipe: Aloo Fry\nIngredients: potato, chili powder\nTaste: spicy\nProcess: Slice potatoes. Fry until crisp.\nNutrients: carb-rich",
        metadata={"name":"Aloo Fry","type":"veg","ingredients":["potato","chili powder"],"taste":"spicy","nutrient":"carb-rich","meal_type":"side"},
    ),

    Document(
        page_content="Recipe: Paneer Tikka\nIngredients: paneer, yogurt, spices\nTaste: smoky\nProcess: Marinate paneer. Grill until charred.\nNutrients: protein-rich",
        metadata={"name":"Paneer Tikka","type":"veg","ingredients":["paneer","yogurt","spices"],"taste":"smoky","nutrient":"protein-rich","meal_type":"starter"},
    ),

    Document(
        page_content="Recipe: Lemon Rice\nIngredients: rice, lemon, peanuts\nTaste: tangy\nProcess: Mix rice with lemon juice. Add seasoning.\nNutrients: carb-rich",
        metadata={"name":"Lemon Rice","type":"veg","ingredients":["rice","lemon","peanuts"],"taste":"tangy","nutrient":"carb-rich","meal_type":"lunch"},
    ),

    Document(
        page_content="Recipe: Curd Rice\nIngredients: rice, curd, mustard seeds\nTaste: mild\nProcess: Mix rice with curd. Add tempering.\nNutrients: probiotic-rich",
        metadata={"name":"Curd Rice","type":"veg","ingredients":["rice","curd","mustard seeds"],"taste":"mild","nutrient":"probiotic-rich","meal_type":"lunch"},
    ),

    Document(
        page_content="Recipe: Egg Curry\nIngredients: eggs, onion, tomato, spices\nTaste: spicy\nProcess: Prepare gravy. Add boiled eggs and simmer.\nNutrients: protein-rich",
        metadata={"name":"Egg Curry","type":"non-veg","ingredients":["eggs","onion","tomato","spices"],"taste":"spicy","nutrient":"protein-rich","meal_type":"dinner"},
    ),

    Document(
        page_content="Recipe: Veg Noodles\nIngredients: noodles, vegetables, soy sauce\nTaste: savory\nProcess: Cook noodles. Stir fry with veggies.\nNutrients: carb-rich",
        metadata={"name":"Veg Noodles","type":"veg","ingredients":["noodles","vegetables","soy sauce"],"taste":"savory","nutrient":"carb-rich","meal_type":"dinner"},
    ),

    Document(
        page_content="Recipe: Chicken Fry\nIngredients: chicken, spices, oil\nTaste: spicy\nProcess: Marinate chicken. Fry until golden.\nNutrients: protein-rich",
        metadata={"name":"Chicken Fry","type":"non-veg","ingredients":["chicken","spices","oil"],"taste":"spicy","nutrient":"protein-rich","meal_type":"dinner"},
    ),

    Document(
        page_content="Recipe: Roti\nIngredients: wheat flour, water\nTaste: neutral\nProcess: Knead dough. Cook on tawa.\nNutrients: fiber-rich",
        metadata={"name":"Roti","type":"veg","ingredients":["wheat flour","water"],"taste":"neutral","nutrient":"fiber-rich","meal_type":"lunch"},
    ),

    Document(
        page_content="Recipe: Vegetable Salad\nIngredients: cucumber, carrot, onion\nTaste: fresh\nProcess: Chop vegetables. Mix and season.\nNutrients: vitamin-rich",
        metadata={"name":"Vegetable Salad","type":"veg","ingredients":["cucumber","carrot","onion"],"taste":"fresh","nutrient":"vitamin-rich","meal_type":"starter"},
    ),

]