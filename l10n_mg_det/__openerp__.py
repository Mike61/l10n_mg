# -*- coding: utf-8 -*-
##############################################################################
#
#    Module written to odoo for Detailed Malagasy Accounting
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
{   'name': 'Madagascar - Comptabilité et Fiscalité Détaillée',
    'version': '1.0',
    'category': 'Localization/Account Charts',
    'author': 'Frédéric Harison RAMANDANIARIVO',
    'depends': [
        'account',
        'account_chart'],
    'init_xml': [],
    'data': [
        'data/taxcode_det.xml',
        'data/pcg_mg_det.xml',
        'data/fpos_tax_det.xml',
        'l10n_mg_wizard.xml'],
    'demo_xml': [],
    'installable': True,
    'website': 'https://github.com/redykely/odoo_mg',
}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
