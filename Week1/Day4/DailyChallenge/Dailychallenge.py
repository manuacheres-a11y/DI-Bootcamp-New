class Pagination:
    def __init__(self,items=None,page_size=10):
        
        self.items=items
        self.page_size = page_size

        if self.items == None:
            self.items = []

        self.current_idx = 0
        # Total pages : Number of items / Page Size => We apply ceil, to get to the superior integer
        self.total_pages = math.ceil(len(self.items) / self.page_size)

    # Return the item visibles, according to the page_size specified
    def get_visible_items(self):
        first_item = self.current_idx * self.page_size
        last_item = first_item + self.page_size
        return self.items[first_item:last_item]
    
    # We pay attention here to the page_num entered by ther user
    # If the page_num is superior to the max page -> Raise an error
    # If the page_num is 1, the index is 0 ! (The index of the items list)
    # For all other page_num entered, we substract 1 to the index
    def go_to_page(self, page_num):
        if page_num > self.total_pages:
            raise ValueError(f"The page specified is out of range. Max page = {self.total_pages}")
        elif page_num == 1:
            self.current_idx = 0
        else:
            self.current_idx = page_num - 1

    def first_page(self):
        self.current_idx = 0
        return self

    def last_page(self):
        self.current_idx = self.total_pages -1
        return self

    def next_page(self):
        if self.current_idx != self.total_pages:
            self.current_idx += 1
        else:
            print("Your are already at the last page !")
        return self

    def previous_page(self):
        if self.current_idx != 0:
            self.current_idx -= 1
        else:
            print("You are already at the first page !")
        return self
    
   