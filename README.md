# Image-Hashing-API
This is an Image Hashing API which accepts an image url and computes the md5 and phash for the image.
The phash and md5 codes are stored in a databse along with the url and image name. 
This api can be accesed at http://127.0.0.1:8000/api/ on your browser and can be interacted with on Postman.
On postman you can List/Create/Update/Delete image entries using the following endpoints:
For Creating an entry you will have to use this url "http://127.0.0.1:8000/api/images/create/?image_url=<imageurl>" and make sure the method is "GET".
For Listing all the entries: "images/" and make sure the method is "GET".
For Listing a particular entry: "images/(serial number of the entry)" and make sure the method is "GET".
For updating an entry "images/(serial number of the entry)/update/" and make sure the method is "PUT"/"PATCH".
For deleting an entry "images/(serial number of the entry)/delete/" and make sure the method is "DELETE".

Contributions are always welcome, If you'd like to contribute to this project, feel free to fork the repository and submit a pull request. Please ensure that your changes align with the code style of the project.
