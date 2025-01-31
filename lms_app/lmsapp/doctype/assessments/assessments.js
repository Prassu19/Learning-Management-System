// Copyright (c) 2025, prasanna and contributors
// For license information, please see license.txt

frappe.ui.form.on('Assessments', {
    validate: function(frm) {
        const total_marks = frm.doc.total_marks;
        const obtained_marks = frm.doc.obtained_marks;
        const due_date = frm.doc.due_date;

    
        if (obtained_marks > total_marks) {
            frappe.msgprint(__('Obtained marks cannot exceed Total marks.'));
            frappe.validated = false;
            return;
        }

        if (total_marks && obtained_marks !== undefined) {
            const percentage = (obtained_marks / total_marks) * 100;
            frm.set_value('percentage', percentage.toFixed(2)); // Update the percentage field
            console.log('Calculated Percentage:', percentage.toFixed(2));
        }

        if (due_date && due_date <= frappe.datetime.get_today()) {
            frappe.msgprint(__('Due date must be a future date.'));
            frappe.validated = false;
            return;
        }
    }
});


