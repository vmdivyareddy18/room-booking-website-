function checkLogin() {

    let email = document.getElementById("email").value;
    let pass = document.getElementById("pass").value;

    if (email == "" || pass == "") {
        alert("Please fill all fields");
        return false;
    }

    return true;
}
