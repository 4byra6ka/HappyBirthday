from django import template

register = template.Library()


@register.simple_tag(name='subscriptions_check', takes_context=True)
def subscriptions_check(context, object, user):
    subscription = object.subscriptions_set.filter(employees=user)
    if subscription:
        context['sub_check'] = True
        context['sub_pk'] = subscription[0].pk
        return True
    else:
        context['sub_check'] = False
        context['sub_pk'] = None
        return False
