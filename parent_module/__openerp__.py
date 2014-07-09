# -*- encoding: utf-8 -*-

{
    'name': 'Parent Module',
    'version': '0.1',
    'author': 'Savoir-faire Linux',
    'maintainer': 'Savoir-faire Linux',
    'website': 'http://www.savoirfairelinux.com',
    'license': 'AGPL-3',
    'category': 'Others',
    'description': """
Parent Module
======

Contributors
------------
* Sandy Carter (sandy.carter@savoirfairelinux.com)
""",
    'depends': [
        'b_module',
        'a_module',
    ],
    'external_dependencies': {
        'python': [],
    },
    'data': [],
    'installable': True,
}
