class City:

    def __init__(self, name, country, visited, comment, id = None):
        self.name = name
        self.country = country
        self.visited = visited
        self.comment = comment
        self.id = id

    # def city_dictionary(self, name, country, visited, comment, id):
    #     return {name:self.name, country:self.country, visited:self.visited, comment:self.comment, id:self.id}