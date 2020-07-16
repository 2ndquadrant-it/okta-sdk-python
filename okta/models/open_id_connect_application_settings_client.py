"""
Copyright 2020 - Present Okta, Inc.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

# AUTO-GENERATED! DO NOT EDIT FILE DIRECTLY
# SEE CONTRIBUTOR DOCUMENTATION

from okta.okta_object import OktaObject
from okta.models.open_id_connect_application_type\
    import OpenIdConnectApplicationType
from okta.models.open_id_connect_application_consent_method\
    import OpenIdConnectApplicationConsentMethod
from okta.models.open_id_connect_application_issuer_mode\
    import OpenIdConnectApplicationIssuerMode


class OpenIdConnectApplicationSettingsClient(
    OktaObject
):
    """
    A class for OpenIdConnectApplicationSettingsClient objects.
    """

    def __init__(self, config=None):
        if config:
            if "application_type" in config:
                if isinstance(config["application_type"],
                              OpenIdConnectApplicationType):
                    self.application_type = config["application_type"]
                else:
                    self.application_type = OpenIdConnectApplicationType(
                        config["application_type"]
                    )
            else:
                self.application_type = None
            self.client_uri = config["client_uri"]\
                if "client_uri" in config else None
            if "consent_method" in config:
                if isinstance(config["consent_method"],
                              OpenIdConnectApplicationConsentMethod):
                    self.consent_method = config["consent_method"]
                else:
                    self.consent_method = OpenIdConnectApplicationConsentMethod(
                        config["consent_method"]
                    )
            else:
                self.consent_method = None
            self.grant_types = config["grant_types"]\
                if "grant_types" in config else None
            self.initiate_login_uri = config["initiate_login_uri"]\
                if "initiate_login_uri" in config else None
            if "issuer_mode" in config:
                if isinstance(config["issuer_mode"],
                              OpenIdConnectApplicationIssuerMode):
                    self.issuer_mode = config["issuer_mode"]
                else:
                    self.issuer_mode = OpenIdConnectApplicationIssuerMode(
                        config["issuer_mode"]
                    )
            else:
                self.issuer_mode = None
            self.logo_uri = config["logo_uri"]\
                if "logo_uri" in config else None
            self.policy_uri = config["policy_uri"]\
                if "policy_uri" in config else None
            self.post_logout_redirect_uris = config["post_logout_redirect_uris"]\
                if "post_logout_redirect_uris" in config else None
            self.redirect_uris = config["redirect_uris"]\
                if "redirect_uris" in config else None
            self.response_types = config["response_types"]\
                if "response_types" in config else None
            self.tos_uri = config["tos_uri"]\
                if "tos_uri" in config else None
        else:
            self.application_type = None
            self.client_uri = None
            self.consent_method = None
            self.grant_types = None
            self.initiate_login_uri = None
            self.issuer_mode = None
            self.logo_uri = None
            self.policy_uri = None
            self.post_logout_redirect_uris = None
            self.redirect_uris = None
            self.response_types = None
            self.tos_uri = None
