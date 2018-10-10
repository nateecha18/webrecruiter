from rolepermissions.roles import AbstractUserRole

class Hr(AbstractUserRole):
    available_permissions = {
        'Can add candidate rank': True,
        'Can change candidate rank': True,
        'Can delete candidate rank': True,
        'Can view candidate rank': True,
    }

# class Engineer(AbstractUserRole):
#     available_permissions = {
#         'edit_patient_file': True,
#     }
