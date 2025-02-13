# Site Title

(Developers: Anish Fatima, Mitali Chavan, Adam Campbell, Isaac Nicholls )

![am i responive]![Am i reponsive]()


## Live website

Link to live website:[]()

## Overview

### Purpose
For contractors, out site offers a user-friendly interface to create comprehensive profiles, including their qualifications, work experience, and areas of expertise. They can also manage their availability by updating their calendar, making it easier for clients to find and book them for projects. Clients, on the other hand, benefit from advanced search functionalities that allow them to filter contractors based on their specific needs. Once they find a suitable match, clients can view detailed profiles, read reviews, and contact contractors directly through the platform to discuss project details and requirements. This streamlined approach ensures that both clients and contractors can connect efficiently, leading to successful project completions.

### Target Audience
The target audience is : 
Tradespeople/Contractors: Skilled professionals such as electricians, plumbers, and builders looking to create profiles, showcase their skills, and manage their availability to attract clients.
Clients: Homeowners, property managers, and business owners searching for qualified contractors based on skills, location, and availability to complete their projects efficiently.

## User Stories

### Must-Have User Stories:

1. ##### Customer Registration 



##### Acceptance Criteria

##### Tasks


2. ##### Login/Log-out

 As a Customer I can **Login and Log-out of the site and see my login status** so that I can **access my personal information and order history and know what account is using the site**

##### Acceptance Criteria
The Login/Logout screen is in place.
There is a statement in the header that shows weather a user is logged in and if so which user.
##### Tasks
Create/alter the form for the Login/Logout in forms.py
Create Login/Logout html

3. ##### Navbar 

As a customer I can **use a navbar** so that I can **easily navigate between all pages/features of the site**

##### Acceptance Criteria
A navbar is in place on all relevant pages
The navbar is responsive to different screen-sizes
##### Tasks
Code navbar in base.html
add bootstrap or other responsiveness using a burger icon etc

4. ##### Home Page

As a customer I can **see a clean easy to navigate homepage when I load the sites URL** so that I can **easily take in and move between the sites features leading to a fun shopping experience**

##### Acceptance Criteria
The homepage loads and looks good
-The eye is drawn in a logical fashion around the home page
##### Tasks
Home page HTML in place
Home page Styling via CSS in place
Possibility of some Javascript for modals or Hero-image interactivity/ movement

5. ##### Product range/Product Pagination

As a customer I can **click a product range icon to see a list of all products in the range and likewise click a product to see a products features** so that I can **easily navigate the stores inventory and take in the details of any product I am interested in**

##### Acceptance Criteria
I can see Paginated Cards for product ranges on the Home page
These lead to a product Range page with a paginated list of products that in turn lead to a product features page for each product
##### Tasks
Create Suitable product range html templates and views
Create Suitable product information templates and views
Style the range and product information pages with CSS
Have a product model in models.py that has all fields needed for the product

6. ##### Admin Manage Products

As an admin **I want to be able to add, update or delete products** so that I can **manage the product catalog**

##### Acceptance Criteria
The admin should be able to add new products with name, description, price, images, and category.
The admin should be able to update product details (e.g., price, description).
The admin should be able to remove products from the catalog.
The admin should be able to view a list of all products
##### Tasks
Create a product management page for admins
Implement form to add new products
Implement functionality to update product details.
Implement functionality to delete products from the catalog.

7. ##### 



##### Acceptance Criteria
Product cart visible to customer and has link
Customer can add items to cart on click
##### Tasks
Product Cart has separate page/modal with relevant form/html
Add to Cart button is implemented as part of product detail html
Relevant views and urls updated

### Should-Have User Stories

1. ##### 



##### Acceptance Criteria

##### Tasks


2. ##### 


##### Acceptance Criteria

##### Tasks


3. ##### About Page



##### Acceptance Criteria

##### Tasks


### Could-Have User Stories

1. ##### 



##### Acceptance Criteria

##### Tasks


2. #####


##### Acceptance Criteria

##### Tasks


3. ##### 


##### Acceptance Criteria

##### Tasks



## Design Decisions

### Wireframes

Here are the basic wire-frames we used to establish the design for the site:

![wireframes](wireframe.png)

- Wireframe text

### Colors and Font 

## AI Tools Usage

### Chat-GPT

- Ways we have used ai

- more ways we have used AI

## Features Implementation

### Core Features (Must-Haves)

### Logo and navigation bar

A responsive navigation bar is in place. Concentrating on 'mobile first' design, the navigation bar incorporates a clickable burger icon with a drop down menu on mobile. There is a burger icon at tablet size too, but when moving to monitor size the burger disappears and a navigation bar appears with options to navigate to pages; 'Home', 'About' or 'Create' and depending on the user login status also a 'Register' and 'Login' link or a 'Logout'. The nav bar also displays the user login status with the message 'You are not logged in' or 'You are logged in as XXXXX'. In the top left corner there is a clickable project logo that also acts as a 'Home' button. See wireframes and other screenshots to view these features or log in to the project.

### Clear indication as to whether the user is logged in or out at all times

As mentioned above the nav bar displays user login status with the message 'You are not logged in' or 'You are logged in as XXXXX'

### Pagination

This feature forms the list of 2x2 or 3x2 product ranges or products and generates the next and previous buttons dependent on the users position in the content.


### Sign in form

This form has a Django allauth template which has been modified to inherit from our base to take on the sites main styling.

### Register form (Sign up)

This form has a Django allauth template which has been modified to inherit from our base to take on the sites main styling.

### Sign out page

This form has a Django allauth template which has been modified to inherit from our base to take on the sites main styling.

### Home Page


### Page



###  Page



### Advanced Features (Should-Haves)

### Django alert messages

Every time there is a change in data the user is alerted. For example when a review is created, or edited and the same for comments. Also there is a notification when the user logs in or out to confirm their action. These appear in the blank space in the middle of the navigation bar to be in the users eyeline when possible.


### Optional Features (Could-Haves)

### 




## Testing and Validation

### Testing Results

We used our team to manually test all views and forms in order to determin that our functionality was complete and without error

### Validation

All code has been validated through:
- **HTML**: [W3C Markup Validator]().
  
  
- **CSS**: [W3C CSS Validator]().

- **Python** 

## Technology used

### Languages Used

- Languages used
- HTML5

- CSS

- JavaScript

- Python
   - asgiref==3.8.1
   - cloudinary==1.41.0
   - dj-database-url==0.5.0
   - gunicorn==20.1.0
   - oauthlib==3.2.2
   - psycopg==3.2.1
   - PyJWT==2.9.0
   - python3-openid==3.2.0
   - requests-oauthlib==2.0.0
   - sqlparse==0.5.1
   - urllib3==1.26.19
   - whitenoise==5.3.0

- Django

   - summernote==0.8.20.0
   - allauth==0.57.2
   - crispy-forms==2.3


### Database

- [PostgreSQL from Code Institute](https://dbs.ci-dbs.net/ "link to postgresql from code institute") was used as the PostgreSQL database for this project

### Technologies and tools
### Frameworks, Libraries & Programs Used

1. [Bootstrap 4.4.1:](https://getbootstrap.com/docs/4.4/getting-started/introduction/)
   - Bootstrap was used to assist with the responsiveness and styling of the website.
2. [Google Fonts:](https://fonts.google.com/specimen/Libre+Baskerville?selection.family=Monoton|Orbitron:wght@400..900|VT323&query=libre+bas)
3. [Font Awesome:](https://fontawesome.com/)
   - Font Awesome was used on all pages throughout the website to add icons for aesthetic and UX purposes.
4. [jQuery:](https://jquery.com/)
   - jQuery came with Bootstrap to make the navbar responsive but was also used for the smooth scroll function in JavaScript.
5. [Contrast Finder](https://app.contrast-finder.org/?lang=en)
        - Contrast Finder was used to check the contrast between text colour and background image
6. [Tiny.PNG](https://tinypng.com/)
        - Tiny.PNG was used to compress images
7. [W3 Schools](https://www.w3schools.com/)
        - used to look up syntax for HTML and CSS
8. [Co-Pilot] (https://copilot.microsoft.com/)
   - Used extensively for help with coide, script and de bugging processes. An invaluable tool.  
9. [Balsamiq:](https://balsamiq.com/)
   - Balsamiq was used to create the wireframes during the design process.
10. [Git](https://git-scm.com/)
        - Git was used for version control
11. [GitHub:](https://github.com/IsaacNicholls1/vin-rouge)
   - GitHub is used to store the projects code after being pushed from Git.
12. [W3 Jigsaw](https://jigsaw.w3.org/css-validator/)
        - used to validate the CSS
13. [JSHint](https://jshint.com/)
        - used to validate the JavaScript
14. [W3C HTML validator](https://validator.w3.org/)
        - used to validate the HTML
15. [Python Enhancement Proposals](https://peps.python.org/pep-0008/)
        - for advice on PEP8 compliance
16. [Django framework](https://www.djangoproject.com/)
17. [Heroku](https://dashboard.heroku.com/apps) - for deployment. 

### GitHub Copilot
Brief reflection on the effectiveness of using AI tools for debugging and validation.  

**Guidance:** Reflect on how GitHub Copilot assisted with debugging and validation, particularly any issues it helped resolve.

# Deployment #

The site was deployed to Heroku. The steps to deploy are as follows:
 - Install the gunicorn python package and create a file called 'Procfile' in the repo's root directory
 - In the Procfile write 'web: gunicorn vin-rouge.wsgi'
 - In settings.py add ".herokuapp.com" to the ALLOWED_HOSTS list
 - In settings.py add 'https://*.herokuapp.com' to CSRF_TRUSTED_ORIGINS list, git add, commit and push to github

Navigate to the Heroku dashboard
 - Create a new Heroku app
 - Give it a name and select the region 'Europe'
 - Navigate to settings tab and scroll down to Config Vars
 - Click 'Reveal Config Vars'
 - Add the following keys:
         key = DATABASE_URL | value = (my secret database url)
         key = SECRET_KEY | value = (my secret key)
Navigate to Deploy tab
 - Connect to GitHub and select the repo 'vin-rouge'
 - Scroll down to 'Manual deploy' and select the 'main' branch
 - Click 'Deploy Branch'

Security Measures:
Sensitive data is stored in environment variables.
DEBUG mode is disabled in the production environment to enhance security.

### Clone this repository:

- Go to the GitHub repository
- Click the Code button near the top of the page
- Select 'HTTPS', 'SSH', or 'Github CLI', depending on how you would like to clone
- Click the copy button to copy the URL to your clipboard
- Open Git Bash
- Change the current working directory to where you want the cloned directory
- Type git clone and paste the URL ($ git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY)
- Press enter to create your clone locally

Note: The difference between clone and fork is, you need permissions to push back to the original from a clone, but not a fork because a fork will be completely your own new project.

## Reflection on Development Process

### Challenges

- Most challenging aspects

# Future features #

- 

### Acknowledgements

- 