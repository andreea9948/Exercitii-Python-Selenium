class HealthInst:
    def __init__(self, current_health, max_sev):
        self.current_health = int(current_health)
        self.max_sev = max_sev

    @property
    def displayed_health(self):
        if self.current_health == 100:
            val = 'healthy'
        else:
            val = 'unhealthy'
        return val
