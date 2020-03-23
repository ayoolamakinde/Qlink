An application which manages messages and provides details about those
messages, specifically whether or not a message is a palindrome. Your application
should support the following operations:  
- Create, retrieve, update, and delete a message. 
- List messages. 
These operations follows proper RESTful design.  

## Getting Started

# RUN with Docker
docker build -t newbuild .  
docker run newbuild

# Set up a virtual environment using with python3
pip install virtualenv  
virtualenv -p python3 qlinkrest  
source qlinkrest/bin/activate  

# Install the following  
(qlinkrest) $ pip install flask requests   

# run the palindrome test  

Ensure you are in the code files directory:  
(qlinkrest) $ python test.py  

----------------------------------------------------------------------  
Ran 0 tests in 0.000s  

OK  


# run the restApi  

(qlinkrest) $ python qlink.py  
* Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)  

## Make requests  

# Open another terminal and activate the virtual env  
(base) $ source qlinkrest/bin/activate  

# navigate to the folder containing the code  
if you are not in the directory containing the code, navigate there.  

# open interactive python shell 
(qlinkrest) $ python  

# import request  
>>> import requests   

# List all messages  
>>> response = requests.get("http://127.0.0.1:5000")   
>>> response.json()  

# Retrieve a specific message 
(EXAMPLE - A message “Ayoola Makinde”)  
>>> response = requests.get("http://127.0.0.1:5000/qlink/Ayoola Makinde")  
>>> response.json()  

# Create a new message  
(EXAMPLE - Create a message “I live in Guelph”)  
>>> response = requests.post("http://127.0.0.1:5000/qlink", json={"I live in Guelph":" "})    
>>> response.json()  


# Update a message  
EXAMPLE - Change the message “Cross River State” to "University of Dallas")  
>>> response = requests.put("http://127.0.0.1:5000/qlink/Cross River State", json={"University of Dallas":" "})    
>>> response.json()  


# Delete a message
(EXAMPLE - A message “Ayoola Makinde”)  
>>> response = requests.delete("http://127.0.0.1:5000/qlink/Ayoola Makinde")    
>>> response.json()  
