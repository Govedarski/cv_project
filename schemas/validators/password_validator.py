from marshmallow import ValidationError
from password_strength import PasswordPolicy, PasswordStats


class PasswordValidator:
    _policy = PasswordPolicy.from_names(
        length=8,
        uppercase=1,
        numbers=1,
        special=1,
    )

    policy_error_mapper = {
        "length": "Too short!",
        "uppercase": "Must contain at least one uppercase character!",
        "numbers": "Must contain at least one number!",
        "special": "Must contain at least one special symbol!",
        "weak": "Too common!"
    }

    def validate_password(self, value):
        errors = self._policy.test(value)
        errors_messages = [self.policy_error_mapper[error.name()] for error in errors]

        password_strength = PasswordStats(value).strength()
        if password_strength < 0.2:
            errors_messages.append(self.policy_error_mapper["weak"])

        if errors_messages:
            raise ValidationError(errors_messages)
