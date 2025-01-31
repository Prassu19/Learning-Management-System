# Copyright (c) 2025, prasanna and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class Assessments(Document):
	pass





def validate_grading(doc, method):
    
    if doc.obtained_marks is not None:
        if doc.obtained_marks >= 90:
            doc.grading = "A"
        elif doc.obtained_marks >= 75:
            doc.grading = "B"
        elif doc.obtained_marks >= 50:
            doc.grading = "C"
        elif doc.obtained_marks >= 35:
            doc.grading = "D"
        else:
            doc.grading = "F"

class Assessments(Document):
    def validate(self):
        validate_grading(self, "validate")


