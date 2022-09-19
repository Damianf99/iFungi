# iFungi

It is a moblie app for mushroom pickers created with the python Kivy module. This project was prepared for the univiersity subject - "Engineering Team Project". The project was divided into 3 pieces - main iFungi.py python file, my.kv kivy file (for GUI styling) and the model (which was too big to upload it here). I was fully responsible for the main python file iFungi.py and the related directories.

# Original description of the project

Each year, several dozen people die as a result of complications after eating poisonous mushrooms, and many more suffer from indigestion and other ailments. The subject of the project is the development of an appropriate mobile application that would be able to recognize the species of a given mushroom and warn against inedible and poisonous mushrooms.

As part of the work, it would be necessary to create a convenient mobile application containing:

- Automatic mushroom identification from the photo taken
- Ability to save the location of your favorite places
- Verifying the best location for mushroom picking
- An informative mushroom encyclopedia
- Possibility to test your knowledge in a mushroom quiz

# Libraries/Modules

- All the functions regarding kivy itself (buttons, layout, lists, etc.) were developed using kivy or kivymd modules. 
- To be able to connect with the MySQL database and to do operations - mysql module. 
- For collecting location cooridinates - geocoder module. 
- For processing the video stream and photos - cv2 module.
- For encrypting sensitive data (passwords) - hashlib module
- For sending and receiving information from the trained model engine - MultipartEncoder from requests_toolbelt module + json for formatting data.
- For receiving and sending requests - Flask module
- For training the model and all the other operations within the model porcessing - TensorFlow module

# Additional information

There are missing certain pieces of code due to the safety reasons. There were some encrypting parts and I didn't want to reveal these information because someone could have already used those ideas in their official projects. Unfortunately due to the enormous size of the model I was unable to provide the directory with the necessary model data. If you'd like to see the app itself - please take a look at the images below (or in the Screenshots directory) to have a little insight of the app and its functionalities. If requested - I might share the whole project depending on the reason.

# Screenshots

## Mushroom detecting:

<p align="center">
<img src="https://github.com/Damianf99/iFungi/blob/main/Screenshots/iFungi_Detected_Mushroom.jpg" />
</p>

<p align="center">
<img src="https://github.com/Damianf99/iFungi/blob/main/Screenshots/iFungi_Detected_Mushroom_Result.jpg" />
</p>


## Mushroom detecting from file:

<p align="center">
<img src="https://github.com/Damianf99/iFungi/blob/main/Screenshots/iFungi_Detected_Mushroom_Choose_From_Gallery.jpg" />
</p>

<p align="center">
<img src="https://github.com/Damianf99/iFungi/blob/main/Screenshots/iFungi_Detected_Mushroom_Choose_From_Gallery_2.jpg" />
</p>

<p align="center">
<img src="https://github.com/Damianf99/iFungi/blob/main/Screenshots/iFungi_Detected_Mushroom_Choose_From_Gallery_Detection.jpg" />
</p>

## Locations:

<p align="center">
<img src="https://github.com/Damianf99/iFungi/blob/main/Screenshots/iFungi_Location_list.jpg" />
</p>

<p align="center">
<img src="https://github.com/Damianf99/iFungi/blob/main/Screenshots/iFungi_Location_list_Remove_location.jpg" />
</p>

## Login:

<p align="center">
<img src="https://github.com/Damianf99/iFungi/blob/main/Screenshots/iFungi_Login.jpg" />
</p>

<p align="center">
<img src="https://github.com/Damianf99/iFungi/blob/main/Screenshots/iFungi_Login_Correct.jpg" />
</p>

## Main menu:

<p align="center">
<img src="https://github.com/Damianf99/iFungi/blob/main/Screenshots/iFungi_Main_Menu.jpg" />
</p>

## Map:

<p align="center">
<img src="https://github.com/Damianf99/iFungi/blob/main/Screenshots/iFungi_Map.jpg" />
</p>

<p align="center">
<img src="https://github.com/Damianf99/iFungi/blob/main/Screenshots/iFungi_Map_New_location.jpg" />
</p>

## Mushroom list:

<p align="center">
<img src="https://github.com/Damianf99/iFungi/blob/main/Screenshots/iFungi_Mushroom_Menu.jpg" />
</p>

## Mushroom details:

<p align="center">
<img src="https://github.com/Damianf99/iFungi/blob/main/Screenshots/iFungi_Mushroom_Edible.jpg" />
</p>

<p align="center">
<img src="https://github.com/Damianf99/iFungi/blob/main/Screenshots/iFungi_Mushroom_Edible_Distribution_and_Habitat.jpg" />
</p>

<p align="center">
<img src="https://github.com/Damianf99/iFungi/blob/main/Screenshots/iFungi_Mushroom_Poisonous.jpg" />
</p>

## Mushroom quiz:

<p align="center">
<img src="https://github.com/Damianf99/iFungi/blob/main/Screenshots/iFungi_Quiz.jpg" />
</p>

<p align="center">
<img src="https://github.com/Damianf99/iFungi/blob/main/Screenshots/iFungi_Quiz_2.jpg" />
</p>

<p align="center">
<img src="https://github.com/Damianf99/iFungi/blob/main/Screenshots/iFungi_Quiz_Results.jpg" />
</p>

## Registration:

<p align="center">
<img src="https://github.com/Damianf99/iFungi/blob/main/Screenshots/iFungi_Register.jpg" />
</p>

## Saving new location:

<p align="center">
<img src="https://github.com/Damianf99/iFungi/blob/main/Screenshots/iFungi_Save_Location.jpg" />
</p>

<p align="center">
<img src="https://github.com/Damianf99/iFungi/blob/main/Screenshots/iFungi_Save_Location_Manually.jpg" />
</p>

<p align="center">
<img src="https://github.com/Damianf99/iFungi/blob/main/Screenshots/iFungi_Save_Location_Manually_Popup.jpg" />
</p>
