from django.utils.translation import gettext as _


class TitleName:
    def __init__(self):
        self.save = _('Save')
        self.reg = _('Registration')
        self.update_user = _('Update user')


class Message:
    def __init__(self):
        self.no_rigths_for_user = _("You can`t change another user.")
        self.user_update = _("User was successfully updated.")
        self.user_create = _("User was successfully created.")
        self.user_login = _("You're logged in")
        self.user_create = _("New user here!")
        self.no_delete_user = _("You can not delete another user!")
        self.login = _("You need to be authorized")