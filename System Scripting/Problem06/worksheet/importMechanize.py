import mechanize
#
br = mechanize.Browser()
# The search web site - try it with browser
br.open("http://www.rp.sg/staffdirectory/dept.aspx?Mode=department")
# Select form number 0 - that's the first web form on the page
br.select_form(nr=0)
# This is the form's text field name. In the browser,
# it appears next to "Name of staff" label.
br['ctl00$WebContent$txtName'] = 'Tan'
# Submit the form, as if you're pressing the "Search" button
result = br.submit()
# Print the output (in HTML)
print result.read()