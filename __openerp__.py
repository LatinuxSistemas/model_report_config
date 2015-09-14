# -*- coding: utf-8 -*-
##############################################################################
#
#    Copyright (c) 2015-TODAY Latinux S.A.
#    (http://www.latinux.com.ar) All Rights Reserved.
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################


{
    'name': 'Model Report Config',
    'category': 'Misc',
    'description': """
    """,
    'author': 'Latinux S.A',
    'website': 'http://www.latinux.com.ar/',
    'depends': [
        'account',
    ],
    'init_xml': [],
    'data': [
        'views/model_report_config_view.xml',
        'views/wizard_model_report_config_view.xml',
        'todo_wizard_config.xml',
    ],
    'demo_xml': [],
    'test': [],
    'installable': True,
    'application': True,
}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
