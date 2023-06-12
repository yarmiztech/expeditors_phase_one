from odoo import models,fields,api
import convert_numbers



class AccountMove(models.Model):
    _inherit = 'account.move'

    datetime_field = fields.Datetime(string="Create Date", default=lambda self: fields.Datetime.now())
    decoded_data = fields.Char('Decoded Data')
    description_line = fields.One2many("invoice.description.line","invoice_id")
    recieved_by = fields.Char()
    prepared_by = fields.Char()
    invoice_formate_type = fields.Selection([('normal','Normal'),('manpower','Manpower')],default='normal')

    def total_amount_to_words(self):
        check_amount_in_words = self.currency_id.amount_to_text(self.amount_total)
        return check_amount_in_words

    @api.onchange('invoice_formate_type')
    def check_invoice_formate_type(self):
        for line in self.invoice_line_ids:
            line.invoice_formate_type = self.invoice_formate_type




    def total_vat(self):
        total_vat = self.amount_untaxed * 0.15
        return total_vat



    def amount_amount(self):
        total_amount = 0
        if self.tax_ids:
            for i in self:
                amount = self.price_subtotal * 0.15
                total_amount = self.price_subtotal + amount
                return  total_amount
        else:
            return total_amount

    def ar_total_tax(self):
        value = self.amount_tax
        before, after = str(value).split('.')
        before_int = int(before)
        after_int = int(after)
        before_ar = convert_numbers.english_to_arabic(before_int)
        after_ar = convert_numbers.english_to_arabic(after_int)
        ar_total_tax_amount = before_ar + '.' + after_ar
        return before_ar + '.' + after_ar

    def amount_total_arabic(self):
        value = self.amount_total
        before, after = str(value).split('.')
        before_int = int(before)
        after_int = int(after)
        before_ar = convert_numbers.english_to_arabic(before_int)
        after_ar = convert_numbers.english_to_arabic(after_int)
        ar_total_tax_amount = before_ar + '.' + after_ar
        return before_ar + '.' + after_ar

    def amount_untaxed_convert(self):
        value = self.amount_untaxed
        before, after = str(value).split('.')
        before_int = int(before)
        after_int = int(after)
        before_ar = convert_numbers.english_to_arabic(before_int)
        after_ar = convert_numbers.english_to_arabic(after_int)
        # ar_total_tax_amount = before_ar + '.' + after_ar
        return before_ar + '.' + after_ar

    def ar_advances(self):
        value = 0.00
        before, after = str(value).split('.')
        before_int = int(before)
        after_int = int(after)
        before_ar = convert_numbers.english_to_arabic(before_int)
        after_ar = convert_numbers.english_to_arabic(after_int)
        ar_total_tax_amount = before_ar + '.' + after_ar
        return before_ar + '.' + after_ar

    def ar_amount_residual(self):
        value = self.amount_residual
        before, after = str(value).split('.')
        before_int = int(before)
        after_int = int(after)
        before_ar = convert_numbers.english_to_arabic(before_int)
        after_ar = convert_numbers.english_to_arabic(after_int)
        ar_total_tax_amount = before_ar + '.' + after_ar
        return before_ar + '.' + after_ar


    def ar_invoice_name(self, name):
        interger_part = name[3:]
        interger_part_arabic = convert_numbers.english_to_arabic(interger_part)
        return interger_part_arabic

    def ar_invoice_date(self):
        m = str(self.invoice_date)
        if m.split('-'):
            interger_part_arabic = ''
            for each in m.split('-'):
                if interger_part_arabic:
                    interger_part_arabic = interger_part_arabic + '-'
                interger_part_arabic += convert_numbers.english_to_arabic(int(each))

        return interger_part_arabic


class AccountMoveLine(models.Model):
    _inherit = 'account.move.line'

    invoice_formate_type = fields.Selection([('normal','Normal'),('manpower','Manpower')],default='normal')
    normal_working_hours = fields.Float()
    over_time_hours = fields.Float()

    @api.onchange('normal_working_hours','over_time_hours')
    def compute_working_hours(self):
        self.quantity = self.normal_working_hours + self.over_time_hours

    def product_tax_value(self):
        amount = 0
        if self.tax_ids:
            tax_amount = self.env['account.tax'].search([('name','=',self.tax_ids.name)])
            for tax in tax_amount:
                amount = self.price_subtotal*(tax.amount/100)
        return amount

    def amount_amount(self):
        # amount = self.price_subtotal * (tax.amount / 100)
        total_amount = 0
        if self.tax_ids:
            for i in self:
                amount = self.price_subtotal * 0.15
                total_amount = self.price_subtotal + amount
                return  total_amount
        else:
            return total_amount

class InvoiceDescriptionLine(models.Model):
    _name = 'invoice.description.line'

    invoice_id = fields.Many2one("account.move")
    name = fields.Char()