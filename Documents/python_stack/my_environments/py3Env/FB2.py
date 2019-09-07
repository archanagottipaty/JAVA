class SList:
	def __init__(self):
		self.head = None
    def add_to_front(self, val):#added this line, takes a value

    	
class SLNode:
    def __init__(self, val):
        self.value = val
        self.next = None


    def add_to_front(self, val):
        new_node = SLNode(val)
        current_head = self.head	# save the current head in a variable

    def add_to_front(self, val):
        new_node = SLNode(val)
        current_head = self.head
        new_node.next = current_head	# SET the new node's next TO the list's current head

    def add_to_front(self, val):
        new_node = SLNode(val)
        current_head = self.head
        new_node.next = current_head
       	self.head = new_node	# SET the list's head TO the node we created in the last step
        return self	                # return self to allow for chaining


    def print_values(self):

    def print_values(self):
        runner = self.head	# a pointer to the list's first node

    def print_values(self):
        runner = self.head
        while (runner != None):	# iterating while runner is a node and not None

    def print_values(self):
        runner = self.head
        while (runner != None):
        print(runner.value)	# print the current node's value


    def print_values(self):
        runner = self.head
        while (runner != None):
            print(runner.value)
       	runner = runner.next 	# set the runner to its neighbor
        return self	                # once the loop is done, return self to allow for chaining


    def add_to_back(self, val):	# accepts a value


    def add_to_back(self, val):
        new_node = SLNode(val)	# create a new instance of our Node class with the given value


    def add_to_back(self, val):
        new_node = SLNode(val)
        runner = self.head	    # set an iterator to start at the front of the list


    def add_to_back(self, val):
         new_node = SLNode(val)
         runner = self.head
         while (runner.next != None):	# iterator until the iterator doesn't have a neighbor

    def add_to_back(self, val):
         new_node = SLNode(val)
         runner = self.head
         while (runner.next != None):
            runner = runner.next # increment the runner to the next node in the list


    def add_to_back(self, val):
        if self.head == None:	# if the list is empty
        self.add_to_front(val)	# run the add_to_front method
        return self	# let's make sure the rest of this function doesn't happen if we add to the front
            new_node = SLNode(val)
            runner = self.head
            while (runner.next != None):
                runner = runner.next
            runner.next = new_node	# increment the runner to the next node in the list
            return self                 # return self to allow for chaining

my_list = SList()	# create a new instance of a list
my_list.add_to_front("are").add_to_front("Linked lists").add_to_back("fun!").print_values()    # chaining, yeah!
# output should be:
# Linked lists
# are
# fun!

