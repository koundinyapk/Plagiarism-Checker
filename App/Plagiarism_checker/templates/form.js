const loginBtn = document.querySelector(".loginBtn");
const signUpBtn = document.querySelector(".signUpBtn");
const FormBx = document.querySelector(".FormBx");

const usInput = document.getElementById("username");
const passInput = document.getElementById("password");

const usIn = document.getElementById("userid");
const emailIn = document.getElementById("emailid");
const passIn = document.getElementById("passwdid");
const cpassIn = document.getElementById("cpasswdid");

usInput.addEventListener('click', function () {
    usInput.style.backgroundColor = 'white';
})

passInput.addEventListener('click', function () {
    passInput.style.backgroundColor = 'white';
})

usIn.addEventListener('click', function () {
    usIn.style.backgroundColor = 'white';
})

emailIn.addEventListener('click', function () {
    emailIn.style.backgroundColor = 'white';
})

passIn.addEventListener('click', function () {
    passIn.style.backgroundColor = 'white';
})

cpassIn.addEventListener('click', function () {
    cpassIn.style.backgroundColor = 'white';
})

signUpBtn.onclick = function () {
    FormBx.classList.add("active");
}


loginBtn.onclick = function () {
    FormBx.classList.remove("active");
}

const togglePassword = document.querySelector('#togglePassword1');
togglePassword.addEventListener('click', function (e) {
    // toggle the type attribute
    const type = passInput.getAttribute('type') === 'password' ? 'text' : 'password';
    password.setAttribute('type', type);
    // toggle the eye slash icon
    this.classList.toggle('fa-eye-slash');
});

const togglePassword2 = document.querySelector('#togglePassword2');
togglePassword2.addEventListener('click', () => {
    if (passIn.type === 'password') {
        passIn.type = 'text';
    } else {
        passIn.type = 'password';
    }


});

const togglePassword3 = document.querySelector('#togglePassword3');
togglePassword3.addEventListener('click', () => {

    if (cpassIn.type === 'password') {
        cpassIn.type = 'text';
    } else {
        cpassIn.type = 'password';
    }

});

document.querySelector('#sform').addEventListener('submit', (event) => {
    if (passIn.value !== cpassIn.value) {
        alert('Passwords do not match!');
        event.preventDefault(); // Prevent form submission
    }
})


