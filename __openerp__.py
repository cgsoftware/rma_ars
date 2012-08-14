# -*- coding: utf-8 -*-
#########################################################################
#                                                                       #
#                                                                       #
#########################################################################
#                                                                       #
# Copyright (C) 2009-2011  Akretion, Raphaël Valyi, Sébastien Beau, 	#
# Emmanuel Samyn							#
#                                                                       #
#This program is free software: you can redistribute it and/or modify   #
#it under the terms of the GNU General Public License as published by   #
#the Free Software Foundation, either version 3 of the License, or      #
#(at your option) any later version.                                    #
#                                                                       #
#This program is distributed in the hope that it will be useful,        #
#but WITHOUT ANY WARRANTY; without even the implied warranty of         #
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the          #
#GNU General Public License for more details.                           #
#                                                                       #
#You should have received a copy of the GNU General Public License      #
#along with this program.  If not, see <http://www.gnu.org/licenses/>.  #
#########################################################################


{
    'name': 'CRM Resi In Garanzia e Ciclo Garanzia',
    'version': '1.0',
    'category': 'Generic Modules/CRM & SRM',
    'description': """
            Gestione Accettazione Reclami e attivazione ciclo di garanzia, con verifica del ciclo di controllo e collaudo sino al reso.
    """,
    'author': 'C. & G. Software S.a.s.',
    'website': 'http://www.cgsoftware.it',
    'depends': ['crm_claim_rma','mrp'],
    'init_xml': [],
    'update_xml': ['crm_rma.xml','CreaProdDaRma.xml','rma_difetti.xml'
              #'security/ir.model.access.csv',
    ],
    'demo_xml': [], 


    'installable': True,
    'active': False,
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
