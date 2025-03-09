class User:
    """Foydalanuvchi haqida klass"""
    def __init__(self, name, username, email):
        self.name=name
        self.username=username
        self.email=email
    def get_info(self):
        return f"{self.name}ning emaili-{self.email}"
user1=User("Alimxon", "alimchik777", "alimkhonrakhimov@email.com")
user2=User("Murodil", "murodil1993", "murodilakramov12@email.com")
user3=User("Abdurahim", "joraqulovA", "jurakulova@email.com")
print(user1.name)
print(user2.username)
print(user3.email)
print(user1.get_info())