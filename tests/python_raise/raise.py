raise
raise ValueError
raise ValueError("error")

raise NotImplementedError(
    'The SimpleListFilter.lookups() method must be overridden to '
    'return a list of tuples (value, verbose value).'
)

raise forms.ValidationError(
    self.error_messages['invalid_login'],
    code='invalid_login',
    params={
        'username': self.username_field.verbose_name
    }
)
