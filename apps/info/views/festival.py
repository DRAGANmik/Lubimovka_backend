from django.db.models import Prefetch
from django.shortcuts import get_object_or_404
from drf_spectacular.utils import extend_schema
from rest_framework.generics import RetrieveAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.info.models import Festival, FestivalInfoLink
from apps.info.serializers import FestivalSerializer, YearsSerializer


class FestivalAPIView(RetrieveAPIView):
    """Returns a festival info and statistics.

    URL detailed lookup suffix is `year`.
    """

    queryset = Festival.objects.all()
    serializer_class = FestivalSerializer
    lookup_field = "year"
    pagination_class = None

    def get_object(self):
        festival = get_object_or_404(
            Festival.objects.prefetch_related(
                Prefetch(
                    "festival_links",
                    queryset=FestivalInfoLink.objects.filter(link__type="plays_links"),
                    to_attr="plays_links",
                ),
                Prefetch(
                    "festival_links",
                    queryset=FestivalInfoLink.objects.filter(link__type="additional_links"),
                    to_attr="additional_links",
                ),
            ),
            year=self.kwargs["year"],
        )
        return festival


class FestivalYearsAPIView(APIView):
    """Returns a list of the years in which the festival took place."""

    @extend_schema(responses=YearsSerializer)
    def get(self, request):
        years_values_list = Festival.objects.values_list("year", flat=True)
        years_instance = {"years": years_values_list}
        years_serializer = YearsSerializer(instance=years_instance)
        return Response(years_serializer.data)
