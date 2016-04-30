"""
    Python library for Cpanel's Manage2 API

        https://documentation.cpanel.net/display/SDK/Manage2+API+Functions+-+Request+a+License+Transfer

    @author     Benton Snyder
    @website    http://bensnyde.me
    @email      benton@bensnyde.me
    @created    7/16/15
    @updated    7/16/15
"""

from base64 import b64encode
from httplib import HTTPSConnection
import urllib

API_ENDPOINT = 'manage2.cpanel.net'

class Manage2:
    def __init__(self, username, password):
        self.authHeader = {'Authorization':'Basic ' + b64encode(username+':'+password).decode('ascii')}

    def __query(self, resource, params):
        params['output'] = 'json'
        params = urllib.urlencode(params)

        conn = HTTPSConnection(API_ENDPOINT)
        conn.request('GET', 'https://%s/%s?%s' % (API_ENDPOINT, resource, params), headers=self.authHeader)
        response = conn.getresponse()
        data = response.read()
        conn.close()

        return data

    def list_licenses(self, expired=0):
        """ List account's licenses

                https://documentation.cpanel.net/display/SDK/Manage2+API+Functions+-+List+License+Information
        """
        data = {
            'expired': expired
        }
        return self.__query('XMLlicenseInfo.cgi', data)

    def add_license(self, groupid, packageid, ip):
        """ Add a license

                https://documentation.cpanel.net/display/SDK/Manage2+API+Functions+-+Add+Licenses
        """
        data = {
            'groupid': groupid,
            'packageid': packageid,
            'ip': ip
        }
        return self.__query('XMLtransferRequest.cgi', data)

    def cancel_license_transfer(self, ip, cancel, groupid, packageid):
        """ Cancel a license transfer

                https://documentation.cpanel.net/display/SDK/Manage2+API+Functions+-+Cancel+a+License+Transfer
        """
        data = {
            'cancel': cancel,
            'groupid': groupid,
            'packageid': packageid,
            'ip': ip
        }
        return self.__query('XMLtransferRequest.cgi', data)

    def change_license(self, oldip, newip, packageid, force, dryrun):
        """ Change a license

                https://documentation.cpanel.net/display/SDK/Manage2+API+Functions+-+Change+a+License+IP+Address
        """
        data = {
            'oldip': oldip,
            'newip': newip,
            'packageid': packageid,
            'force': force,
            'dryrun': dryrun
        }
        return self.__query('XMLtransfer.cgi', data)

    def list_groups(self):
        """ List account's groups

                https://documentation.cpanel.net/display/SDK/Manage2+API+Functions+-+Display+Groups
        """
        return self.__query('XMLgroupInfo.cgi', {})

    def expire_license(self, licenseid, expcode="normal"):
        """ Expire a license

                https://documentation.cpanel.net/display/SDK/Manage2+API+Functions+-+Expire+Licenses
        """
        data = {
            'liscid': licenseid,
            'expcode': expcode
        }
        return self.__query('XMLlicenseExpire.cgi', data)

    def extend_license(self, ip):
        """ Extend a license

                https://documentation.cpanel.net/display/SDK/Manage2+API+Functions+-+Extend+One-Time+Licenses
        """
        data = {
            'ip': ip
        }
        return self.__query('XMLonetimeext.cgi', data)

    def fetch_risk_data(self, ip):
        """ Get IP address's fraud risk score

                https://documentation.cpanel.net/display/SDK/Manage2+API+Functions+-+Fetch+Risk+Data
        """
        data = {
            'ip': ip
        }
        return self.__query('XMLsecverify.cgi', data)

    def list_packages(self):
        """ List account's packages

                https://documentation.cpanel.net/display/SDK/Manage2+API+Functions+-+List+Package+Information
        """
        return self.__query('XMLpackageInfo.cgi', {})

    def ip_to_licenseid(self, ip, all_licenses=1):
        """ Get IP address's license

                https://documentation.cpanel.net/display/SDK/Manage2+API+Functions+-+Look+Up+License+ID
        """
        data = {
            'ip': ip,
            'all': all_licenses
        }
        return self.__query('XMLlookup.cgi', data)

    def get_license(self, ip, all_licenses=1):
        """ Get IP address's license information

                https://documentation.cpanel.net/display/SDK/Manage2+API+Functions+-+Raw+Lookup
        """
        data = {
            'ip': ip,
            'all': all_licenses
        }
        return self.__query('XMLRawlookup.cgi', data)

    def reactive_expired_license(self, liscid, force, dryrun):
        """ Reactivate an expired license

                https://documentation.cpanel.net/display/SDK/Manage2+API+Functions+-+Reactivate+Expired+Licenses

        """
        data = {
            'liscid': liscid,
            'force': force,
            'dryrun': dryrun
        }
        return self.__query('XMLlicenseReActivate.cgi', data)

    def license_transfer(self, groupid, packageid, ip):
        """ Transfer a license

                https://documentation.cpanel.net/display/SDK/Manage2+API+Functions+-+Request+a+License+Transfer
        """
        data = {
            'groupid': groupid,
            'packageid': packageid,
            'ip': ip
        }
        return self.__query('XMLtransferRequest.cgi', data)
