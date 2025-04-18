movies = [
{
"name": "Usual Suspects", 
"imdb": 7.0,
"category": "Thriller"
},
{
"name": "Hitman",
"imdb": 6.3,
"category": "Action"
},
{
"name": "Dark Knight",
"imdb": 9.0,
"category": "Adventure"
},
{
"name": "The Help",
"imdb": 8.0,
"category": "Drama"
},
{
"name": "The Choice",
"imdb": 6.2,
"category": "Romance"
},
{
"name": "Colonia",
"imdb": 7.4,
"category": "Romance"
},
{
"name": "Love",
"imdb": 6.0,
"category": "Romance"
},
{
"name": "Bride Wars",
"imdb": 5.4,
"category": "Romance"
},
{
"name": "AlphaJet",
"imdb": 3.2,
"category": "War"
},
{
"name": "Ringing Crime",
"imdb": 4.0,
"category": "Crime"
},
{
"name": "Joking muck",
"imdb": 7.2,
"category": "Comedy"
},
{
"name": "What is the name",
"imdb": 9.2,
"category": "Suspense"
},
{
"name": "Detective",
"imdb": 7.0,
"category": "Suspense"
},
{
"name": "Exam",
"imdb": 4.2,
"category": "Thriller"
},
{
"name": "We Two",
"imdb": 7.2,
"category": "Romance"
}
]

#1 Write a function that takes a single movie and returns True if its IMDB score is above 5.5
def isabove(moviewnum):
    try:
        if movies[int(moviewnum)]["imdb"] > 5.5: return True
    except:
        return None
#print(isabove(input()))

#2 Write a function that returns a sublist of movies with an IMDB score above 5.5
def ratingfilter(n):
    sublist = []
    for i in movies:
        if i.get("imdb") > n:
            sublist.append(i)
    return sublist
#filtered_movies = ratingfilter(5.5)
#for movie in filtered_movies:
#    print(movie)

#3 Write a function that takes a category name and returns just those movies under that category.
def categoryfilter(category):
    sublist = []
    for i in movies:
        if i.get("category") == category:
            sublist.append(i)
    return sublist
#filtered_movies = categoryfilter("Romance")
#for movie in filtered_movies:
#    print(movie)

#4 Write a function that takes a list of movies and computes the average IMDB score.
def avgimdb():
    sum = 0.0
    for i in movies:
        sum += i.get("imdb")
    return sum/len(movies)
#print(avgimdb())

#5 Write a function that takes a category and computes the average IMDB score.
def avgbycategory(category):
    sum, ctr = 0.0, 0
    for i in movies:
        if i.get("category") == category:
            sum += i.get("imdb")
            ctr += 1
    return sum/ctr
#print(avgbycategory("Adventure"))