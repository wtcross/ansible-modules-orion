ansible-modules-orion
=====================

Ansible modules for SolarWinds Orion.

Requirements
------------

The [`orionsdk`](https://github.com/solarwinds/orionsdk-python) Python package must be installed on the Ansible control host in
order to use these modules.

It can be installed with `pip install orionsdk`.

Example Playbook
----------------

```yaml
    - hosts: localhost
      roles:
        - ansible-modules-orion
      tasks:
        orion_ipam_query:
          api_url: "{{ orion_api_url }}"
          username: "{{ orion_username }}"
          password: "{{ orion_password }}"
          query: >
            SELECT I.Caption, I.Node.Contact
            FROM Orion.NPM.Interfaces I
            WHERE I.TypeName='{{ interface_type }}'
        register: query_result
```
