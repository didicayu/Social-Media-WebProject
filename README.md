# Final Deliverable - Social Media Project
Our project aims to explore the relationship between social media engagement and consumer behavior. By analyzing interactions between users, brands, and products/services, we intend to understand how social media influences purchasing decisions.

The data model depicts three main entities: Social Media Users (with their interactions), Brands/Companies, and Products/Services, with various relationships among them. Users engage with multiple brands and products/services, while brands target multiple users and offer various products/services.

We will utilize APIs from social media platforms to collect relevant data. This data will enable us to analyze user interactions, brand mentions, and product/service reviews, providing insights into the impact of social media on consumer behavior.

## *Execution Guide*
### Follow the next steps to correctly launch the project application
### -Prerequisites
Before you begin, ensure you have the following installed on your system:  
[Docker Desktop](https://www.docker.com/products/docker-desktop/)  
[Git](https://git-scm.com/downloads)

### -Deployment
#### 1. Download or Clone the github Repository  
If you choose to download, check for the _**code**_ button and select Download ZIP and extract it in your desired directory  

An easiest way is to directly clone the github project, then choose the directory you want the project to be cloned and clone it from git:  
```bash
$ git clone https://github.com/didicayu/Social-Media-WebProject.git
```
#### The link below allows to clone the repository using the previous command 
[Social-Media-WebProject](https://github.com/didicayu/Social-Media-WebProject.git)

#### 2. Build and Start Docker Containers
Navigate to your project directory and compose the Docker image:
```bash
$ docker-compose up -d
```
###### This will ensure to fullify all the requirements to run the application
#### 3. The application should be launched correctly
You can check it out by navigating in a browser at: <http://localhost:8000>  
To check the admin page you can visit <http://localhost:8000/admin>

#### 4. Terminate the aplication
After your work is done you can shutdown the docker compose using:
```bash
$ docker-compose down
```
And the application should be correctly finalized
### -Alternatively, you can start it in local
```bash
$ python3 -m venv .venv
```
```bash
$ source .venv/bin/activate       (LINUX)
$ source .venv\Scripts\activate   (WINDOWS)
```
```bash
$ pip install poetry
```
```bash
$ poetry install
```
```bash
$ poetry run python manage.py runserver
```


## *Data Model*

### BrandCompany

- **Attributes:**
  - `name` (CharField): The name of the brand or company. Maximum length: 100.
  - `industry` (CharField): The industry to which the brand or company belongs. Maximum length: 100.

### ProductService

- **Attributes:**
  - `name` (CharField): The name of the product or service. Maximum length: 100.
  - `category` (CharField): The category or type of the product or service. Maximum length: 100.
  - `company` (ForeignKey): Links to a `BrandCompany` instance, representing the company that offers this product or service.

### SocialMediaPost

- **Attributes:**
  - `content` (TextField): The content of the post.
  - `likes` (IntegerField): The number of likes the post has received. Default: 0.
  - `shares` (IntegerField): The number of shares the post has received. Default: 0.
  - `comments` (IntegerField): The number of comments the post has received. Default: 0.
  - `timestamp` (DateTimeField): The timestamp of when the post was created. Automatically set to the current timestamp.
  - `user` (ForeignKey): Represents the user who created the post.
  - `product` (ForeignKey): Links to a `ProductService` instance, representing the product or service mentioned in the post. This field is optional (`null=True`), allowing for posts that may not be directly related to a specific product or service. When a product is deleted, any posts linked to it will also be removed (`on_delete=models.CASCADE`).
### UserInteraction

- **Attributes:**
  - `INTERACTION_CHOICES` (list): Choices for types of interactions.
  - `user` (ForeignKey): Represents the user who interacted with the post.
  - `post` (ForeignKey): Represents the post being interacted with.
  - `interaction_type` (CharField): The type of interaction (like, comment, share). Maximum length: 10.
  - `timestamp` (DateTimeField): The timestamp of the interaction. Automatically set to the current timestamp.

## *First Deliverable Design Considerations*
1. For testing and evaluation purposes, a superuser has already been created.
You can log in as superuser by:

   -**User**: root
   
   -**Password**: root

2. **Consistency Across Pages**: We ensure consistency in design elements like color schemes, typography, and layout across all pages for a cohesive user experience.

3. **User Authentication**: We implement a user authentication system, providing a personalized experience for logged-in users while also offering clear prompts and calls-to-action for those who are not logged in.

4. **Form Validation**: We include form validation to ensure that users provide accurate and complete information during the signup process, enhancing data integrity and user experience.

## *Agile Behaviour Driven Development (BDD)*

The aim of this application is to help users keep track of social media interaction and posts. 

- **Features:**
  - `Register Company`
  - `Register Product` 
  - `Create Post` 
  - `Create User Interaction` 
  - `Edit Company` 
  - `Edit Product` 
  - `Edit Post` 
  - `Remove Company` 
  - `Remove Product` 
  - `Remove Post` 
  - `Remove Interaction`
  
To execute the tests, you can use:
```bash
$ python manage.py behave
```
Or alternately
```bash
$ poetry run manage.py behave
```
The result is the following list of feature files with their corresponding content in the features/ folder:
- **Content**
  - `register_company.feature`    
  Feature: Register Company    
  In order to keep track of the companies registered   
  As a user   
  I want to register a company together with its industry type   
  - `register_product.feature`  
  Feature: Register Product   
  In order to keep track of the products registered  
  As a user  
  I want to register a product together with its category and company type  
  - `create_post.feature`  
  Feature: Create Post  
  In order to keep track of the posts created  
  As a user  
  I want to create a post  
  - `create_user_interaction.feature`  
  Feature: Create Interaction  
  In order to keep track of the interactions created  
  As a user  
  I want to create an interaction  
  - `edit_company.feature`  
  Feature: Edit Company  
  In order to keep track of the companies registered  
  As a user  
  I want to edit a company  
  - `edit_product.feature`  
  Feature: Edit Product  
  In order to keep track of the products registered  
  As a user  
  I want to edit a product  
  - `edit_post.feature`  
  Feature: Edit Post    
  In order to keep track of the posts registered    
  As a user    
  I want to edit a post  
  - `remove_company.feature`  
  Feature: Remove Company  
  In order to remove the companies registered  
  As a user  
  I want to remove a company together with its industry type  
  - `remove_product.feature`  
  Feature: Remove Product  
  In order to keep track of the companies registered  
  As a user  
  I want to edit a company  

  - `remove_post.feature`  
  Feature: Remove Post  
  In order to keep track of the Posts registered  
  As a user  
  I want to remove a post  

  - `remove_interaction.feature`  
  Feature: Remove Interaction  
  In order to keep track of the interactions registered  
  As a user  
  I want to edit an interaction  



## Model Changes Overview

In the recent update of our application, we've made several significant changes to our data models to enhance functionality and streamline data relationships. Here's a brief overview of these changes:

1. **Company Association in ProductService**: We've added a `company` field to the `ProductService` model. This change allows each product or service to be directly linked to a specific brand or company, facilitating easier tracking and management of products under their respective companies.

2. **Product Relationship in SocialMediaPost**: Previously, the relationship between products and social media posts was managed through a ManyToMany relationship. We've simplified this by changing the `product` field in the `SocialMediaPost` model to a ForeignKey. Now, each post is linked to a single product or service.

3. **Removal of SocialMediaUser Model**: The `SocialMediaUser` model has been removed from our data structure. This decision was made to streamline our user management process by utilizing Django's built-in `User` model for handling user data, thereby reducing redundancy and simplifying our data model.


## Creating New Instances: Step-by-Step Guide

Our application is designed to follow a specific order when creating new instances, ensuring data integrity and logical relationships between entities. Here's the recommended sequence:

1. **BrandCompany**: First, create a `BrandCompany` instance. This is essential as products and posts are associated with companies.

2. **ProductService**: After establishing a company, you can create a `ProductService` instance. Each product must be linked to a previously created company.

3. **SocialMediaPost**: With companies and products set up, you can now create `SocialMediaPost` instances. These posts can reference both the products and the companies they are related to.

4. **UserInteraction**: Finally, `UserInteraction` instances can be created. These are interactions (like, comment, share) that users have with the social media posts.

Following this order ensures that all entities are correctly linked and that the data reflects the real-world relationships between companies, products, and user interactions.

## API Integration: Reddit Topic Search Posts

Our application now includes a powerful feature that allows users to search for topics across Reddit. This functionality enables users to explore the top 10 subreddits related to a specific topic of interest. Here's how it works:

1. **Topic Search**: Users can enter a topic into the search bar. The application then queries Reddit's API to find subreddits that match the entered topic.

2. **Display Results**: The search results are displayed on a dedicated page, listing the top 10 matching posts from the selected subreddit. This page provides an overview of each post, including its title and a brief description.

3. **Integration with Database**: Alongside viewing the subreddit information, users have the option to integrate selected data into our application's database. This means that any interesting posts found within these subreddits can be saved directly as posts in our application.

4. **Creating Posts**: For each selected subreddit post, users can click a "Save Post" button. This action saves the post's content, along with its metadata (such as likes and comments), into our database as a new post. 

5. **Redirection**: After saving a post, users are redirected to the "Home" page, where they are greeted with a success message confirming that the post has been saved.

****About Reddit API Credentials**** 

API Key and Secret, Username and all necessary information to access the Reddit API are stored in the .env file  which is attached in the task assignment at Campus Virtual. This file is not included in the repository for security reasons.

## RDFa Update in User Interaction Template

### Overview

In this update, RDFa (Resource Description Framework in Attributes) annotations have been added to the HTML template used to display user interaction details. This enriches the data with semantic metadata, enhancing its accessibility and understanding for both humans and machines.

### Changes Made

1. **Incorporation of schema.org vocabularies:**
   - The `schema.org` vocabulary has been added with the type `UserInteraction` to provide a semantic context to the user interaction data.

2. **Specific Properties:**
   - The following RDFa properties have been introduced to enrich the data:
     - `performer` for the user.
     - `director` for the creator of the interaction.
     - `name` for the content of the post.
     - `description` for the type of interaction.
     - `startDate` for the timestamp.
     - `location` for the origin of the post.

### Code Example

**Before:**
```html
<p><strong>User:</strong> {{ user }}</p>
<p><strong>Creator:</strong> {{ interaction.user }}</p>
````

**After:**
```html
<p><strong>User:</strong> <span property="performer">{{ user }}</span></p>
<p><strong>Creator:</strong> <span property="director">{{ interaction.user }}</span></p>
````

This update enhances the semantic clarity and machine-readability of user interaction data by leveraging the power of RDFa and schema.org vocabularies.
And we can check it's effectiveness by passing the tests:
![Google Test](https://imgur.com/zJ2UjyY.png)
![Schema test](https://imgur.com/hwNOI4h.png)
![Schema tree](https://imgur.com/72lrIDR.png)
