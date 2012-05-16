# -*- coding: utf-8 -*-

from osv import fields, osv
from crm import crm
from datetime import datetime
from dateutil.relativedelta import relativedelta
import time
from tools.translate import _
import netsvc


class production_from_returned_lines(osv.osv_memory):
    _name='production_from_returned_lines'
    _description='Crea ordini di produzione dalle righe rma'
    _columns = {
                }
    def action_cancel(self,cr,uid,ids,conect=None):
        return {'type': 'ir.actions.act_window_close',}
    
    
    def crea_productions(self, cr, uid, ids, context):
        if context.get('active_id',False):
            claim_brw=  self.pool.get('crm.claim').browse(cr,uid, context['active_id'],context)
            if claim_brw:
                for line in claim_brw.return_line_ids:
                    if line.selected:
                        ok = self.create_order_prod(cr, uid, line.product_id.id, line.product_returned_quantity,line.name, context) 
                #import pdb;pdb.set_trace()
        
        return {'type': 'ir.actions.act_window_close',}



    def create_order_prod(self, cr, uid, id,quantity,origin,context):
        #import pdb;pdb.set_trace()
        prod_obj = self.pool.get('mrp.production')
        vals = prod_obj.default_get(cr,uid,[],context)
        vals['product_id']=id
        res = prod_obj.product_id_change( cr, uid, id, id, context)
        value = res.get('value',False)
        if value:
            vals['product_uom']= value['product_uom']
            vals['bom_id']= value['bom_id']
            vals['routing_id'] = value['routing_id']
        vals['product_qty']=quantity
        
        vals['origin']=origin
        production_id = self.pool.get('mrp.production').create(cr, uid, vals, context)
        prod_obj.action_compute(cr, uid, [ production_id])
        workflow = netsvc.LocalService("workflow")
        workflow.trg_validate(uid, 'mrp.production', production_id, 'button_confirm', cr)
        res=[]
        
        return True    


production_from_returned_lines()