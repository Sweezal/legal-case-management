    close_date = fields.Date(string='Closed Date', readonly=True)    @api.onchange('stage')
    def _onchange_stage(self):
        """Set the closed date when the case is moved to the 'closed' stage."""
        if self.stage == 'closed':
            self.close_date = fields.Date.today()
        else:
            self.close_date = False    def action_create_invoice(self):
        """Creates a draft invoice for the case based on a fixed fee."""
        self.ensure_one()
        
        # Find the correct income account ID
        income_account = self.env['account.account'].search([
            ('user_type_id.type', '=', 'other'),
            ('user_type_id.internal_group', '=', 'income')
        ], limit=1)
        
        # Create a new invoice object in the 'draft' state
        invoice_vals = {
            'move_type': 'out_invoice',  # This means it's a Customer Invoice
            'partner_id': self.client_id.id,
            'invoice_origin': f"Case: {self.name}",  # Helps link invoices to this case
            'invoice_line_ids': [(0, 0, {  # (0, 0, {values}) creates a new line
                'name': f"Legal services for case: {self.name}",
                'quantity': 1,
                'price_unit': self.fixed_fee or 100.0,  # Use the case's fee, default to 100
                'account_id': income_account.id if income_account else False,
            })]
        }
        new_invoice = self.env['account.move'].create(invoice_vals)

        # Open the newly created invoice form view
        return {
            'name': 'Customer Invoice',  # Title of the window
            'view_mode': 'form',
            'res_model': 'account.move',
            'res_id': new_invoice.id,  # ID of the record to open
            'type': 'ir.actions.act_window',
            'target': 'current',  # Opens in the main content area
        }
    def action_view_hearings(self):
        """Smart button action: filters hearings to show only those for this case."""
        self.ensure_one()
        return {
            'name': 'Case Hearings',  # Window title
            'view_mode': 'tree,form',  # Show list first, then form
            'res_model': 'legal.hearing',
            'type': 'ir.actions.act_window',
            'domain': [('case_id', '=', self.id)],  # The magic filter
            'context': {'default_case_id': self.id},  # Pre-fills case_id when creating new hearing
        }

    def action_view_invoices(self):
        """Smart button action: filters invoices to show those generated from this case."""
        self.ensure_one()
        return {
            'name': 'Case Invoices',
            'view_mode': 'tree,form',
            'res_model': 'account.move',
            'type': 'ir.actions.act_window',
            'domain': [('invoice_origin', 'ilike', self.name)],  # Filters by case name/number
        }
    def action_print_case_report(self):
        return self.env.ref('legal_case_mgmt.report_legal_case').report_action(self)