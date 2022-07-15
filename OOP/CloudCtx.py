import datetime


class CloudCtx:

    countInstances = 0

    def __init__(self, name, tenant_name, description, name_alias, ctx_profile_name, health_inst, last_modif):
        self.name = name
        self.tenant_name = tenant_name
        self.description = description
        self.name_alias = name_alias
        self.ctx_profile_name = ctx_profile_name
        self.health_inst = health_inst
        self.last_modif = last_modif
        CloudCtx.countInstances += 1


    @staticmethod
    def check_null(elem):
        if elem == '':
            return '-'
        return elem

    def format_date(self):
        modified = datetime.datetime.strptime(self.last_modif, '%Y-%m-%dT%H:%M:%S.%f%z')
        modified = modified.strftime('%d-%m-%Y %H:%M:%S %p')

        return modified

    def display(self):
        print(f'Name:{CloudCtx.check_null(self.name)}, Tenant-name:{CloudCtx.check_null(self.tenant_name)}, '
              f'Descr:{CloudCtx.check_null(self.description)}, Name-alias:{CloudCtx.check_null(self.name_alias)}, '
              f'Ctx_prof-name:{CloudCtx.check_null(self.ctx_profile_name)}, CurrHealth:{self.health_inst.current_health},'
              f'{self.health_inst.displayed_health}, LastModif:{self.format_date()}')

    def display_health(self):
        print(f'CloudCtx - Name:{self.name} Tenant-name:{self.tenant_name} '
              f'Corresponding health:{self.health_inst.displayed_health}')
