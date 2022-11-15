from SIGPE.settings import MEDIA_URL, STATIC_URL


class Media:
    def get_image(self, image):
        if image:
            return '{}{}'.format(MEDIA_URL,image)
        return '{}{}'.format(STATIC_URL,'img/empty.png')