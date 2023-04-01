from django.utils.translation import gettext as _


class TitleName:
    def __init__(self):
        self.save = _("Save")
        self.reg = _("Registration")
        self.update_user = _("Update user")
        self.create_status = _("Create status")
        self.create = _("Create")
        self.delete_user = _("Delete user")
        self.update_status = _("Update status")
        self.update = _("Update")


class Message:
    def __init__(self):
        self.no_rigths_for_user = _("You can`t change another user.")
        self.user_update = _("User was successfully updated.")
        self.user_create = _("User was successfully created.")
        self.user_login = _("You're logged in")
        self.user_create = _("New user here!")
        self.no_delete_user = _("You can not delete another user!")
        self.login = _("You need to be authorized")
        self.status_create = _("You created new status!")
        self.status_update = _("Status was successfulle updated.")
