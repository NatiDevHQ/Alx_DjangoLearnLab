# bookshelf/management/commands/create_groups.py
from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission
from django.apps import apps

class Command(BaseCommand):
    help = 'Creates user groups and assigns permissions.'

    def handle(self, *args, **kwargs):
        Book = apps.get_model('bookshelf', 'Book')

        permissions = {
            "can_view": Permission.objects.get(codename="can_view"),
            "can_create": Permission.objects.get(codename="can_create"),
            "can_edit": Permission.objects.get(codename="can_edit"),
            "can_delete": Permission.objects.get(codename="can_delete"),
        }

        groups_permissions = {
            "Viewers": ["can_view"],
            "Editors": ["can_view", "can_create", "can_edit"],
            "Admins": ["can_view", "can_create", "can_edit", "can_delete"],
        }

        for group_name, perms in groups_permissions.items():
            group, _ = Group.objects.get_or_create(name=group_name)
            group.permissions.clear()
            for perm_code in perms:
                group.permissions.add(permissions[perm_code])
            self.stdout.write(f"Group '{group_name}' created/updated with permissions.")
