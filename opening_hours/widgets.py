import json

from django.forms.widgets import Widget

from django.template import loader
from django.utils.safestring import mark_safe
from django.conf import settings


class OpeningHoursWidget(Widget):
    is_required = False
    template = "opening_hours/widget.html"
    def render(self, name, value, attrs=None):
        if not value:
            value = '{"Monday": [], "Tuesday":[], "Wednesday":[], "Thursday":[], "Friday":[], "Saturday":[], "Sunday":[], "Monday_note": "", "Tuesday_note": "", "Wednesday_note":"", "Thursday_note":"", "Friday_note":"", "Saturday_note":"", "Sunday_note":""}'
        if type(value) == dict:
            value = json.dumps(value)
        return mark_safe(loader.render_to_string(self.template, {
            "value": value,
            "name": name,
            "STATIC_URL": settings.STATIC_URL,
        }))