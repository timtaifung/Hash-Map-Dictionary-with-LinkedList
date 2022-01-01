#data collection
flower_definitions = [['begonia', 'cautiousness'], ['chrysanthemum', 'cheerfulness'], ['carnation', 'memories'], ['daisy', 'innocence'], ['hyacinth', 'playfulness'], ['lavender', 'devotion'], ['magnolia', 'dignity'], ['morning glory', 'unrequited love'], ['periwinkle', 'new friendship'], ['poppy', 'rest'], ['rose', 'love'], ['snapdragon', 'grace'], ['sunflower', 'longevity'], ['wisteria', 'good luck']]



#basic node class
class Node:
    def __init__(self,value,next_node=None):
        self.value=value
        self.next_node=next_node
    def get_value(self):
        return self.value
    def get_next_node(self):
        return self.next_node
    def set_next_node(self,next_node):
        self.next_node=next_node

#linked list class
class LinkedList:
    def __init__(self,head_node=None):
        self.head_node=head_node
    #inserting at the end of the linkedlist
    def insert(self,new_node):
        current_node=self.head_node
        #if the head_node is empty, new_node will become the new node
        if not current_node:
            self.head_node=new_node
        while current_node:
            next_node=current_node.get_next_node()
            if not next_node:
                current_node.set_next_node(new_node)
            current_node=next_node
        

        

class HashMap:
    def __init__(self,array_size):
        self.array_size=array_size
        self.array=[LinkedList() for i in range(self.array_size)]

    def hash(self,key):
        hash_code=key.encode()
        return hash_code
    def compressor(self,hash_code):
        return hash_code%self.array_size
    
    def assign(self,key,value):
        array_index=self.compressor(self.hash(key))
        payload=Node([key,value])
        list_at_array=self.array[array_index]
        for item in list_at_array:
            if item.value[0]==key:
                item.value[1]=value
                return
        list_at_array.insert([key,value]) 

    def retrieve(self,key):
        array_index=self.compressor(self.hash(key))
        list_at_array=self.array[array_index]
        for item in list_at_array:
            if item.value[0]==key:
                return item.value[1]
        return None

blossm=HashMap(len(flower_definitions))
for pair in flower_definitions:
    key = pair[0]
    value = pair[1]
    blossm.assign(key,value)


#testing data
print(blossm.retrieve('daisy'))