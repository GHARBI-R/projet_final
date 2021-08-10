# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request


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

class Topnet(http.Controller):
    @http.route('/user-success', website='true', auth='user')
    def index(self, **kw):
        return http.request.render("pfe_topnet.user_thanks", {})

    class Topnet(http.Controller):
        @http.route('/user/list', website='true', auth='user')
        def index(self, **kw):
            return http.request.render("pfe_topnet.user_list", {})