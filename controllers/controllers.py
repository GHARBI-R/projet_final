# -*- coding: utf-8 -*-
from odoo import http
from werkzeug.wrappers import Request
from odoo.http import request


class Topnet(http.Controller):

    @http.route('/user/list/', website=True, auth='public')
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
    @http.route('/addsubscription_form', website='true', auth='user')
    def index(self, **kw):
        return http.request.render("pfe_topnet.create_subscription", {})

class Topnet(http.Controller):
    @http.route('/CreateContact', website='true', auth='user')
    def index(self, **kw):
        return http.request.render("pfe_topnet.create_contact", {})

class Topnet(http.Controller):
    @http.route('/contact_thanks', website='true', auth='user')
    def index(self, **kw):
        return http.request.render("pfe_topnet.contact_thanks", {})


class Topnet(http.Controller):
    @http.route('/create/contact',type='http', methods=['POST'], website='true', auth='user')
    def index(self, **post):
        contact = request.env['topnet.contact'].sudo().create({
            'name': post.get('contact_name'),
            'tel_fixe': post.get('contact_telfix'),
            'tel_gsm': post.get('contact_telgsm'),
            'email': post.get('contact_email'),
            'nature': post.get('contact_nature'),
            #'client_id': request.uid,
        })
        return http.request.render("topnet.contact_thanks", {})



