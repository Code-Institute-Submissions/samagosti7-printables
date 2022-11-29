# E-Commerce Store

## Introduction



A live website can be found [here](https://printables.herokuapp.com/).

![website preview](documentation_assets/images/home.jpg)

# Table of Contents

-   [1. UX](#ux)
    -   [1.1. Strategy](#strategy)
        -   [Project Goals](#project-goals)
            -   [User Goals:](#user-goals)
            -   [User Expectations:](#user-expectations)
            -   [Trends of Modern Websites](#trends-of-modern-websites)
            -   [Strategy Table](#strategy-table)
    -   [1.2. Structure](#structure)
    -   [1.3. Skeleton](#skeleton)
    -   [1.4. Surface](#surface)
-   [2. Features](#features)
-   [3. Technologies Used](#technologies-used)
-   [4. Testing](#testing)
-   [5. Deployment](#deployment)
-   [6. SEO](#seo)
-   [7. Marketing](#marketing)
-   [8. Social Media](#social-media)
-   [9. End Product](#end-product)
-   [10. Known Bugs](#known-bugs)
-   [11. Credits](#credits)

<a name="ux"></a>

# 1. UX

[Go to the top](#table-of-contents)

Intro


<a name="strategy"></a>

## 1.1. Strategy

[Go to the top](#table-of-contents)

### Project Goals
 - 

### User Goals:
 - 

### User Expectations:
 - 

### User Stories
 - 


### Strategy Table
Opportunity/Problem/Feature| Importance| Viability/Feasibility
------------ | -------------------------|---------


## Scope
minimum viable product--extra


<a name="structure"></a>

## 1.2. Structure

[Go to the top](#table-of-contents)

 - 

### Database Model
 - models

<a name="skeleton"></a>

## 1.3. Skeleton

[Go to the top](#table-of-contents)

### Wire-frames


<a name="surface"></a>

## 1.4. Surface

[Go to the top](#table-of-contents)


### Typography


<a name="features"></a>

# 2. Features

[Go to the top](#table-of-contents)

### All Pages

- 

### Sign Up Page
- 

### Login Page
- 

### Logout Page
- 

### Landing Page
- 
### Products Page
- 

### Products Detail Page
- 

### Bag Page
- 

### Checkout Page
- 

### Checkout Success Page
- 

### User Profile Page
- 

### Product Management Page
- 

### Newsletter Subscribe Page
- features

<a name="technologies-used"></a>

## 3. Technologies Used

[Go to the top](#table-of-contents)

-   [HTML5](https://en.wikipedia.org/wiki/HTML)
    -   The project uses HyperText Markup Language.
-   [CSS3](https://en.wikipedia.org/wiki/CSS)
    -   The project uses Cascading Style Sheets.
-   [JavaScript](https://en.wikipedia.org/wiki/JavaScript)
    -   The project uses JavaScript.
-   [Python](https://en.wikipedia.org/wiki/Python_(programming_language))
    -   The project uses Python.
-   [Django](https://www.djangoproject.com/)
    -   The project uses Django as the main framework.
-   [Boostrap 4](https://getbootstrap.com/docs/4.0/getting-started/introduction/)
    -   The project uses Bootstrap 4.
-   [PostgreSQL](https://www.postgresql.org/)
    -   The project uses PostgreSQL as a database.
-   [AWS](https://aws.amazon.com/)
    -   The project uses Amazon Web Services to host all static and media files.
-   [Gitpod](https://www.gitpod.io/)
    -   The project uses Gitpod.
-   [Chrome](https://www.google.com/intl/en_uk/chrome/)
    -   The project uses Chrome to debug and test the source code using HTML5.
-   [Heroku](https://www.heroku.com/)
    -   The project is deployed and hosted by Heroku.
-   [Balsamiq](https://balsamiq.com/)
    -   Balsamiq was used to create the wireframes during the design process.
-   [Google Fonts](https://fonts.google.com/)
    -   Google fonts were used to import the "Be Vietnam Pro" font into the style.css file which is used on all pages throughout the project.
-   [GitHub](https://github.com/)
    -   GitHub was used to store the project's code after being pushed from Git.
-   [Stripe](https://github.com/)
    -   GitHub was used to store the project's code after being pushed from Git.


<a name="testing"></a>

# 4. Testing

[Go to the top](#table-of-contents)
### Responsive Tools
responsive tools

### W3C Validator Tools

#### HTML:
w3c markup validation

#### CSS:
w3c css validation

### JavaScript:
jshint validation image

### Python:
I used python3 -m flake8 to test code in gitpod, and evaluated problems as they displayed in the terminal for each file.  This allowed me to rememdy some pieces (mostly deleting imports that generate automatically) and add several new lines at the bottom of file when demanded, but some linetoolong errors were kept as those files were finnicky to format, such as in settings.py 


## Manual Testing

The deployed version of the site was tested through the following: 
-   

### Navigation Bar

All Pages:
TEST            | OUTCOME                          | PASS / FAIL  
--------------- | -------------------------------- | ---------------
Home link | When clicking on the logo in the top left, or on back to home links, the browser redirects me to the home page. | Pass
Navbar | When clicking through the different nav bar elements, they take me to their respective correct destinations, sorting by category accordingly if necessary. | Pass
Footer | When clicking the social media links, they open to the correct destinations in a new tab | Pass
Bag | When clicking the bag icon in the top right, I am taken to the shopping bag page | Pass
Profile | When clicking the My Account link, I am taken from the dropdown menu to either the profile page or logout page accurately | Pass
Search | Search bar displays and searches when enter is pressed or the search icon is clicked, and displays results relevant to the search | Pass
Styling | Styling loads correctly | Pass

### Home page
TEST            | OUTCOME                          | PASS / FAIL  
--------------- | -------------------------------- | ---------------
Media Queries | Media queries are functioning accurately for the background image | Pass

### Products page
TEST            | OUTCOME                          | PASS / FAIL  
--------------- | -------------------------------- | ---------------
Products | Products load and display correctly sorted based on sorting parameters | Pass
Style | Styling loads correctly | Pass
Links | Clicking on either the image or the product name takes you to the product detail page | Pass
CRUD | Admins have CRUD functionality on products page | Pass
Sorting | Sorting bar works as intended, sorting by chosen parameter | Pass

### Products details page
TEST            | OUTCOME                          | PASS / FAIL  
--------------- | -------------------------------- | ---------------
Style | Styling loads correctly | Pass
Quantity | Quantity selector accurately ticks quantity either upward or downward with a minimum of 1 | Pass
Back | Back to shopping link sends me back to products | Pass
Bag | Add to bag button takes me to my bag | Pass
Images | Product image and image preview load | Pass

### Shopping bag page
TEST            | OUTCOME                          | PASS / FAIL  
--------------- | -------------------------------- | ---------------
Quantity | Quantity selector and removal option accurately removes or adds item to bag | Pass
Style | Styling loads correctly | Pass
Back | Keep shopping button redirects users to products | Pass
Checkout | Checkout button redirects users to checkout | Pass
Total | Grand total and subtotals tally accurately | Pass

### Checkout page
TEST            | OUTCOME                          | PASS / FAIL  
--------------- | -------------------------------- | ---------------
Style | Styling loads correctly | Pass
Form | Checkout form in its entirety loads correctly | Pass
Address | Address format from django loads properly, with the accompanying countryfield selector in the dropdown | Pass
Payment | Card details can be provided and payment functions, facilitated by stripe | Pass
Back | Adjust bag button takes me to bag | Pass
Complete order | Button completes order | Pass
Save | Save delivery checkbox saves info of user | Pass

### Checkout success page
TEST            | OUTCOME                          | PASS / FAIL  
--------------- | -------------------------------- | ---------------
Order details | Order details display properly | Pass 
Style | Styling loads correctly | Pass
Order history | Order is added to order history | Pass

### My profile pags
TEST            | OUTCOME                          | PASS / FAIL  
--------------- | -------------------------------- | ---------------
Update | Delivery info can be edited and updates accordingly | Pass 
Style | Styling loads correctly | Pass
Order history | Order history loads correctly | Pass

### Contact US
TEST            | OUTCOME                          | PASS / FAIL  
--------------- | -------------------------------- | ---------------
Style | Styling loads correctly | Pass
Contact form | Contact form loads correctly | Pass
Newsletter form | Newsletter form loads correctly | Pass
Redirects | Forms redirect to home upon completion, with success message | Pass

### Authorization
TEST            | OUTCOME                          | PASS / FAIL  
--------------- | -------------------------------- | ---------------
Login | Login function works for verified users and sends message | Pass
Logout | Logout function works and sends message | Pass
Register | Unregistered users can signup and receive an email for confirmation on signup | Pass
Admin | Admin panel loads at appropriate URL, and admin functionality follows if the user is a superuser | Pass


<a name="deployment"></a>

# 5. Deployment
[Go to the top](#table-of-contents)

I used the terminal to deploy my project locally. To do this I had to:

1. Create a repository on GitHub.
2. Open repo via an editor, GitPod 
3. Enter "python3 manage.py runserver into the terminal to access a locally hosted port
 

For the final deployment to Heroku, I had to:

1. Create Heroku App
2. Install dj_database_url and psycopg2 in my local environment
3. Complete requirements.txt file with all the necessary installments for the project
4. In settings.py import dj_database_url
5. Back up the local database using "./manage.py dumpdata --exclude auth.permission --exclude contenttypes > db.json" in the terminal window.
6. Comment out the local default database
7. Add the Heroku database url via dj_database_url.parse()
8. Run migrations to the Postgres database
9. Restore the database using this command "./manage.py loaddata db.json" in the terminal windows.
10. Create a SuperUser for the Postgres database
11. Configure the database so that when the app is running on Heroku it uses the Postgres database and when it's running locally it uses the SQLite database
12. Create Procfile so that Heroku creates a web dyno so that it will run gunicorn and serve the Django app
13. Disable Heroku collect static
14. Add the Heroku hostname to allowed hosts in settings.py
15. Generate a new Django secret key and add this to the Heroku config variables
16. Replace the secret key in settings.py to grab it from the environment
17. Set debug to True only if the environment is a development environment
18. Commit changes and deploy to GitHub and Heroku
19. Create an AWS account
20. Create an S3 bucket
21. Configure the S3 bucket settings and policies
22. Create and configure the IAM service
23. In the terminal install Boto3 and Django-storages
24. Freeze requirements.txt file
25. Add a statement to the AWS bucket if the environment is "USE_AWS"
26. Add AWS keys to the Heroku config variables
27. Create custom storage classes for media and static files
28. In settings.py add a statement to use the static and media storage class and locations
29. Commit and push to GitHub and Heroku
30. In the S3 bucket create a new folder for media
31. Upload all used images to the media file in the S3 bucket
32. Add the Stripe keys to the Heroku config variables
33. Create a new webhook endpoint from the Stripe dashboard
34. Add all the Stripe keys to the Heroku config variables

<a name="seo"></a>

# 6. SEO
[Go to the top](#table-of-contents)

To improve the search engine optimisation (SEO) of the site I:

- Added keywords in a meta tag to my base.html. The keywords were researched using [WordTracker](https://www.wordtracker.com/), there are a number of short-tail and long-tail keywords.


- 

I chose these keywords because they didn't have incredibly high volume and competition.


<a name="marketing"></a>

# 7. Marketing
[Go to the top](#table-of-contents)

Marketing

- 


<a name="social-media"></a>

# 8. Social Media Business Page
[Go to the top](#table-of-contents)

pic of fake facebook page

The business will use social media as a platform to promote the business.

<a name="end-product"></a>

# 9. End Product
[Go to the top](#table-of-contents)

images of end product


<a name="known-bugs"></a>

# 10. Known Bugs
[Go to the top](#table-of-contents)

- 

<a name="credits"></a>

# 11. Credits

[Go to the top](#table-of-contents)

### Code

 - Boutique Ado



### Content

- All images on the site came from 
- Readme Skeleton
