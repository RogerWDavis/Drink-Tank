# We Love Whiskey

We Love Whiskey  is a fictional recipe sharing site that allows bartenders and whiskey enthsiasts to join a community and share their best whiskey recioes. It allowy users to browse, like, upload, edit and delete their favorite whiskey recipes. Its simple and easy to use.

## Table of Contents

* User-Experience-Design
 * The-Strategy-Plane
   * Site-Goals
   * Agile Planning
     * Epics
     * User Stories
 * The-Scope-Plane
 * The-Structure-Plane
   * Features
   * Features Left To Implement
 * The-Skeleton-Plane
   * Wireframes
   * Database-Design
   * Security
 * The-Surface-Plane
   * Design
   * Colour-Scheme
   * Typography
   * Imagery
 * Technolgies
 * Testing
 * Deployment
   * Version Control
   * Heroku Deployment
   * Run Locally
   * Fork Project
 * Credits

 ## User Experience Design
 ### The Strategy Plane

 The site is aimed to help whiskey enthusiasts to easily share whiskey recipes on the website, and find recipes that they may never have tried before.

### Agile Planning

This project was developed using agile methodologies by delivering small features in incremental sprints. There were 3 sprints in total, spaced out evenly over four weeks.

All projects were assigned to epics, prioritized under the labels, Must have, should have, could have. They were assigned to sprints and story pointed according to complexity. "Must have" stories were completed first, "should haves" and then finally "could haves". It was done this way to ensure that all core requirements were completed first to give the project a complete feel, with the nice to have features being added should there be capacity.

The Kanban board was created using github projects and can be located here and can be viewed to see more information on the project cards. All stories except the documentation tasks have a full set of acceptance criteria in order to define the functionality that marks that story as complete.

![kanban board](media/kanban.PNG)

#### Epics
The project had 7 main Epics (milestones):

##### EPIC 1 - Base Setup

The base setup epic is for all stories needed for the base set up of the application. Without the base setup, the app would not be possible so it was the first epic to be delivered as all other features depend on the completion of the base setup.

##### EPIC 2 - Site Navigation

The site navigation epic handles functions associated with the user navigation of the site.

##### EPIC 3 - Authentication Epic

The authentication epic is for all stories related to the registration, login and authorization of views. This epic provides critical functionality and value as without it the staff would not be able to managed the bookings securely without regular site visitors also being able to see and perform actions.

##### EPIC 4 - Deployment Epic

This epic is for all stories related to deploying the app to heroku so that the site is live for staff and customer use.

##### EPIC 5 - Documentation

This epic is for all document related stories and tasks that are needed to document the software development lifecycle of the application. It aims to deliver quality documentation, explaining all stages of development and necessary information on running, deploying and using the application.

#### EPIC 1 - Base Setup

As a developer, I need to create the base.html page and structure so that other pages can reuse the layout

As a developer, I need to create static resources so that images, css and javascript work on the website

As a developer, I need to set up the project so that it is ready for implementing the core features

As a developer, I need to create the footer with social media links and contact information


#### EPIC 2 - Site Navigation

As a developer, I need to create the navbar so that users can navigate the website from any device

As a developer, I need to implement links throughout the site

As a user, I would like a home page so that I can view recipes

#### EPIC 3 - Authentication Epic

As a developer, I need to implement allauth so that users can sign up and have access to the websites features

As a user, I want to register an account so that I can use member functionality

As a site owner, I would like the allauth pages customized to that they fit in with the sites styling

#### EPIC 4 - Deployment Epic

As a developer, I need to set up whitenoise so that my static files are served in deployment

As a developer, I need to deploy the project to heroku so that it is live for customers

#### EPIC 5 - Documentation

 Tasks:

* Complete readme documentation
* Complete testing documentation write up

### The Scope Plane

* Responsive Design - Site should be fully functional on all devices from 320px up
* Hamburger menu for mobile devices
* Ability to perform CRUD functionality on Menus and Bookings
* Restricted role based features
* Home page with basic site information

### The Structure Plane

#### Features

User Story: As a **site user** I can **view a paginated list of recipes** so as to **pick which recipe I wish to view**

# Acceptance Criteria
* Recipes clearly displayed on landing page
* Clicking on a recipe opens it on a dedicated page


## Tasks
- [ ] Create view
- [ ] Create template
- [ ] Create model


User Story: As a **site user** I can **browse recipes by whiskey sort** so as to **find recipes with my preferred whiskey**
# Acceptance Criteria
* Dropdown in navbar with whiskey sorts
* Landing pages with whiskey recipes according to sort


## Tasks
- [ ] Create views
- [ ] Create urls
- [ ] Link to homepage


User Story: As a **site admin** I can **create, update and delete recipes** so as to **manage site content**

# Acceptance Criteria
* Site admin user creation
* Site admin functionality


## Tasks
- [ ] Create admin user in Django
- [ ] Create recipes
- [ ] Edit recipes


User Tory: As a **site admin** I can **approve or dissaprove recipes** so as to **filter unwanted or irrelevant content**

# Acceptance Criteria
* Admin can see user generated content
* Admin can decide which content is visable to user

## Tasks
- [ ] First task
- [ ] Second task
- [ ] Third task


User Story: As a **site user** I can **view a recipe list** so as to **select a recipe to view**

# Acceptance Criteria
* Viewer can go from landing page to recipe list page
* Recipes displayed asthetically on page


## Tasks
- [ ] Create view
- [ ] Create url
- [ ] Link to Home Page


User Story: As a **site user** I can **create, update and delete recipes** so as to **interact with community**

# Acceptance Criteria
* User can create recipes
* User can edit recipes
* User can delete recipes

## Tasks
- [ ] Create user profiles
- [ ] Assign functionality


User Story: As a **site user** I can **create an account** so as to **create, update and delete recipes**

# Acceptance Criteria
* User can login and log out
* User can create, update and delete recipes


## Tasks
- [ ] Create user app
- [ ] Create registration form
- [ ] Create "logged in" view with user functionality
- [ ] Create "logged in" url
- [ ] Create "logged in" and "logged out" messages


User Story: As a **site user** I can **open a recipe** so as to **view it in detail**

# Acceptance Criteria
* Clicking a recipe opens a dedicated page
* Details displayed asthetically


## Tasks
- [ ] Create View
- [ ] Create Url


User Story: As a **Site User / Admin** I can **view the number of likes on each post** so as to **see which is the most popular or viral**

# Acceptance Criteria
* Display # of likes

## Tasks
- [ ] Create like button
- [ ] Count likes
- [ ] Display # of likes asthetically


User Story: As a **site user** I can **like and unlike content** so as to **interact with community**

# Acceptance Criteria
* Like and Unlike button displayed
* User can interact with buttons

## Tasks
- [ ] Create Buttons
- [ ] Count Likes/Unlikes
- [ ] Display Likes/Unlikes



### The Skeleton Plane

#### Wireframes

![Wireframe](media/wirepage1.PNG)
![Wireframe](media/wirepage2.PNG)
![Wireframe](media/wirepage4.PNG)
![Wireframe](media/wirepage5.PNG)
![Wireframe](media/wirepage6.PNG)


#### Database-Design

The database was designed to allow CRUD functionality to be available to registered users, when signed in. The user model is at the heart of the application.

![kanban board](media/erd.pgn.PNG)

#### Security

Views were secured by using the django class based view mixin, UserPassesTextMixin. A test function was created to use the mixin and checks were ran to ensure that the user who is trying to access the page is authorized. Any user restricted functionality, user edit/delete functionality listed in the features was secured using this method.

Environment variables were stored in an env.py for local development for security purposes to ensure no secret keys, api keys or sensitive information was added the the repository. In production, these variables were added to the heroku config vars within the project.


#### Technolgies
* HTML
  * The structure of the Website was developed using HTML as the main language.
* CSS
  * The Website was styled using custom CSS in an external file.
* JavaScript
  * JavaScript was used to make the custom slider on the menu page change and the bootstrap date picker.
* Python
  * Python was the main programming language used for the application using the Django Framework.
* Visual Studio Code
  * The website was developed using Visual Studio Code IDE
* GitHub
  * Source code is hosted on GitHub
* Git
  * Used to commit and push code during the development of the Website
* Favicon.io
  * favicon files were created at https://favicon.io/favicon-converter/
* balsamiq
  * wireframes were created using balsamiq from https://balsamiq.com/wireframes/desktop/#
* Python Modules Used

#### Python Modules Used
* Django Class based views (ListView, UpdateView, DeleteView, CreateView) - Used for the classes to create, read, update and delete
* Mixins (LoginRequiredMixin, UserPassesTestMixin) - Used to enforce login required on views and test user is authorized to perform actions
* messages - Used to pass messages to the toasts to display feedback to the user upon actions
* timedelta, date - Date was used in order to search for objects by date and timedelta for searching date ranges


#### External Python Modules

* cloudinary==1.29.0 - Cloundinary was set up for use but no custom uploads were made, settings remain for future development
* crispy-bootstrap5==0.6 - This was used to allow bootstrap5 use with crispy forms
* dj-database-url==0.5.0 - Used to parse database url for production environment
* dj3-cloudinary-storage==0.0.6 - Storage system to work with cloudinary
* Django==4.0.5 - Framework used to build the application
* django-allauth==0.51.0 - Used for the sites authentication system, sign up, sign in, logout, password resets ect.
* django-crispy-forms==1.14.0 - Used to style the forms on render
* gunicorn==20.1.0 - Installed as dependency with another package
* psycopg2==2.9.3 - Needed for heroku deployment
* python3-openid==3.2.0 - Installed as dependency with another package


### Deployment

#### Version Control

The site was created using the Visual Studio Code editor and pushed to github to the remote repository ‘Drink-Tank’.

The following git commands were used throughout development to push code to the remote repo:

git add <file> - This command was used to add the file(s) to the staging area before they are committed.

git commit -m “commit message” - This command was used to commit changes to the local repository queue ready for the final step.

git push - This command was used to push all committed code to the remote repository on github.

Heroku Deployment
The site was deployed to Heroku. The steps to deploy are as follows:

Navigate to heroku and create an account
Click the new button in the top right corner
Select create new app
Enter app name
Select region and click create app
Click the resources tab and search for Heroku Postgres
Select hobby dev and continue
Go to the settings tab and then click reveal config vars
Add the following config vars:
SECRET_KEY: (Your secret key)
DATABASE_URL: (This should already exist with add on of postgres)
EMAIL_HOST_USER: (email address)
EMAIL_HOST_PASS: (email app password)
CLOUNDINARY_URL: (cloudinary api url)
Click the deploy tab
Scroll down to Connect to GitHub and sign in / authorize when prompted
In the search box, find the repositoy you want to deploy and click connect
Scroll down to Manual deploy and choose the main branch
Click deploy
The app should now be deployed.

The live link can be found :[here](https://drink-tank-f365b9a8022a.herokuapp.com/) Live Site

Run Locally
Navigate to the GitHub Repository you want to clone to use locally:

Click on the code drop down button
Click on HTTPS
Copy the repository link to the clipboard
Open your IDE of choice (git must be installed for the next steps)
Type git clone copied-git-url into the IDE terminal
The project will now have been cloned on your local machine for use.