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
from okta.models.authorization_server_credentials_rotation_mode\
    import AuthorizationServerCredentialsRotationMode
from okta.models.authorization_server_credentials_use\
    import AuthorizationServerCredentialsUse


class AuthorizationServerCredentialsSigningConfig(
    OktaObject
):
    """
    A class for AuthorizationServerCredentialsSigningConfig objects.
    """

    def __init__(self, config=None):
        if config:
            self.kid = config["kid"]\
                if "kid" in config else None
            self.last_rotated = config["lastRotated"]\
                if "lastRotated" in config else None
            self.next_rotation = config["nextRotation"]\
                if "nextRotation" in config else None
            if "rotationMode" in config:
                if isinstance(config["rotationMode"],
                              AuthorizationServerCredentialsRotationMode):
                    self.rotation_mode = config["rotationMode"]
                else:
                    self.rotation_mode = AuthorizationServerCredentialsRotationMode(
                        config["rotationMode"]
                    )
            else:
                self.rotation_mode = None
            if "use" in config:
                if isinstance(config["use"],
                              AuthorizationServerCredentialsUse):
                    self.use = config["use"]
                else:
                    self.use = AuthorizationServerCredentialsUse(
                        config["use"]
                    )
            else:
                self.use = None
        else:
            self.kid = None
            self.last_rotated = None
            self.next_rotation = None
            self.rotation_mode = None
            self.use = None
