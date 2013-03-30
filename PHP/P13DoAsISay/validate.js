function validate(form) {

    var name = form.full_name.value;
    var nric = form.nric.value;
    var dob = form.dob.value;
    var email = form.email.value;
    var contactNo = form.contact_no.value;
    var postalCode = form.postal_code.value;
    var username = form.username.value;
    var password = form.password.value;
    var confirm_password = form.confirm_password.value;

    var name_regex = /^[A-Z]\w+([ ][A-Z]\w+)*$/;
    var nric_regex = /^[S]\d{7}[A-Z]$/
    var dob_regex = /^(\d{4}\-\d{2}\-\d{2})?$/
    var email_regex = /^(\w+[\-\.])*\w+@(\w+\.)+[A-Za-z]+$/;
    var contactno_regex = /^[689][0-9]{7}$/;
    var postalcode_regex = /^[0-9]{6}$/;
    var username_regex = /^[A-Za-z\d]{6,15}$/;
    var password_regex = /^[A-Za-z\d]{6,8}$/;

    var errors = [];

    if (name == null || name == "") {

        errors[errors.length] = "Name cannot be empty!";

    }

    if (!name_regex.test(name)) {

        errors[errors.length] = "Name must start with a capital letter";

    }

    if (nric == null || nric == "") {

        errors[errors.length] = "NRIC cannot be empty!";

    }

    if (!nric_regex.test(nric)) {

        errors[errors.length] = "NRIC must start with an S, followed by 7 numbers, and a capital letter at the end";

    }

    if (!dob_regex.test(dob)) {

        errors[errors.length] = "Date of birth must be in yyyy-mm-dd format";

    }

    if (email == null || email == "") {

        errors[errors.length] = "Email cannot be empty!";

    }

    if (!email_regex.test(email)) {

        errors[errors.length] = "Email must be valid!";

    }

    if (contactNo == null || contactNo == "") {

        errors[errors.length] = "Contact cannot be empty!";

    }

    if (!contactno_regex.test(contactNo)) {

        errors[errors.length] = "Contact number must contain 8 digits, starting either with 6/8/9";

    }

    if (postalCode == null || postalCode == "") {

        errors[errors.length] = "Postal code cannot be empty!";

    }

    if (!postalcode_regex.test(postalCode)) {

        errors[errors.length] = "Postal code must be of 6 digits!";

    }

    if (username == null || username == "") {

        errors[errors.length] = "Username cannot be empty!";

    }

    if (!username_regex.test(username)) {

        errors[errors.length] = "Username must contain 6-15 alphanumeric letters";

    }

    if (password == null || password == "" || confirm_password == null || confirm_password == "") {

        errors[errors.length] = "Password field(s) cannot be empty!";

    }

    if (password != confirm_password) {

        errors[errors.length] = "Password(s) do not tally";

    }

    if(!password_regex.test(password)) {

        errors[errors.length] = "Password must contain 6-8 alpnumeric letters";

    }

    if (errors.length>0) {

        reportErrors(errors);
        return false;

    }

    else {

        return true;

    }

}

function reportErrors(errors) {

    var msg = "There are some problems in your registration.\n";

    for (var i = 0; i< errors.length; i++) {

        var numError = i + 1;
        msg += "\n" + numError + ". " + errors[i];

    }

    alert(msg);
}