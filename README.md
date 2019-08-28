# The Shadows

[Check it out here!](https://the-shadows.herokuapp.com/)

The Shadows is a we application which was inspired by my love of black and white photographs and images. It is the home of all things black, white and grey. It is a web application where users can view images, sign up, upload there own, like and comment on images. 


## UX

The primary goal of the The Shadows is the provide a web application where users can view, like and comment on greyscale images. As well as uploading there own and contrubting to the online community. 

#### User Goals 
- Allow the user to register and upload photos.
- Have a space where users can view all the greyscale photos and images.
- Have a simple and enjoyable user experience.
- Allow the user to like and comment on content. 

#### Business Goals 
- Showcase a space for photographers and artists to provide work.
- Build brand awareness of The Shadows.
- Encourage site visitors to sign up, increasing engagement.
- Showcase the full stack developers skills.

#### Ideal User

- Loves greyscale photos and images.
- Computer savvy.
- Can read English.
- Is interested in photography.
- Wants somewhere to upload there photos and images.

#### User Stories

- As a user, I want to easily be able to see the images.
- As a user, I want to be able to see images relating to a certain category.
- As a user, I want to be able to upload my own images.
- As a user, I want to be able to like images.
- As a user, I want to be able to comment on images. 
- As a user, I want the site to be clean and easy to navigate.
- As a user, I want to be able to register on the site.
- As a returning user, I want to be able to login to my account.

#### Wireframe mockups

[PC](https://raw.githubusercontent.com/Rorywork/milestone-project-3/master/wireframes/desktop-wireframes.PNG)  
[Tablet](https://raw.githubusercontent.com/Rorywork/milestone-project-3/master/wireframes/tablet-wireframes.PNG)  
[Mobile](https://raw.githubusercontent.com/Rorywork/milestone-project-3/master/wireframes/mobile-wireframes.PNG)

## Features

#### Cross Application

Each page has a reponsive navigation bar which is built with Bootstap, and incorperates the Bootstrap Lux theme. This nav-bar is used to navigate the application. It uses a clean white background with black text in keeping with the themes of the application. When logged in this nav-bar changes to show other links such as the Logout option and the upload photo option.

Each page also has a footer again built with Bootstap. This has a clean layout similar to the heading. It contains some further information as well as the social links for the website. These link out in a new tab to Facebook and Instagram. There is also a link to my Github for anyone who wants to know more abour the creator of The Shadows. 

#### Home

The home page uses the parallax feature on two images to create a smooth scrolling experience down the page for the user. Overlaid on top of this is the text with the name fo the application and a tag line. I use a white div betweeen the two parallaxes to tell the user more about the website and impulsive buttons to encourage them to sign up or log in. These buttons use the Lux theme and follow the theme of the application. 

#### Gallery

The gallery page is the main part of The Shadows. It uses a heading followed by a series of buttons which are used to select what catgeory of image you would like to see. These buttons are responsive and utilise the Bootstrap grid system. The images themeselves are held in MongoDB and are assigned various attributes which allows them to be filtered by category. The images have a greyscale filter ensuring that no coloured images make it onto the site from the users perspective. They have a darkened overlay built using CSS which has the image name and description as well as the uploaders username in the bottom right. 

When logged in as Rorywork (my admin account) the overlay also contains and edit and a delete button allowing me to administer the site and remove any images that violate site policy. I can also make changes where needed. These buttons take the form of icons on a grey background and do not intrude with the design.

Below the images are the comments, when a user is logged in there is also a like button and the ability to add new comments. Again the buttons use the Lux Bootswatch theme in keeping with the style.

At the bottom of the gallery page is the pagination feature, this ensures that only 5 images are displayed at a time, ensuring load times are no too long. The user can then navigate through the pages of images by clicking on the numbered buttons or the arrow keys. 

 #### Register
 The register page uses a form with the following fields:
 - Name
 - Email
 - Username
 - Password
 - Confirm Password
 
 It then has a submit button which will create a new user within MongoDB. Each user is given a unique identifier and attributes depending on what they filled out on the form.

Below this form is a greyscale image in order to improve the aesthetic of the page. This image has been made responsive.

#### Login 
The login page has a simple form containing the username field and a password field. This allows the user to logon, whatever they put will be checked via MongoDB and access will be granted if there is an account that matches what is submitted. 
The form is styled using the Boostwwatch Lux theme and includes a submit button.

Below this is another responsive image in keeping with the convention of the register page. 

If a user puts a username or password that is not recognized then a prompt will appear in red at the top of the page saying either 'Username not found' in case of an incorrect username or 'Invalid Login' if the username is correct but the password is not. 

#### Upload Photo 
The upload photo page uses a jumbotron to explain the purposer of the page. it stands out visually and engages the user. It also contains a further button linking to the gallery page.

Below this is a form which allows the user to uplaod there own images, it has the following fields:
- Contributor - this field is autofilled with the users username, it gets this info from MongoDB.
- Choose File - allows the user to select which file they would like to upload from their server.
- Name - the name the user would like to give the image.
- Description - A short description about the image.
- Category - The user casn select from a list of categories for the image which allows the site to filter what is shown on the gallery page. 

There is then a submit button which will create a new entry within MongoDB.

#### Features to be implemented in future
- Privacy policy, as the website captures user data I will create a policiy in the future.
- GDPR cookie opt in - this will be a pop up on the landing page and the register page so the user can decide what cookies they want. 
- In the future it is planned users will be able to edit there photos, currently on the admin (Rorywork) can do this. 

## Technologies Used
- HTML
- CSS
- Javascript
- Python
- Flask
- [Bootstrap](https://getbootstrap.com/)
- [MongoDB](https://www.mongodb.com/cloud/atlas) - both locally and using Atlas.

## Deployment

### How to run this project locally
You will need:

-   An IDE, I use  [Visual Studio Code](https://code.visualstudio.com/)

The following  must be installed  on your machine:

-   [PIP](https://pip.pypa.io/en/stable/installing/)
-   [Python 3](https://www.python.org/downloads/)
-   [Git](https://gist.github.com/derhuerst/1b15ff4652a867391f03)
-   An account at  [MongoDB Atlas](https://www.mongodb.com/cloud/atlas)  or MongoDB running locally on your machine.
    -   How to set up your Mongo Atlas account  [here](https://docs.atlas.mongodb.com/).

#### Instructions

1.  Save a copy of the github repository located at  [https://github.com/Rorywork/milestone-project-3](https://github.com/Rorywork/milestone-project-3)  by clicking the "download zip" button at the top of the page and extracting the zip file to your chosen folder. If you have Git installed on your system, you can clone the repository with the following command.

```
git clone https://github.com/Rorywork/milestone-project-3

```

2.  If possible open a terminal session in the unzip folder or cd to the correct location.
    
3.  A virtual environment is recommended for the Python interpreter, I'd use Pythons built in virtual environment. Enter the following command:
    

```
python -m .venv venv

```

_NOTE: Your Python command may differ, such as python3 or py_

4.  Activate the .venv with the command:

```
.venv\Scripts\activate 

```

_Again this  **command may differ depending on your operating system**, please check the  [Python Documentation on virtual environments](https://docs.python.org/3/library/venv.html)  for further instructions._

4.  If needed, Upgrade pip locally with

```
pip install --upgrade pip.

```

5.  Install all required modules with the command

```
pip -r requirements.txt.

```

6.  In your local IDE create a file called  `.flaskenv`.
    
7.  Inside the .flaskenv file, create a SECRET_KEY variable and a MONGO_URI to link to your own database. Please make sure to call your database  `myTestDB`, with 2 collections called  `users`  and  `photos`. 
    
8.  You can now run the application with the command
    

```
python app.py

```

9.  You can visit the website at  `http://127.0.0.1:5000`

## Heroku Deployment

To deploy The Shadows to heroku, take the following steps:

1.  Create a  `requirements.txt`  file using the terminal command  `pip freeze > requirements.txt`.
    
2.  Create a  `Procfile`  with the terminal command  `echo web: python app.py > Procfile`.
    
3.  `git add`  and  `git commit`  the new requirements and Procfile and then  `git push`  the project to GitHub.
    
4.  Create a new app on the  [Heroku website](https://dashboard.heroku.com/apps)  by clicking the "New" button in your dashboard. Give it a name and set the region to Europe.
    
5.  From the heroku dashboard of your newly created application, click on "Deploy" > "Deployment method" and select GitHub.
    
6.  Confirm the linking of the heroku app to the correct GitHub repository.
    
7.  In the heroku dashboard for the application, click on "Settings" > "Reveal Config Vars".
    
8.  Set the following config vars:
    
|   Key             |Value                                                
|----------------|-----|
|Debug|`'FALSE'`|
|IP         |`0.0.0.0`|
|MONGO_URI|`mongodb+srv://<username>:<password>@<cluster_name>-qtxun.mongodb.net/<database_name>?retryWrites=true&w=majority`|
|PORT|5000
|SECRET_KEY|<your_secret_key>

-   To get your MONGO_URI read the MongoDB Atlas documentation  [here](https://docs.atlas.mongodb.com/)

8.  In the heroku dashboard, click "Deploy".
    
9.  In the "Manual Deployment" section of this page, made sure the master branch is selected and then click "Deploy Branch".
    
10.  The site is now successfully deployed.  

## Credits

#### Media

-   [Pexels](https://www.pexels.com/)  provided the majority of images on each page.
- Users - users can upload there own images so credit is provided by the username witin the overlay on the photo to whoever uploaded it.

Code

-   [W3 Schools](https://www.w3schools.com/) gave me a starting point for implementing pagination within the spplication. 
-   The HTML code for the favicon was provided by  [Favicon](https://favicon-generator.org/).
- [Traversy](https://www.youtube.com/user/TechGuyWeb) provided a number of tutorials I followed to help me with certain features in my application. 

#### Acknowledgements

-   My tutor Simen Daehlin provided useful links, tips and advice on improving the website.
-   [Check out Simen's Github](https://github.com/Eventyret)

#### Disclaimer

The content of this website is currently for entertainment and educational purposes only, it does not have a commercial function. 
