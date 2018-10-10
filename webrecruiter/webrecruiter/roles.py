from rolepermissions.roles import AbstractUserRole

class Hr(AbstractUserRole):
    available_permissions = {
        'create_medical_record': True,
    }

class Engineer(AbstractUserRole):
    available_permissions = {
        'edit_patient_file': True,
    }
