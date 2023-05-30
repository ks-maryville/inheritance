class Article:
    def __init__(self, article_name):
        self.article_name = article_name

    def get_article_name(self):
        return self.article_name

    def __str__(self):
        return self.article_name


class UserProfile:
    def __init__(self, user_id, profile_id):
        self.user_id = user_id
        self.profile_id = profile_id
        self.__firstname = None
        self.__lastname = None
        self.__address = None

    def get_firstname(self):
        return self.__firstname

    def set_firstname(self, fname):
        self.__firstname = fname

    def get_lastname(self):
        return self.__lastname

    def set_lastname(self, lname):
        self.__lastname = lname

    def get_address(self):
        return self.__address

    def set_address(self, address):
        self.__address = address


class WriterProfile(UserProfile):
    # pass
    def __init__(self, user_id, profile_id):
        super().__init__(user_id, profile_id)
        self.__posts = []

    def get_posts(self):
        return self.__posts

    def create_post(self, article):
        self.__posts.append(article)


class ReaderProfile(UserProfile):
    def __init__(self, user_id, profile_id):
        super().__init__(user_id, profile_id)
        self.__bookmarked = []

    def get_bookmarked(self):
        return self.__bookmarked

    def add_bookmark(self, article):
        self.__bookmarked.append(article)


class EditorProfile(UserProfile):
    def __init__(self, user_id, profile_id):
        super().__init__(user_id, profile_id)
        self.__edited = []

    def get_edited(self):
        return self.__edited

    def add_edited(self, article):
        self.__edited.append(article)


profile = UserProfile(1, 2)
writerProfile = WriterProfile(1, 2)
readerProfile = ReaderProfile(1, 2)
editorProfile = EditorProfile(1, 2)
article = Article("new article")

profile.set_firstname("Kevin")
print(profile.get_firstname())

writerProfile.set_firstname("Michael")
print(writerProfile.get_firstname())
writerProfile.create_post(article)
print(writerProfile.get_posts()[0])

readerProfile.set_firstname("Joseph")
print(readerProfile.get_firstname())
readerProfile.add_bookmark(article)
print(readerProfile.get_bookmarked()[0])

editorProfile.set_firstname("Max")
print(editorProfile.get_firstname())
editorProfile.add_edited(article)
print(editorProfile.get_edited()[0])

