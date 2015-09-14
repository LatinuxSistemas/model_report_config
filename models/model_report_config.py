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

from openerp import models, api, fields, _


class IrModelReportConfiguration(models.Model):
    _name = 'ir.model.report.configuration'
    _description = 'Retrieve a report action name by model'

    model_id = fields.Many2one('ir.model', string='Model', required=True)
    action_id = fields.Many2one('ir.actions.report.xml', string='Action', required=True,)
                                #domain=[('model', '=', 'model_id.name')])

    _sql_constraints = [
        ('uniq_model_action_check', 'unique(model_id, action_id)',
         _('ERROR: Just one report per model is allowed!')),
    ]
