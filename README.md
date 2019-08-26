## Project Name
- GalleryPics

## Project Author(s)
#### Daniel Muthui

## Description

A personal gallery application that enables the administrator to post images to the websites, users are able to see the images nd copy link for download. A user clicks on an image to view details.
## User Stories
-As a user of the application I should be able to:

1. View different photos that interest me.
2. Click on a single photo to expand it and also view the details of the photo. The photo details must appear on a modal within the same route as the main page.
3. Search for different categories of photos. (ie. Travel, Food)
4. Copy a link to the photo to share with my friends.
5. View photos based on the location they were taken.

## Cloning and running
Clone the application using git clone. In the terminal:

  ```  $ git clone https://github.com/sanii-muthui/Gallery```
  
  ```  $ cd Django-images```

## Creating the virtual environment

  ```  $ python3.6 -m venv virtual```
  
  ```  $ source virtual/bin/env```
  
  ```  $ curl https://bootstrap.pypa.io/get-pip.py | python```



## Testing the Application
To run the tests for the class file:
Run  python3.6 manage.py test imageapp


## Behavior Driven Development

| Behaviour                                           | Input                            | Output                                 |
| :-------------------------------------------------- | :--------------------------------|:---------------------------------------|
|View images from Admin site                          |     Image is saved               | Displays Image from database           |
|Search form a category                               |Name of category                  |Display category                        |
|Show more info of image when toggle button is clicked|Click toggle button               |Display image details                   |
|Show image as per category                           |Click Category on nav-bar         |Display filtered images as [per category|


## Technologies Used
* Python
* Bootstrap
* WhiteNoise
* Django
* PostgreSQL Database
* JavaScript
* CSS

## Support and contact details

In need of support please reach me at 'muthuisanii@gmail.com' for any queries.

## License

IHUB LICENSE [Sanii-Muthui][2019]
