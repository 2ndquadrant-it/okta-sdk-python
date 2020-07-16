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
from okta.models.okta_sign_on_policy_rule_signon_session_actions\
    import OktaSignOnPolicyRuleSignonSessionActions


class OktaSignOnPolicyRuleSignonActions(
    OktaObject
):
    """
    A class for OktaSignOnPolicyRuleSignonActions objects.
    """

    def __init__(self, config=None):
        if config:
            self.access = config["access"]\
                if "access" in config else None
            self.factor_lifetime = config["factorLifetime"]\
                if "factorLifetime" in config else None
            self.factor_prompt_mode = config["factorPromptMode"]\
                if "factorPromptMode" in config else None
            self.remember_device_by_default = config["rememberDeviceByDefault"]\
                if "rememberDeviceByDefault" in config else None
            self.require_factor = config["requireFactor"]\
                if "requireFactor" in config else None
            if "session" in config:
                if isinstance(config["session"],
                              OktaSignOnPolicyRuleSignonSessionActions):
                    self.session = config["session"]
                else:
                    self.session = OktaSignOnPolicyRuleSignonSessionActions(
                        config["session"]
                    )
            else:
                self.session = None
        else:
            self.access = None
            self.factor_lifetime = None
            self.factor_prompt_mode = None
            self.remember_device_by_default = "false"
            self.require_factor = "false"
            self.session = None
