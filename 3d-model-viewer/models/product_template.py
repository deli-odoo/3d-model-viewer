from odoo import fields, models


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    model_viewer = fields.Binary(string="Model Viewer")
    file_name = fields.Char()
