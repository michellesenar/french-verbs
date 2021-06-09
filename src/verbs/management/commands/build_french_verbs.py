import csv
import unicodedata

from django.core.management.base import BaseCommand

from verbs.models import FrenchVerb

real_file = "french_verbs.csv"


class Command(BaseCommand):
    def handle(self, *args, **options):
        with open(real_file, "rU") as fp:
            reader = csv.reader(fp)
            for row in reader:
                french = row[0]
                english = "".join(row[1:])
                for english_word in english.split(","):
                    nfkd_form = unicodedata.normalize("NFKD", french)
                    french_ascii = nfkd_form.encode("ASCII", "ignore")
                    print(english_word, french)
                    fv = FrenchVerb()
                    fv.english = english_word
                    fv.french = french
                    fv.french_ascii = french_ascii
                    fv.save()
