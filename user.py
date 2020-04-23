
class User:

    def __init__(self, name, followers, following, business_category, is_verified, media_amount):
        self.name = name
        self.followers = followers
        self.following = following
        self.business_category = business_category
        self.is_verified = is_verified
        self.media_amount = media_amount
        self.photos = []
        self.videos = []
        self.total_likes = 0
        self.avg_likes = 0
        self.total_comments = 0
        self.avg_comments = 0
        self.avg_likes_photos = 0
        self.avg_comments_photos = 0
        self.avg_likes_videos = 0
        self.avg_comments_videos = 0
        self.avg_duration_videos = 0
        self.avg_views_videos = 0

    def print_info(self):
        print('Name: ' + self.name)
        print('Followers: ' + str(self.followers))
        print('Following: ' + str(self.following))
        print('Business category: ' + str(self.business_category))
        print('Account verified: ' + str(self.is_verified))
        print('Amount of posts: ' + str(self.media_amount))
        print('Amount of photos: ' + str(len(self.photos)))
        print('Amount of videos: ' + str(len(self.videos)))
        print('Average of likes per post: ' + str(self.avg_likes))
        print('Average of comments per post: ' + str(self.avg_comments))
        print('Average of likes per photo: ' + str(self.avg_likes_photos))
        print('Average of comments per photo: ' + str(self.avg_comments_photos))
        print('Average of likes per video: ' + str(self.avg_likes_videos))
        print('Average of comments per video: ' + str(self.avg_comments_videos))

    def calculate_photo_averages(self):
        total_likes_photos = 0
        total_comments_photos = 0

        for photo in self.photos:
            total_likes_photos = total_likes_photos + photo.likes_amount
            total_comments_photos = total_comments_photos + photo.comments_amount

        print(total_likes_photos)

        if len(self.photos) != 0:
            self.avg_likes_photos = total_likes_photos / len(self.photos)
            self.avg_comments_photos = total_comments_photos / len(self.photos)
            self.total_likes = self.total_likes + total_likes_photos
            self.total_comments = self.total_comments + total_comments_photos

    def calculate_videos_averages(self):
        total_likes_videos = 0
        total_comments_videos = 0

        for video in self.videos:
            total_likes_videos = total_likes_videos + video.likes_amount
            total_comments_videos = total_comments_videos + video.comments_amount

        if len(self.videos)!= 0:
            self.avg_likes_videos = total_likes_videos / len(self.videos)
            self.avg_comments_videos = total_comments_videos / len(self.videos)
            self.total_likes = self.total_likes + total_likes_videos
            self.total_comments = self.total_comments + total_comments_videos

    def calculate_media_averages(self):
        media_length = len(self.photos) + len(self.videos)
        self.avg_likes = self.total_likes/ media_length
        self.avg_comments = self.total_comments / media_length