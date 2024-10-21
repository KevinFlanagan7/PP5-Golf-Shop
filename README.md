![Logo](/documentation/features/logo.png)

# Welcome to the GOLFshop

## Project Goals

The goal of the Golfshop project is to create a user-friendly, fully responsive e-commerce website that provides both guest users and registered users with an easy and enjoyable shopping experience. The site showcases a range of golf products while offering features like user account management, wishlist functionality, and a seamless cart checkout. Guest users can browse products and make purchases without creating an account, while registered users benefit from additional features like order history and saved preferences.

The target audience includes golf enthusiasts of all skill levels, from beginners looking to purchase their first set of equipment to seasoned players seeking the latest gear. The site is also designed for golf shop owners and administrators who need an intuitive platform to manage products and customer interactions. Additionally, casual shoppers looking for golf gifts or accessories.

The project includes features such as newsletters, product search, and a FAQ section to improve user engagement, boost online sales, and enhance customer satisfaction.

## UX

## User Stories

### Guest User

- As a guest user, I want the option of an easy and straightforward registration process.

- As a guest user, I want to browse the product catalog without needing to create an account.

- As a guest user, I want to search for specific golf products easily.

- As a guest user, I want to filter products by categories such as clubs, shoes, or bags.

- As a guest user, I want to view detailed product descriptions, including images and ratings.

- As a guest user, I want to add items to my shopping cart without creating an account.

- As a guest user, I want to make a purchase by summitting my details and using a secure checkout process.

- As a guest user, I want to receive an order confirmation email after completing a purchase.

- As a guest user, I want to contact the store through a "Contact Us" page if I have any questions.

- As a guest user, I want to access a FAQ section to find answers to common questions about products and services.

### Registered User

- As a registered user, I want to log into my account to access personalized features.

- As a registered user, I want to save items to a wishlist to view or purchase later.

- As a registered user, I want to view my order history to track previous purchases.

- As a registered user, I want to save my shipping information for faster checkouts.

- As a registered user, I want to update my account information, including my address.

- As a registered user, I want to receive an order confirmation email after completing a purchase.

### Super User

- As a super user, I want to easily add new products so that I can keep the product offerings up to date.

- As a super user, I want to edit existing products to update details like prices, descriptions and images to ensure accurate information is available to customers.

- As a super user, I want to delete products to remove items that are no longer available for sale.

\
&nbsp;
[Back to Top](#welcome-to-the-golfshop)
\
&nbsp;

## Design

### Colours 

![Coolors](/documentation/features/pp5-coolors.png)

I used the colours above which mainly consist of the bootstrap colour classes, see details below:

- 007BFF: bg-primary and btn-primary classes, used in navigation bar and for primary action buttons.
- 555C63: site body font colour.
- FFFFFF: btn-white class, background colour of shadow boxes.
- F3EDED: body backgroud colour, good contrast with white shadow boxes. 
- 000000: text-black class, font colour in navigation bar.
- F8F9FA: bg-light, footer background colour for good text contrast.  
- 6C757D: btn-seconday, used for secondary action buttons like returning back to products page.
- 0000FF: footer links and complete order button for emphasis and sharper contrast.

\
&nbsp;
[Back to Top](#welcome-to-the-golfshop)
\
&nbsp;

### Fonts

I have used the default font families provided by Bootstrap for different devices and browsers. This ensures optimal readability and a consistent look. Below is a list of the default fonts depending on the device and browser used: 

font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, "Noto Sans", "Liberation Sans", sans-serif, "Apple Color Emoji", "Segoe UI Emoji", "Segoe UI Symbol", "Noto Color Emoji".

### Icons

I have used the [Font Awesome library](https://fontawesome.com/ "Font Awesome") for the icons throughout the website and [Favicon generator](https://favicon.io/favicon-converter/ "Favicon") for the browser tab icon.

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
[Back to Top](#welcome-to-the-golfshop)
\
&nbsp;

### Wireframes

The wireframes include the site's main pages to showcase the overall design and layout. The allauth templates, used for user authentication, have been styled in a similar theme to ensure consistency across the entire website.

<details><summary>Mobile Wireframes</summary>

<br>

**Home Page**

![Home](/documentation/wireframes/home-page-mobile.png)

<br>

**Products Page**

![Products](/documentation/wireframes/product-page-mobile.png)

<br>

**Product detail Page**

![Product detail](/documentation/wireframes/product-details-page-mobile.png)

<br>

**Cart Page**

![Cart](/documentation/wireframes/cart-page-mobile.png)

<br>

**Checkout Page**

![Checkout](/documentation/wireframes/checkout-page-mobile.png)

<br>

**Contact Us Page**

![Contact](/documentation/wireframes/contact-us-mobile.png)

<br>

**FAQ Page**

![FAQ](/documentation/wireframes/faq-mobile.png)

</details>

<br>

<details><summary>Desktop Wireframes</summary>

<br>

**Home Page**

![Home](/documentation/wireframes/home-page.png)

<br>

**Products Page**

![Products](/documentation/wireframes/product-page.png)

<br>

**Product details Page**

![Product details](/documentation/wireframes/product-details-page.png)

<br>

**Cart Page**

![Cart](/documentation/wireframes/cart-page.png)

<br>

**Checkout Page**

![Checkout](/documentation/wireframes/checkout-page.png)

<br>

**Contact Us Page**

![Contact](/documentation/wireframes/contact-us-page.png)

<br>

**FAQ Page**

![FAQ](/documentation/wireframes/faq-page.png)

</details>

\
&nbsp;
[Back to Top](#welcome-to-the-golfshop)
\
&nbsp;

### Database Schema

![Database schema](/documentation/database/database.png)

**User model**

Represents the users of the application. Each user has a unique username and email, along with a hashed password for authentication. It has a One-to-One relationship so each user has a corresponding UserProfile.

**UserProfile model**

Maintains default delivery information and order history for a user. It allows storing additional details related to a user beyond the basic authentication information. It has a One-to-One relationship with user model and also a One-to-Many relationship with orders so a user can have multiple orders.

**Category model**

Represents product categories, allowing for better organization and classification of products in the shop. It has a One-to-Many relationship so multiple products associated with each category.

**Product model**

Represents items available for sale in the shop. Each product is categorized and can have associated attributes such as size and price. It has a One-to-One relationship with a category so each product is associated with a single Category. It also has a One-to-Many relationship with order line item and wishlist item so a product can be linked with multiple order line items and user wishlists.

**Order model**

Represents a customer's order, containing all necessary information for processing and delivery. It includes customer details and the order's total amounts. It has Many-to-One relationship with user profile so multiple oreders can be linked to a user profile or null for a guest user. It also has a One-to-Many with order line item so an order can have multiple products.

**OrderLineItem model**

Represents a specific product included in an order. It includes information on product size, quantity, and the total price for that line item. It has a Many-to-One relationship so each order line item is linked to a single order and product.

**Contact model**

Represents a contact request made by users to the application. It stores the user's name, email, and their message. It operates independently without relationships to other models.

**Wishlist model**

Represents a user's wishlist, which can hold multiple products. It allows users to save items for future consideration. It has a One-to-One relationship so it is Linked to a single UserProfile.

**WishlistItem model**

Represents a specific product in a user's wishlist. It tracks when the item was added. It has a Many-to-One relationship so each wishlist item is linked to a single Wishlist and each wishlist item is linked to a single Product.

**FAQ model**

Represents frequently asked questions along with their answers. This helps users find information quickly. It operates independently without relationships to other models.

\
&nbsp;
[Back to Top](#welcome-to-the-golfshop)
\
&nbsp;
    
### Agile Methodology

#### Overview

I used Agile methodology to plan my project. It allowed me to break down the project into smaller manageable clear tasks. It made it easier to prioritize tasks, to track progress and to maintain momentum during development. 

#### Epics & Milestones

My project is made up of several Epics which are large bodies of work that can be broken down into smaller, more manageable tasks. They provide an overview of the main functionalities to deliver, there are ten milestones associated to the projects Epics. For my project, the Milestones with associated Epics, stories and tasks can be viewed at the links below:

- [Milestone 1 - Initial Set Up](https://github.com/KevinFlanagan7/PP5-Golf-Shop/milestone/1)

- [Milestone 2 - Homepage creation](https://github.com/KevinFlanagan7/PP5-Golf-Shop/milestone/2)

- [Milestone 3 - Product setup, filtering and searching](https://github.com/KevinFlanagan7/PP5-Golf-Shop/milestone/3)

- [Milestone 4 - Shopping cart setup](https://github.com/KevinFlanagan7/PP5-Golf-Shop/milestone/4)

- [Milestone 5 - Heroku deployment](https://github.com/KevinFlanagan7/PP5-Golf-Shop/milestone/5)

- [Milestone 6 - Checkout app and stripe payment setup](https://github.com/KevinFlanagan7/PP5-Golf-Shop/milestone/6)

- [Milestone 7 - Profile app, Wishlist app and Product Admin setup](https://github.com/KevinFlanagan7/PP5-Golf-Shop/milestone/7)

- [Milestone 8 - Page Footer setup](https://github.com/KevinFlanagan7/PP5-Golf-Shop/milestone/8)

- [Milestone 9 - User-Friendly Website Styling](https://github.com/KevinFlanagan7/PP5-Golf-Shop/milestone/10)

- [Milestone 10 - README documentation and Testing](https://github.com/KevinFlanagan7/PP5-Golf-Shop/milestone/11)

\
&nbsp;
[Back to Top](#welcome-to-the-golfshop)
\
&nbsp;

#### Github Project

The Github projects tool was used to implement Agile development practices efficiently. By using Kanban boards, tasks were visually managed and tracked through various stages of completion. The MoSCoW (Must have, Should have, Could have & Won't have) method was used to prioritize features and tasks, view below links to the project's Kanban board and MoSCoW prioritization method:

- [Kanban board](https://github.com/users/KevinFlanagan7/projects/6)

- [MoSCoW Prioritization](https://github.com/KevinFlanagan7/PP5-Golf-Shop/issues?q=is%3Aissue+is%3Aclosed)

\
&nbsp;
[Back to Top](#welcome-to-the-golfshop)
\
&nbsp;

## SEO (Search Engine Optimization)
To optimize the visibility of the Golf Shop in search engine results, the following SEO strategies have been implemented:

- **Meta** Tags: Included detailed meta descriptions and meta keywords to improve relevance in search results. The keywords include both short and long-tail terms, such as:

    - Short-tail: "golf shop," "golf clubs," "golf shoes"
    - Long-tail: "premium golf clubs for sale," "Titleist GT golf drivers online," "buy Adidas golf shoes with fast shipping"

- **Sitemap**: A sitemap.xml file has been generated to help search engines efficiently crawl the site. It includes URLs   for all key pages like product categories (e.g., drivers, bags, shoes), individual product listings, and informational pages such as contact and FAQ.

- **robots.txt**: A robots.txt file has been added to control search engine crawlers' access, allowing them to index the most important pages while avoiding less relevant content, like certain backend files or administrative URLs.

- **Semantic HTML**: The use of semantic HTML elements like `<header>`, `<nav>`, `<section>`, and `<footer>` helps search engines understand the structure of the page better, also including detailed `alt` description for images improves accessibility and SEO ranking. By clearly defining sections of content, these tags help search engines identify important content like product details, navigation menus, and footers, boosting the chances of appearing in relevant search queries.

By utilizing these SEO techniques and following semantic HTML best practices, the site is designed to improve its visibility in search engines for users searching for golf equipment, leading to better rankings and increased traffic.

## Marketing

The Golf shop is a B2C (business-to-consumer) business, focused on providing high-quality golf equipment directly to individual customers. Several marketing tools and strategies have been implemented to enhance the customer experience, engage with visitors, and build brand loyalty.

- **Mailchimp Newsletter Sign-Up**: A newsletter sign-up form is integrated in the site’s footer using Mailchimp. This allows visitors to subscribe easily to potentially receive updates about new product releases and exclusive deals.

- **Facebook Page**: The Golf Shop connects with customers on social media via its dedicated Facebook page. This platform is used to engage with the golf community, post updates about new arrivals and promote content. By interacting with followers on Facebook, the shop builds brand awareness and developes an active customer base. The `rel="noopener external"`attribute is added to link for the golf shop's site security and tells search engines that the site is external.

    <details><summary>Facebook page</summary>

    <br>

    ![Facebook page](/documentation/features/facebook-page.png)

<br>

- **Privacy Policy**: A detailed privacy policy is included to inform customers about how their personal data is collected, used, and protected. This ensures compliance with privacy laws and builds trust with visitors, assuring them that their information, particularly email addresses gathered via the Mailchimp newsletter, is handled securely.

- **Contact Us and FAQ Links**: The footer contains helpful links to the Contact Us page and FAQ section, providing direct access to customer service and commonly asked questions. These links enhance the user experience by offering clear paths for support and additional information, making it easy for customers to reach out for assistance or find answers to product-related queries.

## Features

### Guest user features

<details><summary>Home page</summary>

<br>

The home page includes three sectioms, the header, the main landing page and the footer section, details below:

**Header**

![header](/documentation/features/header.png)

- The header is part of the base.html template, it contains the GOLFshop name and logo which links back to home page. 

- Product navigation links and a search product functionality field.

- A My Account dropdown menu to give the user the option to register an account or login if already registered.

- A cart icon which links to the cart page and updates total when products are added.

<br>

![Header mob](/documentation/features/header-mobile.png)

- For smaller screen sizes the logo, navigation links and search field collaspe down to dropdown menues.

<br>

**Landing**

![Landing page](/documentation/features/landing-page.png)

- The main landing page content is the index.html template, it contains the hero image advertising latest product and links to all products page.

- The four images below the hero image are site products which link to the four product categories.

<br>

![Landing mobile](/documentation/features/landing-mobile.png)

- The category images reduce down to a row of two for smaller screen size so the site is responsive for all screen sizes.

<br>

**Footer**

![Footer](/documentation/features/footer.png)

- The footer is also part of the base.html template and contains two sections, the mailchimp news letter subscription and the information section.

- The Information section has links to the sites facebook page, a contact us form, FAQ page and the sites privacy policy

<br>

![Footer mobile](/documentation/features/footer-mobile.png)

- Again for smaller screen sizes the footer reduces down to one column to maintain responsiveness.

</details>

<br>

<details><summary>Products page</summary>

<br>

![Products](/documentation/features/products.png)

- The products page lists all the products on the site.

- It includes the product iamge, name, price, category and rating.

- A back to the top button is available so the user can easily come back to the top of the page after scrolling down through products.

- The links in the header filters the products down to their category and displayes either drivers, bags, irons or shoes.

<br>

![Products mobile](/documentation/features/products-mobile.png)

- The products page reduces down to one column for smaller screen sizes.

</details>

<br>

<details><summary>Product details page</summary>

<br>

![Products detail](/documentation/features/product-details.png)

- Product details page give a more detailed description of the product.

- A quantity selector field and the option to add to your cart for purchase.

- A back to products page option if user does not want to purchae product.

![Shoe sizes](/documentation/features/product-details-shoes.png)

- Shoe products gives a dropdown option to select a size.

<br>

![Products detail mobile](/documentation/features/product-details-mobile.png)

- The product details page reduces down to one column for smaller screen sizes.

</details>

<br>

<details><summary>Cart page</summary>

<br>

![Cart](/documentation/features/cart.png)

- Displays list of products in the cart

- Option to update quantity or remove product from the cart.

- Displays the subtotal and grand total of the cart.

- Option to proceed to secure checkout or navigate back to products to continue shopping.

<br>

![Cart mobile](/documentation/features/cart-mobile.png)

- The cart page reduces down to one column for smaller screen sizes.

</details>

<br>

<details><summary>Checkout page</summary>

<br>

![Checkout](/documentation/features/checkout.png)

- Provides a checkout form for the user to provide contact and shipping details.

- Links to create an account or login so details in the form can be saved.

- Displays the order summary and total cost.

- Option to enter card details and complete order with a message informing user the amount card will be charged.

<br>

![Checkout mobile](/documentation/features/checkout-mobile.png)

- The checkout page reduces down to one column for smaller screen sizes.

</details>

<br>

<details><summary>Checkout success page</summary>

<br>

![Checkout success](/documentation/features/checkout-success.png)

- Displays the order summary, a Thank you message and that a confirmation email will be sent to the address entered on the checkout form.

- Option to go Back to products if the user wants to continue shopping.

<br>

![Checkout success mobile](/documentation/features/checkout-success-mobile.png)

- The checkout success page reduces down to one column for smaller screen sizes.

</details>

<br>

<details><summary>Contact Us page</summary>

<br>

![Contact Us](/documentation/features/contact.png)

- Provides fields for the user to enter name, email and message to send to the GOLFshop email address.

</details>

<br>

<details><summary>FAQ page</summary>

<br>

![FAQ](/documentation/features/faq.png)

- Displays list of FAQs and answers.

</details>

<br>

<details><summary>Privacy Policy page</summary>

<br>

![Privacy](/documentation/features/privacy.png)

</details>

\
&nbsp;
[Back to Top](#welcome-to-the-golfshop)
\
&nbsp;

### Registered user features

<details><summary>Registration pages</summary>

<br>

**Registration page**

![Register](/documentation/features/registration.png)

**Verify email page**

![Verify](/documentation/features/verify-email.png)

**Confirm email page**

![Confirm](/documentation/features/confirm-email.png)

**Log in page**

![Login](/documentation/features/login.png)

- When the registration form is completed and the user clicks sign up an email is sent to the entered email address and the user is directed to the verify email page.

- When the user clicks on the link provided in the email they are directed to the confirm email page.

- When the user clicks on confirm they are directed to the login page where they now can enter their details and log in to the site.

**Forgot password page**

![Forgot](/documentation/features/forgot-password.png)

**Password reset page**

![Password reset](/documentation/features/password-reset.png)

**Change password page**

![Change password](/documentation/features/change-password.png)

**Password changed page**

![Password changed](/documentation/features/password-changed.png)

- When the user click on Forgot password link they are directed to to the password reset page with a message that a password reset email has been sent.

- When user clicks on link in email they are directed to the change password page.

- When new password is entered the user is direct to the Password changed page and they now can continue to the login and log in with new password.

</details>

Once a guest user completes registraion they have (along with all the guest features) the features below once logged in:

<details><summary>Home page</summary>

<br>

![Account options](/documentation/features/logged-in.png)

- Registered users once logged in now have access to the My Profile and My Wishlist page from the account menu.

- Also now has the option to log out.

</details>

<br>

<details><summary>Product details page</summary>

<br>

![Details](/documentation/features/product-details-reg.png)

- Page now has the add to wishlist button.

</details>

<br>

<details><summary>My Profile page</summary>

<br>

![My Profile](/documentation/features/profile-reg.png)

- Form to enter and update registered user details.

- List of order history displayed.

</details>

<br>

<details><summary>Checkout page</summary>

<br>

![Checkout](/documentation/features/checkout-reg.png)

- Checkout form populated with details entered in My Profile page.

- Option to save to profile if edited.

</details>

<br>

<details><summary>My Wishlist page</summary>

<br>

![My Wishlist](/documentation/features/wishlist.png)

- List of products that have been added from the product details page with the option to remove.

- When user clicks on wishlist product they are directed to that product's detail page.

</details>

<br>

<details><summary>Contact Us page</summary>

<br>

![Contact Us](/documentation/features/contact-reg.png)

- Username and email field populated with registration details.

- Registered users just have to type in their message and send.

</details>

<br>

<details><summary>Sign out page</summary>

<br>

![Sign out](/documentation/features/signout.png)

- Signs out user back to home page.

</details>

\
&nbsp;
[Back to Top](#welcome-to-the-golfshop)
\
&nbsp;

### Super user features

Along with having all the features of a guest and registered user, the super user also has the below features:

<details><summary>Home page</summary>

<br>

![Admin panel](/documentation/features/home-super.png)

- Super users now have access to the product admin page from the My account dropdoen menu.

</details>

<br>

<details><summary>Products page</summary>

<br>

![Products](/documentation/features/products-super.png)

- Edit and delete options in the products page.

</details>

<br>

<details><summary>Product details page</summary>

<br>

![Products](/documentation/features/product-details-super.png)

- Edit and delete options in the products details page.

</details>

<br>

<details><summary>Product Admin page</summary>

<br>

![Product Admin](/documentation/features/product-admin.png)

- Form to add a new product details and image.

</details>

<br>

<details><summary>Edit page</summary>

<br>

![Edit](/documentation/features/edit-admin.png)

- Form to edit product details and image.

</details>

<br>

<details><summary>Django Admin Panel</summary>

<br>

![Admin panel](/documentation/features/admin-panel.png)

- Super has full access to django admin panel.

</details>


### Message features

The project uses Django's built-in messaging framework to provide real-time feedback to users. These messages are used to display success, error and informational messages throughout the site after completeing an action. For example, when a user logs in, adds a product to the cart, completes a purchase, they receive immediate confirmation via on-screen notifications that displays in the top right corner of the site. See below examples:

<details><summary>Messages</summary>

<br>

**Login**

![log in](/documentation/messages/signin.png)

**Add to Wishlist**

![Wishlist](/documentation/messages/add-wishlist.png)

**Add to Cart**

![Cart](/documentation/messages/add-product.png)

- Add to cart message also includes cart content and option to checkout.

**Checkout**

![Checkout](/documentation/messages/checkout_success.png)

- Checkout message also includes order number and the provided email address the confirmation is sent too.

**Log out**

![Sign out](/documentation/messages/signout.png)

</details>

\
&nbsp;
[Back to Top](#welcome-to-the-golfshop)
\
&nbsp;

### Email features

The project includes email notifications for important actions such as order confirmations, contact form submissions and email verification during user registration. A dedicated Gmail address of 
thegolfshop2024@gmail.com was created for the project to handle outgoing and incoming emails. Registered users receive a verification email when signing up, ensuring the authenticity of their accounts before they can fully access the site's features. This enhances security and user experience. See below examples:

<details><summary>Emails</summary>

<br>

**Confirm email**

![Confirm](/documentation/messages/confirm-email.png)

**Order confirmation email**

![Order](/documentation/messages/order-email.png)

**Contact Us email**

![Contact email](/documentation/messages/contact-us-email.png)

</details>

### Validation features

The project implements validation for user inputs both on the frontend and backend. For example, quantity input fields are validated in both, see below examles:

<details><summary>Validation</summary>

<br>

**Quantity buttons disabled at 1 and 99**

![Disabled](/documentation/validation/disabled-1.png)

![Disabled](/documentation/validation/disabled-99.png)

**Input manually entered by user**

![Manual](/documentation/validation/frontend-validation-neg.png)

![Manual](/documentation/validation/frontend-validation.png)

**If frontend HTML input min and max deleted by user**

![Backend](/documentation/validation/backend-html.png)

**Input field deleted**

![Deleted](/documentation/validation/backend-input-empty.png)

</details>

### Defensive design features

This project is designed with user experience and data integrity in mind, applying defensive design principles to ensure a secure site. It includes a delete confirmation modal that prompts super users to confirm deletion actions to prevent accidental deletions. Additionally, the project handles authorization by redirecting attempts to access restricted URLs based on user status. It also features custom error pages that display friendly message for broken links.

<details><summary>Defensive design</summary>

<br>

**Confirm deletion modal**

![Delete modal](/documentation/features/products-delete-modal.png)

**Unauthorized URLs errors**

![Disabled](/documentation/validation/urls-error.png)

**404.html error page**

![404 error](/documentation/validation/404error.png)

</details>

## Features to be Implemented

Below are a list of features to be implemented in the future:

- Integrate social media account login to provide users with a faster, more convenient way to register and log in to the site.

- Add functionality for users to leave reviews, providing valuable feedback and enhancing the shopping experience for future customers.

- Implement a discount code feature where users can apply promotional codes to receive discounts on their purchases during checkout.

\
&nbsp;
[Back to Top](#welcome-to-the-golfshop)
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

### Python Libraries

- [Django-allauth](https://docs.allauth.org/en/latest/)
- [Crispy Forms](https://django-crispy-forms.readthedocs.io/en/latest/)
- [Django Countries](https://pypi.org/project/django-countries/)
- [Pillow](https://pypi.org/project/Pillow/)
- [django-storages](https://django-storages.readthedocs.io/en/latest/)

\
&nbsp;
[Back to Top](#welcome-to-the-golfshop)
\
&nbsp;

### Database

- [PostgreSQL from Code Institute](https://dbs.ci-dbs.net/)

### Tools

- [Python Validator](https://pep8ci.herokuapp.com/)
- [W3C HTML Validation Service](https://validator.w3.org/ "W3C HTML")
- [W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/ "W3C CSS")
- [JShint Validation Service](https://jshint.com/ "JSHint")
- [Heroku](https://dashboard.heroku.com/apps)
- [Balsamic](https://balsamiq.com/wireframes/ "Balsamic")
- [Lighthouse](https://developer.chrome.com/docs/lighthouse/overview "Lighthouse")
- [Coolers](https://coolors.co/ "Coolers")
- [Favicon Converter](https://favicon.io/favicon-converter/ "Favicon Converter")
- [Font Awesome library](https://fontawesome.com/ "Font Awesome")
- [dbdiagram](https://dbdiagram.io/home/ "dbdiagram")
- [Stripe](https://stripe.com/en-gb-nl)
- [Amazon Web Service S3](https://aws.amazon.com/s3/)

\
&nbsp;
[Back to Top](#welcome-to-the-golfshop)
\
&nbsp;

## Testing

Testing summary and results can be found in [TESTING.md](TESTING.md) file.

## Deployment

### AWS configuration

Golfshop uses Amazon Web Services (AWS) to store static and media files securely in the cloud, it was setup by following the steps below:

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
    
    -   Click "Review Policy" and name it, then click "Create Policy."

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

### Stripe

The GOLFshop uses Stripe as its primary payment system to securely process e-commerce transactions, it was setup by following the steps below:
    
-   Go to [stripe.com](https://stripe.com) and create an account. Log in to your Stripe dashboard.
    
-   From your Stripe dashboard, locate the "API Keys" section under "Developers."
    -   Retrieve the following keys:
        -   **STRIPE_PUBLIC_KEY**: Your Publishable Key (starts with `pk`)
        -   **STRIPE_SECRET_KEY**: Your Secret Key (starts with `sk`)

-   These keys will be used to authenticate your application with Stripe.
    
-   To handle scenarios where a user may close the payment page prematurely, set up Stripe Webhooks to receive real-time payment updates.

- In your Stripe dashboard:
    -   Navigate to "Developers" and select "Webhooks."
    -   Click "Add Endpoint."
    -   Enter your endpoint URL (e.g., `https://pp5-golf-shop-a06971bbe403.herokuapp.com/wh/`).
    -   Select "Receive all events" to capture all relevant payment events.
    -   Click "Add Endpoint" to complete the process.

- This will generate a new key:
    -   STRIPE_WH_SECRET: Your Webhook Signing Secret.

- Configure settings.py with Stripe settings and add keys to config vars on Heroku.

**Testing Payments**
    
-   Stripe provides a test mode to simulate payment transactions.

-   Use the following test card details for interactive testing:
    -   **Card Number:** `4242 4242 4242 4242`
    -   **Expiry Date:** Any valid future date
    -   **CVC:** Any three-digit number
    -   **Other Fields:** Use any value for other fields.

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
[Back to Top](#welcome-to-the-golfshop)
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
[Back to Top](#welcome-to-the-golfshop)
\
&nbsp;

## Credits

My mentor For help and advice:

- [Simen Daehlin](https://github.com/Eventyret "Simen Daehlin")

Code inspiration:

- [LMS and PP5 Walkthrough Project from Codeinstitute](https://codeinstitute.net "Boutique Ado")

For all media images:

- [Pinterest](https://ie.pinterest.com/pin/72057662781606958/ "Pinterest")

\
&nbsp;
[Back to Top](#welcome-to-the-golfshop)
\
&nbsp;