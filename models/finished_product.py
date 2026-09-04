from datetime import date
from odoo import api, models, fields
import math


class FinishedProduct(models.Model):
    _name = 'finished.product'
    _description = 'Finished Product Model'
    _rec_name = 'product_name'

    product_code = fields.Char(string='Ma hang', required=True)
    product_name = fields.Char(string='Ten hang', required=True)
    customer_name = fields.Many2one('customer.partner', string='Ten khach hang', ondelete='restrict')

    quantity = fields.Integer(string='So luong', required=True, default=1)
    manufacturing_date = fields.Date(string='Ngay san xuat', required=True, default=date.today())
    delivery_date = fields.Date(string='Ngay giao hang', required=True, default=date.today())

    pallet_number = fields.Integer(string='So pallet', required=True, default=1)
    quantity_per_pallet = fields.Integer(string='So luong tren pallet',compute='compute_quantity_per_pallet', store=True)
    date_finished = fields.Datetime(
            string='Ngay Nhap', 
            default=lambda self: self._get_default_date_finished()
        ) 
    note = fields.Text(string='Ghi chu')

    @api.model
    def _get_default_date_finished(self):
        if self.env.context.get('default_date_finished'):
            date_finished = fields.Datetime.to_datetime(self.env.context.get('default_date_finished'))
            return date_finished
        return fields.Datetime.now()

    def print_finished_product_tag(self):
        return self.env.ref('finshed_products.action_report_finished_product_tag').report_action(self)

    @api.depends('quantity', 'pallet_number')
    def compute_quantity_per_pallet(self):
        for record in self:
            if  record.pallet_number > 0:
                record.quantity_per_pallet = math.ceil(record.quantity / record.pallet_number)
            else:
                record.quantity_per_pallet = 0

class CustomerPartner(models.Model):
    _name = 'customer.partner'
    _description = 'Customer Partner Model'

    name = fields.Char(string='Ten khach hang', required=True)