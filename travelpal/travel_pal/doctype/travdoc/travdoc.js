// Copyright (c) 2024, George Michael and contributors
// For license information, please see license.txt

frappe.ui.form.on('TravDoc' , {
	refresh: function(frm) {
		frm.add_custom_button(_('HHHH'), function(){
			frappe.msgprint(frm.doc.item_name);
		}, _("Actions"));

	 }
});
