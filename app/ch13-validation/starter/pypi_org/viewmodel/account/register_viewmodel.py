from pypi_org.services import user_service
from pypi_org.viewmodel.view_modelbase import ViewModelBase


class RegisterViewModel(ViewModelBase):
    def __init__(self):

        super().__init__()
        self.name = self.request_dict.name
        self.email = self.request_dict.email.lower().strip()
        self.password = self.request_dict.password.strip()

    def validate(self):
        if not self.name or not self.name.strip():
            self.error="You must specify a name"
        elif not self.email or not self.email.strip():
            self.error="You must specify a email"
        elif not self.password or not self.password.strip():
            self.error="You must specify a password"
        elif len(self.password.strip()) < 5:
            self.error="Your password must be at least 5 characters"

