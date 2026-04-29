import pytest

from .md_conf import MDConf
from .md_env import MDTestEnv

class TestCertDuration:

    @pytest.fixture(autouse=True, scope='class')
    def _class_scope(self, env):
        env.clear_store()

    def test_cert_duration_config(self, env):
        domain = "duration.test"
        conf = MDConf(env)
        conf.add(f"MDomain {domain}")
        conf.add("MDCertificateDuration 10d")
        conf.add("MDCertificateNotBefore -1d")
        conf.install()
        # Ensure it starts properly with this config
        assert env.apache_restart() == 0
