# Site Title

(Developers: Anish Fatima, Mitali Chavan, Adam Campbell, Isaac Nicholls )

![Am I Responsive](/assets/images-readme/responsivehack.png)


## Live website

Link to live website:(https://contract-connect-0afa001eb2c1.herokuapp.com/)

## Overview

### Purpose
For contractors, our site offers a user-friendly interface to create comprehensive profiles, including their qualifications, work experience, and areas of expertise. They can also manage their availability by updating their calendar, making it easier for clients to find and book them for projects. Clients, on the other hand, benefit from advanced search functionalities that allow them to filter contractors based on their specific needs. Once they find a suitable match, clients can view detailed profiles, read reviews, and contact contractors directly through the platform to discuss project details and requirements. This streamlined approach ensures that both clients and contractors can connect efficiently, leading to successful project completions.

### Target Audience
The target audience is : 
Tradespeople/Contractors: Skilled professionals such as electricians, plumbers, and builders looking to create profiles, showcase their skills, and manage their availability to attract clients.
Clients: Homeowners, property managers, and business owners searching for qualified contractors based on skills, location, and availability to complete their projects efficiently.

Link to Project Board:(https://github.com/users/AnishAzharudeen/projects/14/views/1)

## User Stories

1. ## Customer Registration 
- As a contractor, I want to register on the site so that I can create a profile and be discovered by clients.
##### Acceptance Criteria
- A contractor can fill out a registration form with required fields (e.g., name, email, password).
- Upon successful registration, the contractor receives a confirmation email.
- The contractor is redirected to the login page after registration.
##### Tasks
- Create a registration form for contractors.
- Implement backend logic to save contractor details in the database.
- Redirect the contractor to the login page upon successful registration.

2. ## Login/Log-out
- As a contractor, I want to log in using my registered email and password so that I can access and update my profile.
##### Acceptance Criteria
- A contractor can log in using their registered email and password.
- The contractor is redirected to their profile page upon successful login.
##### Tasks
- Create a login form for contractors.
- Implement authentication logic.
- Redirect the contractor to their profile page upon successful login.

3. ## Enter Availability Dates 
- As a contractor, I want to enter and save the dates I am available for work so that clients can see when I am free to work.
##### Acceptance Criteria
- A contractor can enter and save the dates they are available for work.
- The availability dates are displayed on the contractor's profile.
##### Tasks
- Add a calendar input field for contractors to enter availability dates.
- Save the entered dates in the database.
- Display the availability dates on the contractor's profile page.

4. ## Update Contractor Profile
- As a contractor, I want to update my profile information (e.g., skills, experience, contact details) so that clients have the most current details about my skills and availability.
##### Acceptance Criteria
- A contractor can update their profile information.
- The updated information is saved and displayed on the contractor's profile.
##### Tasks
- Create an editable profile form for contractors.
- Implement backend logic to save the updated profile information.
- Display the updated information on the contractor's profile page.

5. ## Client Registration
- As a client, I want to register on the site so that I can search for contractors.
##### Acceptance Criteria
- A client can fill out a registration form with required fields (e.g., name, email, password).
- Upon successful registration, the client receives a confirmation email.
- The client is redirected to the login page after registration.
##### Tasks
- Create a registration form for clients.
- Implement backend logic to save client details in the database.
- Redirect the client to the login page upon successful registration.

6. ## Client Login
- As a client, I want to log in using my registered email and password so that I can access the search and contractor details pages.
##### Acceptance Criteria
- A client can log in using their registered email and password.
- The client is redirected to the search page upon successful login
##### Tasks
- Create a login form for clients.
- Implement authentication logic.
- Redirect the client to the search page upon successful login.

7. ## Search for Contractors
- As a client, I want to search for contractors based on specific criteria (e.g., location, availability) so that I can find the right contractor for my project.
##### Acceptance Criteria
- A client can search for contractors based on specific criteria.
- The search results display a list of contractors that match the criteria.
##### Tasks
- Create a search form with filters for location and availability.
- Implement backend logic to query the database based on search criteria.
- Display the search results as a list of contractors.

8. ## View Contractor Profile
- As a client, I want to view a contractor's profile page with detailed information and contact details so that I can see their details and contact information.
##### Acceptance Criteria
- A client can view a contractor's profile page with detailed information and contact details.
- The profile page displays the contractor's availability, skills, and reviews.
##### Tasks
- Create a profile page template for contractors.
- Populate the profile page with contractor details from the database.
- Display the contractor's availability, skills, and reviews on the profile page.

9. ## Leave Review for Contractor
- As a client, I want to leave a review for a contractor I have worked with so that other clients can benefit from my experience.
##### Acceptance Criteria
- A client can leave a review for a contractor.
- The review is saved and displayed on the contractor's profile page.
##### Tasks
- Create a review form for clients.
- Implement backend logic to save the review in the database.
- Display the review on the contractor's profile page.

10. ## View Reviews
- As a client, I want to see reviews left by other clients so that I can make a more informed decision when choosing a contractor.
##### Acceptance Criteria
- A client can see reviews left by other clients on a contractor's profile page.
- Reviews are displayed in chronological order with the most recent review at the top.
##### Tasks
- Implement logic to fetch reviews from the database.
- Display the fetched reviews on the contractor's profile page in chronological order.


## Design Decisions

### Wireframes

Here are the basic wire-frames we used to establish the design for the site:

![wireframes](/assets/images-readme/wireframe/Wireframe_ContactForm_Desktop.png)
![wireframes](/assets/images-readme/wireframe/Wireframe_ContractorDetails_Desktop.png)
![wireframes](/assets/images-readme/wireframe/Wireframe_LandingPage_Desktop_LoggedIn.png)
![wireframes](/assets/images-readme/wireframe/Wireframe_Register_Desktop.png)
![wireframes](/assets/images-readme/wireframe/Wireframe_SearchListing_Desktop.png)
![wireframes](/assets/images-readme/wireframe/Wireframe_UpdateForm_Desktop.png)

### Colors and Font 

- It was decided to user font styling that would be easy to read and accessible to all visitors. 
![font](/assets/images-readme/fonthack2.png)

- We wanted to use colours that were accessible, easy to view but also with some interest and a bit of fun so that the users would feel like they wished to stay and view the site. 

![colours](/assets/images-readme/coolers2.png)

## Data Model 

- ![erddiagram](/assets/images-readme/erddiagram.png)



## AI Tools Usage

### Chat-GPT / Co pilot

- Code Completion: AI-assisted code completion has accelerated the development process by suggesting context-aware code snippets, reducing manual coding effort.

- Debugging: AI-powered debugging tools have helped identify and rectify code errors, ensuring smoother functionality.

- Imaging: AI-driven imaging tools have assisted in generating and editing visuals, creating a more engaging user experience on the website.

- Text Population: AI has been utilized to auto-generate text for user profiles, form fields, and other content areas, ensuring consistency and saving time.

## Features Implementation

### Core Features (Must-Haves)

### Logo and navigation bar

A responsive navigation bar is in place. Concentrating on 'mobile first' design, the navigation bar incorporates a clickable burger icon with a drop down menu on mobile. There is a burger icon at tablet size too, but when moving to monitor size the burger disappears and a navigation bar appears with options to navigate to pages; 'Home', 'About' or 'Create' and depending on the user login status also a 'Register' and 'Login' link or a 'Logout'. The nav bar also displays the user login status with the message 'You are not logged in' or 'You are logged in as XXXXX'. In the top left corner there is a clickable project logo that also acts as a 'Home' button. See wireframes and other screenshots to view these features or log in to the project.

### Clear indication as to whether the user is logged in or out at all times

As mentioned above the nav bar displays user login status with the message 'You are not logged in' or 'You are logged in as XXXXX'

### Sign in form

This form has a Django allauth template which has been modified to inherit from our base to take on the sites main styling.

### Register form (Sign up)

This form has a Django allauth template which has been modified to inherit from our base to take on the sites main styling.

### Sign out page

This form has a Django allauth template which has been modified to inherit from our base to take on the sites main styling.

### Home Page
- TheHome page is a simple homepage displaying our imaging, styling and allowing the user to see information and then decide where to go from there.

### About Page
- A simple about page is included, to display FAQ's that might help the UX and also a short explanation about the site. 

###  Contractor Sign up page
- Contractor can sign up as a contractor which will then take them to their profile page, this page can be edited after wards if needed. 

###  Contractor Profile Page
- Profile page will display imaging, information and other profile details which will allow a user to see availability etc, as well as leave reviews. 

### Search Page
- This allows clients to search for the contractor based upon the skills they require, the location and the availability. It will then render a list of results. 

### Advanced Features (Should-Haves)

### Django alert messages

Every time there is a change in data the user is alerted. For example when a review is created, or edited and the same for comments. Also there is a notification when the user logs in or out to confirm their action. These appear in the blank space in the middle of the navigation bar to be in the users eyeline when possible.


## Testing and Validation

### Testing Results

We used our team to manually test all views and forms in order to determin that our functionality was complete and without error

## Responsiveness
 All pages on the live site were tested with the default list of devices in Chrome Devtools. Special attention was given to ensuring the images and layout displayed optimally across screen breakpoints, with images specifically optimised for responsive viewing.

## Lighthouse testing

- ![lighthouse1](/assets/images-readme/lighthouse1.png)
- ![lighthouse2](/assets/images-readme/lighthouse2.png)
- ![lighthouse3](/assets/images-readme/lighthouse3.png)


### Validation

All code has been validated through:
- **HTML**: ![W3C Markup Validator](/assets/images-readme/htmlabout.png).
  
- **CSS**: ![W3C CSS Validator](/assets/images-readme/cssvalid.png). 

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

## Reflection

### Team work
- We had to work as a team during this project, as it was only our second Hackathon. We had to ensure that git and github commands/operations were correctly observed so that the process was as smooth as possible. However there were some merge conflicts and issues which were dealt with by the team at the time. 

- We also had to make sure we were speaking all the time, so that no ones work was wiped over. To do this we used mainly slack messaging, whilst also having stand up and stand downs every day, and a middle of the day progress meeting. 

- We used a Miro board to plan and update tasks as we went along, ensuring everyone was on track and up to date with the project. 

# Future features #

- We would like in the future to add another section for the client whereby they can add in the work they need doing, like a job listing page that would connect automatically with available contractors. 

- Another section we wish to implement in the future is an in site messaging app/system where clients can directly get in touch with contractors. 


### Acknowledgements

- We would like to thank Emma and Roo at CI for their help for this project, keeping us on track and to Roo for helping sovle coding problems when they arose. 
- We would like to thanks all members of the Hackathon team, for contributions and develoment, and a smooth project as a team. 