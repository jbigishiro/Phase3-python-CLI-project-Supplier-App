from simple_term_menu import TerminalMenu
from models import Supplier, Product
from prettycli import red, yellow, blue


class Cli():

    
    print(blue("WELCOME"))
    print(blue("Search for Products and their Suppliers"))

    def start(self):
  
        self.clear_screen()

        options = ["Search for product", "Add product","Update product price", "Delete Product" ,"Exit"]
        terminal_menu = TerminalMenu(options)
        menu_entry_index = terminal_menu.show()

        if options[menu_entry_index] == "Search for product":
            self.handle_search()
        elif options[menu_entry_index] == "Add product":
            self.handle_add()
        elif options[menu_entry_index] == "Update product price":
            self.handle_update()
        elif options[menu_entry_index] == "Delete Product":
            self.handle_delete()
        else:
            self.exit()

    
    def handle_search(self):
        
        self.clear_screen()
        
        search_product= input("Enter the product name").lower()
        products = Product.show_product_by_name()

        matching_products = []
        for product in products:
            if search_product in product.name.lower().split():
                matching_products.append(product)

        if matching_products:
            print(yellow("Matching products:"))
            self.handle_print(matching_products)            
        else:
            print(yellow("Product not found."))
    def handle_add():
        pass


    def handle_update():
        pass

    def handle_delete():

        pass


    def handle_print(self, products):
        for product in products:
                print(blue(f"Item: {product.name}"))
                print(f"Unit Price: {product.unit_price}")
                supplier = Supplier.search_supplier_by_id(product.supplier_id)    
                print(f"Sold by: {supplier.name}")

    def exit(self):
        self.clear_screen()
        print(blue("Goodbye!"))
    
    def clear_screen(self):
        print("\n")
     


app = Cli()
app.start()