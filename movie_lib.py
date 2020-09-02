import random
class Movie:
    def __init__(self, title, year, genre, watched):
        self.title = title
        self.year = year
        self.genre = genre
        self.watched = watched
    
    def __repr__(self):
        return f'{self.__class__.__name__}(title = {self.title}, year = {self.year}, genre = {self.genre}, watched = {self.watched})'

    def __str__(self):
        return f'{self.title} ({self.year})'

    @property
    def play(self):
        self.watched += 1
        return self.watched
    
class Series(Movie):
    def __init__(self, title, year, genre, watched, season, episode):
        super().__init__(title, year, genre, watched)
        self.episode = episode
        self.season = season
    
    def __repr__(self):
        return f'{self.__class__.__name__}(title={self.title}, year={self.year}, genre={self.genre}, watched={self.watched}, season={self.season}, episode={self.episode})'
 
    def __str__(self):
        return f'{self.title} S{self.season} E{self.episode}'

m1 = Movie("Bridget Jones", "1996", "romantic comedy", 1)
m2 = Movie("Spiderman", "2005", "sci-fi", 2)
m3 = Movie("Salf of the Earth", "2000", "documentary", 3)
m4 = Movie("Jaws", "1988", "thriller", 7)
s1 = Series("Friends", "1994", "comedy", 4, 21, 10)
s2 = Series("Modern Family", "2010", "comedy", 5, 22, 11)
s3 = Series("This is us", "2012", "drama comedy", 6, 21, 6)
s4 = Series("Blue Planet", "2016", "documentary", 8, 6, 2)

library = [m1, m2, m3, s1, s2, s3]
   
def get_movies(library):
    movie_lib = []
    for n in library:
        if isinstance(n, Movie) and not isinstance(n, Series):
            movie_lib.append(n)
    movie_lib = sorted(movie_lib, key=lambda movie:movie.title)
    return movie_lib


def get_series(library):
    series_lib = []
    for n in library:
        if isinstance(n, Series):
            series_lib.append(n)
    series_lib = sorted(series_lib, key=lambda series:series.title)
    return print(series_lib)


'''search_title = input("What title are you looking for? ")
def search(library, search_title):
    for n in library:
        if n.title == search_title:
            print(f"Found movie you are looking for! {n}" )
        else:
            pass

def generate_views_x10(func):
    for n in range(10):
        func()
        

@generate_views_x10
def generate_views():
    r = random.randint(0,len(library)-1)
    library[r].watched = random.randint(1,100)
    return library[r].watched

top = input("how many top titles you want to see? ")
top = int(top)
content_type = input("do you want to see top_list only for Movies [M] or Series [S] or Both Categories [B]? ")

def top_titles(top, content_type):
    if top < len(library)-1:
        print("works so far")
        if content_type == "M":
            library_sorted = get_movies(library)
        elif content_type == "S":
            library_sorted = get_series(library)
        elif content_type == "B":
            library_sorted = library     
        
        library_sorted = sorted(library_sorted,reverse = True, key=lambda item:item.watched)
        
        for k, n in enumerate(library_sorted):
            if k < top:
                print(f"top list: {library_sorted[k]} with numbers of views: {library_sorted[k].watched}")
                
    else:
        print("choose smaller number for top_list")'''


