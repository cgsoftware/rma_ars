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
                    if line.selected :
                        ok = self.create_order_prod(cr, uid, line.product_id.id, line.product_returned_quantity,line.name,line, context) 
                #import pdb;pdb.set_trace()
        
        return {'type': 'ir.actions.act_window_close',}



    def create_order_prod(self, cr, uid, id,quantity,origin,line,context):
        #import pdb;pdb.set_trace()       
        repair_obj = self.pool.get('mrp.repair')
        origine = "RMA/"+line.claim_id.sequence
        id_move = self.pool.get('stock.move').search(cr,uid,[('origin','=',origine)])
        note = ""
        if line.claim_id.description:
            note+=line.claim_id.description+"\n"
        if  line.claim_descr:
            note+=line.claim_descr+"\n"
        if  line.claim_origine:
            note+=line.claim_origine+"\n"
        
        if id_move: 
            vals = repair_obj.default_get(cr,uid,[],context)
            vals['product_id']=id
            res = repair_obj.onchange_product_id(cr, uid, id)
            value = res.get('value',False)  
            vals.update(value)    
            vals['move_id']=  id_move[0]
            ids = False
            res2 = repair_obj.onchange_move_id(cr, uid, ids, id, vals['move_id'])
            move_data = res2.get('value',False)
            vals.update(move_data)
            vals['origin']=origin
            vals['production_id'] = line.production_id.id
            vals['internal_notes'] = note
            vals['partner_id']= line.claim_id.partner_id.id
            vals['invoice_method']= 'none'
            vals['deliver_bool']=False
            
            for qant in range(0,int(quantity)):
                id_rep = repair_obj.create(cr,uid,vals)
        else:
            raise osv.except_osv(_('Error !'), _('Devi prima creare un Movimento di Ingresso dell Articolo !'))
        return True    


production_from_returned_lines()