from django import template
from django.contrib.staticfiles.storage import staticfiles_storage

register = template.Library()


@register.simple_tag
def jquery():
    version = '1.8.3'
    filename = 'jquery-%s.min.js' % version
    link = staticfiles_storage.url(filename)
    return '<script type="text/javascript" src="%s"></script>' % link


@register.simple_tag
def jquery_tablesorter():
    version = '2.7'
    filename = 'jquery.tablesorter-%s.min.js' % version
    link = staticfiles_storage.url(filename)
    return '<script type="text/javascript" src="%s"></script>' % link


@register.simple_tag
def konami():
    filename = 'konami.min.js'
    link = staticfiles_storage.url(filename)
    return '<script type="text/javascript" src="%s"></script>' % link


@register.simple_tag
def bootstrap_typeahead():
    filename = 'bootstrap-typeahead.js'
    link = staticfiles_storage.url(filename)
    return '<script type="text/javascript" src="%s"></script>' % link


# vim: set ts=4 sw=4 et:
