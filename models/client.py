from odoo import models, fields, api, _

class TopnetClient(models.Model):
    _name = 'topnet.clt'
    # _inherit = ['res.users']
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Topnet Clients'

    # création de la séquence numéro du dossier client
    @api.model
    def create(self, vals):
        if vals.get('name_seq', _('New')) == _('New'):
            vals['name_seq'] = self.env['ir.sequence'].next_by_code('topnet.client.sequence') or _('New')

        result = super(TopnetClient, self).create(vals)
        return result
   # création de l'état de dossier
    def action_depose(self):
        for rec in self:
            rec.state = 'déposé'

    def action_valide(self):
         for rec in self:
               rec.state = 'validé'
    def action_annule(self):
         for rec in self:
               rec.state = 'annulé'
    name = fields.Char(string='Nom', required=True, track_visibility="always")
    cin = fields.Integer(string='cin', required=True, track_visibility="always")
    raison = fields.Char(string='Raison Sociale', required=True)
    #rc = fields.Char(string='Registre de Commerce', required=True)
    tva = fields.Char(string='TVA', required=True)
    exoneration = fields.Boolean(string='Exoneration', required=True)
    douane = fields.Char(string='Douane', required=True)
    activity = fields.Char(string='Activité', required=True)
    adresse_siege = fields.Char(string='Adresse Siege Sociale', required=True)
    ville_siege = fields.Char(string='Ville du Siege')
    #tel_siege = fields.Integer(string='Tel Siege', size=8)
    #adresse_facture = fields.Text(string='Adresse Facturation', required=True)
    #ville_facture = fields.Integer(string='Ville Facturation', required=True)
    #tel_facture = fields.Char(string='Tel Facturation', size=8, required=True)
    #email = fields.Char(string='Email', required=True)
    #contact_id = fields.One2many('topnet.contact', 'client_id', string='Contact ID')
    ville_id = fields.Many2one('topnet.ville', 'ville')
    gouv_id = fields.Many2one('topnet.gouvernorat', string='gouvernorat')
    active = fields.Boolean(default=True)

    name_seq = fields.Char(string='Order Reference', required=True, copy=False, readonly=True,
                       states={'draft': [('readonly', False)]}, index=True, default=lambda self: _('New'))

    state = fields.Selection([
        ('déposé', 'Déposé'),
        ('validé', 'Validé'),
        ('annulé', 'Annulé'),
    ], string='Status', readonly=True, default='déposé', track_visibility="always")




class TopnetGouvernorat(models.Model):
    _name = 'topnet.gouvernorat'
    _description = 'Liste des Gouvernorats'

    name = fields.Selection([
        ('Ariana', 'Ariana'), ('Béja', 'Béja') , ('Mannouba', 'Mannouba'), ('Jendouba', 'Jendouba')
    ], default='', required= True)
    clt_ids = fields.One2many('topnet.clt', 'gouv_id', string='hhh')


    ville_id = fields.Many2one('topnet.ville','ville')



class TopnetVille(models.Model):
    _name = 'topnet.ville'
    _description = 'Liste des villes'

    name = fields.Selection([
        ('menzah', 'menzah'), ('manar', 'manar') , ('sidi thabet', 'sidi thabet'), ('midoun', 'midoun')
    ], required=True)
    postal = fields.Integer(string='Code Postal', required=True)


