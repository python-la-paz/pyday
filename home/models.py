from django.db import models
from wagtail.fields import RichTextField, StreamField
from wagtail.models import Page
from wagtail.admin.panels import FieldPanel
from wagtail import blocks
from wagtail.images.blocks import ImageChooserBlock


class HomePage(Page):
    event = models.CharField(max_length=250, blank=True)
    about = RichTextField(blank=True)
    location = models.CharField(max_length=250, blank=True)
    literal_date = models.CharField(max_length=250, blank=True)
    url_get_tickets = models.URLField(blank=True)
    text_get_tickets = models.CharField(
        max_length=250, blank=True, default="Get tickets"
    )
    event_date = models.DateField(blank=True, null=True)

    logo_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )
    logo_image_big = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )
    hero_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )
    footer_title = models.CharField(max_length=250, blank=True)
    footer_site_info = RichTextField(blank=True)
    footer_networks = StreamField(
        [
            (
                "networks",
                blocks.StructBlock(
                    [
                        ("classname", blocks.CharBlock(max_length=250, required=True)),
                        (
                            "lni_icon",
                            blocks.CharBlock(
                                help_text="(lni lni-help) https://lineicons.com/icons/",
                                required=True,
                            ),
                        ),
                        (
                            "url",
                            blocks.URLBlock(required=True),
                        ),
                    ]
                ),
            ),
        ],
        blank=True,
        use_json_field=False,
    )
    color_gradient_1 = models.CharField(max_length=250, blank=True, default="#FF4D79")
    color_gradient_2 = models.CharField(max_length=250, blank=True, default="#FF809F")
    color_primary = models.CharField(max_length=250, blank=True, default="#ff4a67")
    show_time = models.BooleanField(default=True)
    message_show_time = models.CharField(max_length=250, blank=True, default="Pr??ximamente...")

    content_panels = Page.content_panels + [
        FieldPanel("event"),
        FieldPanel("about"),
        FieldPanel("location"),
        FieldPanel("literal_date"),
        FieldPanel("url_get_tickets"),
        FieldPanel("text_get_tickets"),
        FieldPanel("event_date"),
        FieldPanel("logo_image"),
        FieldPanel("logo_image_big"),
        FieldPanel("hero_image"),
        FieldPanel("footer_title"),
        FieldPanel("footer_site_info"),
        FieldPanel("footer_networks"),
        FieldPanel("color_gradient_1"),
        FieldPanel("color_gradient_2"),
        FieldPanel("color_primary"),
        FieldPanel("show_time"),
        FieldPanel("message_show_time"),
    ]

    def get_context(self, request):
        # Update context to include only published posts, ordered by reverse-chron
        context = super().get_context(request)
        segments = SegmentPage.objects.child_of(self).live().order_by("order")
        context["segments"] = segments  # sorted (segments, key=lambda x: x.order)
        return context


class InformationBlock(blocks.StructBlock):
    lni_icon = blocks.CharBlock(help_text="(lni lni-help) https://lineicons.com/icons/")
    title = blocks.CharBlock()
    description = blocks.CharBlock()


class SponsorBlock(blocks.StructBlock):
    name = blocks.CharBlock()
    image = ImageChooserBlock(required=False)
    level = blocks.ChoiceBlock(
        choices=[
            ("silver", "Plata"),
            ("gold", "Oro"),
            ("diamond", "Diamante"),
        ],
        default="silver",
    )
    url = blocks.URLBlock(required=False)

class TiersBlock(blocks.StructBlock):
    classname = blocks.CharBlock(required=False)
    name = blocks.CharBlock()
    pricing = blocks.CharBlock()
    detail_pricing = blocks.CharBlock()
    image = ImageChooserBlock(required=False)
    benefits = blocks.ListBlock(blocks.CharBlock(required=False))
    no_benefits = blocks.ListBlock(blocks.CharBlock(required=False))
    url = blocks.URLBlock(required=False)
    url_text = blocks.CharBlock(required=False, default="Buy now")


class SegmentPage(Page):
    order = models.IntegerField(default=0)
    segments = StreamField(
        [
            # detail segment
            (
                "detail_segment",
                blocks.StructBlock(
                    [
                        ("name", blocks.CharBlock(max_length=250, blank=False)),
                        ("description", blocks.RichTextBlock(required=False)),
                        (
                            "list_options",
                            blocks.ListBlock(blocks.CharBlock(required=False)),
                        ),
                        ("url", blocks.URLBlock(required=False)),
                        (
                            "url_text",
                            blocks.CharBlock(
                                max_length=250, required=False, default="More info"
                            ),
                        ),
                        ("image", ImageChooserBlock(required=False)),
                        (
                            "position",
                            blocks.ChoiceBlock(
                                choices=[
                                    ("left", "Izquierda"),
                                    ("right", "Derecha"),
                                ],
                                default="left",
                            ),
                        ),
                    ]
                ),
            ),
            # video segment
            (
                "video_segment",
                blocks.StructBlock(
                    [
                        (
                            "url",
                            blocks.URLBlock(blank=True),
                        ),
                    ]
                ),
            ),
            (
                "information_segment",
                blocks.StructBlock(
                    [
                        (
                            "id_tag",
                            blocks.CharBlock(
                                max_length=250, required=False, default="contact-text"
                            ),
                        ),
                        (
                            "class_name",
                            blocks.CharBlock(
                                max_length=250,
                                required=False,
                                default="contact-wrapper",
                            ),
                        ),
                        (
                            "list_information",
                            blocks.ListBlock(InformationBlock, max_num=4),
                        ),
                    ]
                ),
            ),
            (
                "sponsor_segment",
                blocks.StructBlock(
                    [
                        (
                            "name",
                            blocks.CharBlock(
                                max_length=250, required=True, default="Sponsors"
                            ),
                        ),
                        ("description", blocks.RichTextBlock(required=False)),
                        ("background", ImageChooserBlock(required=False)),
                        ("sponsors", blocks.ListBlock(SponsorBlock)),
                    ]
                ),
            ),
            (
                "maps_segment",
                blocks.StructBlock(
                    [
                        (
                            "url",
                            blocks.URLBlock(
                                blank=True,
                                help_text="https://www.google.com/maps/embed?pb=.....",
                            ),
                        ),
                    ]
                ),
            ),
            (
                "pricing_segment",
                blocks.StructBlock(
                    [
                        (
                            "name",
                            blocks.CharBlock(
                                max_length=250, required=True, default="Pricing"
                            ),
                        ),
                        ("description", blocks.RichTextBlock(required=False)),
                        ("tiers", blocks.ListBlock(TiersBlock)),
                    ]
                ),
            ),
        ],
        blank=True,
        use_json_field=False,
        max_num=1,
    )

    content_panels = Page.content_panels + [
        FieldPanel("order"),
        FieldPanel("segments"),
    ]
