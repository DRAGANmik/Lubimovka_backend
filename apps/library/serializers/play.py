from rest_framework import serializers

from apps.library.models import Author, Play


class AuthorForPlaySerializer(serializers.ModelSerializer):
    """Сериализатор полного имени Автора."""

    name = serializers.ReadOnlyField(source="person.full_name")

    class Meta:
        model = Author
        fields = ("name", "slug")


class OtherPlaySerializer(serializers.ModelSerializer):
    """Сериализатор Пьесы с программой 'Другие пьесы'."""

    class Meta:
        model = Play
        fields = (
            "name",
            "link",
        )


class PlaySerializer(serializers.ModelSerializer):
    """Сериализатор Пьесы."""

    authors = AuthorForPlaySerializer(many=True)
    city = serializers.CharField(required=False, max_length=200, label="Город")
    year = serializers.IntegerField(required=False, min_value=0, max_value=32767, label="Год написания пьесы")
    url_reading = serializers.URLField(required=False)

    class Meta:
        fields = (
            "id",
            "name",
            "authors",
            "city",
            "year",
            "url_download",
            "url_reading",
        )
        model = Play
