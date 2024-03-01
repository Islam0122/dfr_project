from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import  Product
from ..Group.models import Group


@receiver(post_save, sender=Product)
def distribute_users_to_groups(sender, instance, created, **kwargs):
    if created:
        distribute_users(instance)

def distribute_users(product):
    groups = product.groups.all()
    users = product.users.all()

    total_users = len(users)
    min_users_per_group = min(group.min_users for group in groups)
    max_users_per_group = max(group.max_users for group in groups)

    if total_users > 0:
        users_per_group = min(max_users_per_group, (total_users + min_users_per_group - 1) // min_users_per_group)
        users = list(users)[:users_per_group * len(groups)]

        for i, group in enumerate(groups):
            start_index = i * users_per_group
            end_index = (i + 1) * users_per_group
            group.users.set(users[start_index:end_index])