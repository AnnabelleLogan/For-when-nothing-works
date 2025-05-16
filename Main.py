# Write Python code for both the Novel and Magazine classes modelled in the previous slide. Include a suitable constructor method which uses the Book constructor method. Instantiate 2 novels and 2 magazines and print their details.
# Create the Book class (plus methods and attributes)
# Create the Novel class that inherits from Book class.
# Create the Magazine class that inherits from Book class.



class Book:
    def __init__(self, title, genre, num_chapters, author, year):
        self.title = title
        self.genre = genre
        self.num_chapters = num_chapters
        self.author = author
        self.year = year

    def ReviewBook(Review):
        return "Review book"
    
    def RateBook(Rating):
        return "Rating book"
    
    def DisplayDetails():
        return "Review book"

class Novel(Book):
    def __init__(self, title, genre, year, author):
        super().__init__(title, genre, author, year)
        self.title = title
        self.genre = genre
        self.year = year
        self.author = author


    def CalcReadTime(ReadSpeed):
        return "Calculate Read Time"
    
Novel_1 = Novel("Great Gatsby", "Fiction", 1925, "F. Scott Fitzgerald")
Novel_2 = Novel("Captains", "Non-Fiction", 2014, "Yuval Noah Harari")

print = (Novel_1)
print = (Novel_2)

    
class Magazine(Book):
    def __init__(self, issue_num, num_articles, brand):
        super().__init__(issue_num, num_articles)
        self.issue_num = issue_num
        self.num_articles = num_articles
        self.brand = brand
    
    def GetArticleByTitle(title):
        return "Get Article By Title"
    
Magazine_1 = Magazine("Magpie Season comes to an end", "Non-Fiction", 2025, "John Pokins")
Magazine_2 = Magazine("Italian bread bakeries are popping up everywhere! Find out their recipes here", "Non-Fiction", 2025, "Ratasha Filnda")

print = (Magazine_1)
print = (Magazine_2)
