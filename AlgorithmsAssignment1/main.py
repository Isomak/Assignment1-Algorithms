#Assignment 1
import datetime
class Product:

    # Create masterlist of all products in the class
    products = []

    def __init__(self, id, name, price, category):
        self.id = int(id)
        self.name = name
        self.price = float(price)
        self.category = category
        
    def __lt__(self, other):
        return self.price < other.price

    def __gt__(self, other):
        return self.price > other.price

    def __eq__(self, other):
        if other == None:
            return 0
        else:
            return self.price == other.price

    def __str__(self):
        return f"ID: {self.id}\tPrice: {self.price}\tName: {self.name}\tCategory: {self.category}"

    def insert(id, name, price, category):
        new_product = Product(id, name, price, category)
        Product.products.append(new_product)
        # start timer
        start = datetime.datetime.now()
        Product.products = insertion_sort(Product.products)
        # print the amount of time it took to sort
        length = datetime.datetime.now() - start
        print(f"it took {length.seconds}.{length.microseconds} seconds to sort {new_product.id}")
        return new_product

    def equals(self,other):
        # Stealing function ideas from java :)
        return self.id == other.id and self.name == other.name and self.price == other.price and self.category == other.category
   
    def delete(self):
        if self is None:
            return 1

        for i in range(len(Product.products)):
            if self.equals(Product.products[i]):
                Product.products.pop(i)  
                return 0
        return 1

    def search(search,type):
        # type here lets the program know whether to seach for ID's or Names
        if type == 0:
            for i in range(len(Product.products)):
                if search.lower() == Product.products[i].name.lower():
                    return Product.products[i]
                
        # Search for IDS
        elif type == 1:
            for i in range(len(Product.products)):
                if search == Product.products[i].id:
                    return Product.products[i]
        return None    
        
    def print_all():
        for product in Product.products:
            print(product)
    
    def parse(file_name):
        with open('product_data.txt', 'r') as file:
            for line in file:
                id, name, price, category = line.strip().split(', ')
                Product.insert(id, name, price, category)

# Helper Functions
def insertion_sort(list_to_sort):

    # Set unsorted portion of list to 0
    unsorted = 0
    check = unsorted
    # While we still have a unsorted list
    while (unsorted <= len(list_to_sort)):
        # Check if the current item is at the zero index or is unsorted
        if check >= 1 and list_to_sort[check] < list_to_sort[check - 1]:
            # Swap
            swap = list_to_sort[check]
            list_to_sort[check] = list_to_sort[check - 1]
            list_to_sort[check - 1] = swap
            # Deincriment so we can stay with the element we just swapped
            check -= 1
        else: 
            # Now we know the element is sorted, incriment to next unsorted elem
            check = unsorted
            unsorted += 1
    return list_to_sort

def selections(items):
    while True:
        itemstring = ""
        for i in range(len(items)):
            itemstring += f"{i+1}) {items[i]}\n"
        print("\nPlease Select an Option:")
        print(itemstring)
        selection = input()
        if selection.isdigit():
            sel_int = int(selection)
            if sel_int >= 1 and sel_int <= len(items):
                return sel_int - 1
            
        print("That is not a valid input.\nPlease try again.\n")

def search_helper():
    print("What would you like to search for?:")
    options = ["Name","ID"]
    type = selections(options)
    object_found = None
    if type == 0:
        name = input("Please enter the exact name of the product you are looking for:\n")
        object_found = Product.search(name,type)
    
    elif type == 1:
        while True:
            print("Please enter an ID:")
            id = input()
            if id.isdigit():
                object_found = Product.search(int(id),type)
                break
            else:
                print("that is not a valid ID")

    if object_found == None:
        print("Your Seach Returned no results.")
    else:
        print("\nFound Object:")
        print(object_found)
    return object_found

def insert_helper():
    while True:
            try:
                id = int(input("Please enter an ID:\n"))
                name = input("Please enter a name:\n")
                price = float(input("Please enter a price:\n"))
                category = input("Please enter a catagory:\n")
                return Product.insert(id,name,price,category)

            except ValueError:
                print("Those are not correct Values,\nPlease try again.\n") 

def update_helper(product):
    if product is None:
        print("No product selected to update.")
        return None

    for i in range(len(Product.products)):
        if product.equals(Product.products[i]):
            try:
                options = ["ID", "Name", "Price", "Category"]
                current_option = selections(options)
                match current_option:
                    case 0:
                        new_id = int(input("Please enter an ID:\n"))
                        Product.products[i].id = new_id
                        return_product = Product.products[i]   
                    case 1:
                        new_name = input("Please enter a name:\n")
                        Product.products[i].name = new_name
                        return_product = Product.products[i]
                    case 2:
                        new_price = float(input("Please enter a price:\n"))
                        Product.products[i].price = new_price
                        return_product = Product.products[i]
                        Product.products = insertion_sort(Product.products)
                    case 3:
                        new_category = input("Please enter a category:\n")
                        Product.products[i].category = new_category
                        return_product = Product.products[i]
                print("Successfully Updated")
                return return_product
            except ValueError:
                print("There was an error with the input. Please Try Again.")
                return product
    print("Object Not Found")
    return None


def main():
    file_name = "product_data.txt" 
    Product.parse(file_name)
    selected_product = None
    options = ["Insert A Product","Update An existing Product","Search For A Product","Delete Currently Seleted Product", "Print Currently Seleted Product","Print All Products","Exit"]
    
    while True:
        current_option = selections(options)
        match current_option:
            case 0:
                selected_product = insert_helper()

            case 1:
                updated_product = update_helper(selected_product)
                if updated_product is not None:
                    selected_product = updated_product  # Update the reference to the selected product

            case 2:
                returned_product = search_helper()
                if returned_product != None:
                    selected_product = returned_product
            case 3:
                if selected_product is not None:
                    returned_status = Product.delete(selected_product)
                    if returned_status == 0:
                        print("\nObject deleted successfully.\n")
                        selected_product = None
                    else:
                        print("\nObject not found\n")
                else:
                    print("\nNo product selected to delete.\n")

            case 4:
                print("\n" + str(selected_product) + "\n")
            case 5:
                Product.print_all()
            case 6:
                exit()

            

if __name__ == "__main__":
    main()