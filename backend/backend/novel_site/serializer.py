from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        return token

    def validate(self, attrs):
        data = super().validate(attrs)
        re_data = {
            "data": data,
            "code": 200,
            "message": "success",
            "user_id": self.user.user_uuid,
            "user_name": self.user.username,
            "user_type": self.user.user_type
        }
        return re_data