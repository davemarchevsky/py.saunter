# Copyright 2011 Element 34
# 
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# 
#     http://www.apache.org/licenses/LICENSE-2.0
# 
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""
========
Checkbox
========
"""
from saunter.po.remotecontrol.element import Element
from saunter.SeleniumWrapper import SeleniumWrapper as wrapper
from saunter.exceptions import ElementNotFound

class Checkbox(Element):
    """
    Base element class for Checkboxes
    """
    def __set__(self, obj, val):
        if (val == True and str(wrapper().connection.get_value(self.locator)) == 'off') or (val == False and str(wrapper().connection.get_value(self.locator)) == 'on'):
            wrapper().connection.click(self.locator)

    def __get__(self, obj, cls=None):
        try:
            return str(wrapper().connection.get_value(self.locator))
        except AttributeError as e:
            if str(e) == "'SeleniumWrapper' object has no attribute 'connection'":
                pass
            else:
                raise e
        except ElementNotFound as e:
            msg = "Element %s was not found. It is used in the %s page object in the %s module." % (self.locator, obj.__class__.__name__, self.__module__)
            raise ElementNotFound(msg)