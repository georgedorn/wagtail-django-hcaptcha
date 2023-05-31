Wagtail hCaptcha
======================

Wagtail forms with a hCaptcha form field/widget integration app. Wagtail hCaptcha provides an easy way to integrate the `django-hCaptcha <https://github.com/AndrejZbin>`_ field when using the Wagtail formbuilder.

This app is a modification of `wagtail-django-recaptcha <https://github.com/springload/wagtail-django-recaptcha>` by Springload.

Check out `Awesome Wagtail <https://github.com/springload/awesome-wagtail>`_ for more awesome packages and resources from the Wagtail community.

Installation
------------

#. Install wagtailcaptcha via pip ``pip install wagtail-django-hcaptcha`` or add ``wagtailcaptcha`` to your Python path.  (Note: not yet on PyPI; use ``pip install git+https://github.com/georgedorn/wagtail-django-hcaptcha`` until it is).

#. Add ``wagtailcaptcha`` and ``hcaptcha`` to your ``INSTALLED_APPS`` setting.

#. Configure django-hCaptcha as explained in `here <https://github.com/AndrejZbin/django-hcaptcha>`_.

Usage
-----

Field
~~~~~

The quickest way to add a captcha field to a Wagtail Form Page is to inherit from the two options provided, ``WagtailCaptchaForm`` or ``WagtailCaptchaEmailForm``. The first options inherits from ``AbstractForm`` while the seconds does it from ``AbstractEmailForm``. Either way your page is going to display a captcha field at the end of the form.

Example

.. code-block:: python

    from wagtail.contrib.forms.models import AbstractFormField
    from wagtail.admin.edit_handlers import FieldPanel, InlinePanel, MultiFieldPanel
    from wagtail.core.fields import RichTextField
    
    # Or, if using Wagtail < 2.0
    #from wagtail.wagtailforms.models import AbstractFormField
    #from wagtail.wagtailadmin.edit_handlers import FieldPanel, InlinePanel, MultiFieldPanel
    #from wagtail.wagtailcore.fields import RichTextField
    
    from modelcluster.fields import ParentalKey

    from wagtailcaptcha.models import WagtailCaptchaEmailForm


    class SubmitFormField(AbstractFormField):
        page = ParentalKey('SubmitFormPage', related_name='form_fields')


    class SubmitFormPage(WagtailCaptchaEmailForm):
        body = RichTextField(blank=True, help_text='Edit the content you want to see before the form.')
        thank_you_text = RichTextField(blank=True, help_text='Set the message users will see after submitting the form.')

        class Meta:
            verbose_name = "Form submission page"


    SubmitFormPage.content_panels = [
        FieldPanel('title', classname="full title"),
        FieldPanel('body', classname="full"),
        FieldPanel('thank_you_text', classname="full"),
        InlinePanel('form_fields', label="Form fields"),
        MultiFieldPanel([
            FieldPanel('to_address'),
            FieldPanel('from_address'),
            FieldPanel('subject'),
        ], "Email notification")
    ]


The captcha field can't be added from the admin UI but will appear in your frontend as the last of the form fields.

If you need to customize the behavior of the form builder, make sure to inherit from ``wagtailcaptcha.forms.WagtailCaptchaFormBuilder`` instead of Wagtail's default form builder, then declare it as usual on the page model:

.. code-block:: python

    from wagtailcaptcha.forms import WagtailCaptchaFormBuilder
    from wagtailcaptcha.models import WagtailCaptchaForm


    class CustomFormBuilder(WagtailCaptchaFormBuilder):
        # Some custom behavior...


    class FormPage(WagtailCaptchaForm):
        form_builder = CustomFormBuilder
        # The rest of the page definition as usual...

For a more thorough example, `Made with Wagtail <http://madewithwagtail.org/>`_ (`github.com/springload/madewithwagtail <https://github.com/springload/madewithwagtail>`_) is an example of an open-source site using the module in which this app is based from.

Development
-----------

Installation
~~~~~~~~~~~~

    Requirements: ``virtualenv``, ``pyenv``, ``twine``

.. code:: sh

    git clone git@github.com:georgedorn/wagtail-django-hcaptcha.git
    cd wagtail-django-hcaptcha/
    virtualenv .venv
    source ./.venv/bin/activate
    make init

Commands
~~~~~~~~

Use `make help` to get a list of commands.

Copyright
---------

&copy; 2020 Timothy Bautista. Original code &copy; 2016 Springload. Licensed under MIT License
