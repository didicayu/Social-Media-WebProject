# First Deliverable - Social Media Project
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
#### The link below allows to clone the repository using the following command (link)
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
