# coding: utf-8

from statsd.client import StatsClient


class StatsdClient(StatsClient):

    def __init__(self, *args, **kwargs):
        if args or kwargs:
            # __init__(self, host='localhost', port=8125, prefix=None,
            #          maxudpsize=512, ipv6=False)
            super(StatsdClient, self).__init__(*args, **kwargs)

    def init_app(self, app):
        cfg = app.config
        kwargs = dict(
            host=cfg.get('STATSD_HOST', 'localhost'),
            port=cfg.get('STATSD_PORT', 8125),
            prefix=cfg.get('STATSD_PREFIX', None),
            maxudpsize=cfg.get('STATSD_MAXUDPSIZE', 512),
            ipv6=cfg.get('STATSD_IPV6', False)
        )
        self.__init__(**kwargs)
