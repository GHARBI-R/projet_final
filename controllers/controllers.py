# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request

#creation d'un simple controlleur
class Topnet(http.Controller):

    @http.route('/utilisateur/list/', website=True, auth='public')
    def topnet_user(self, **kw):
         # return "Thanks for watching"

        utilisateurs = request.env['topnet.user'].sudo().search([])
        return request.render("pfe_topnet.user_list", {'utilisateurs': utilisateurs})

class Topnet(http.Controller):
    @http.route('/adduser_form', website='true', auth='user')
    def index(self, **kw):
        return http.request.render("pfe_topnet.create_user", {})
