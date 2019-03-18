from typing import Optional, Union, Dict, Any

from algoliasearch.configs import AnalyticsConfig
from algoliasearch.helpers import endpoint, is_async_available
from algoliasearch.http.request_options import RequestOptions
from algoliasearch.http.requester import Requester
from algoliasearch.http.transporter import Transporter
from algoliasearch.http.verbs import Verbs


class AnalyticsClient(object):
    def __init__(self, transporter, search_config):
        # type: (Transporter, AnalyticsConfig) -> None

        self._transporter = transporter
        self._config = search_config

    @staticmethod
    def create(app_id, api_key, region='us'):
        # type: (str, str, str) -> AnalyticsClient

        config = AnalyticsConfig(app_id, api_key, region)
        requester = Requester()
        transporter = Transporter(requester, config)

        client = AnalyticsClient(transporter, config)

        if is_async_available():
            from algoliasearch.analytics_client_async import \
                AnalyticsClientAsync
            from algoliasearch.http.transporter_async import \
                TransporterAsync
            from algoliasearch.http.requester_async import RequesterAsync

            return AnalyticsClientAsync(
                client, TransporterAsync(RequesterAsync(), config), config
            )

        return client

    def get_ab_tests(self, request_options=None):
        # type: (Optional[Union[Dict[str, Any], RequestOptions]]) -> dict

        return self._transporter.read(
            Verbs.GET,
            '2/abtests',
            None,
            request_options
        )

    def get_ab_test(self, ab_test_id, request_options=None):
        # type: (str, Optional[Union[Dict[str, Any], RequestOptions]]) -> dict

        assert ab_test_id, 'ab_test_id cannot be empty.'

        return self._transporter.read(
            Verbs.GET,
            endpoint('2/abtests/{}', ab_test_id),
            None,
            request_options
        )

    def add_ab_test(self, ab_test, request_options=None):
        # type: (dict, Optional[Union[Dict[str, Any], RequestOptions]]) -> dict

        return self._transporter.write(
            Verbs.POST,
            '2/abtests',
            ab_test,
            request_options
        )

    def stop_ab_test(self, ab_test_id, request_options=None):
        # type: (int, Optional[Union[Dict[str, Any], RequestOptions]]) -> dict

        assert ab_test_id, 'ab_test_id cannot be empty.'

        return self._transporter.write(
            Verbs.POST,
            endpoint('2/abtests/{}/stop', ab_test_id),
            None,
            request_options
        )

    def delete_ab_test(self, ab_test_id, request_options=None):
        # type: (int, Optional[Union[Dict[str, Any], RequestOptions]]) -> dict

        assert ab_test_id, 'ab_test_id cannot be empty.'

        return self._transporter.write(
            Verbs.DELETE,
            endpoint('2/abtests/{}', ab_test_id),
            None,
            request_options
        )
