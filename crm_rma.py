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

class difetti_garanzia(osv.osv):
    _name='difetti.garanzia'
    _columns = {
                'codice': fields.char('Codice Difetto', size=20, required=False),
                'name': fields.char('Descrizione Difetto', size=64, required=False),
                }
difetti_garanzia()

class return_line(osv.osv):
    """
    Class to handle a product return line (corresponding to one invoice line)
    """
    _inherit = "return.line"
    def _get_difetti(self, cr, uid, context={}):
        res = []
        idd = self.pool.get('difetti.garanzia').search(cr,uid,[])
        for line in self.pool.get('difetti.garanzia').browse(cr,uid,idd):            
            res.append((line.codice,line.name))
        return res          
    
    _columns = {
                
                'claim_origine': fields.selection(_get_difetti, 'Difetto Dichiarato ', required=True, help="Problema Indicato dal cliente"),               
                'data_acqu_vend':fields.date('Data Acquisto Vendita',required=False),
                'stato_sigillo': fields.selection([('none','Non Specificato'),
                                    ('integro','Integro'),
                                    ('danneggiato','Danneggiato'),
                                    ('assente','Assente/Rimosso'),                                    
                                    ('dubbio','Condizioni Incerte'),
                                    ('other','Altro')], 'Condizioni Articolo/Sigillo', required=True, help="Stato dei controlli all' accettazione Garanzia"),        
                'production_id': fields.many2one('mrp.production', 'Id. Produzione'),      
                }
    _defaults ={
               'product_returned_quantity':1,
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


class crm_claim(crm.crm_case, osv.osv):
    _inherit="crm.claim"
    _defaults = {
                 'name':'Richiesta Garanzia',
                 }    

crm_claim()