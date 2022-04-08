{% include nav.html %}
# Create Task Documentation
***
# Site Search Feature

<iframe width="560" height="315" src="https://www.youtube.com/embed/98KXo33uTuY" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

### [Final Commited Code](https://github.com/YashShah138/Team-MicrosoftTechSupport/blob/ee14dfae0d25b1812d7c171747f12bcc4982f839/templates/layouts/base.html#L44-L112)
### Interactive Runtime Found Here: [Website](http://teammicrosofttechsupport.com/)
### 3A 
**Overall purpose:** Navigate our Beach Resource Website easier by searching for pages.
**Functionality/Input:** Input text and submit into a search bar which returns a rendered HTML page based on what was searched for. Inputted invalid request for a page that does not exist and an error message is displayed with a prompt that includes an example of what to search for.
**Input/Output:** Text is inputted, rendered HTML page or error message is outputted.

### 3B
Storing Data in a List:

<img width="584" alt="Screen Shot 2022-02-14 at 11 07 01 AM" src="https://user-images.githubusercontent.com/89219514/153929719-5b4d9f67-8d41-403a-8c74-a664aaa18083.png">

Using the Data:

<img width="1011" alt="Screen Shot 2022-02-14 at 11 08 21 AM" src="https://user-images.githubusercontent.com/89219514/153929873-dbe1e322-4932-439a-a93c-4df032a9a401.png">

The list being used in this example is beach pages. The other lists can be used by changing the function's used parameter value. The data in the list is organized as a dictionary, and each item in the list represents the name of one of the beach pages and its corresponding URL. The list is used to manage complexity by organizing all of the pages into a list that can be iterated through. This makes searching for the desired list easy by iterating through each item and checking whether it matches the user's input. Without using a list like this, searching all of the pages and their URLs would not be possible. 

### 3C
Procedure:

<img width="1006" alt="Screen Shot 2022-02-14 at 11 16 09 AM" src="https://user-images.githubusercontent.com/89219514/153930922-2a556827-2c0a-4f89-8ef5-7f26c0caaa15.png">

Calling the procedure:

<img width="837" alt="Screen Shot 2022-02-14 at 11 17 17 AM" src="https://user-images.githubusercontent.com/89219514/153931049-79f06f38-2d21-4406-ae52-1d51f728f3e2.png">

The general function of the procedure recognizes the user's input into a text box, searches the dictionary for a matching beach page, and returns the link of the page. 

**Detailed Description:** variable "x" contains the dictionary data as JSON information. Variable "input" gets the user's input from the HTML search bar with the id "beach search". The input is turned to lowercase to prevent case sensitivity. A for loop sets an index marker at position 0, and loops the following instructions _n_ number of times where _n_ is the length of the list "beach pages": The algorithm checks if the substring of the input from index 0 to the length of the input matches any item in the dictionary using the same substring method. This allows a valid return even if the user does not enter the entire name of the page. If true, the variable "link" gets assigned to the corresponding URL page and is returned. If none of the items in the list match the input, an error message is displayed and gives an example using a random number function to pick a random index in the valid list to display as an example.

### 3D
**Call 1:** Search bar takes the input of "Del Mar Beach", while function takes a parameter "beach pages", and submit button is pressed. Condition tested by the first call is if the input matches an item in the "beach pages" list. The result of this call would return a rendered page with the URL "/del-mar-beach/", and display the page. 

**Call 2:** Search bar takes the input of "Pacific Beach", while function takes a parameter "about pages", and submit button is pressed. Condition tested by the second call is if the input matches an item in the "about pages" list. The result of the call would not find a matching page in the list, and run the error code block, by returning the same page, and displaying an error message saying, "Page Does Not Exist. Please search for pages similar to: " and provides a random example of a page in "about pages".
