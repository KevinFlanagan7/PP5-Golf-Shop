![Logo]()

# Golf Shop

## Project Goals




## UX

## User Stories

-  As a user, 

\
&nbsp;
[Back to Top](#table-of-contents)
\
&nbsp;

## Design

### Colours 

![Coolors]()



\
&nbsp;
[Back to Top](#table-of-contents)
\
&nbsp;

### Fonts

### Icons

### Structure



\
&nbsp;
[Back to Top](#table-of-contents)
\
&nbsp;

### Wireframes



\
&nbsp;
[Back to Top](#table-of-contents)
\
&nbsp;

### Database Schema

\
&nbsp;
[Back to Top](#table-of-contents)
\
&nbsp;
    
### Agile Methodology

#### Overview


#### Epics & Milestones


\
&nbsp;
[Back to Top](#table-of-contents)
\
&nbsp;

#### Github Project


\
&nbsp;
[Back to Top](#table-of-contents)
\
&nbsp;

## Features

## Existing Features

### Home


\
&nbsp;
[Back to Top](#table-of-contents)
\
&nbsp;


## Features to be Implemented



\
&nbsp;
[Back to Top](#table-of-contents)
\
&nbsp;

## Technologies used

### Languages

- [HTML](https://en.wikipedia.org/wiki/HTML "HTML") 
- [CSS](https://en.wikipedia.org/wiki/CSS "CSS")
- [JavaScript](https://en.wikipedia.org/wiki/JavaScript "JS")
- [Python](https://en.wikipedia.org/wiki/Python_(programming_language) "Python")

### Frameworks

- [Django](https://en.wikipedia.org/wiki/Django_(web_framework) "Django")
- [Bootstrap](https://en.wikipedia.org/wiki/Bootstrap_(front-end_framework) "Bootstrap")

\
&nbsp;
[Back to Top](#table-of-contents)
\
&nbsp;

### Database



### Tools




\
&nbsp;
[Back to Top](#table-of-contents)
\
&nbsp;

## Testing

### Code Validation

<details><summary>HTML files</summary>

- Home page

    ![Home]()


<details><summary>CSS file</summary>

- style.css file

    ![CSS]()

</details>

<br>

<details><summary>JavaScript file</summary>

- script.js

    ![JS]()

</details>

<br>

<details><summary>Python files</summary>

- model.py

    ![Model]()

- views.py

    ![Views]()

- forms.py

    ![Forms]()

- urls.py

    ![Urls]()

- admin.py

    ![Admin]()

- settings.py

    ![Settings]()

</details>
   
\
&nbsp;
[Back to Top](#table-of-contents)
\
&nbsp;

### Lighthouse


### Features Testing

- Home Page 

    |Items being tested|Actions taken to test|Expected result|Outcome|
    |---|---|---|---|
  
    
\
&nbsp;
[Back to Top](#table-of-contents)
\
&nbsp;
        
### User Stories Testing

- Table of User Story Testing.

    |User Story|Testing|Result|
    |---|---|---|
    |As a user, ||:white_check_mark:|
    
\
&nbsp;
[Back to Top](#table-of-contents)
\
&nbsp;

### Responsiveness

\
&nbsp;
[Back to Top](#table-of-contents)
\
&nbsp;

### Browser Compatibility


\
&nbsp;
[Back to Top](#table-of-contents)
\
&nbsp;

### Bugs

### Unfixed Bugs


\
&nbsp;
[Back to Top](#table-of-contents)
\
&nbsp;

## Deployment

### Heroku

The site was deployed using Heroku following the steps below:

- Create a list of requirements using the following command in the terminal (`pip3 freeze > requirements.txt`).

- Heroku searches for this exact file name as it builds the project. This file contains the list of the packages installed during project development which are called dependencies. We need Heroku to install these dependecies as well in order for the project to run. 

- A **Procfile** is required to allow Heroku deployment to be properly configured to a gunicorn web app.

- In settings.py file configure the ALLOWED_HOSTS list with **heroku.com**.

- All environment variables in the env.py which gitignored on the repo must be configured correctly with the database details and secret keys.

- Activate your Heroku Student Pack account at the following link: [Heroku for Students]( https://www.heroku.com/github-students).

- From Heroku Dashboard click on **Create New App**, enter name of app, choose your region and then click **Create App**.

- Click on the **Settings** tab of the newly created app.

- Go to **Config Vars** section and enter the required hidden variables like database details and secret keys.

- Click on **Deploy** tab at top of screen.

- In **Deployment method** section selct **GitHub** and confirm by clicking **Connect to GitHub**.

- Serach for your GitHub repository name, once found click **Connect**.

- Scroll down on page and select either **Enable Automatic Deploys** which will rebuild your app every time you push a new change to GitHub or **Deploy Branch** which is a manual deployment so has to be selected after each change pushed to GitHub.

- Once app is built you can click on **Open app** at top of page which will open app on new page where you can copy URL.

\
&nbsp;
[Back to Top](#table-of-contents)
\
&nbsp;

### Fork

To make a copy of a repository or to fork it using Github follow below steps:

- Go to **Github repository** to be copied.
- Click on the **Fork** button in upper right corner of page to copy.

### Clone

To copy the repository to your local machine in Github follow steps below:

- Go to **Github repository** to be cloned.
- Click on the **Code** button above the list of files.
- Select to clone using either  **HTTPS**, **SSH**, or **Github CLI** and click the **copy** button to copy the URL to clipboard.
- Open **Git Bash**.
- Change the current working directory to the one where you want the cloned directory.
- Type **git clone** and paste the URL from the clipboard. 
- Press **Enter** to create your local clone.

### Run Locally

- Go to the **GitHub repository**.
- Locate the green **Code** button above the list of files and click it.
- From the dropdown menu select **download Zip**.
- **Download** and open the zip file to run in an editor.
- Create an **env.py** file and input the environment variables
- Ensure **PostgreSQL** is installed on your computer and ports are open
- Create a virtual environment for installing the **python modules** in the pip file.
- Run python **makemigrations, migrate and runserver**.

\
&nbsp;
[Back to Top](#table-of-contents)
\
&nbsp;

## Credits

My mentor For help and advice:

- [Simen Daehlin](https://github.com/Eventyret "Simen Daehlin")




\
&nbsp;
[Back to Top](#table-of-contents)
\
&nbsp;