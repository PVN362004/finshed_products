from datetime import date
from odoo import api, models, fields


class ProductRouting(models.Model):
    _name = 'product.routing'
    _description = 'Routing Information Model'

    product_relate = fields.Many2one('finished.product', string='Thong tin san pham', ondelete='cascade', required=True)

    product_code = fields.Char(related='product_relate.product_code', string='Ma hang', store=True)
    product_name = fields.Char(related='product_relate.product_name', string='Ten hang', store=True)
    customer_name = fields.Many2one(related='product_relate.customer_name', string='Ten khach hang', store=True)
    quantity= fields.Integer(related='product_relate.quantity', string='So luong', store=True)
    delivery_date= fields.Date(related='product_relate.delivery_date', string='Ngay giao', store=True)
    pallet_number= fields.Integer(related='product_relate.pallet_number', string='So pallet', store=True)
    note = fields.Text(related='product_relate.note',string='Ghi chu')

