class SdkConfiguration:
    def __init__(self, api_key, environment, jwt_token, client_id, version):
        self.api_key = api_key
        self.environment = environment
        self.jwt_token = jwt_token
        self.client_id = client_id
        self.version = version

    def get_base_url(self):
        if self.environment == EnvironmentType.Live:
            return f"https://api.live.fysapp.co/{self.version}"
        elif self.environment == EnvironmentType.Test:
            return f"https://api.test.fysapp.co/{self.version}"
        else:
            raise ValueError("Invalid environment specified.")


class EnvironmentType:
    Live = 'Live'
    Test = 'Test'
