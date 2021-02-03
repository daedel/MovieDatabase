from django import template

register = template.Library()


@register.simple_tag(takes_context=True)
def page_replace(context, **kwargs):
    query = context["request"].GET.copy()
    query["page"] = kwargs["page"]
    return query.urlencode()
