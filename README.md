Software Development Using Machine Learning and Generative AI: Tech Challenge

Task 1: Simple React App
Steps followed:
Open Visual Studio Code 
Ran the following commands in a new terminal: 
npx create-react-app@latest hello-world
cd hello-world
npm start
Note: The above commands work because I already have Node Package Manager (npm) installed on my laptop,. 
Once the application is running on a local server, I opened up the hello-world folder on my VS code and navigated to src -> App.js 
Within the App.js file, I removed the image logo and the text, to the following:
	<h1>Hello World!</h1>

Outcome:
The React app successfully displayed a “Hello World!” message on http://localhost:3000 following the latest React setup guidelines.The outcome of this in the local server is as follows:
	















Task 2: Simple Streamlit App
Steps followed: 
Created a new folder with app.py file 
Within the file, wrote code to install an existing built-in wine dataset from sci-kit learn and used the Streamlit UI to create a “Wine Recommender” system
Used a RandomForestClassifer from scikit-learn to make the predictions based on some values the user enters.
Outcome:
 A fully functional Wine Recommender App that allows users to adjust sliders and see a predicted wine class along with a probability chart.


Task 3: LLM API
For this task, I build upon the Wine Recommender App from task 2 and added an AI chat assistant to the app
Steps followed:
Using the OpenAI API, got an API key
Created a secrets file and added the API key
Created an OPENAI client with the API key and added a chat section to ask anything about wine
Below is an example of what the app looks like:

Outcome:
 An integrated Streamlit app that combines traditional machine-learning predictions with a conversational LLM-powered assistant, enhancing user interactivity and engagement.



How I used AI & Vibe Coding:
Throughout the challenge I used AI to debug, troubleshoot and explore concepts in the following ways:
Version Control - Some of the Python packages were using different versions which were not compatible with each other. To solve this issue, I asked AI how to fix the version problems and what to uninstall/install again. Ideally, I would have gone about implementing pip-tools for version locking so that errors like this do not occur in the future. However, due to the time constraints, for this challenge, I simply uninstalled a library that was being indirectly installed but not used in my code (pyarrow) 
Storage issues - one of the biggest problems with using LLMs, APIs and Software Development in general is having enough memory and disk space for all packages, dependencies and files. Since this was all being done on my personal computer and not the cloud, I had to troubleshoot some problems with storage when it came to installing packages and used AI to help me run commands to get rid of temporary and unused files so that I can make space for new files. 
Understanding the wine dataset - Since I was using a built-in wine dataset, I wasn’t sure how the features are structured and what the dataset looks like. I did not implement Exploratory Data Analysis so instead to do this, I used AI to help me decide which features to expose on the sliders.
Writing and structuring - Lastly, I used AI to summarize my findings and improve my clarity and structure of my documentation.
