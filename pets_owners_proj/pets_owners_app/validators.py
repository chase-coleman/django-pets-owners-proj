from django.core.validators import RegexValidator

owner_name_validator = RegexValidator(regex=r'^[A-Z][a-z]+ [A-Z][a-z]+$', message="Invalid name. Name must but in First Last format.")

pet_name_validator = RegexValidator(regex=r'^[A-Z][a-z]+(?: [A-Z][a-z]+)*$', message="Invalid pet name. First letter must be capitalized.")