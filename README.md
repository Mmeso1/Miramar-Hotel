# Miramar-Hotel

A project to create a hotel web app that has both admin and user side for booking rooms in the hotel. Built with Python and Flask.

## READ THIS BEFORE YOU START WRITING YOUR CODE

## Before You Start

- **Virtual Environment**: Start by setting up your virtual environment. Run the following commands to create and activate it. The command prompt should display (venv) in green, indicating you're in a virtual environment.

   ```bash
   python -m venv venv
   source venv/bin/activate  # On macOS and Linux
   venv\Scripts\activate    # On Windows

   
- **Running**: Lastly run this to start the app, then click on the url to see it on your browser
   ```bash
   python main.py

- The HTML codes are contained in the templates folder. Since we are starting with the user, inside the templates folder, go to the user folder and create your HTML files there. The person doing the landing page, I have already created your HTML file.

- Create your CSS file with the name of the screen you are styling, for example if the screen or page you are doing is landing, the css file should be landing.css. The style.css file contains general styling like the font styles, colors and *, navbar, and footer styles.

- Name your classes when styling explicitly to avoid clashing of styles when merged. Remember what we discussed.

- When creating a page and you want to see it, remember to create a route for it in user.py for the user side forntend in the views folder, else do it in the admin.py. See the syntax I used for the landing page and do yours. Please note two functions (in Python it is declared with def) should have the same name. Better yet, it should be the name of the page you are doing.

- If you have a component to create that will be reused, you can create a file and put it there and then extend it and call the block content and endblock content to include it in that particular part. If it chokes, please let me know. It will be needed on some pages that some elements will be reused, like the rest of the nav pages, aside from Home and Profile, the header where the picture is that contains the name of the page. I will create it and make a video if needed on how to use it, but I believe you'll figure it out.

- Please try to be done as soon as possible so that as the user side is done, the backend can start, and then the rest can now start the UI for the admin.

If I remember anything, I'll just update the README.


