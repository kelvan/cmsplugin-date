from django.utils.translation import ugettext_lazy as _

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from .models import Date


class DatePlugin(CMSPluginBase):
    model = Date
    name = _('Date')
    render_template = 'cms/plugins/date.html'

    def render(self, context, instance, placeholder):
        context.update({
            'object': instance,
            'placeholder': placeholder,
        })
        return context

plugin_pool.register_plugin(DatePlugin)
