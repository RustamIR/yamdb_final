from rest_framework import serializers
from users.models import Users
from api.models import Review, Comment


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ("username",
                  "pk",
                  "first_name",
                  "last_name",
                  "email",
                  "role",
                  "bio")


class EmailSerializer(serializers.ModelSerializer):
    email = serializers.EmailField()

    class Meta:
        model = Users
        fields = ('email',)


class EmailCodeSerializer(serializers.ModelSerializer):
    email = serializers.EmailField()
    code = serializers.CharField(max_length=30)

    class Meta:
        model = Users
        fields = ('email', 'code')


class ReviewSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username'
    )

    class Meta:
        model = Review
        exclude = ('title',)


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username'
    )

    class Meta:
        model = Comment
        exclude = ('review',)
