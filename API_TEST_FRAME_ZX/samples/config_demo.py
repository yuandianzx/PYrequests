from API_TEST_FRAME_ZX.common.config_utils import configUtils

configUtils = configUtils()
hosts = configUtils.read_config('default','hosts')
print(hosts)
