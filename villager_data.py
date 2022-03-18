"""Functions to parse a file containing villager data."""


# def all_species(filename):
#     """Return a set of unique species in the given file.

#     Arguments:
#         - filename (str): the path to a data file

#     Return:
#         - set[str]: a set of strings
#     """
#     file = open("villagers.csv")
#     # file = file.split("|")
#     #return a set() with the name of the species, which is the 
#     #second index [1] in each line of the file
#     # species = {specie for specie in file file.split("|")[1]}
#     species = set()
#     # file = file.split("|")
#     for line in file:
#         line = line.split("|")
#         species.add(line[1])
        
#     file.close()
#     # TODO: replace this with your code

#     return species


# def get_villagers_by_species(filename, search_string="All"):
#     """Return a list of villagers' names by species.

#     Arguments:
#         - filename (str): the path to a data file
#         - search_string (str): optional, the name of a species

#     Return:
#         - list[str]: a list of names
#     """
#     file = open(filename)
#     villagers = []
    
#     #open the file, list of strings with their names and species
#     #name is index [0]

#     for line in file:
#         line = line.split("|")
#         if line[1] == search_string:
#             villagers.append(line[0])
        # file.close()
#     return sorted(villagers)


# def all_names_by_hobby(filename):
#     """Return a list of lists containing villagers' names, grouped by hobby.

#     Arguments:
#         - filename (str): the path to a data file

#     Return:
#         - list[list[str]]: a list of lists containing names
#     """
#     #return nested lists containing name (index [0]) 
#     #hobby (index[3])
#     #each nested list will share the same hobbies
#     file = open(filename)

#     # names_by_hobby = []
#     education = []
#     fitness = []
#     nature = []
#     music = []
#     fashion = []
#     play = []
    
    

#     for line in file:
#         line = line.split("|")
#         hobby = line[3]
#         name = line[0]
#         if hobby == "Education":
#             education.append(name)

#         elif hobby == "Fitness":
#             fitness.append(name)

#         elif hobby == "Nature":
#             nature.append(name)

#         elif hobby == "Music":
#             music.append(name)

#         elif hobby == "Fashion":
#             fashion.append(name)

#         elif hobby == "Play":
#             play.append(name)
        
        # file.close()
#     return [education, fitness, nature, music, fashion, play]


def all_data(filename):
    """Return all the data in a file.

    Each line in the file is a tuple of (name, species, personality, hobby,
    saying).

    Arguments:
        - filename (str): the path to a data file

    Return:
        - list[tuple[str]]: a list of tuples containing strings
    """
    #open file, loop through each line and split by "|"
    #make the strings at indices [0:4] into tuples and
    #then add them to an empty list and then close the file
    file = open(filename)
    all_data = []

    for line in file:
        line = line.rstrip()
        line = line.split("|")
        # a_tuple = (line[0:5])
        line = tuple(line)
        all_data.append(line)
        file.close()
    return print(all_data)


# def find_motto(filename, villager_name):
#     """Return the villager's motto.

#     Return None if you're not able to find a villager with the
#     given name.

#     Arguments:
#         - filename (str): the path to a data file
#         - villager_name (str): a villager's name

#     Return:
#         - str: the villager's motto or None
#     """

#     # TODO: replace this with your code


# def find_likeminded_villagers(filename, villager_name):
#     """Return a set of villagers with the same personality as the given villager.

#     Arguments:
#         - filename (str): the path to a data file
#         - villager_name (str): a villager's name
    
#     Return:
#         - set[str]: a set of names

#     For example:
#         >>> find_likeminded_villagers('villagers.csv', 'Wendy')
#         {'Bella', ..., 'Carmen'}
#     """

#     # TODO: replace this with your code
