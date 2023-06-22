# by Collins07

## GreenLead

## Table of Content

+ [Description](#description)
+ [Requirements](#requirements)
+ [Installation](#installation)
+ [Running Project](#running-project)
+ [Project Objectives](#project-objectives)
+ [Features](#features)
+ [BDD](#bdd)
+ [Technologies Used](#technologies-used)
+ [Licence](#licence)
+ [Authors Info](#authors-info)

## Description

GreenLead is a web-based platform that fosters on accountable reforestation and restoration activities by groups that carry out tree-planting initiatives. More often than not, the number of trees planted is not the same number of trees that go past early growth because of negligence.The early growth stages of trees is the most crucial stage but we always put tree seedlings into the ground and leave the rest for mother nature to take care of. We have always concentrated on HOW MANY TREES WE PLANT and its now time to shift to HOW MANY OF THOSE TREES, PLANTED, REACH MATURITY.

GreenLead offers a platform to monitor on the activities of groups running out tree-planting programs, be it learning institutions, NGOs, government institutions, factories, companies, social groups etc. All citizens get to visualize the summarized details also on the platform. We don't exclude individuals who also wish to be sole participants towards greening our future. GreenLead also gives individuals an opportunity to plant trees and their efforts be rewarded. Through affiliate marketing, we strive to strike a balance between consumption and production, where we look to market for businesses and a tree is planted for every product that is bought through GreenLead.

Live link to the project
[GreenLead] link to  ademo video on Youtube `https://www.youtube.com/watch?v=y0ZcVxmkSEk`

## Requirements

+ A computer running on either Windows, MacOS or Ubuntu operating system installed with the following:

```-Python version 3.8
    -Django
    -Pip
    -pipenv
```

## Installation

+ Open Terminal {Ctrl+Alt+T} 
+ git clone `https://github.com/Collins07/GreenLead.git`
+ cd GreenLead
+ code . or atom . based on prefered text editor

## Running Project

+ On terminal where you have opened the cloned project
  + `sudo pip3 install pipenv` - To install virtual enviroment
  + `pip install --user pipenv` - To create virtual enviroment
  + `pipenv shell` - To activate virtual enviroment
  + `pipenv install -r requirements.txt` - To install requirements
  + Setup your database User, Password, Host, Port and Database Name in the `.env` file.
  + `python manage.py makemigrations` - To create migrations
  + `python manage.py migrate` - To migrate database  
  + `python manage.py runserver` - to start the server



+ (will be included when App is deployed)

## Project Objectives

+ GreenLead main objective is ACCOUNTABILITY for SUSTAINABILITY.
+ Hold tree-planting groups accountable in their tree-planting initiatives by doing follow ups.
+ Give farmers a platform where they can post and connect with their colleagues and supporters.
+ Educate farmers by giving them a platform to see events and seminars available that they can attend to learn on agroforestry, regenerative agriculture etc.
+ Give a chance to individuals who wish to participate in tree planting activities to do so through GreenLead and get a certificate for their effort.
+ Create partnerships with organizatiions, NGOs, learning instituitions, businesses and various industries so as to get all involved actively or proactively.
+ Act as an affiliate for businesses to raise funds that will be directed towards increasing our green spaces
+ Provide users with updated data of the progress of tree planting groups we have in the country and have registered with us.


## Features

+ Users can register and get login confirmation links through their emails (check your spam folder if the email doesn't show up in your inbox).
+ Random users can view other pages without creating an account but CANNOT post until they create an account.
+ Users can post seedlings they sell.
+ Users can comment on other users posts.
+ Users can follow and unfollow other users.
+ Users can view other users' profiles and their posts.
+ Users can update their profiles for easier contacting by interested parties.
+ Users search for various groups involved in tree planting initiatives under the `summary dashboard `
+ Users can visualize summarized on charts
+ Users can actively participate in tree planting activities and get certificates for their effort.
+ Users can purchase items from Jiji, Kilimall, Jumia through GreenLead `Business Corner`.


## BDD

+ Landing page with various descriptions on our objective. A navigation bar as well with home, login and register routes.
+ Create an account with a unique username,an email and password.
+ User can also create and update their profile.
+ Profile view displays users posts, click on the username to view more details of the user and get access to contact details.



## Technologies Used

+ Django 4
+ Bootstrap 5
+ Javascript
+ Google Maps
+ Postgres

## Licence

MIT License

Copyright (c) [2022] [Collins07]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

## Authors Info

LinkedIn - [https://www.linkedin.com/in/collins-abaya-549237233/]


