from marshmallow import ValidationError



class ValidateUniqueness:
    ERROR = "is already taken"

    def __init__(self, column, *models):
        self.models = models
        self.column = column

    def validate(self, value):
        criteria = {self.column: value}
        for model in self.models:
            obj = model.query.filter_by(**criteria).first()
            if obj:
                raise ValidationError(self._get_error_message(value))

    def _get_error_message(self, value):
        return value + ' ' + self.ERROR


class ValidateExtension:
    def __init__(self, file_type, valid_extensions):
        self.file_type = file_type
        self.valid_extensions = valid_extensions

    def validate(self, value):
        if value not in self.valid_extensions:
            raise ValidationError(f"Valid extension for {self.file_type} are {', '.join(self.valid_extensions)}!")
