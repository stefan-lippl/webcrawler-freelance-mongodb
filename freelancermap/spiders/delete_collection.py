from pymongo import MongoClient


def main():
    connection = MongoClient(
            "mongodb+srv://stefan-lippl:Windows64bit$@cluster0.kkskd.mongodb.net/Freelance?retryWrites=true&w=majority")
    db = connection.Freelance
    collection = db.projects

    collection.delete_many({})


if __name__ == main():
    # main()
    pass
