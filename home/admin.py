from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from parler.admin import TranslatableAdmin, TranslatableTabularInline

from .models import Section, Branch, Phone, Slider, Service, Partner, Client, Testimonial

# Register your models here.

admin.site.site_header = _("itbuild Dashboard")
admin.site.site_title = _("itbuild Admin")


class InlineSlider(TranslatableTabularInline):
    model = Slider
    extra = 1


class InlineService(TranslatableTabularInline):
    model = Service
    extra = 1


class InlinePartner(TranslatableTabularInline):
    model = Partner
    extra = 1


class InlineClient(TranslatableTabularInline):
    model = Client
    extra = 1


class InlineTestimonial(TranslatableTabularInline):
    model = Testimonial
    extra = 1


@admin.register(Section)
class SectionAdmin(TranslatableAdmin):
    inlines = [InlineSlider, InlineService, InlinePartner, InlineClient, InlineTestimonial]
    fieldsets = [
        (
            _('SEO'),
            {
                "fields": ['page_title', 'page_description'],
            },
        ),
        (
            _('Short Services'),
            {
                "fields": ['short_service_title1', 'short_service_description1', 'short_service_icon1',
                           'short_service_title2', 'short_service_description2', 'short_service_icon2',
                           'short_service_title3', 'short_service_description3', 'short_service_icon3'],
            },
        ),
        (
            _('ABOUT ITBUILD'),
            {
                "fields": ['about_us_title', 'about_us_description', 'about_us_footer_text', 'about_us_main_image',
                           'about_us_sec_image', 'our_vision_text', 'our_mission_text'],
            },
        ),
        (
            _('Professional Team'),
            {
                "fields": ['team_title1', 'team_description1', 'team_title2', 'team_description2', 'team_image'],
            },
        ),
        (
            _('Data Center'),
            {
                "fields": ['data_center_text', 'data_center_main_image', 'data_center_sec_image'],
            },
        ),
        (
            _('Digital Workspaces Solutions'),
            {
                "fields": ['digital_workspace_title1', 'digital_workspace_description1', 'digital_workspace_title2',
                           'digital_workspace_description2', 'digital_workspace_title3',
                           'digital_workspace_description3', 'digital_workspace_title4',
                           'digital_workspace_description4', 'digital_workspace_image'],
            },
        ),
        (
            _('contact'),
            {
                "fields": ['main_phone', 'email', 'map', 'whatsapp_phone', 'facebook', 'twitter', 'linkedin'],
            },
        ),
        (
            None,
            {
                "fields": ['active'],
            },
        ),
    ]
    list_display = ('page_title', 'active')
    list_filter = ('active',)


class InlinePhone(TranslatableTabularInline):
    model = Phone
    extra = 1


@admin.register(Branch)
class BranchAdmin(TranslatableAdmin):
    inlines = [InlinePhone, ]
    fields = ('section', 'address')
    search_fields = ['translations__address__icontains']


@admin.register(Phone)
class PhoneAdmin(TranslatableAdmin):
    fields = ('branch', 'phone', 'phone_type')
    search_fields = ['phone']


@admin.register(Slider)
class SliderAdmin(TranslatableAdmin):
    fields = ('section', 'bg_image', 'title', 'sub_title')
    search_fields = ['translations__title__icontains']


@admin.register(Service)
class ServiceAdmin(TranslatableAdmin):
    fields = ('section', 'name', 'description', 'icon', 'image')
    search_fields = ['translations__name__icontains']


@admin.register(Partner)
class PartnerAdmin(TranslatableAdmin):
    fields = ('section', 'name', 'image')
    search_fields = ['translations__name__icontains']


@admin.register(Client)
class ClientAdmin(TranslatableAdmin):
    fields = ('section', 'name', 'image')
    search_fields = ['translations__name__icontains']


@admin.register(Testimonial)
class TestimonialAdmin(TranslatableAdmin):
    fields = ('section', 'name', 'description', 'feedback', 'image')
    search_fields = ['translations__name__icontains', 'translations__description__icontains',
                     'translations__feedback__icontains']
