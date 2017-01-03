# -*- coding: utf-8 -*-
#
# Copyright 2014 Bernard Yue
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
#
import json as JSON

from .utils import BeautifierBase


class JSONBeautifier(BeautifierBase):
    """A JSON Beautifier that pretty print JSON"""

    @classmethod
    def beautify(cls, json, indent=2, encoding='utf-8'):
        result = json

        try:
            result = JSON.dumps(JSON.loads(json, encoding), indent=indent, encoding=encoding, ensure_ascii=False, sort_keys=True)
        except:
            pass

        return result

    @classmethod
    def beautifyTextInHTML(cls, html, indent=2, encoding=None):
        return cls._findAndReplace(html, cls.reIndentAndJSON,
                                   cls.beautify, (indent,), indent)
