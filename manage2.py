"""
    Python library for Cpanel's Manage2 API

        https://documentation.cpanel.net/display/SDK/Manage2+API+Functions+-+Request+a+License+Transfer

    @author     Benton Snyder
    @website    http://bensnyde.me
    @email      benton@bensnyde.me
    @created    7/16/15
    @updated    7/16/15
"""

from httplib import HTTPSConnection
from base64 import b64encode

API_ENDPOINT = 'manage2.cpanel.net'

class Manage2:
    def __init__(self, username, password):
        self.authHeader = {'Authorization':'Basic ' + b64encode(username+':'+password).decode('ascii')}

    def __query(self, resource_string):
        conn = HTTPSConnection(API_ENDPOINT)
        conn.request('GET', 'https://%s/%s' % (API_ENDPOINT, resource_string), headers=self.authHeader)
        response = conn.getresponse()
        data = response.read()
        conn.close()
        return data

    def list_licenses(self, expired=0):
        """ List account's licenses

                https://documentation.cpanel.net/display/SDK/Manage2+API+Functions+-+List+License+Information
        """
        return self.__query('XMLlicenseInfo.cgi?output=json&expired=%s' % (expired))

    def add_license(self, groupid, packageid, ip):
        """ Add a license

                https://documentation.cpanel.net/display/SDK/Manage2+API+Functions+-+Add+Licenses
        """
        return self.__query('XMLtransferRequest.cgi?output=json&groupid=%s&packageid=%s&ip=%s' % (groupid, packageid, ip))

    def cancel_license_transfer(self, ip, cancel, groupid, packageid):
        """ Cancel a license transfer

                https://documentation.cpanel.net/display/SDK/Manage2+API+Functions+-+Cancel+a+License+Transfer
        """
        return self.__query('XMLtransferRequest.cgi?output=json&cancel=%s&groupid=%s&packageid=%s&ip=%s' % (cancel, groupid, packageid, ip))

    def change_license(self, oldip, newip, packageid, force, dryrun):
        """ Change a license

                https://documentation.cpanel.net/display/SDK/Manage2+API+Functions+-+Change+a+License+IP+Address
        """
        return self.__query('XMLtransfer.cgi?output=json&oldip=%s;newip=%s;packageid=%s;force=%s;dryrun=%s' % (oldip, newip, packageid, force, dryrun))

    def list_groups(self):
        """ List account's groups

                https://documentation.cpanel.net/display/SDK/Manage2+API+Functions+-+Display+Groups
        """
        return self.__query('XMLgroupInfo.cgi?output=json')

    def expire_license(self, licenseid, expcode="normal"):
        """ Expire a license

                https://documentation.cpanel.net/display/SDK/Manage2+API+Functions+-+Expire+Licenses
        """
        return self.__query('XMLlicenseExpire.cgi?output=json&liscid=%s&expcode=%s' % (license, expcode))

    def extend_license(self, ip):
        """ Extend a license

                https://documentation.cpanel.net/display/SDK/Manage2+API+Functions+-+Extend+One-Time+Licenses
        """
        return self.__query('XMLonetimeext.cgi?output=json&ip=%s' % (ip))

    def fetch_risk_data(self, ip):
        """ Get IP address's fraud risk score

                https://documentation.cpanel.net/display/SDK/Manage2+API+Functions+-+Fetch+Risk+Data
        """
        return self.__query('XMLsecverify.cgi?output=json&ip=%s' % (ip))

    def list_packages(self):
        """ List account's packages

                https://documentation.cpanel.net/display/SDK/Manage2+API+Functions+-+List+Package+Information
        """
        return self.__query('XMLpackageInfo.cgi')

    def ip_to_licenseid(self, ip, all=1):
        """ Get IP address's license

                https://documentation.cpanel.net/display/SDK/Manage2+API+Functions+-+Look+Up+License+ID
        """
        return self.__query('XMLlookup.cgi?ip=%s;all=%s' % (ip, all))

    def get_license(self, ip, all=1):
        """ Get IP address's license information

                https://documentation.cpanel.net/display/SDK/Manage2+API+Functions+-+Raw+Lookup
        """
        return self.__query('XMLRawlookup.cgi?output=json&ip=%s;all=%s' % (ip, all))

    def reactive_expired_license(self, liscid, force, dryrun):
        """ Reactivate an expired license

                https://documentation.cpanel.net/display/SDK/Manage2+API+Functions+-+Reactivate+Expired+Licenses

        """
        return self.__query('XMLlicenseReActivate.cgi?output=json&liscid=%s' % (liscid))

    def license_transfer(self, groupid, packageid, ip):
        """ Transfer a license

                https://documentation.cpanel.net/display/SDK/Manage2+API+Functions+-+Request+a+License+Transfer
        """
        return self.__query('XMLtransferRequest.cgi?output=json&groupid=%s&packageid=%s&ip=%s' % (groupid, packageid, ip))

