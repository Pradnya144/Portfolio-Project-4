The CLean Eater is a recipe sharing and meal planning app built using the Django Framework in python.

The app provides a platform for the users to browse through multiple available recipes, share their own recipes and create a meal plan for the week; encouraging users to eat healthy home cooked meals without the stress of having to plan daily.

Here is a link to the live project [The CLean Eater]()

![Mockup]()

## Table of Contents

* [User Experience (UX)](#User-Experience-(UX))  
  * [User Stories](#User-Stories)  
* [Design](#Design)  
  * [Colour Scheme](#Colour-Scheme)  
  * [Imagery](#Imagery)  
  * [Wireframes](#Wireframes)  
  * [Database Schema](#Database-Schema)  
* [Features](#Features)  
  * [Home page](#Home-Page)  
  * [Account page](#Account-page)  
  * [Recipes page](#Recipes-page)  
  * [Recipe detail page](#Recipe-detail-page)  
  * [Add Recipe Form](#add-recipe-form)  
  * [Update Recipe Form](#update-recipe-form)  
  * [Delete Recipe](#delete-recipe)  
  * [My Meal Plan](#my-meal-plan)  
  * [My Recipes Page](#my-recipes-page)  
  * [My Bookmarks Page](#my-bookmarks-page)  
  * [Error Pages](#error-pages)  
* [Technologies](#Technologies)  
  * [Languages used](#Languages-used)  
  * [Libraries and Programs](#Libraries-and-Programs)  
* [Testing](#Testing)  
* [Deployment](#Deployment)  
  * [Github pages](#Github-pages)  
  * [Django and Heroku](#Django-and-Heroku)  
  * [Forking](#Forking)  
  * [Clone](#Clone)  
* [Credits and Acknowledgements](#Credits-and-Acknowledgements)  

## User Experience (UX)  

A visitor to Clean Eater would be someone who likes to share and lookup new recipes. Also someone who wants to eat home cooked meals and likes to plan their week ahead of time.  

### User Stories  

#### EPIC | Navigation  
- As a User I can immediately understand the website's purpose so that I know if it's what I'm looking for.
- As a User I can navigate around the site so that I can easily view desired content.  
- As a User I can view a list of recipes so that I can choose one to read.  
- As a User I can click on a recipe so that I can read the recipe details.  
- As a User I can search recipes so that I can find specific recipes I'm looking for.  

#### EPIC | User Account  
- As a User I can register for an account so that I can begin to use the services afforded to members.  
- As a User I can log in/out so that I can like recipes, comment on recipes and manage my recipes.  
- As a User I can see my login status so that I know if I'm logged in or out.  

#### EPIC | Manage Recipes  
- As a User, I can input my favourite recipes onto the app through an easy to use interface so that I can share them with other users.  
- As a User, I can edit and delete recipes that I have created so that I can easily make changes without having to start over.  
- As a User I can view my recipes so that I can see and manage all recipes I have created in the one location.  
- As a User I can view my bookmarked recipes so I can find them easily in the one location.  

#### EPIC | Manage Meal Plan    
- As a User, I can add/delete recipes to my meal planner for a particular day of the week so that I can create a meal plan for the week ahead.  
- As a User, I can view my meal plan for the week when I log into my account so that I can plan for the week ahead.  

#### EPIC | Admin  
- As a Site Administrator, I can create, read, update and delete recipes, comments and meal plan items so that I can manage the app content.  

## Design  

### Colour Scheme  

I wanted to keep the colour scheme friendly and inviting hence I choose the colour scheme around yellow and earthy tones.  
Contrast between background and foreground colours is implemented to maintain clear visibility.  

![Colour Palette]()  

### Imagery  

All of the current imagery on the website has been taken from Pelex.  
The home page displays a family that's cooking together to portray the idea that cooking too can be fun.  
Images of the dish will be unloaded by individual website users when they upload a new recipe they would like to share.  

### Wireframes  

### Database Schema  

I used principles of Object-Oriented Programming throughout this project and Django’s Class-Based Generic Views.  
Django AllAuth was used for the user authentication system.  
In order for the users to create recipes a custom recipe model was required. The recipe author is a foreign key to the User model given a recipe can only have one author.  
The Comment model allows users to comment on individual recipes and the Recipe is a foreign key in the comment model given a comment can only be linked to one recipe.  
The meal plan item model allows users to add recipes to a meal plan for a particular day. A meal plan item can only have one user and one recipe and is therefore linked to the User and Recipe models through foreign keys.  

![Database Schema]()  

