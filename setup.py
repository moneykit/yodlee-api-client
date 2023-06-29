# coding: utf-8

"""
    Yodlee Core APIs

    This file describes the Yodlee Platform APIs using the swagger notation. You can use this swagger file to generate client side SDKs to the Yodlee Platform APIs for many different programming languages. Yodlee API v1.1 - Overview</a>.<br><br>You will have to set the header before making the API call. The following headers apply to all the APIs:<ul><li>Authorization: This header holds the access token</li> <li> Api-Version: 1.1</li></ul><b>Note</b>: If there are any API-specific headers, they are mentioned explicitly in the respective API's description.  # noqa: E501

    The version of the OpenAPI document: 1.1.0
    Contact: developer@yodlee.com
    Generated by: https://openapi-generator.tech
"""


from setuptools import setup, find_packages  # noqa: H301

NAME = "yodlee"
VERSION = "1.0.0"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = ["urllib3 >= 1.25.3", "six >= 1.10", "python-dateutil"]

setup(
    name=NAME,
    version=VERSION,
    description="Yodlee Core APIs",
    author="OpenAPI Generator community",
    author_email="developer@yodlee.com",
    url="",
    keywords=["OpenAPI", "OpenAPI-Generator", "Yodlee Core APIs"],
    install_requires=REQUIRES,
    packages=find_packages(exclude=["test", "tests"]),
    include_package_data=True,
    license="Yodlee Developer License",
    long_description_content_type='text/markdown',
    long_description="""\
    This file describes the Yodlee Platform APIs using the swagger notation. You can use this swagger file to generate client side SDKs to the Yodlee Platform APIs for many different programming languages. Yodlee API v1.1 - Overview&lt;/a&gt;.&lt;br&gt;&lt;br&gt;You will have to set the header before making the API call. The following headers apply to all the APIs:&lt;ul&gt;&lt;li&gt;Authorization: This header holds the access token&lt;/li&gt; &lt;li&gt; Api-Version: 1.1&lt;/li&gt;&lt;/ul&gt;&lt;b&gt;Note&lt;/b&gt;: If there are any API-specific headers, they are mentioned explicitly in the respective API&#39;s description.  # noqa: E501
    """
)
