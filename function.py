from connect import *

def insert_data():
    
    filmTitle = input("Enter film Title: ")
    filmYear = input("Enter year of film: ")
    filmRating = input("Enter film rating: ")
    filmDuration = input("Enter film duration: ")
    filmGenre = input("Enter film Genre: ")

    dbCursor.execute("INSERT INTO tblFilms(title, yearReleased, rating, duration, genre) VALUES(?,?,?,?,?)",(filmTitle,filmYear,filmRating,filmDuration,filmGenre))
    
    dbCon.commit()

    print(f"'{filmTitle}' by {filmYear} inserted into the tblFilms table")

if __name__ == "__main__":
    insert_data()



def delete_data():
        idField = input("Enter the filmID of the record to be deleted: ")
        dbCursor.execute(f"DELETE FROM tblFilms WHERE filmID = {idField}")
        dbCon.commit()

        print(f"Record {idField} deleted from the films table")
if __name__ == "__main__":
        delete_data()



def update_data():

    idField = input("Enter filmID of the record to be updated: ")

    fieldName = input("Enter filmID or title or yearReleased or rating or duration or Genre as field name: ").title()

    fieldValue = input(f"Enter the value for the {fieldName} field: ")

    fieldValue = "'"+fieldValue+"'"

    dbCursor.execute(F"UPDATE tblFilms SET {fieldName} = {fieldValue} WHERE filmID = {idField}")

    dbCon.commit()

    print(f"Record {idField} updated in the tblFilms table: ")

if __name__ == "__main__":
    update_data()



def read_data():

    dbCursor.execute("SELECT * FROM tblFilms")
    allRecords = dbCursor.fetchall()

    for eachRecord in allRecords:
        print(eachRecord)

if __name__ == "__main__":
    read_data()

def all_films():
    """Print details of all films."""
    dbCursor.execute("SELECT * FROM tblFilms")
    allRecords = dbCursor.fetchall()
    for eachRecord in allRecords:
        print(eachRecord)

def by_genre(genre):
    """Print all films of a particular genre."""
    dbCursor.execute(f"SELECT * FROM tblFilms WHERE genre = '{genre}'")
    allRecords = dbCursor.fetchall()
    for eachRecord in allRecords:
        print(eachRecord)

def by_year(year):
    """Print all films of a particular year."""
    dbCursor.execute(f"SELECT * FROM tblFilms WHERE yearReleased = '{year}'")
    allRecords = dbCursor.fetchall()
    for eachRecord in allRecords:
        print(eachRecord)

def by_rating(rating):
    """Print all films of a particular rating."""
    dbCursor.execute(f"SELECT * FROM tblFilms WHERE rating = '{rating}'")
    allRecords = dbCursor.fetchall()
    for eachRecord in allRecords:
        print(eachRecord)

def reportSearch():
    """Search for a film by its title."""
    titleValue = input("Enter the film Title to search for: ")
    dbCursor.execute(f"SELECT * FROM tblFilms WHERE title = '{titleValue}'")
    allRecords = dbCursor.fetchall()
    for eachRecord in allRecords:
        print(eachRecord)

if __name__ == "__main__":
    all_films()
    reportSearch()
