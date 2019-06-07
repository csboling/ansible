from schemata.ansible.v161 import PresetSchema_v161
from schemata.ansible.v161_dev import PresetSchema_v161_dev
from schemata.ansible.v161_es import PresetSchema_v161_es
from schemata.ansible.vnext import PresetSchema_vnext

ANSIBLE_SCHEMATA = {
    '1.6.1': PresetSchema_v161,
    '1.6.1-dev': PresetSchema_v161_dev,
    '1.6.1-es': PresetSchema_v161_es,
    'next': PresetSchema_vnext,
}
