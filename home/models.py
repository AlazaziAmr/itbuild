from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.dispatch import receiver
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django_resized import ResizedImageField
from fontawesome_6.fields import IconField
from parler.models import TranslatableModel, TranslatedFields


# Create your models here.
class Section(TranslatableModel):
    translations = TranslatedFields(
        page_title=models.CharField(_('page_title'), max_length=60, help_text=_('page_title_help_text')),
        page_description=models.TextField(_('page_description'), help_text=_('page_description_help_text')),
        short_service_title1=models.CharField(_('short_service_title1'), max_length=60,
                                              help_text=_('short_service_title1_help_text')),
        short_service_description1=models.CharField(_('short_service_description1'), max_length=255,
                                                    help_text=_('short_service_description1_help_text')),
        short_service_title2=models.CharField(_('short_service_title2'), max_length=60,
                                              help_text=_('short_service_title2_help_text')),
        short_service_description2=models.CharField(_('short_service_description2'), max_length=255,
                                                    help_text=_('short_service_description2_help_text')),
        short_service_title3=models.CharField(_('short_service_title3'), max_length=60,
                                              help_text=_('short_service_title3_help_text')),
        short_service_description3=models.CharField(_('short_service_description3'), max_length=255,
                                                    help_text=_('short_service_description3_help_text')),
        about_us_title=models.CharField(_('about_us_title'), max_length=60, help_text=_('about_us_title_help_text')),
        about_us_description=models.TextField(_('about_us_description'), help_text=_('about_us_description_help_text')),
        about_us_footer_text=models.TextField(_('about_us_description'), help_text=_('about_us_footer_text_help_text')),
        our_vision_text=models.TextField(_('our_vision_text'), help_text=_('our_vision_help_text')),
        our_mission_text=models.TextField(_('our_mission_text'), help_text=_('our_mission_text_help_text')),
        team_title1=models.CharField(_('team_title1'), max_length=60, help_text=_('team_title1_help_text')),
        team_description1=models.TextField(_('team_description1'), help_text=_('team_description1_help_text')),
        team_title2=models.CharField(_('team_title2'), max_length=60, help_text=_('team_title2_help_text')),
        team_description2=models.TextField(_('team_description2'), help_text=_('team_description2_help_text')),
        data_center_text=models.TextField(_('data_center_text'), help_text=_('data_center_text_help_text')),
        digital_workspace_title1=models.CharField(_('digital_workspace_title1'), max_length=60,
                                                  help_text=_('digital_workspace_title1_help_text')),
        digital_workspace_description1=models.TextField(_('digital_workspace_description1'),
                                                        help_text=_('digital_workspace_description1_help_text')),
        digital_workspace_title2=models.CharField(_('digital_workspace_title2'), max_length=60,
                                                  help_text=_('digital_workspace_title2_help_text')),
        digital_workspace_description2=models.TextField(_('digital_workspace_description2'),
                                                        help_text=_('digital_workspace_description2_help_text')),
        digital_workspace_title3=models.CharField(_('digital_workspace_title3'), max_length=60,
                                                  help_text=_('digital_workspace_title3_help_text')),
        digital_workspace_description3=models.TextField(_('digital_workspace_description3'),
                                                        help_text=_('digital_workspace_description3_help_text')),
        digital_workspace_title4=models.CharField(_('digital_workspace_title4'), max_length=60,
                                                  help_text=_('digital_workspace_title4_help_text')),
        digital_workspace_description4=models.TextField(_('digital_workspace_description4'),
                                                        help_text=_('digital_workspace_description4_help_text')),
    )
    short_service_icon1 = IconField(_('short_service_icon1'), help_text=_('short_service_icon1_help_text'), null=False, blank=False)
    short_service_icon2 = IconField(_('short_service_icon2'), help_text=_('short_service_icon2_help_text'))
    short_service_icon3 = IconField(_('short_service_icon3'), help_text=_('short_service_icon3_help_text'))
    about_us_main_image = ResizedImageField(_('about_us_main_image'), size=[470, 528], quality=90, force_format="WEBP",
                                            upload_to="images/home/")
    about_us_sec_image = ResizedImageField(_('about_us_sec_image'), size=[301, 373], quality=90, force_format="WEBP",
                                           upload_to="images/home/")
    team_image = ResizedImageField(_('team_image'), size=[958, 695], quality=90, force_format="WEBP",
                                   upload_to="images/home/")
    data_center_main_image = ResizedImageField(_('data_center_main_image'), size=[370, 540], quality=90,
                                               force_format="WEBP", upload_to="images/home/")
    data_center_sec_image = ResizedImageField(_('data_center_sec_image'), size=[421, 288], quality=90,
                                              force_format="WEBP", upload_to="images/home/")
    digital_workspace_image = ResizedImageField(_('digital_workspace_image'), size=[502, 700], quality=90,
                                                force_format="WEBP", upload_to="images/home/")
    main_phone = PhoneNumberField(_('main_phone'), help_text=_('main_phone_help_text'))
    email = models.EmailField(_('email'))
    map = models.TextField(_('map'), help_text=_('map_help_text'))
    whatsapp_phone = PhoneNumberField(_('whatsapp_phone'), help_text=_('whatsapp_phone_help_text'))
    facebook = models.URLField(_('facebook_url'))
    twitter = models.URLField(_('twitter_url'))
    linkedin = models.URLField(_('linkedin_url'))
    active = models.BooleanField(_('active'), default=True)

    def __str__(self):
        return self.page_title

    def get_absolute_url(self):
        return reverse('home')

    class Meta:
        verbose_name = _('home_page')
        verbose_name_plural = _('home_page')
        ordering = ['id']


class Branch(TranslatableModel):
    translations = TranslatedFields(
        address=models.TextField(_('address'), help_text=_('branch_address_help_text')),
    )
    section = models.ForeignKey(Section, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.address
        
    class Meta:
        verbose_name = _('branch')
        verbose_name_plural = _('branches')
        ordering = ['id']


class Phone(TranslatableModel):
    Types = (
        ("0", _('Mobile')),
        ("1", _('Landline')),
    )
    translations = TranslatedFields(
        phone_type=models.CharField(_('phone_type'), max_length=20, choices=Types, default=0,
                                    help_text=_('phone_type_help_text')),
    )
    phone = PhoneNumberField(_('phone'), help_text=_('phone_help_text'))
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)
    
    def __str__(self):
        return str(self.phone)
        
    class Meta:
        verbose_name = _('phone')
        verbose_name_plural = _('phones')
        ordering = ['id']


class Slider(TranslatableModel):
    translations = TranslatedFields(
        title=models.CharField(_('title'), max_length=200, help_text=_('title_help_text')),
        sub_title=models.CharField(_('sub_title'), max_length=30, help_text=_('sub_title_help_text')),
    )
    bg_image = ResizedImageField(_('bg_image'), size=[1920, 900], quality=90, force_format="WEBP",
                                 upload_to="images/home/slider/")
    section = models.ForeignKey(Section, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('slider')
        verbose_name_plural = _('sliders')
        ordering = ['id']


class Service(TranslatableModel):
    translations = TranslatedFields(
        name=models.CharField(_('service_name'), max_length=60, help_text=_('service_name_help_text')),
        description=models.TextField(_('service_description'), help_text=_('service_description_help_text'))
    )
    icon = IconField(_('service_icon'), help_text=_('service_icon'))
    image = ResizedImageField(_('service_image'), size=[550, 450], quality=90, force_format="WEBP",
                              upload_to="images/home/service/")
    section = models.ForeignKey(Section, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('service')
        verbose_name_plural = _('services')
        ordering = ['id']


class Partner(TranslatableModel):
    translations = TranslatedFields(
        name=models.CharField(_('partner_name'), max_length=30, help_text=_('partner_name_help_text')),
    )
    image = ResizedImageField(_('partner_image'), size=[309, 172], quality=90, force_format="WEBP",
                              upload_to="images/home/partner/")
    section = models.ForeignKey(Section, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('partner')
        verbose_name_plural = _('partners')
        ordering = ['id']


class Client(TranslatableModel):
    translations = TranslatedFields(
        name=models.CharField(_('client_name'), max_length=30, help_text=_('client_name_help_text')),
    )
    image = ResizedImageField(_('client_image'), size=[144, 120], quality=90, force_format="WEBP",
                              upload_to="images/home/client/")
    section = models.ForeignKey(Section, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('client')
        verbose_name_plural = _('clients')
        ordering = ['id']


class Testimonial(TranslatableModel):
    translations = TranslatedFields(
        name=models.CharField(_('testimonial_name'), max_length=30, help_text=_('testimonial_name_help_text')),
        description=models.CharField(_('testimonial_description'), max_length=60,
                                     help_text=_('testimonial_description_help_text')),
        feedback=models.TextField(_('testimonial_feedback'), max_length=1000,
                                  help_text=_('testimonial_feedback_help_text')),
    )
    image = ResizedImageField(_('testimonial_image'), size=[110, 110], quality=90, force_format="WEBP",
                              upload_to="images/home/testimonial/")
    section = models.ForeignKey(Section, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('testimonial')
        verbose_name_plural = _('testimonials')
        ordering = ['id']


@receiver(models.signals.post_delete, sender=Section)
def delete_home_images(sender, instance, **kwargs):
    instance.about_us_main_image.delete(save=False)
    instance.about_us_sec_image.delete(save=False)
    instance.team_image.delete(save=False)
    instance.data_center_main_image.delete(save=False)
    instance.data_center_sec_image.delete(save=False)
    instance.digital_workspace_image.delete(save=False)


@receiver(models.signals.post_delete, sender=Slider)
def delete_slider_images(sender, instance, **kwargs):
    instance.bg_image.delete(save=False)


@receiver(models.signals.post_delete, sender=Service)
def delete_service_images(sender, instance, **kwargs):
    instance.image.delete(save=False)


@receiver(models.signals.post_delete, sender=Partner)
def delete_partner_images(sender, instance, **kwargs):
    instance.image.delete(save=False)


@receiver(models.signals.post_delete, sender=Client)
def delete_client_images(sender, instance, **kwargs):
    instance.image.delete(save=False)


@receiver(models.signals.post_delete, sender=Testimonial)
def delete_testimonial_images(sender, instance, **kwargs):
    instance.image.delete(save=False)
