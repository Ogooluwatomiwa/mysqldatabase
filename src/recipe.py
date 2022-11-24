#!/usr/bin/env python3
import db
import models

# Make these settings match your Makefile
user="recipe"
password="swordfish"
dbname="recipe"
port="3334"


def menu():
    print("Welcome to the recipe tool")
    print("------------------------")
    print()
    print("1: Initialise Database")
    print("2: List recipes")
    print("3: Add recipe")
    print("4: Read recipe")
    print("5: Delete recipe")
    print("0: Quit")
    print()
    return int(input("Choose option: "))

if __name__=="__main__":

    session=db.connect(user,password,port,dbname)
    
    userInput=None

    while userInput!=0:
        userInput=menu()
        print()
        if userInput==1:            
            db.create_db(user,password,port,dbname)

        elif userInput==2:            
            recipe=session.query(models.Recipe).all()
            for recip in recipe:
                print(f"{recip.id}: {recip.title}")
                
        elif userInput==3:
            title=input("Enter new recipe title: ")
            content=input("Enter new recipe content: ")
            newRecipe = models.Recipe(title=title,content=content)
            session.add(newRecipe)    
            session.commit()

        elif userInput==4:
            noteNum=int(input("Enter recipe number: "))
            recipe = session.query(models.Recipe).filter_by(id=noteNum).first()
            if recipe==None:
                print("There is no recipe with that number")
            else:
                print(recipe.title)
                print("-"*len(recipe.title))
                print(recipe.content)

        elif userInput==5:
            noteNum=int(input("Enter note number: "))
            recipe = session.query(models.Recipe).filter_by(id=noteNum)
            if recipe==None:
                print("There is no recipe with that number")
            else:
                recipe.delete()
                session.commit()
        print()