
frappe.ui.form.on('Assessment Enrollments', {
    member: function(frm) {
       
        if (frm.doc.member) {
            frappe.call({
                method: 'frappe.client.get',
                args: {
                    doctype: 'Students',
                    name: frm.doc.member
                },
                callback: function(response) {
                    if (response.message) {
                        var students = response.message;
                        
                        frm.set_value('age', students.age);
                        frm.set_value('email_address', students.email_address);
                        frm.set_value('gender', students.gender);
                        frm.set_value('national_id', students.national_id);
                        frm.set_value('address', students.address);
                        frm.set_value('enrollment_date', students.enrollment_date);

                    }
                }
            });
        }
    }
});
