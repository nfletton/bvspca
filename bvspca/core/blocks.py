from wagtail.contrib.table_block.blocks import TableBlock
from wagtail.core import blocks
from wagtail.documents.blocks import DocumentChooserBlock
from wagtail.images.blocks import ImageChooserBlock
from wagtail.embeds.blocks import EmbedBlock
from wagtail.core.blocks import (
    CharBlock, ChoiceBlock, RichTextBlock, StreamBlock, StructBlock, TextBlock,
    RawHTMLBlock, PageChooserBlock)


class DonateBlock(blocks.StructBlock):
    button_name = CharBlock(default='Donate5.png')

    class Meta:
        template = 'core/blocks/donate_button.html'
        icon = 'fa-money'


class VideoBlock(StructBlock):
    video = EmbedBlock(required=True)
    caption = CharBlock(required=False)

    class Meta:
        label = 'Video'
        template = 'core/blocks/video.html'
        icon = 'fa-video-camera'


class ImageBlock(StructBlock):
    image = ImageChooserBlock(required=True)
    caption = CharBlock(required=False)
    attribution = CharBlock(required=False)

    class Meta:
        label = 'Image'
        icon = 'image'
        template = 'core/blocks/image_block.html'


class DocumentBlock(StructBlock):
    document = DocumentChooserBlock(required=True)

    class Meta:
        label = 'Document'
        icon = 'fa-file-text'
        template = 'core/blocks/document_block.html'


class HeadingBlock(StructBlock):
    heading_text = CharBlock(classname='title', required=True)
    size = ChoiceBlock(choices=[
        ('', 'Select a header size'),
        ('h2', 'H2'),
        ('h3', 'H3'),
        ('h4', 'H4')
    ], blank=True, required=False)

    class Meta:
        label = 'Heading'
        icon = 'fa-header'
        template = 'core/blocks/heading_block.html'


class BlockQuote(StructBlock):
    text = TextBlock()
    attribute_name = CharBlock(
        blank=True, required=False, label='e.g. Mary Berry')

    class Meta:
        label = 'Quote'
        icon = 'fa-quote-left'
        template = 'core/blocks/quote-block.html'


class ContentTableBlock(StructBlock):
    table = TableBlock()
    caption = CharBlock(required=False)

    class Meta:
        label = 'Table'
        icon = 'fa-table'
        template = 'core/blocks/table_block.html'


class ContentRawHTML(StructBlock):
    html = RawHTMLBlock()

    class Meta:
        label = 'Raw HTML'
        icon = 'fa-code'
        template = 'core/blocks/raw_html_block.html'


class ExternalLinkBlock(StructBlock):
    title = blocks.CharBlock()
    url = blocks.URLBlock()

    class Meta:
        template = 'core/blocks/external_link_block.html'
        icon = 'fa-external-link'


class ContentStreamBlock(StreamBlock):
    heading_block = HeadingBlock()
    paragraph_block = RichTextBlock(
        label='Paragraph',
        icon='fa-paragraph',
    )
    image_block = ImageBlock()
    document_block = DocumentBlock()
    external_link = ExternalLinkBlock()
    block_quote = BlockQuote()
    embed_block = EmbedBlock(
        label='Embedded Media',
        help_text='Insert an embed URL e.g https://www.youtube.com/embed/SGJFWirQ3ks',
        icon='fa-external-link-square',
        template='core/blocks/embed_block.html',
    )
    table_block = ContentTableBlock()
    raw_html = ContentRawHTML()
    donate_button = DonateBlock()


class TeamMemberBlock(blocks.StructBlock):
    name = blocks.CharBlock(max_length=50)
    role = blocks.CharBlock(max_length=50, required=False)
    role_since = blocks.CharBlock(max_length=50, required=False)
    location = blocks.CharBlock(max_length=50, required=False)
    pets = blocks.CharBlock(max_length=200, required=False)
    bio = blocks.RichTextBlock(required=False)
    photo = ImageChooserBlock(
        required=False,
        help_text='Image should be at least 350px x 350px',
    )

    class Meta:
        template = 'core/blocks/team_member.html'
        icon = 'user'


class PictureLinkBlock(blocks.StructBlock):
    title = blocks.CharBlock(max_length=50)
    image = ImageChooserBlock()
    page = PageChooserBlock()

    class Meta:
        template = 'core/blocks/picture_link.html'
        icon = 'fa-camera-retro'


class SupporterBlock(blocks.StructBlock):
    name = blocks.CharBlock(max_length=100)
    summary = blocks.TextBlock()
    logo = ImageChooserBlock(required=False)
    url = blocks.URLBlock(required=False)

    class Meta:
        template = 'core/blocks/supporter_block.html'
        icon = 'fa-money'


class SliderBlock(blocks.StructBlock):
    title = blocks.CharBlock(max_length=25, required=False)
    summary = blocks.TextBlock(max_length=60, required=False)
    photo = ImageChooserBlock(help_text='This image MUST BE EXACTLY 1400px by 475px')
    page = PageChooserBlock(required=False)

    class Meta:
        template = 'core/blocks/slider_block.html'
        icon = 'fa-slideshare'
