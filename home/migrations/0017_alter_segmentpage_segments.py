# Generated by Django 4.1.7 on 2023-02-22 05:11

from django.db import migrations
import home.models
import wagtail.blocks
import wagtail.fields
import wagtail.images.blocks


class Migration(migrations.Migration):
    dependencies = [
        ("home", "0016_alter_segmentpage_segments"),
    ]

    operations = [
        migrations.AlterField(
            model_name="segmentpage",
            name="segments",
            field=wagtail.fields.StreamField(
                [
                    (
                        "detail_segment",
                        wagtail.blocks.StructBlock(
                            [
                                (
                                    "name",
                                    wagtail.blocks.CharBlock(
                                        blank=False, max_length=250
                                    ),
                                ),
                                (
                                    "description",
                                    wagtail.blocks.RichTextBlock(required=False),
                                ),
                                (
                                    "list_options",
                                    wagtail.blocks.ListBlock(
                                        wagtail.blocks.CharBlock(required=False)
                                    ),
                                ),
                                ("url", wagtail.blocks.URLBlock(required=False)),
                                (
                                    "url_text",
                                    wagtail.blocks.CharBlock(
                                        default="More info",
                                        max_length=250,
                                        required=False,
                                    ),
                                ),
                                (
                                    "image",
                                    wagtail.images.blocks.ImageChooserBlock(
                                        required=False
                                    ),
                                ),
                                (
                                    "position",
                                    wagtail.blocks.ChoiceBlock(
                                        choices=[
                                            ("left", "Izquierda"),
                                            ("right", "Derecha"),
                                        ]
                                    ),
                                ),
                            ]
                        ),
                    ),
                    (
                        "video_segment",
                        wagtail.blocks.StructBlock(
                            [("url", wagtail.blocks.URLBlock(blank=True))]
                        ),
                    ),
                    (
                        "information_segment",
                        wagtail.blocks.StructBlock(
                            [
                                (
                                    "class_name",
                                    wagtail.blocks.CharBlock(
                                        default="contact-text",
                                        max_length=250,
                                        required=False,
                                    ),
                                ),
                                (
                                    "list_information",
                                    wagtail.blocks.ListBlock(
                                        home.models.InformationBlock, max_num=4
                                    ),
                                ),
                            ]
                        ),
                    ),
                    (
                        "sponsor_segment",
                        wagtail.blocks.StructBlock(
                            [
                                (
                                    "name",
                                    wagtail.blocks.CharBlock(
                                        default="Sponsors",
                                        max_length=250,
                                        required=True,
                                    ),
                                ),
                                (
                                    "description",
                                    wagtail.blocks.RichTextBlock(required=False),
                                ),
                                (
                                    "sponsors",
                                    wagtail.blocks.ListBlock(home.models.SponsorBlock),
                                ),
                            ]
                        ),
                    ),
                    (
                        "maps_segment",
                        wagtail.blocks.StructBlock(
                            [
                                (
                                    "url",
                                    wagtail.blocks.URLBlock(
                                        blank=True,
                                        help_text="https://www.google.com/maps/embed?pb=.....",
                                    ),
                                )
                            ]
                        ),
                    ),
                ],
                blank=True,
                use_json_field=False,
            ),
        ),
    ]
