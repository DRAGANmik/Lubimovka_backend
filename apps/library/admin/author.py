from adminsortable2.admin import SortableInlineAdminMixin
from django.contrib import admin
from django.forms import BaseInlineFormSet, ValidationError
from django.forms.formsets import DELETION_FIELD_NAME

from apps.library.forms import OtherLinkForm
from apps.library.models import Author, AuthorPlay, OtherLink, SocialNetworkLink


class PlayCheckInlineFormset(BaseInlineFormSet):
    def clean(self):
        super().clean()
        if any(self.errors):
            return  # Don't bother validating the formset unless each form is valid on its own
        for form in self.forms:
            if form.cleaned_data.get(DELETION_FIELD_NAME, False):
                if form.instance.play.author_plays.count() == 1:
                    raise ValidationError(
                        f"{form.instance.play} не может быть удалена, так как это единственный её автор"
                    )


class PlayInline(SortableInlineAdminMixin, admin.TabularInline):
    model = AuthorPlay
    extra = 0
    verbose_name = "Пьеса"
    verbose_name_plural = "Пьесы"
    classes = ("collapsible",)
    autocomplete_fields = ("play",)
    formset = PlayCheckInlineFormset

    readonly_fields = (
        "play_festival_year",
        "play_program",
    )

    def get_queryset(self, request):
        return AuthorPlay.objects.filter(play__other_play=False).select_related(
            "author__person",
            "play",
        )

    @admin.display(description="Год участия в фестивале")
    def play_festival_year(self, obj):
        return f"{obj.play.festival.year}"

    @admin.display(description="Программа")
    def play_program(self, obj):
        return f"{obj.play.program}"


class OtherPlayInline(SortableInlineAdminMixin, admin.TabularInline):
    model = AuthorPlay
    extra = 0
    verbose_name = "Другая пьеса"
    verbose_name_plural = "Другие пьесы"
    classes = ("collapsible",)
    autocomplete_fields = ("play",)

    def get_queryset(self, request):
        return AuthorPlay.objects.filter(play__other_play=True).select_related(
            "author__person",
            "play",
        )


class AchivementInline(admin.TabularInline):
    model = AuthorPlay
    extra = 0
    verbose_name = "Достижение"
    verbose_name_plural = "Достижения"
    classes = ("collapsible",)
    fields = ("achievement",)
    readonly_fields = ("achievement",)

    @admin.display(
        description="Достижения",
    )
    def achievement(self, obj):
        return f"{obj.play.program} - {obj.play.festival.year}"

    def get_queryset(self, request):
        return (
            AuthorPlay.objects.filter(play__other_play=False)
            .select_related("author__person", "play__program", "play__festival")
            .order_by("-play__festival__year")
            .distinct("play__festival__year", "play__program")
        )

    def has_add_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


class SocialNetworkLinkInline(admin.TabularInline):
    model = SocialNetworkLink
    extra = 1
    classes = ("collapsible",)


class OtherLinkInline(SortableInlineAdminMixin, admin.TabularInline):
    form = OtherLinkForm
    model = OtherLink
    extra = 1
    classes = ("collapsible",)


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = (
        "person",
        "quote",
        "biography",
        "slug",
    )
    inlines = (
        PlayInline,
        OtherPlayInline,
        SocialNetworkLinkInline,
        OtherLinkInline,
        AchivementInline,
    )
    exclude = (
        "plays",
        "social_network_links",
        "other_links",
    )
    search_fields = (
        "biography",
        "slug",
        "person__first_name",
        "person__last_name",
        "person__middle_name",
        "person__email",
        "plays__name",
    )
    autocomplete_fields = ("person",)
    empty_value_display = "-пусто-"

    def get_queryset(self, request):
        return super().get_queryset(request).select_related("person")

    class Media:
        js = ("admin/author_admin.js",)
