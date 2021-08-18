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
    name = fields.Char(string='Nom et Prénom du gérant', required=True, track_visibility="always")
    cin = fields.Integer(string='Numéro CIN/Passeport', required=True, track_visibility="always")
    email_p=  fields.Char(String= 'E-mail principal')
    raison = fields.Char(string='Raison Sociale')
    rc = fields.Char(string='Registre de Commerce')
    tva = fields.Char(string='Code TVA')
    exonere = fields.Boolean(string='Exonéré')
    douane = fields.Char(string='code en douane')
    activity = fields.Char(string="Activité de l'entreprise")
    adresse_s = fields.Char(string='Adresse Siege Sociale')
    adresse_f = fields.Char(string='Adresse de facturation')
    # ville  et code postale
    tel_s = fields.Integer(string='Tél', size=8)
    fax_s = fields.Integer(string='Fax', size=8)

    adresse_i = fields.Text(string="Adresse D'installation ")
    #ville et code postal
    tel_i = fields.Char(string='Tel', size=8)
    fax_i = fields.Integer(string='Fax', size=8)


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


