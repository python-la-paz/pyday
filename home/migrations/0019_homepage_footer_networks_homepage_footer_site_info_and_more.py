# Generated by Django 4.1.7 on 2023-02-22 05:28

from django.db import migrations, models
import wagtail.blocks
import wagtail.fields


class Migration(migrations.Migration):
    dependencies = [
        ("home", "0018_alter_segmentpage_segments"),
    ]

    operations = [
        migrations.AddField(
            model_name="homepage",
            name="footer_networks",
            field=wagtail.fields.StreamField(
                [
                    (
                        "networks",
                        wagtail.blocks.StructBlock(
                            [
                                (
                                    "classname",
                                    wagtail.blocks.CharBlock(
                                        max_length=250, required=True
                                    ),
                                ),
                                (
                                    "lni_icon",
                                    wagtail.blocks.CharBlock(
                                        help_text="(lni lni-help) https://lineicons.com/icons/",
                                        required=True,
                                    ),
                                ),
                                ("url", wagtail.blocks.URLBlock(required=True)),
                            ]
                        ),
                    )
                ],
                blank=True,
                use_json_field=False,
            ),
        ),
        migrations.AddField(
            model_name="homepage",
            name="footer_site_info",
            field=wagtail.fields.RichTextField(blank=True),
        ),
        migrations.AddField(
            model_name="homepage",
            name="footer_title",
            field=models.CharField(blank=True, max_length=250),
        ),
    ]