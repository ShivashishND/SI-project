# Introduction

This application makes use of few of the computer vision API's provided by Azure.

Mainly we will look at 3 different API's :

- Object detection in an image
- Image description
- Text reading from an image

[Server URL](http://159.89.94.37:5000) - URL where the application is deployed. This is just the homepage, in order to use the project you would need to use one of the below provided endpoints.

[API Documentation](http://159.89.94.37:5000/api/docs/) - For all the response types of the endpoints and technical documentation using Swagger.

Tools needed to use the application :
[Postman](https://www.postman.com/s)

## Object detection in an Image

- Description - Given an URL of the image, this api would return all the objects in that image.
- API Endpoint - http://159.89.94.37:5000/detect
- Method Type - POST
- How to run:
  - Open Postman
  - Paste the above API Endpoint
  - In the body, choose raw/json format
  - Paste the following :
  ```
  {"url":"https://img.freepik.com/free-photo/close-up-shot-surprised-pleased-bearded-man-holds-burger-piece-pizza-eats-junk-food-doesnt-care-about-health-nutrition-wears-spectacles-neat-jumper_273609-51240.jpg?w=2000"}
  ```
  - You will get an output :
  ```
  [
    "Hamburger",
    "person"
  ]
  ```
- Similarly you can pick any image url and it would try to detect objects inside the image.
- For an incorrect url or incorrect image format, it would return

```
Not a valid image
```

- If the service is not able to detect any objects, it would return

```
No objects detected
```

## Image description

- Description - Given an URL of the image, this api would return its description.
- API Endpoint - http://159.89.94.37:5000/describe
- Method Type - POST
- How to run:
  - Open Postman
  - Paste the above API Endpoint
  - In the body, choose raw/json format
  - Paste the following :
  ```
  {"url":"https://plus.unsplash.com/premium_photo-1661567408466-27899e8a4a2f?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxzZWFyY2h8MXx8Y2hpbGRyZW4lMjBwbGF5aW5nfGVufDB8fDB8fA%3D%3D&w=1000&q=80"}
  ```
  - You will get an output :
  ```
  a group of children playing in the sand
  ```
- Similarly you can pick any image url and it would try to describe whats happening in the image.
- For an incorrect url or incorrect image format, it would return

```
Not a valid image
```

## Text reading from an image

- Description - Given an URL of the image, this api would read the text from it.
- API Endpoint - http://159.89.94.37:5000/read_text
- Method Type - POST
- How to run:
  - Open Postman
  - Paste the above API Endpoint
  - In the body, choose raw/json format
  - Paste the following :
  ```
  {"url":"https://i.stack.imgur.com/i1Abv.png"}
  ```
  - You will get an output :
  ```
  It was the best of times, it was the worst of times, it was the age of wisdom, it was the age of foolishness...
  ```
- Similarly you can pick any image url and it would try to read whats written in the image.
- For an incorrect url or incorrect image format, it would return

```
Not a valid image
```

- If the service is not able to read any text, it would return

```
Could not detect any text
```
