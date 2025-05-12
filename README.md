# My-Social-App
Learning RIG Django Day8-Django-Day3

###################################################################################3
### setting.py #####
### for templates ###
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR/'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

### for static ###
STATIC_URL = 'static/'

STATICFILES_DIRS = [BASE_DIR / 'static']
STATIC_ROOT = BASE_DIR / 'static_a'

### for media ###
MEDIA_URL = 'media/'
MEDIA_ROOT = BASE_DIR / 'media'


### url.py #####
from django.conf import settings
from django.conf.urls.static import static

......

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

#########################################################################################



### Day8-Django-Day3 ###

### Django Templates ######

### Templaes Variable ###
{{ variabel_name }}

### Template Tags ###

# comment
{% comment 'optional note' %} 
{{data}}
{%  endcomment %}


# cycle
{% cycle 'row1' 'row2' %} //no endblock
{% for i in data %}
    <dir class="{% cycle 'row1' 'row2' %}">
    <p> {{i}} </p>
    </div>
{% endfor %}

# extends
{% extends "./base.html' %} // extends to base.html

# include
{% include './footer.html' %}

# if
{% if data == a %} 
    {{data}}

{% elif data == b %}
    {{data}}

{% else %}
    {{data}}

{% endif %}


# for 
{% for i in data%} 
    {{i}}
{% endfor %}

# firstof
{% firstof var1 var2 var3 %}

{% if var1 %}
    {{var}}

{% elif var2 %}
    {{var2}}

{% elif var3 %}
    {{var3}}

{% endif %}


# now
{% now "D d M Y" %}
{% now "D" %}
{% now "d" %}
{% now "M" %}
{% now "Y" %}

# url


#########################################################################

### Day9-Djnago-Day4 ######################3


# lecture Note






# Homework

Create new Blog Project
mode = (tile,body,photo1, photo2,photo3,create)
templates = cerateblog.html, bloglist.html

CSS Design
upload project to github








