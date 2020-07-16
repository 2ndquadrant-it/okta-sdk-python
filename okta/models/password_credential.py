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
from okta.models.password_credential_hash\
    import PasswordCredentialHash
from okta.models.password_credential_hook\
    import PasswordCredentialHook


class PasswordCredential(
    OktaObject
):
    """
    A class for PasswordCredential objects.
    """

    def __init__(self, config=None):
        if config:
            if "hash" in config:
                if isinstance(config["hash"],
                              PasswordCredentialHash):
                    self.hash = config["hash"]
                else:
                    self.hash = PasswordCredentialHash(
                        config["hash"]
                    )
            else:
                self.hash = None
            if "hook" in config:
                if isinstance(config["hook"],
                              PasswordCredentialHook):
                    self.hook = config["hook"]
                else:
                    self.hook = PasswordCredentialHook(
                        config["hook"]
                    )
            else:
                self.hook = None
            self.value = config["value"]\
                if "value" in config else None
        else:
            self.hash = None
            self.hook = None
            self.value = None
