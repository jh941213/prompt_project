from flask import Flask, render_template, request, redirect, url_for , jsonify
import recipe
import image 
import os

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    menu_image_url = None  

    if request.method == 'POST':
        ingredients = request.form.get('ingredients').split(',')
        
        recipe_answer = recipe.get_recipe(ingredients)
        menu, detailed_recipe = recipe.extract_recipe_and_menu(recipe_answer)
        
      
        if menu:
            menu_image_url = image.fetch_image_url(menu)

        return render_template('index.html', menu=menu, detailed_recipe=detailed_recipe, menu_image_url=menu_image_url)

    return render_template('index.html', menu=None, detailed_recipe=None, menu_image_url=None)

@app.route('/chatbot', methods=['GET', 'POST'])
def chatbot():
    if request.method == 'POST':
        user_message = request.form.get('message')
        
      
        response = "You said: " + user_message
        
        return render_template('chatbot.html', response=response)
    
    return render_template('chatbot.html', response=None)

@app.route('/get_response', methods=['POST'])
def get_response():
    data = request.get_json()  
    user_message = data.get('message', '')  #


    bot_response = f"You said: {user_message}"

    return jsonify({'response': bot_response}) 

@app.route('/')
def chatbot_page():
    return render_template('chatbot.html')

if __name__ == '__main__':
    app.run(debug=True)
