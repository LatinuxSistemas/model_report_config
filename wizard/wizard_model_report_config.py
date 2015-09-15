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

from psycopg2 import IntegrityError
from openerp import models, api, fields


class WizarModelReportConfig(models.TransientModel):
    _name = 'wizard.model.report.config'
    _description = ''

    @api.model
    def fields_view_get(self, view_id=None, view_type='form', toolbar=False, submenu=False):
        """filter action_id"""

        res = super(WizarModelReportConfig, self).fields_view_get(
            view_id=view_id, view_type=view_type, toolbar=toolbar, submenu=submenu
        )

        model = self.model_id.browse(self.env.context.get("model_id", False))
        if res["fields"].get("action_id", False) and model:
            res["fields"]["action_id"]["domain"] = [("model", "=", model.model)]

        return res

    model_id = fields.Many2one('ir.model', string='Model', required=True)
    action_id = fields.Many2one('ir.actions.report.xml', string='Action', required=False)
    override = fields.Boolean(string='Override', help='Check this to override existing report')

    @api.multi
    def button_continue(self):
        view = self.env.ref('model_report_config.view_wizard_model_report_config_form1')
        ctx = self.env.context.copy()
        ctx["model_id"] = self.model_id.id
        #ctx["override"] = self.override
        return {
            'name': 'Select Report for model %s' % self.model_id.name,
            'res_model': 'wizard.model.report.config',
            'type': 'ir.actions.act_window',
            'views': [(view.id, 'form')],
            'view_id': view.id,
            'target': 'new',
            'res_id': self.ids[0],
            'context': ctx,
        }

    @api.multi
    def button_done(self):
        config_obj = self.env["ir.model.report.configuration"]
        for wiz in self:
            try:
                config_obj.create({"model_id": wiz.model_id.id, "action_id": wiz.action_id.id})
            except IntegrityError as e:
                # we must rollback transaction to avoid further InternalError exceptions
                self.env.cr.rollback()
                if wiz.override:
                    config = config_obj.search([("model_id", "=", wiz.model_id.id)])
                    config.write({"action_id": wiz.action_id.id})
                    continue

                # if override is not checked raise the exception
                raise e

        if self.env.context.get("continue", False):
            view = self.env.ref('model_report_config.view_wizard_model_report_config_form0')
            return {
                'name': "Reports Configuration",
                'res_model': 'wizard.model.report.config',
                'type': 'ir.actions.act_window',
                'views': [(view.id, 'form')],
                'view_id': view.id,
                'target': 'new',
                'res_id': self.ids[0],
                'context': self.env.context,
            }

        return True
