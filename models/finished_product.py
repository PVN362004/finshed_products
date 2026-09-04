from datetime import date
from odoo import api, models, fields


class FinishedProduct(models.Model):
    _name = 'finished.product'
    _description = 'Finished Product Model'

    
    product_name = fields.Char(string='Ten hang', required=True)
    product_code = fields.Char(string='Ma hang', required=True)
    quantity = fields.Integer(string='So luong', required=True, default=1)
    customer_order_name = fields.Char(string='Ten khach hang', required=True)
    delivery_date = fields.Date(string='Ngay giao hang', required=True, default=date.today())

    date_finished = fields.Datetime(
        string='Ngay Nhap', 
        default=lambda self: self._get_default_date_finished()
    )

    @api.model
    def _get_default_date_finished(self):
        if self.env.context.get('default_date_finished'):
            date_finished = fields.Datetime.to_datetime(self.env.context.get('default_date_finished'))
            return date_finished
        return fields.Datetime.now()

    def print_finished_product_tag(self):
        return self.env.ref('finshed_products.action_report_finished_product_tag').report_action(self)



