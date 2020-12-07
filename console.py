import pdb

from models.user import User 
from models.transaction import Transaction
from models.merchant import Merchant
from models.tag import Tag

import repositories.user_repository as user_repository
import repositories.tag_repository as tag_repository
import repositories.merchant_repository as merchant_repository
import repositories.transaction_repository as transaction_repository

user_repository.delete_all()
tag_repository.delete_all()
merchant_repository.delete_all()
transaction_repository.delete_all()

user1 = User("Troy", "Barnes", "troybarnes@taaitm.com", 160.00)
user_repository.save(user1)
user2 = User("Abed", "Nadir", "abednadir@taaitm.com", 250.00)
user_repository.save(user2)
user3 = User("Ben", "Chang", "changsyaboi@taaitm.com", 145.60)
user_repository.save(user3)

tag1 = Tag("Groceries")
tag_repository.save(tag1)
tag2 = Tag("Business")
tag_repository.save(tag2)
tag3 = Tag("Snacks")
tag_repository.save(tag3)
tag4 = Tag("Leisure")
tag_repository.save(tag4)

merchant1 = Merchant("Scotmid", "General grocieries and provider of snax.")
merchant_repository.save(merchant1)
merchant2 = Merchant("Netflix", "Online streaming platform for movies and tv shows.")
merchant_repository.save(merchant2)
merchant3 = Merchant("Apple" , "Electronic hardware and software provider.")
merchant_repository.save(merchant3)

transaction1 = Transaction(user1, "2020-05-05", "19:40", merchant1, 6.50, tag3)
transaction_repository.save(transaction1)
transaction2 = Transaction(user2, "2020-06-07", "14:32", merchant2, 9.99, tag4)
transaction_repository.save(transaction2)
transaction3 = Transaction(user3, "2020-12-20", "12:20", merchant3, 59.00, tag2)
transaction_repository.save(transaction3)
transaction4 = Transaction(user1, "2020-09-15", "18:55", merchant1, 6.50, tag1)
transaction_repository.save(transaction4)
transaction5 = Transaction(user2, "2020-03-04", "07:29", merchant3, 19.99, tag4)
transaction_repository.save(transaction5)

