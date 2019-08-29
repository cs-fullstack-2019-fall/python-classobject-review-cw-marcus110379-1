def main():
    problem1()
    problem2()

# !! : your file does not run becasue of syntax errors 

# Problem 1:
# Create a Movie class with the following properties/attributes: movieName, rating, and yearReleased.
#
# Override the default str (to-String) method and implement the code that will print the value of all the properties/attributes of the Movie class
#
# In your main function create two instances of the Product class
#
# Assign a value of your choosing for each property/attribute
#
# Print all properties to the console.
#
# Remember, this is the basic model of a Python file with a class

class Movie:
    def __init__(self,movieName, rating, yearReleased):
        # Class constructor code and property handling
        self.movieName = movieName
        self.rating =rating
        self.yearReleased = yearReleased

    #OTHER PROPERTIES AND METHODS HERE
    def __str__(self):#this method Override the default str (to-String) method
        my_instance_str = f" Properties Movie Class\n\nmovieName = {self.movieName}\nrating = {self.rating}\nyearReleased = {self.yearReleased}\n" 
        return my_instance_str
        # !! : instance string is a varibale, you can't list three seperate f strings as a varibale definition 

def problem1():
    #Create class instance(s) and perform other activities in/from this function
    myMovie = Movie("robocop", "R", "1985")# creating instances
    myMovie2 = Movie("robocop2", "R", "1987")
    print(myMovie)
    print(myMovie2)






# Problem 2:
# Create a class Product that represents a product sold online.
#
# A Product has price, quantity and name properties/attributes.
#
# Override the default str (to-String) method and implement the code that will print the value of all the properties/attributes of the Product class
#
# In your main function create two instances of the Product class
#
# Assign a value of your choosing for each property/attribute
#
# Print all properties to the console.


class Product:
    def __init__(self, price, quantity, name):# creation of product class with properties
        self.price = price
        self.quantity = quantity
        self.name = name



    def __str__(self): #this method Override the default str (to-String) method
        my_instance_str = f" Properties of Product Class\n\nprice = {self.price}\nquantity = {self.quantity}\nname = {self.name}\n" 
        # !! : instance string is a varibale, you can't list three seperate f strings as a varibale definition 


        return my_instance_str
def problem2():

    product1 = Product("$2","5", "grove")# creating instances
    product2 = Product("$5","5", "ridge")
    print(product1)
    print(product2)


main()