nextplaces = []
def adderlocation(location,nextplaces):
    pass
class Place():
    def __init__(self, given_name, locked=True):
        # locked=False means that the locked parameter will be False by default if not provided.
        self.name = given_name
        self.locked = locked
        self.next_places = []
        self.items = []
        # add more atributes as needed

    def add_next_place(self, place_instance):
        self.next_places.append(place_instance)

    def add_item(self, item_instance):
        self.items.append(item_instance)

    def show_next_places(self):
        print("The possible places you can go to are: ")
        for place in self.next_places:
            # remember that next_places is a list of Place instances hence why we can use place.name
            print(place.name)

# def placeselectionchooser(selectionchoice):
#     doneselection = False
#     while doneselection == False:
#         if selectionchoice == "Home":
#             CurrentPlace = "Home"
#             doneselection = True
#             print("Done")
#         else:
#             print("You have typed an invalid location")
#             selectionchoice = input("Please enter a valid location you would like to travel to. ")