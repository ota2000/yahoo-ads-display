# coding: utf-8

"""
    Yahoo!広告 ディスプレイ広告 API リファレンス / Yahoo! Ads Display Ads API Reference

    <div lang=\"ja\">Yahoo!広告 ディスプレイ広告 APIのWebサービスについて説明します。<br> 「Try it out」のご利用には、事前にアプリケーションの登録が必要です。また、アプリケーションのリダイレクトURIの1つに<br> https://yahoojp-marketing.github.io/ads-display-api-documents/oauth2-redirect.htmlを登録してください。 </div> <div lang=\"en\">Display Ads API Web Services supported in Yahoo! Ads API.<br> When you use \"Try it out\", you need to register your application in advance.<br> As one of redirect URI for application, you need to set \"https://yahoojp-marketing.github.io/ads-display-api-documents/oauth2-redirect.html\". </div>   # noqa: E501

    The version of the OpenAPI document: v1
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from yahoo_ads_display.configuration import Configuration


class AdGroupAdServiceTextAd(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'description': 'str',
        'description2': 'str',
        'display_url': 'str',
        'headline': 'str',
        'url': 'str'
    }

    attribute_map = {
        'description': 'description',
        'description2': 'description2',
        'display_url': 'displayUrl',
        'headline': 'headline',
        'url': 'url'
    }

    def __init__(self, description=None, description2=None, display_url=None, headline=None, url=None, local_vars_configuration=None):  # noqa: E501
        """AdGroupAdServiceTextAd - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._description = None
        self._description2 = None
        self._display_url = None
        self._headline = None
        self._url = None
        self.discriminator = None

        self.description = description
        self.description2 = description2
        self.display_url = display_url
        self.headline = headline
        self.url = url

    @property
    def description(self):
        """Gets the description of this AdGroupAdServiceTextAd.  # noqa: E501

        <div lang=\"ja\"> 説明文（1行目）です。<br> このフィールドは、ADD時は必須となり、SET時は省略可能となります。 </div> <div lang=\"en\"> Description text (line 1).<br> This field is required in ADD operation, and will be optional in SET operation. </div>   # noqa: E501

        :return: The description of this AdGroupAdServiceTextAd.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this AdGroupAdServiceTextAd.

        <div lang=\"ja\"> 説明文（1行目）です。<br> このフィールドは、ADD時は必須となり、SET時は省略可能となります。 </div> <div lang=\"en\"> Description text (line 1).<br> This field is required in ADD operation, and will be optional in SET operation. </div>   # noqa: E501

        :param description: The description of this AdGroupAdServiceTextAd.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def description2(self):
        """Gets the description2 of this AdGroupAdServiceTextAd.  # noqa: E501

        <div lang=\"ja\"> 説明文（2行目）です。<br> ADDおよびSET時、このフィールドは省略可能となります。 </div> <div lang=\"en\"> Description text (line 2).<br> This field is optional in ADD and SET operation. </div>   # noqa: E501

        :return: The description2 of this AdGroupAdServiceTextAd.  # noqa: E501
        :rtype: str
        """
        return self._description2

    @description2.setter
    def description2(self, description2):
        """Sets the description2 of this AdGroupAdServiceTextAd.

        <div lang=\"ja\"> 説明文（2行目）です。<br> ADDおよびSET時、このフィールドは省略可能となります。 </div> <div lang=\"en\"> Description text (line 2).<br> This field is optional in ADD and SET operation. </div>   # noqa: E501

        :param description2: The description2 of this AdGroupAdServiceTextAd.  # noqa: E501
        :type: str
        """

        self._description2 = description2

    @property
    def display_url(self):
        """Gets the display_url of this AdGroupAdServiceTextAd.  # noqa: E501

        <div lang=\"ja\"> 表示URLです。<br> ADDおよびSET時、このフィールドは省略可能となります。<br> ・標準キャンペーンの場合<br> &nbsp;&nbsp;ADDでは入力必須です。SETでの入力は任意です。<br> ・アプリキャンペーンの場合<br> &nbsp;&nbsp;ADD、SETのどちらも指定できません。<br> &nbsp;&nbsp;※アプリキャンペーンで指定したDeviceOsTypeに基づき、以下のいずれかのURLが自動で設定されます。<br> &nbsp;&nbsp;&nbsp;&nbsp;- iOSの場合：itunes.apple.com<br> &nbsp;&nbsp;&nbsp;&nbsp;- Androidの場合：play.google.com<br> </div> <div lang=\"en\"> Display URL.<br> This field is optional in ADD and SET operation.<br> - Standard campaign:<br> &nbsp;&nbsp;Required for ADD, optional for SET.<br> - Mobile app campaign:<br> &nbsp;&nbsp;Not allowed for ADD and SET.<br> &nbsp;&nbsp;*Based on DeviceOsType specified on Mobile app campaign, any of the following URLs will be automatically set.<br> &nbsp;&nbsp;&nbsp;&nbsp;- For iOS : itunes.apple.com<br> &nbsp;&nbsp;&nbsp;&nbsp;- For Android : play.google.com<br> </div>   # noqa: E501

        :return: The display_url of this AdGroupAdServiceTextAd.  # noqa: E501
        :rtype: str
        """
        return self._display_url

    @display_url.setter
    def display_url(self, display_url):
        """Sets the display_url of this AdGroupAdServiceTextAd.

        <div lang=\"ja\"> 表示URLです。<br> ADDおよびSET時、このフィールドは省略可能となります。<br> ・標準キャンペーンの場合<br> &nbsp;&nbsp;ADDでは入力必須です。SETでの入力は任意です。<br> ・アプリキャンペーンの場合<br> &nbsp;&nbsp;ADD、SETのどちらも指定できません。<br> &nbsp;&nbsp;※アプリキャンペーンで指定したDeviceOsTypeに基づき、以下のいずれかのURLが自動で設定されます。<br> &nbsp;&nbsp;&nbsp;&nbsp;- iOSの場合：itunes.apple.com<br> &nbsp;&nbsp;&nbsp;&nbsp;- Androidの場合：play.google.com<br> </div> <div lang=\"en\"> Display URL.<br> This field is optional in ADD and SET operation.<br> - Standard campaign:<br> &nbsp;&nbsp;Required for ADD, optional for SET.<br> - Mobile app campaign:<br> &nbsp;&nbsp;Not allowed for ADD and SET.<br> &nbsp;&nbsp;*Based on DeviceOsType specified on Mobile app campaign, any of the following URLs will be automatically set.<br> &nbsp;&nbsp;&nbsp;&nbsp;- For iOS : itunes.apple.com<br> &nbsp;&nbsp;&nbsp;&nbsp;- For Android : play.google.com<br> </div>   # noqa: E501

        :param display_url: The display_url of this AdGroupAdServiceTextAd.  # noqa: E501
        :type: str
        """

        self._display_url = display_url

    @property
    def headline(self):
        """Gets the headline of this AdGroupAdServiceTextAd.  # noqa: E501

        <div lang=\"ja\"> タイトルです。<br> このフィールドは、ADD時は必須となり、SET時は省略可能となります。 </div> <div lang=\"en\"> Title.<br> This field is required in ADD operation, and will be optional in SET operation. </div>   # noqa: E501

        :return: The headline of this AdGroupAdServiceTextAd.  # noqa: E501
        :rtype: str
        """
        return self._headline

    @headline.setter
    def headline(self, headline):
        """Sets the headline of this AdGroupAdServiceTextAd.

        <div lang=\"ja\"> タイトルです。<br> このフィールドは、ADD時は必須となり、SET時は省略可能となります。 </div> <div lang=\"en\"> Title.<br> This field is required in ADD operation, and will be optional in SET operation. </div>   # noqa: E501

        :param headline: The headline of this AdGroupAdServiceTextAd.  # noqa: E501
        :type: str
        """

        self._headline = headline

    @property
    def url(self):
        """Gets the url of this AdGroupAdServiceTextAd.  # noqa: E501

        <div lang=\"ja\"> リンク先URLです。<br> このフィールドは、ADD時は必須となり、SET時は省略可能となります。 </div> <div lang=\"en\"> Destination URL.<br> This field is required in ADD operation, and will be optional in SET operation. </div>   # noqa: E501

        :return: The url of this AdGroupAdServiceTextAd.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this AdGroupAdServiceTextAd.

        <div lang=\"ja\"> リンク先URLです。<br> このフィールドは、ADD時は必須となり、SET時は省略可能となります。 </div> <div lang=\"en\"> Destination URL.<br> This field is required in ADD operation, and will be optional in SET operation. </div>   # noqa: E501

        :param url: The url of this AdGroupAdServiceTextAd.  # noqa: E501
        :type: str
        """

        self._url = url

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, AdGroupAdServiceTextAd):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AdGroupAdServiceTextAd):
            return True

        return self.to_dict() != other.to_dict()