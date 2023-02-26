from marshmallow import ValidationError


class ValidateExtension:
    def __init__(self, valid_extensions):
        self.valid_extensions = valid_extensions

    def validate(self, value):
        if value not in self.valid_extensions:
            raise ValidationError(f"Valid extensions are {', '.join(self.valid_extensions)}!")


class ValidateIsAlphaNumericAndSpace:
    ERROR = "Must contain only letters and spaces!"

    def validate(self, value):
        if not value.replace(" ", "").isalnum():
            raise ValidationError(self.ERROR)


class ValidateIsAlphaAndSpace:
    ERROR = "Must contain only letters and spaces!"

    def validate(self, value):
        if not value.replace(" ", "").isalpha():
            raise ValidationError(self.ERROR)


class ValidateIsNumeric:
    ERROR = "Must contain only numbers!"

    def validate(self, value):
        try:
            int(value)
        except ValueError:
            raise ValidationError(self.ERROR)

