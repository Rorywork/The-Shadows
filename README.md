# The Shadows

The Shadows is a web application that was inspired by my love of black and white photographs and images. It is the home of all things black, white and grey. It is a web application where users can view images, sign up, upload there own, like and comment on images. 

[Check it out here!](https://the-shadows.herokuapp.com/)

## UX

The primary goal of The Shadows is the provide a web application where users can view, like and comment on greyscale images. As well as uploading their images, and contributing to the online community. 

#### User Goals 
- Allow the user to register and upload photos.
- Create a space where users can view all the greyscale photos and images.
- Have a simple and enjoyable user experience.
- Allow the user to like and comment on content. 

#### Business Goals 
- Showcase a space for photographers and artists to provide work.
- Build brand awareness of The Shadows.
- Encourage site visitors to sign up, increasing engagement.
- Showcase the full stack developer's skills.

#### Ideal User

- Loves greyscale photos and images.
- Computer savvy.
- Can read English.
- Is interested in photography.
- Wants somewhere to upload there photos and images.

#### User Stories

- As a user, I want to easily be able to see the images.
- As a user, I want to be able to see images relating to a certain category.
- As a user, I want to be able to upload my images.
- As a user, I want to be able to like images.
- As a user, I want to be able to comment on images. 
- As a user, I want the site to be clean and easy to navigate.
- As a user, I want to be able to register on the site.
- As a returning user, I want to be able to login to my account.

#### Wireframe mockups

[PC]()  
[Tablet]()  
[Mobile]()

## Features

#### Cross Application

Each page has a responsive navigation bar that is built with Bootstrap and incorporates the Bootstrap Lux theme. This nav-bar is used to navigate the application. It uses a clean white background with black text in keeping with the themes of the application. When logged in this nav-bar changes to show other links such as the Logout option and the upload photo option.

Each page also has a footer again built with Bootstrap. This has a clean layout similar to the heading. It contains some further information as well as the social links for the website. These link out in a new tab to Facebook and Instagram. There is also a link to my Github for anyone who wants to know more about the creator of The Shadows. 

#### Home

The home page uses the parallax feature on two images to create a smooth scrolling experience down the page for the user. Overlaid on top of this is the text with the name fo the application and a tag line. I use a white div between the two parallaxes to tell the user more about the website and impulsive buttons to encourage them to sign up or log in. These buttons use the Lux theme and follow the theme of the application. 

#### Gallery

The gallery page is the main part of The Shadows. It uses a heading followed by a series of buttons that are used to select what category of the image you would like to see. These buttons are responsive and utilize the Bootstrap grid system. The images themselves are held in MongoDB and are assigned various attributes which allows them to be filtered by category. The images have a greyscale filter ensuring that no colored images make it onto the site from the user's perspective. They have a darkened overlay built using CSS which has the image name and description as well as the uploader's username in the bottom right. 

When logged in as Rorywork (my admin account) the overlay also contains an edit and a delete button allowing me to administer the site and remove any images that violate site policy. I can also make changes where needed. These buttons take the form of icons on a grey background and do not intrude with the design.

Below the images are the comments when a user is logged in there is also a like button and the ability to add new comments. Again the buttons use the Lux Bootswatch theme in keeping with the style.

At the bottom of the gallery page is the pagination feature, this ensures that only 5 images are displayed at a time, ensuring load times are no too long. The user can then navigate through the pages of images by clicking on the numbered buttons or the arrow keys. 

 #### Register
 The register page uses a form with the following fields:
 - Name
 - Email
 - Username
 - Password
 - Confirm Password
 
 It then has a submit button which will create a new user within MongoDB. Each user is given a unique identifier and attributes depending on what they filled out on the form.

Below this form is a greyscale image to improve the aesthetic of the page. This image has been made responsive.

#### Login 
The login page has a simple form containing the username field and a password field. This allows the user to logon, whatever they put will be checked via MongoDB and access will be granted if there is an account that matches what is submitted. 
The form is styled using the Boostwwatch Lux theme and includes a submit button.

Below this is another responsive image in keeping with the convention of the register page. 

If a user puts a username or password that is not recognized then a prompt will appear in red at the top of the page saying either 'Username not found' in case of an incorrect username or 'Invalid Login' if the username is correct but the password is not. 

#### Upload Photo 
The upload photo page uses a jumbotron to explain the purposer of the page. it stands out visually and engages the user. It also contains a further button linking to the gallery page.

Below this is a form which allows the user to upload there own images, it has the following fields:
- Contributor - this field is auto-filled with the user's username, it gets this info from MongoDB.
- Choose File - allows the user to select which file they would like to upload from their server.
- Name - the name the user would like to give the image.
- Description - A short description of the image.
- Category - The user can select from a list of categories for the image which allows the site to filter what is shown on the gallery page. 

There is then a submit button which will create a new entry within MongoDB.

#### Create/Read/Update/Delete (CRUD)
Users can upload there own photos when they have an account, they also can edit or delete photos which they have uploaded. This is done using the buttons on the overlay, these will only be seen on photos the user has uploaded. 

All the images can be seen by any user regardless of whether they are logged in to the site.

Rorywork is the superuser, that account (mine) can edit or delete any image on the site so that I can ensure the site works properly and people don't upload inappropriate images or content. 

#### Javascript
The site originally used a JS folder with js file, however I ended up having to embed the Javascript on the showphotos.html page in order to make the application work. In the next
version I would like to have a seperate Javascript file however I have not managed to find a solution to the problem yet, it is proposed that I will solve this problem in version 2. For now though the application works and is fully functional. 

#### Features to be implemented in future
- Privacy policy, as the website captures user data I will create a policy in the future.
- GDPR cookie opt-in - this will be a pop up on the landing page and the register page so the user can decide what cookies they want. 
- In the future it is planned users will be able to edit their photos, currently on the admin (Rorywork) can do this. 

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

1.  Save a copy of the Github repository located at  [https://github.com/Rorywork/The-Shadows](https://github.com/Rorywork/The-Shadows)  by clicking the "download zip" button at the top of the page and extracting the zip file to your chosen folder. If you have Git installed on your system, you can clone the repository with the following command.

```
git clone https://github.com/Rorywork/The-Shadows

```

2.  If possible open a terminal session in the unzip folder or cd to the correct location.
    
3.  A virtual environment is recommended for the Python interpreter, I'd use Python's built-in virtual environment. Enter the following command:
    

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
    
7.  Inside the .flaskenv file, create a SECRET_KEY variable and a MONGO_URI to link to your database. Please make sure to call your database  `myTestDB`, with 2 collections called  `users`  and  `photos`. 
    
8.  You can now run the application with the command
    

```
python app.py

```

9.  You can visit the website at  `http://127.0.0.1:5000`

## Heroku Deployment

To deploy The Shadows to Heroku, take the following steps:

1.  Create a  `requirements.txt`  file using the terminal command  `pip freeze > requirements.txt`.
    
2.  Create a  `Procfile`  with the terminal command  `echo web: python app.py > Procfile`.
    
3.  `git add`  and  `git commit`  the new requirements and Procfile and then  `git push`  the project to GitHub.
    
4.  Create a new app on the  [Heroku website](https://dashboard.heroku.com/apps)  by clicking the "New" button on your dashboard. Give it a name and set the region to Europe.
    
5.  From the Heroku dashboard of your newly created application, click on "Deploy" > "Deployment method" and select GitHub.
    
6.  Confirm the linking of the Heroku app to the correct GitHub repository.
    
7.  In the Heroku dashboard for the application, click on "Settings" > "Reveal Config Vars".
    
8.  Set the following config vars:
    
|   Key             |Value                                                
|----------------|-----|
|Debug|`'FALSE'`|
|IP         |`0.0.0.0`|
|MONGO_URI|`mongodb+srv://<username>:<password>@<cluster_name>-qtxun.mongodb.net/<database_name>?retryWrites=true&w=majority`|
|PORT|5000
|SECRET_KEY|<your_secret_key>

-   To get your MONGO_URI read the MongoDB Atlas documentation  [here](https://docs.atlas.mongodb.com/)

8.  In the Heroku dashboard, click "Deploy".
    
9.  In the "Manual Deployment" section of this page, making sure the master branch is selected and then click "Deploy Branch".
    
10.  The site is now successfully deployed.  


## Testing

#### W3
I used automated testing with the W3 HTML checker. This displays any syntax errors within the HTML code. I used it on each page on the site to try and ensure there were no errors.

One of the challenges I encountered was that due to the use of Flask, parts of the code which were not in HTML were picked up by the validator as errors when in fact they were necessary for the application to run.

I also ran the CSS code through the W3 validator to remove unnecessary bugs or errors. 

#### Audits / Chrome Dev Tools

I used Chrome Dev Tools to run audits on the performance, accessibility and best practices on the website for both mobile and desktop layouts. I then took on board the feedback and made changes to my website where necessary to achieve higher scores. 

#### Manual Testing

I have tested each page on the following browsers:

-   Google Chrome
-   Apple Safari
-   Microsoft Edge
-   Internet Explorer - I found with Internet Explorer parts of my application do not work and has a lot of bugs, It is proposed that in version 2 I will try to build a version that is more compatible with Internet Explorer. However, as Internet Explorer is being phased out by more modern operating systems I am okay with it not being IE compatible for now.

#### Devices Tested

-   iPhone X
-   iPhone 8
-   Microsoft Surface Book Pro
-   Samsung Tablet
-   Ultra Large Samsung Display
-   iPad Pro
-   iPad

#### Debugging
During my user tests and having other users test the application, there were a lot of different examples where I had to debug, including:

- When a user was already registered in the site the registration function did not pick up that they were already registered meaning a user could create multiple duplicate accounts. To fix this bug the code in the app.py file now has a check that the username does not already exist.
- If the user refreshed the browser after uploading a photo the photo would be reuploaded, to fix this bug I changed the redirect function in app.py so that it now has a hard redirect to the main showphotos.html page which eliminated that bug.
- A bug in the CSS was causing the screen on home.html to have white space on the far right-hand side, I fixed this by introducing the width: 100% attribute to the body.
- At one point the image overlay in the gallery was overlaying onto the comment section as opposed to just the image. To fix this bug I relaid out the image and comment section and made the HTML code more concise, the overlay now only goes over the image.
- To improve load times I changed the CDN's in layout.html to all link from the same site [CDNJS](https://cdnjs.com/), this improved load speeds and readability of the code.
- Originally the homepage did not work properly on mobile, in particular, the Iphone's due to the Safari browser. To combat this I used a media query which ensures that the parallax is only used on larger screen sizes. I also changed the img-overlay class on larger screens with a media query so I could make it look better on mobile. 
- The site was originally using Materialize to style the navbars and other features, after running into numerous bugs where Materialize did not work properly with Javascript I opted to use Bootstrap as it seems a lot more reliable and usable for the application. 

## Credits

#### Media

-   [Pexels](https://www.pexels.com/)  provided the majority of images on each page.
- Users - users can upload there own images so credit is provided by the username within the overlay on the photo to whoever uploaded it.

Code

-   [W3 Schools](https://www.w3schools.com/) gave me a starting point for implementing pagination within the application. 
-   The HTML code for the favicon was provided by  [Favicon](https://favicon-generator.org/).
- [Traversy](https://www.youtube.com/user/TechGuyWeb) provided several tutorials I followed to help me with certain features in my application. 

#### Acknowledgements

-   My tutor Simen Daehlin provided useful links, tips, and advice on improving the website.
-   [Check out Simen's Github](https://github.com/Eventyret)

#### Disclaimer

The content of this website is currently for entertainment and educational purposes only, it does not have a commercial function. Users who upload images are responsible for the content of those images and ensuring they do not breach copyright laws. 