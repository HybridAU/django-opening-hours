from django import forms
from django.db.models import get_model
from django.core.exceptions import ValidationError

from .widgets import OpeningHoursWidget

from django.forms import widgets

import json

class OpeningHoursField(forms.CharField):
    def __init__(self, **kwargs):
        defaults = {
            'widget': OpeningHoursWidget(),
        }
        defaults.update(kwargs)
        return super(OpeningHoursField, self).__init__(**defaults)

    def clean(self, value):
        def is_time(s): # XXX:
            import re
            if s and re.match(r"\d+:\d+", s) and re.match(r"\d+:\d+", s).group() == s:
                return True
            return False

        data = json.loads(value)
        for day in ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]:
            for d in data[day]:
                if not is_time(d[0]) or not is_time(d[1]):
                    raise ValidationError("Time not valid")

        return json.dumps(data)
