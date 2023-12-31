# coding: utf-8

"""
    Yodlee Core APIs

    This file describes the Yodlee Platform APIs using the swagger notation. You can use this swagger file to generate client side SDKs to the Yodlee Platform APIs for many different programming languages. Yodlee API v1.1 - Overview</a>.<br><br>You will have to set the header before making the API call. The following headers apply to all the APIs:<ul><li>Authorization: This header holds the access token</li> <li> Api-Version: 1.1</li></ul><b>Note</b>: If there are any API-specific headers, they are mentioned explicitly in the respective API's description.  # noqa: E501

    The version of the OpenAPI document: 1.1.0
    Contact: developer@yodlee.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import yodlee
from yodlee.models.third_party_adr import ThirdPartyADR  # noqa: E501
from yodlee.rest import ApiException

class TestThirdPartyADR(unittest.TestCase):
    """ThirdPartyADR unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ThirdPartyADR
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = yodlee.models.third_party_adr.ThirdPartyADR()  # noqa: E501
        if include_optional :
            return ThirdPartyADR(
                name = '', 
                url = ''
            )
        else :
            return ThirdPartyADR(
                name = '',
                url = '',
        )

    def testThirdPartyADR(self):
        """Test ThirdPartyADR"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
