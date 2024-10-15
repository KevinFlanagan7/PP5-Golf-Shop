![Logo]()

# Golf Shop

## Project Goals




## UX

## User Stories

-  As a user, 

\
&nbsp;
[Back to Top](#golf-shop)
\
&nbsp;

## Design

### Colours 

![Coolors]()



\
&nbsp;
[Back to Top](#golf-shop)
\
&nbsp;

### Fonts

I have used the default font families provided by Bootstrap for different devices and browsers. This ensures optimal readability and a consistent look. Below is a list of the default fonts depending on the device and browser used: 

font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, "Noto Sans", "Liberation Sans", sans-serif, "Apple Color Emoji", "Segoe UI Emoji", "Segoe UI Symbol", "Noto Color Emoji".


### Icons

I have used the [Font Awesome library](https://fontawesome.com/ "Font Awesome") for the social media icons in the footer and a [Favicon generator](https://favicon.io/favicon-converter/ "Favicon") for the browser tab icon.

### Structure

I have built the website with a mobile first mindset using the iPhone SE (375px) as the smallest screen size for styling to look good on. The screen size breakpoints that I will be using are from [Bootstrap breakpoints](https://getbootstrap.com/docs/5.0/layout/breakpoints/).

| Screen Size | Breakpoint |
| ----------- | ---------- |
| x-small     | <576px     |
| small       | => 576px   |
| medium      | => 768px   |
| large       | => 992px   |
| x-large     | => 1200px  |

\
&nbsp;
[Back to Top](#golf-shop)
\
&nbsp;

### Wireframes



\
&nbsp;
[Back to Top](#golf-shop)
\
&nbsp;

### Database Schema

![Database schema](/documentation/database/database.png)

#### User model
Represents the users of the application. Each user has a unique username and email, along with a hashed password for authentication. It has a One-to-One relationship so each user has a corresponding UserProfile.

#### UserProfile model
Maintains default delivery information and order history for a user. It allows storing additional details related to a user beyond the basic authentication information. It has a One-to-One relationship with user model and also a One-to-Many relationship with orders so a user can have multiple orders.

#### Category model
Represents product categories, allowing for better organization and classification of products in the shop. It has a One-to-Many relationship so multiple products associated with each category.

#### Product model
Represents items available for sale in the shop. Each product is categorized and can have associated attributes such as size and price. It has a One-to-One relationship with a category so each product is associated with a single Category. It also has a One-to-Many relationship with order line item and wishlist item so a product can be linked with multiple order line items and user wishlists.

#### Order model
Represents a customer's order, containing all necessary information for processing and delivery. It includes customer details and the order's total amounts. It has Many-to-One relationship with user profile so multiple oreders can be linked to a user profile or null for a guest user. It also has a One-to-Many with order line item so an order can have multiple products.

#### OrderLineItem model
Represents a specific product included in an order. It includes information on product size, quantity, and the total price for that line item. It has a Many-to-One relationship so each order line item is linked to a single order and product.

#### Contact model
Represents a contact request made by users to the application. It stores the user's name, email, and their message. It operates independently without relationships to other models.

#### Wishlist model
Represents a user's wishlist, which can hold multiple products. It allows users to save items for future consideration. It has a One-to-One relationship so it is Linked to a single UserProfile.

#### WishlistItem model
Represents a specific product in a user's wishlist. It tracks when the item was added. It has a Many-to-One relationship so each wishlist item is linked to a single Wishlist and each wishlist item is linked to a single Product.

#### FAQ model
Represents frequently asked questions along with their answers. This helps users find information quickly. It operates independently without relationships to other models.

\
&nbsp;
[Back to Top](#golf-shop)
\
&nbsp;
    
### Agile Methodology

#### Overview

I used Agile methodology to plan my project. It allowed me to break down the project into smaller manageable clear tasks. It made it easier to prioritize tasks, to track progress and to maintain momentum during development. 

#### Epics & Milestones

My project is made up of several Epics which are large bodies of work that can be broken down into smaller, more manageable tasks. They provide an overview of the main functionalities to deliver, there are six milestones associated to the projects Epics. For my project, the Milestones with associated Epics, stories and tasks can be viewed at the links below:

- [Milestone 1 - Initial Set Up](https://github.com/KevinFlanagan7/PP5-Golf-Shop/milestone/1)

- [Milestone 2 - Homepage creation](https://github.com/KevinFlanagan7/PP5-Golf-Shop/milestone/2)

- [Milestone 3 - Product setup, filtering and searching](https://github.com/KevinFlanagan7/PP5-Golf-Shop/milestone/3)

- [Milestone 4 - Shopping cart setup](https://github.com/KevinFlanagan7/PP5-Golf-Shop/milestone/4)

- [Milestone 5 - Heroku deployment](https://github.com/KevinFlanagan7/PP5-Golf-Shop/milestone/5)

- [Milestone 6 - Checkout app and stripe payment setup](https://github.com/KevinFlanagan7/PP5-Golf-Shop/milestone/6)

- [Milestone 7 - Profile app, Wishlist app and Product Admin setup](https://github.com/KevinFlanagan7/PP5-Golf-Shop/milestone/7)

- [Milestone 8 - Page Footer setup](https://github.com/KevinFlanagan7/PP5-Golf-Shop/milestone/8)

- [Milestone 9 - ]()

- [Milestone 10 - ]()


\
&nbsp;
[Back to Top](#golf-shop)
\
&nbsp;

#### Github Project

The Github projects tool was used to implement Agile development practices efficiently. By using Kanban boards, tasks were visually managed and tracked through various stages of completion. The MoSCoW (Must have, Should have, Could have & Won't have) method was used to prioritize features and tasks, view below links to the project's Kanban board and MoSCoW prioritization method:

- [Kanban board]()

- [MoSCoW Prioritization]()

\
&nbsp;
[Back to Top](#golf-shop)
\
&nbsp;

## SEO (Search Engine Optimization)
To optimize the visibility of the Golf Shop in search engine results, the following SEO strategies have been implemented:

- Meta Tags: Included detailed meta descriptions and meta keywords to improve relevance in search results. The keywords include both short and long-tail terms, such as:

    - Short-tail: "golf shop," "golf clubs," "golf shoes"
    - Long-tail: "premium golf clubs for sale," "Titleist GT golf drivers online," "buy Adidas golf shoes with fast shipping"

- Sitemap: A sitemap.xml file has been generated to help search engines efficiently crawl the site. It includes URLs   for all key pages like product categories (e.g., drivers, bags, shoes), individual product listings, and informational pages such as contact and FAQ.

- robots.txt: A robots.txt file has been added to control search engine crawlers' access, allowing them to index the most important pages while avoiding less relevant content, like certain backend files or administrative URLs.

- Semantic HTML: The use of semantic HTML elements like `<header>`, `<nav>`, `<section>`, and `<footer>` helps search engines understand the structure of the page better, also including detailed `alt` description for images improves accessibility and SEO ranking. By clearly defining sections of content, these tags help search engines identify important content like product details, navigation menus, and footers, boosting the chances of appearing in relevant search queries.

By utilizing these SEO techniques and following semantic HTML best practices, the site is designed to improve its visibility in search engines for users searching for golf equipment, leading to better rankings and increased traffic.

## Marketing

The Golf shop is a B2C (business-to-consumer) business, focused on providing high-quality golf equipment directly to individual customers. Several marketing tools and strategies have been implemented to enhance the customer experience, engage with visitors, and build brand loyalty.

- Mailchimp Newsletter Sign-Up: A newsletter sign-up form is integrated in the site’s footer using Mailchimp. This allows visitors to subscribe easily to regular updates about new product releases and exclusive deals.

- Facebook Page: The Golf Shop connects with customers on social media via its dedicated Facebook page. This platform is used to engage with the golf community, post updates about new arrivals and promote content. By interacting with followers on Facebook, the shop builds brand awareness and developes an active customer base. The `rel="noopener external"`attribute is added to link for thye golf shop site security and tells search engines that the site is external.

    ![Facebook page](/documentation/features/facebook-page.png)

- Privacy Policy: A detailed privacy policy is included to inform customers about how their personal data is collected, used, and protected. This ensures compliance with privacy laws and builds trust with visitors, assuring them that their information, particularly email addresses gathered via the Mailchimp newsletter, is handled securely. Having a clear privacy policy is essential for customer trust and retention.

- Contact Us and FAQ Links: The footer contains helpful links to the Contact Us page and FAQ section, providing direct access to customer service and commonly asked questions. These links enhance the user experience by offering clear paths for support and additional information, making it easy for customers to reach out for assistance or find answers to product-related queries.

## Features

## Existing Features

### Home


\
&nbsp;
[Back to Top](#golf-shop)
\
&nbsp;


## Features to be Implemented



\
&nbsp;
[Back to Top](#golf-shop)
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
[Back to Top](#golf-shop)
\
&nbsp;

### Database



### Tools




\
&nbsp;
[Back to Top](#golf-shop)
\
&nbsp;

## Testing

### Code Validation

<details><summary>HTML files</summary>

A few errors found with HTML files, see details below:

- Home page

    ![Home](/documentation/code_validation/home-html.png)

- Login page

    ![Login](/documentation/code_validation/login-html.png)

- Signup page, error caused by Allauth signup form

    ![Signup](/documentation/code_validation/signup-html.png)

- Products

    ![Products](/documentation/code_validation/products-html.png)

- Drivers page

    ![Drivers](/documentation/code_validation/drivers-html.png)

- Bags page

    ![Bags](/documentation/code_validation/bags-html.png)

- Irons page

    ![Irons](/documentation/code_validation/irons-html.png)

- Shoes page

    ![Shoes](/documentation/code_validation/shoes.html.png)

- Cart page, Duplicate errors caused by 2 quantity form includes, one for small screen layout size and one for large.

    ![Cart](/documentation/code_validation/cart-html.png)

- Cart empty page

    ![Cart empty](/documentation/code_validation/cart-empty-html.png)

- Checkout page

    ![Checkout](/documentation/code_validation/checkout-html.png)

- Checkout success page

    ![Checkout success](/documentation/code_validation/checkout-success-html.png)

- Product Admin page, error caused by custom widget template used for adding images.

    ![Product Admin](/documentation/code_validation/product-admin-html.png)

- Edit page, error caused by custom widget template used for editing images.

    ![Edit](/documentation/code_validation/edit-html.png)

- My Profile page

    ![Profile](/documentation/code_validation/profile-html.png)

- My Wishlist page

    ![Wishlist](/documentation/code_validation/wishlist-html.png)

- My Wishlist empty page

    ![Wishlist empty](/documentation/code_validation/wishlist-empty-html.png)

- Sign out page

    ![Signout](/documentation/code_validation/signout-html.png)

- Contact us page

    ![Contact](/documentation/code_validation/contact-html.png)

- Password reset page

    ![reset](/documentation/code_validation/password-reset-html.png)

- Change password page

    ![change](/documentation/code_validation/change-password-html.png)

- Password changed page

    ![changed](/documentation/code_validation/password-changed-html.png)

- Verify email page

    ![verify](/documentation/code_validation/verify-email.html.png)


</details>

<br>


<details><summary>CSS files</summary>

No errors found on the css files below:

- Base.css

    ![Base](/documentation/code_validation/base-css.png)

- Profile css

    ![Profile](/documentation/code_validation/profile-css.png)

- Checkout css

    ![Checkout](/documentation/code_validation/checkout-css.png)

</details>

<br>

<details><summary>JavaScript files</summary>

No erros found with any of the JS files below:

- Quantity selector script

    ![Quantity](/documentation/code_validation/quantity-selector-js.png)

- Scroll icon script

    ![Quantity](/documentation/code_validation/scroll-js.png)

- Update and Remove product script

    ![Update](/documentation/code_validation/update-remove-js.png)

- Country Select field script

    ![Country](/documentation/code_validation/countryfield-js.png)

- Image selector script

    ![Image](/documentation/code_validation/image-selector-js.png)

- Stripe elements script

    ![Stripe](/documentation/code_validation/stripe-elements-js.png)

</details>

<br>

<details><summary>Python files</summary>

No errors for project files and each app, see below:

Golfshop Project files

- settings.py

    ![settings](/documentation/code_validation/settings-py.png)

- urls.py

    ![urls](/documentation/code_validation/golfshop-urls-py.png)

- views.py

    ![Settings](/documentation/code_validation/golfshop-views-py.png)

<br>

Home App files

- urls.py

    ![urls](/documentation/code_validation/home-urls-py.png)

- views.py

    ![views](/documentation/code_validation/home-views-py.png)

<br>

Product App files

- admin.py

    ![admin](/documentation/code_validation/products-admin-py.png)

- forms.py

    ![forms](/documentation/code_validation/products-forms-py.png)

- models.py

    ![models](/documentation/code_validation/products-models-py.png)

- urls.py

    ![urls](/documentation/code_validation/products-urls-py.png)

- views.py

    ![views](/documentation/code_validation/products-views-py.png)

- widgets.py

    ![widgets](/documentation/code_validation/products-widgets-py.png)

<br>

Cart App files

- cart_tools.py

    ![tools](/documentation/code_validation/cart-tools-py.png)

- contexts.py

    ![context](/documentation/code_validation/cart-contexts-py.png)

- urls.py

    ![urls](/documentation/code_validation/cart-urls-py.png)

- views.py

    ![views](/documentation/code_validation/cart-views-py.png)

<br>

Checkout App files

- admin.py

    ![admin](/documentation/code_validation/checkout-admin-py.png)

- forms.py

    ![forms](/documentation/code_validation/checkout-forms-py.png)

- models.py

    ![models](/documentation/code_validation/checkout-models-py.png)

- signals.py

    ![signals](/documentation/code_validation/checkout-signals-py.png)

- urls.py

    ![urls](/documentation/code_validation/checkout-urls-py.png)

- views.py

    ![Settings](/documentation/code_validation/checkout-views-py.png)

- webhook_handler.py

    ![handler](/documentation/code_validation/checkout-webhook-handler-py.png)

- webhooks.py

    ![webhooks](/documentation/code_validation/checkout-webhooks-py.png)

<br>

Profiles App files

- forms.py

    ![forms](/documentation/code_validation/profiles-forms-py.png)

- models.py

    ![models](/documentation/code_validation/profiles-models-py.png)

- urls.py

    ![urls](/documentation/code_validation/profiles-urls-py.png)

- views.py

    ![views](/documentation/code_validation/profiles-views-py.png)

<br>

Contact App files

- admin.py

    ![admin](/documentation/code_validation/contact-admin-py.png)

- forms.py

    ![forms](/documentation/code_validation/contact-forms-py.png)

- models.py

    ![models](/documentation/code_validation/contact-models-py.png)

- urls.py

    ![urls](/documentation/code_validation/contact-urls-py.png)

- views.py

    ![views](/documentation/code_validation/contact-views-py.png)

<br>

Wishlist App files

- admin.py

    ![admin](/documentation/code_validation/wishlist-admin-py.png)

- models.py

    ![models](/documentation/code_validation/wishlist-models-py.png)

- urls.py

    ![urls](/documentation/code_validation/wishlist-urls-py.png)

- views.py

    ![views](/documentation/code_validation/wishlist-views-py.png)

<br>

FAQ App files

- admin.py

    ![admin](/documentation/code_validation/faq-admin.py.png)

- models.py

    ![models](/documentation/code_validation/faq-models.py.png)

- urls.py

    ![urls](/documentation/code_validation/faq-urls.py.png)

- views.py

    ![views](/documentation/code_validation/faq-views.py.png)

</details>
   
\
&nbsp;
[Back to Top](#golf-shop)
\
&nbsp;

### Lighthouse

Lighthouse tests were run on all deployed pages for mobile and desktop, see results below:

<details><summary>Home page</summary>

- Desktop

    ![desktop](/documentation/lighthouse/home-lighthouse.png)

- Mobile

    ![mobile](/documentation/lighthouse/home-mobile-lighthouse.png)

</details>

<br>

<details><summary>Products page</summary>

- Desktop

    ![desktop](/documentation/lighthouse/products-lighthouse.png)

- Mobile

    ![mobile](/documentation/lighthouse/home-mobile-lighthouse.png)

</details>

<br>

<details><summary>Product detail page</summary>

- Desktop

    ![desktop](/documentation/lighthouse/product-detail-lighthouse.png)

- Mobile

    ![mobile](/documentation/lighthouse/product-detail-mobile-lighthouse.png)

</details>

<br>

<details><summary>Cart page</summary>

- Desktop

    ![desktop](/documentation/lighthouse/cart-lighthouse.png)

- Mobile

    ![mobile](/documentation/lighthouse/cart-mobile-lighthouse.png)

</details>

<br>

<details><summary>Checkout page</summary>

- Desktop

    ![desktop](/documentation/lighthouse/checkout-lighthouse.png)

- Mobile

    ![mobile](/documentation/lighthouse/checkout-mobile-lighthouse.png)

</details>

<br>

<details><summary>Checkout success page</summary>

- Desktop

    ![desktop](/documentation/lighthouse/checkout-success-lighthouse.png)

- Mobile

    ![mobile](/documentation/lighthouse/checkout-success-mobile-lighthouse.png)

</details>

<br>

<details><summary>Login page</summary>

- Desktop

    ![desktop](/documentation/lighthouse/login-lighthouse.png)

- Mobile

    ![mobile](/documentation/lighthouse/login-mobile-lighthouse.png)

</details>

<br>

<details><summary>Password reset page</summary>

- Desktop

    ![desktop](/documentation/lighthouse/password-reset-lighthouse.png)

- Mobile

    ![mobile](/documentation/lighthouse/password-reset-mobile-lighthouse.png)

</details>

<br>

<details><summary>Sign up page</summary>

- Desktop

    ![desktop](/documentation/lighthouse/signup-lighthouse.png)

- Mobile

    ![mobile](/documentation/lighthouse/signup-mobile-lighthouse.png)

</details>

<br>

<details><summary>Product Admin page</summary>

- Desktop

    ![desktop](/documentation/lighthouse/product-admin-lighthouse.png)

- Mobile

    ![mobile](/documentation/lighthouse/product-admin-mobile-lighthouse.png)

</details>

<br>

<details><summary>Profile page</summary>

- Desktop

    ![desktop](/documentation/lighthouse/profiles-lighthouse.png)

- Mobile

    ![mobile](/documentation/lighthouse/profiles-mobile-lighthouse.png)

</details>

<br>

<details><summary>Wishlist page</summary>

- Desktop

    ![desktop](/documentation/lighthouse/wishlist-lighthouse.png)

- Mobile

    ![mobile](/documentation/lighthouse/wishlist-mobile-lighthouse.png)

</details>

<br>

<details><summary>Sign out page</summary>

- Desktop

    ![desktop](/documentation/lighthouse/signout-lighthouse.png)

- Mobile

    ![mobile](/documentation/lighthouse/signout-mobile-lighthouse.png)

</details>

<br>

<details><summary>Contact Us page</summary>

- Desktop

    ![desktop](/documentation/lighthouse/contact-lighthouse.png)

- Mobile

    ![mobile](/documentation/lighthouse/contact-mobile-lighthouse.png)

</details>

<br>

<details><summary>FAQ page</summary>

- Desktop

    ![desktop](/documentation/lighthouse/faq-lighthouse.png)

- Mobile

    ![mobile](/documentation/lighthouse/faq-mobile-lighthouse.png)

</details>

<br>

### Features Testing

- Home Page 

    |Items being tested|Actions taken to test|Expected result|Outcome|
    |---|---|---|---|
  
    
\
&nbsp;
[Back to Top](#golf-shop)
\
&nbsp;
        
### User Stories Testing

- Table of User Story Testing.

    |User Story|Testing|Result|
    |---|---|---|
    |As a user, ||:white_check_mark:|
    
\
&nbsp;
[Back to Top](#golf-shop)
\
&nbsp;

### Responsiveness

- Using Chrome Mobile [Simulator](https://developer.chrome.com/docs/devtools/device-mode "Simulator") extension I have tested the website's responsiveness on different devices. Test results and screenshots below:

    | Device                | Responsive >=768px | Responsive <768px | Landing page Images |
    | --------------------- | ------------------ | ----------------- | ----------- | 
    | iPhone SE             | N/A                | Good              | Good        |
    | iPhone 6/7/8          | N/A                | Good              | Good        |
    | iPad Pro              | Good               | N/A               | Good        |
    | Desktop 1024px        | Good               | N/A               | Good        |
    | Desktop > 1200px      | Good               | N/A               | Good        |

    <details><summary>Responsiveness Screenshots</summary>

    <br>

    **Mobile**

    | Home Page | Product Page | Cart Page |
    | ---- | ----- | ------ |
    | ![Home]() | ![Product]() | ![Cart]() |

    **Desktop**

    | Home Page | Product Page | Cart Page |
    | ---- | ----- | ------ |
    | ![Home]() | ![Product]() | ![Cart]() |  

\
&nbsp;
[Back to Top](#golf-shop)
\
&nbsp;

### Browser Compatibility

- Table of Browsers tested:

  | Browser | Intented Appearance | Intented Responsiveness | 
    | --------| ------------------- | ----------------------- |
    | Chrome  | Good | Good | 
    | Edge    | Good | Good | 
    | Firefox | Good | Good |

    <details><summary>Browser compatibility Screenshots</summary>

    <br>

    *Chrome*

    ![Chrome]() 

    *Edge*

    ![Edge]()

    *Firefox*

    ![Firefox]()


\
&nbsp;
[Back to Top](#golf-shop)
\
&nbsp;

### Bugs

### Unfixed Bugs


\
&nbsp;
[Back to Top](#golf-shop)
\
&nbsp;

## Deployment

### AWS configuration

Golfshop uses Amazon Web Services (AWS) to store static and media files securely in the cloud, it was setup following steps below:

#### Create and Configure an S3 Bucket
    
-   Go to [aws.amazon.com](https://aws.amazon.com/), create accont and log in to your AWS Management Console.

-   Search for "S3" in the AWS Management Console and create a new bucket.

-   Name the bucket to match your Heroku app name and select the region closest to your target audience.

-   Uncheck the "Block all public access" option and acknowledge that the bucket will be public (required for compatibility with Heroku).

-   Under "Object Ownership," ensure "ACLs enabled" and "Bucket owner preferred" are selected.

-   In the "Properties" tab, enable static website hosting.

-   Set `index.html` as the index document and `error.html` as the error document, then click "Save".
-   In the "Permissions" tab, add the following CORS configuration:
    
    `[
      {
        "AllowedHeaders": ["Authorization"],
        "AllowedMethods": ["GET"],
        "AllowedOrigins": ["*"],
        "ExposeHeaders": []
      }
    ]` 
    
-   Copy your bucket's ARN (Amazon Resource Name).
-   Go to the "Bucket Policy" tab and click on the "Policy Generator" link.
    -   Configure the policy:
        -   **Policy Type:** S3 Bucket Policy
        -   **Effect:** Allow
        -   **Principal:** *
        -   **Actions:** `s3:GetObject`
        -   **ARN:** Paste your bucket's ARN
    -   Click "Add Statement" and "Generate Policy."
    -   Copy the generated policy and paste it into the "Bucket Policy Editor":
    
    ```{
      "Version": "2012-10-17",
      "Statement": [
        {
          "Effect": "Allow",
          "Principal": "*",
          "Action": "s3:GetObject",
          "Resource": "arn:aws:s3:::your-bucket-name/*"
        }
      ]
    }```
    
-   Ensure the `Resource` field ends with `/*` and click "Save."
    
-   In the "Access Control List" (ACL) section, click "Edit" and enable "List" for Everyone (public access). Accept the warning prompt.

-   If the edit option is disabled, ensure the "Object Ownership" settings have ACLs enabled.

#### Configure IAM (Identity and Access Management):**
    
-   Navigate to the IAM service and select "User Groups."

-   Click "Create New Group," and name it appropriately.

-   Select the newly created group and go to the "Permissions" tab.

-   Click "Add Permissions" > "Attach Policies."

-   In the "JSON" tab, click "Import Managed Policy" and search for `AmazonS3FullAccess`.

-   Import the policy and modify it to limit access to your specific bucket:
    
    ```{
      "Version": "2012-10-17",
      "Statement": [
        {
          "Effect": "Allow",
          "Action": "s3:*",
          "Resource": [
            "arn:aws:s3:::your-bucket-name",
            "arn:aws:s3:::your-bucket-name/*"
          ]
        }
      ]
    }```
    
    -   Click "Review Policy" and name it (e.g., `policy-teacup-tales`), then click "Create Policy."

#### Add Users and Assign Permissions
    
-   Go back to "User Groups," select your group, and click "Attach Policy."

-   Select your custom policy and attach it.

-   Click "Add User" and name it appropriately.

-   Select "Programmatic Access" and add the user to your group.

-   Download the CSV file containing the `AWS_ACCESS_KEY_ID` and `AWS_SECRET_ACCESS_KEY`.

#### Heroku Integration
    
-   Remove `DISABLE_COLLECTSTATIC` from Heroku Config Vars and add AWS keys to enable AWS management of static files.

- Configure settings.py file with AWS settings

-   Within your S3 bucket, create a new folder named `media`.

-   Upload your media files into this folder and set "Public read access."

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
[Back to Top](#golf-shop)
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
[Back to Top](#golf-shop)
\
&nbsp;

## Credits

My mentor For help and advice:

- [Simen Daehlin](https://github.com/Eventyret "Simen Daehlin")




\
&nbsp;
[Back to Top](#golf-shop)
\
&nbsp;