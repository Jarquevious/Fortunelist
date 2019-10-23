What happens when you press the “submit” button? Paste the full URL you are sent to on submit. 
file:///fortune_results?firstname=JJJ&bday=2019-10-15&gender=male&age=30&vehicle2=Car&vehicle3=Boat. 
We are redirected to a page that says, "your file was  not found"

What are the keys of this URL query string? How do they correspond to the “name” fields of your HTML form elements?
The keys are first name, bday, gender and age.
The keys are the names we labeled the data inside the html file. Both the keys and the name label are identical. 

What are the values of the URL query string? How do they correspond to what the user entered or typed?
The values are 'jjj', '2019-10-15', 'male', '30'. The values is the result of my inputs I inserted into the form. 

Stretch challenge question:
Is there a way to pass multiple values through the URL query string for a single key? How can we do so?
You can do so by making the key the name name for differebt values. For example:
            <input type="checkbox" name="vehicle" value="Bike"> I have a bike<br><br>
            <input type="checkbox" name="vehicle" value="Car"> I have a car<br><br>
            <input type="checkbox" name="vehicle" value="Boat" checked> I have a boat<br><br>

In the code above, each input has the same 'name' or 'key'. However, for each input, the 'value(s)' are different. This format allows for multiple values through the URL query string for a single key. Its great to note that this happens when the user is presented with a checkbox, which the user can choose multiple values. 