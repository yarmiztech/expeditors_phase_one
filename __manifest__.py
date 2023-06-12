# -*- coding: utf-8 -*-
{
    'name': "Expeditors E-Invoice Report",
    'author':
        'ENZAPPS',
    'summary': """
This module is for printing E-Invoice report for Masar Arabia.
""",

    'description': """
        This module is for printing E-Invoice report for Masar Arabia.
    """,
    'website': "",
    'category': 'base',
    'version': '14.0',
    'depends': ['base', 'account', 'uom_unece', 'base_unece', 'account_tax_unece', 'base_vat_sanitized',
                'onchange_helper', 'base_iban', 'base_bank_from_iban', 'base_business_document_import',
                'account_invoice_import', 'base_ubl_payment', 'account_payment_partner', 'account_invoice_import_ubl',
                'account_invoice_ubl', 'sale', 'purchase', 'stock', 'arabic_strings'],
    'data': [
            'security/ir.model.access.csv',
            'views/account_move.xml',
            'reports/reports.xml',
            'reports/reports_view.xml',
            'reports/reports_without_view.xml',
    ],
    'demo': [
    ],
    'installable': True,
    'application': True,
}
