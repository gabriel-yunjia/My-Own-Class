 #asign10_1
 #Gabriel Li
 #Purpose: Create my Own class(Vertebrate Animals) that can add and remove diffrent species of vertebrate and add/remove animals to those species.
 #The class is a dictionary of lists, with each species being a list of animals within those species. 
 #This program is meant to store and edit info, so the extra two other methods are used to remove info from two diffrent levels. 
 
 
 
 #creating class
class Vertebrate:
    
    #init function
    def __init__(self):
        #cretats a dictionary for later use
        self.dict={}
    
    #add species function
    def add_species(self,species):
        self.species = species
        #add the inputed species if its not in the dictinoary, or print a message saying it has already been added. 
        if self.species in self.dict.keys():
            print("Species,",self.species,"is already in the dictionary.")
        else:
            self.dict[self.species]=[]
            print("New Species,",self.species,"is added in the dictionary.")
            
    #remove species function 
    def remove_species(self,species):
        self.species = species
        #similar idea as add, but for removing species in the dictionary. 
        if self.species in self.dict.keys():
            del self.dict[self.species]
            print("Species,", self.species,"is removed successfully.")
        else:
            print("Species,", self.species,"does not exist.")
    

    #get function for species 
    def get_species(self):
        print(self.dict.keys())
        return(self.dict.keys())
    
    #add function for animals in diffrent species 
    def add(self,species,name):
        self.species = species
        self.name = name
        #if the specie name is in the dictionary, then add the animal into
        if self.species in self.dict.keys():
            self.dict[species].append(self.name)
            print(self.dict[species])
            print(self.species+",",self.name,"is added successfully.")
        else:
            print("Species,",self.species,"does not exist in the dictionary.")
            
    #removing one animal from a species 
    def remove(self,species,name):
        
        self.species = species
        self.name = name
        #if the the name and species is correct, remove that animal in that species, else print either the species doesn't exist, or that the animal isn't found in this species.
        if self.species in self.dict.keys():
            for i in self.dict[species]:
                if i == self.name:
                    self.dict[species].remove(i)
                    print(self.name,"is removed successfully.")
                else:
                    print(self.name,"is not found.")
        else:
            print(self.species,"does not exist.")
            
    # get and a getall  functions for the animals with the input being the species for get.
    def get(self,species):
        print(self.dict[species])
        return (self.dict[species])
    def get_all(self):
        print (self.dict)
        return(self.dict)


#Demo program
def main():
    #setting test variable
    test = Vertebrate()

    #adding 5 diffrent kinds of species
    test.add_species("Mammal")
    test.add_species("Bird")
    test.add_species("Reptile")
    test.add_species("Fish")
    test.add_species("ET")

   #trying to add a repeated species,
    test.add_species("Mammal")

    #getting the species. 
    test.get_species()
    
    #removing 1 species and 1 nonexistent species. 
    test.remove_species("ET")
    test.remove_species("Alien")

    #getting the species again 
    test.get_species()
    
    #adding diffrent animals for each species. 
    test.add("Mammal","Human")
    test.add("Mammal","Whale")
    test.add("Bird","Eagle")
    test.add("Bird","Owl")
    test.add("Reptile","Lizard")
    test.add("Reptile","Snake")
    test.add("Fish","Shark")
    test.add("Fish","Salmon")
    
    #attemping to add an animal to a nonexistent species.
    test.add("Insect","Dragonfly")
    
    #removing an animal for a species
    test.remove("Fish","Shark")
    #attempting to remove an animal from a nonexsistent species.
    test.remove("Dinosaur","T-Rex")
    #attempting to remove a nonexsistent animal from a species.
    test.remove("Fish","Penguin")

    #testing get functions, one for getting the animals of one species, and another that gets all the vertebrates that has been stored. 
    test.get("Fish")
    test.get_all()
    
#main
if __name__ == "__main__" :
    main()