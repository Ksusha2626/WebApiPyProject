from yandex_disk.service_yandex_disk import ServiceYandexDisk
from yandex_passport.service_yandex_passport import ServiceYandexPassport


class Cluster(object):
    """Aggregating api services for easy usage"""

    def __init__(self, cluster_config=None):
        self.cluster_config = cluster_config

        self.yandex_disk = ServiceYandexDisk(self.cluster_config['yandex_disk'])
        self.yandex_passport = ServiceYandexPassport(self.cluster_config['yandex_passport'])
