# Copyright (c) 2025, prasanna and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document

class Students(Document):
	pass
import frappe
def validate_grading(doc, method):
    """Function to set grade based on obtained marks."""
    if doc.obtained_marks is not None:
        if doc.obtained_marks >= 90:
            doc.grade = "Grade A"
        elif doc.obtained_marks >= 75:
            doc.grade = "Grade B"
        elif doc.obtained_marks >= 50:
            doc.grade = "Grade C"
        elif doc.obtained_marks >= 35:
            doc.grade = "Grade D"
        else:
            doc.grade = "Grade F"

def set_student_progress_based_on_grade(doc, method):
    """Function to set student progress based on the assigned grade."""
    if doc.grade:  # Check if grade has been set
        # Define the percentage corresponding to each grade
        grade_percentage = {
            "Grade A": 100,
            "Grade B": 85,
            "Grade C": 60,
            "Grade D": 40
           # Set F as 39% for the range 1 to 39
        }

        # Set student progress based on the grade
        doc.student_progress = grade_percentage.get(doc.grade, 0)  # Default to 0 if grade is not found

class Students(Document):
    def validate(self):
        """Override the validate method to call validate_grading and set_student_progress_based_on_grade"""
        validate_grading(self, "validate")  # Call grade function
        set_student_progress_based_on_grade(self, "validate")  # Call student progress function
