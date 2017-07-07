#!/usr/bin/env python

from orionsdk import SwisClient
from ansible.module_utils.basic import *
from ansible.module_utils.pycompat24 import get_exception

def main():
    module = AnsibleModule(
        argument_spec = dict(
            api_url = dict(required=True, default=None),
            username = dict(required=True, default=None),
            password = dict(required=True, default=None, no_log=True),
            name = dict(required=True)
        ),
        required_together = [['username', 'password']],
        supports_check_mode = False
    )

    api_url = module.params['api_url']
    username = module.params['username']
    password = module.params['password']
    name = module.params['name']

    try:
        client = SwisClient(api_url, username, password)
        subnet = "'" + subnet + '%' + "'"
        query = "SELECT TOP 255 I.DisplayName FROM IPAM.IPNode I WHERE Status=2 AND I.Subnet.DisplayName Like " + subnet
        response = client.query(query)
        available_ip_addresses = [ ip_node['DisplayName'] for ip_node in response['result'] ]
        module.exit_json(changed=True, available_ip_addresses=available_ip_addresses)
    except Exception:
        e = get_exception()
        module.fail_json(msg="Fact gather failed with exception %s" % e)


if __name__ == '__main__':
    main()
