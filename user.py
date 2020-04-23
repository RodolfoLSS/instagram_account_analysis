
class User:

    def __init__(self, name, followers, following, business_category, is_verified, media_amount):
        self.name = name
        self.followers = followers
        self.following = following
        self.business_category = business_category
        self.is_verified = is_verified
        self.media_amount = media_amount

    def print_info(self):
        print('Name: ' + self.name)
        print('Followers: ' + str(self.followers))
        print('Following: ' + str(self.following))
        print('Business category: ' + self.business_category)
        print('Account verified: ' + str(self.is_verified))
        print('Amount of posts: ' + str(self.media_amount))