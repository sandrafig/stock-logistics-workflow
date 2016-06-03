# -*- coding: utf-8 -*-
# © 2016 Sandra Figueroa Varela <sandrafigvar@gmail.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
{
    "name": "Stock group by customer",
    "summary": "This module adds a 'group by' option to group the delivery orders by customer in the tree view.",
    "version": "8.0.1.0.0",
    "category": "Warehouse Management",
    "author": "Sandra Figueroa Varela, Odoo Community Association (OCA)",
    "license": "AGPL-3",
    "application": False,
    "installable": True,
    "depends": [
        "base",
        "sale",
        "stock",
    ],
    "data": [
        "views/group_by_customer_view.xml",
    ],
}
