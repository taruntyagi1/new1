# django imports
from django.core.management import BaseCommand
from django.contrib.sites.models import Site

# inner app imports
from canleath.settings import DEFAULT_DOMAIN_NAME

class Command(BaseCommand):
    help = 'set_default_domain'
    requires_migrations_checks = True

    def create_or_update_domain_name(self, domain_name):
        site_obj = Site.objects.get(id=1)
        site_obj.domain = DEFAULT_DOMAIN_NAME
        site_obj.name = DEFAULT_DOMAIN_NAME
        site_obj.save()
        if site_obj.domain == DEFAULT_DOMAIN_NAME:
            self.stdout.write(self.style.SUCCESS('{0} Domain Created Successfully'.format(domain_name)))
        else:
            self.stdout.write(self.style.SUCCESS('{0} Domain Creation Failed'.format(domain_name)))

    def handle(self, *args, **options):
        domain_name = DEFAULT_DOMAIN_NAME
        self.create_or_update_domain_name(domain_name=domain_name)