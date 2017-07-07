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
            query = dict(required=True)
        ),
        required_together = [['username', 'password']],
        supports_check_mode = False
    )

    api_url = module.params['api_url']
    username = module.params['username']
    password = module.params['password']
    query = module.params['query']

    try:
        client = SwisClient(api_url, username, password)
        response = client.query(query)
        module.exit_json(changed=True, result=response['result'])
    except Exception:
        e = get_exception()
        module.fail_json(msg="Request failed with exception %s" % e)


if __name__ == '__main__':
    main()
