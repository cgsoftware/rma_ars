# -*- coding: utf-8 -*-

from osv import fields, osv
from crm import crm
from datetime import datetime
from dateutil.relativedelta import relativedelta
import time
from tools.translate import _

class crm_claim_product_return(osv.osv):
    _inherit = 'crm.claim'


crm_claim_product_return()


class return_line(osv.osv):
    """
    Class to handle a product return line (corresponding to one invoice line)
    """
    _inherit = "return.line"
    _columns = {
                'data_acqu_vend':fields.date('Data Acquisto Vendita',required=True),
                'stato_sigillo': fields.selection([('none','Non Specificato'),
                                    ('integro','Integro'),
                                    ('danneggiato','Danneggiato'),
                                    ('assente','Assente/Rimosso'),                                    
                                    ('dubbio','Condizioni Incerte'),
                                    ('other','Altro')], 'Condizioni Articolo/Sigillo', required=True, help="Stato dei controlli all' accettazione Garanzia"),        
                'production_id': fields.many2one('mrp.production', 'Id. Produzione'),      
                }

return_line()      


class product_exchange(osv.osv): 
    """
    Class to manage product exchanges history
    """
    _inherit = "product.exchange"
    _columns = {
                'returned_production_id': fields.many2one('mrp.production', 'Id. Prod. Reso'),
                'replacement_production_id': fields.many2one('mrp.production', 'Id. Prod. Sostituzione'),
                }
   
product_exchange()