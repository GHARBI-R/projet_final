# -*- coding: utf-8 -*-
from odoo import http
from werkzeug.wrappers import Request
from odoo.http import request

# affichage de la liste des utilisateurs
class Topnet(http.Controller):
    @http.route('/user/list/', website=True, auth='public')
    def topnet_user(self, **kw):
         # return "Thanks for watching"
        utilisateurs = request.env['topnet.user'].sudo().search([])
        return request.render("pfe_topnet.user_list", {'utilisateurs': utilisateurs})

# Ajout d'un utilisateur
class Topnet(http.Controller):
    @http.route('/adduser',type='http', methods=['POST'], website='true', auth='public')
    def index(self, **kw):
        request.env['topnet.user'].sudo().create()
        return request.render("pfe_topnet.create_user", {})


class Topnet(http.Controller):
    @http.route('/user-success', website='true', auth='user')
    def index(self, **kw):
        return http.request.render("pfe_topnet.user_thanks", {})

#Dépôt de dossier client
class Topnet(http.Controller):
    @http.route('/addsubscription', website='true', auth='user')
    def index(self, **kw):
        contacts = request.env['topnet.clt'].sudo().search([])
        return http.request.render("pfe_topnet.create_subscription")

#création d'un contact
class Topnet(http.Controller):
    @http.route('/CreateContact', website='true', auth='user')
    def index(self, **kw):
        return http.request.redirect("pfe_topnet.create_contact", {})

class Topnet(http.Controller):
    @http.route('/contact_thanks', website='true', auth='user')
    def index(self, **kw):
        return http.request.render("pfe_topnet.contact_thanks", {})


class Topnet(http.Controller):
    @http.route('/create/contact',type='http', methods=['POST'], website='true', auth='public')
    def index(self, **post):
        contact = request.env['topnet.contact'].create({
            'name': post.get('name'),
            'tel_fixe': post.get('telfix'),
            'tel_gsm': post.get('telgsm'),
            'email': post.get('email'),
            'nature': post.get('nature'),
            #'client_id': request.uid,
        })
        return http.request.render("pfe_topnet.contact_thanks", {})

#Affichage de la liste de contact
class Topnet(http.Controller):
    @http.route('/contact_list', website='true', auth='user')
    def index(self, **kw):
        contacts = request.env['topnet.contact'].sudo().search([])
        return http.request.render("pfe_topnet.list_contact", {'contacts':contacts})


#Ajout d'un client
class Topnet(http.Controller):
    @http.route('/addclient', website='true', type='http', auth='public')
    def client(self, **kw):
        return http.request.render("pfe_topnet.create_client", {})

class Topnet(http.Controller):
        @http.route('/create/client', website='true', type='http', auth='public')
        def create_client(self, **kw):
            request.env['topnet.clt'].sudo().create(kw)
            return request.render("pfe_topnet.client_thanks", {})

class Topnet(http.Controller):
    @http.route('/client/list/', website=True, type='http', auth='public')
    def topnet_user(self, **kw):
         # return "Thanks for watching"
        clients = request.env['topnet.clt'].sudo().search([])
        return request.render("pfe_topnet.client_list", {'clients': clients})


#Authentification
class Topnet(http.Controller):
    @http.route('/authentification', website='true', auth='public')
    def index(self, **kw):
        contacts = request.env['topnet.user'].sudo().search([])
        return http.request.render("pfe_topnet.create_user")