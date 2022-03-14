def test_enquiry_str(enquiry):
    """Test the Enquiry model __str__ method."""
    assert enquiry.__str__() == enquiry.email
