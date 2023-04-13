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
        self.delete_status = _("Delete status")
        self.create_task = _("Create task")
        self.update_task = _("Update task")
        self.delete_task = _("Delete task")
        self.create_label = _("Create label")
        self.update_label = _("Update label")
        self.delete_label = _("Delete label")


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
        self.status_update = _("Status was successfully updated.")
        self.status_delete = _("Status was successfully deleted")
        self.no_delete_status = _("Status is in use and cannot be deleted")
        self.task_create = _("Task was successfully created.")
        self.task_update = _("Task was successfully updated.")
        self.label_create = _("Label was successfully created.")
        self.label_update = _("Label was successfully updated.")
        self.label_delete = _("Label was successfully deleted")
        self.no_delete_label = _("Label is in use and cannot be deleted")
