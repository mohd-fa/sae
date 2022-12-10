function myFunction() {
    var x = document.getElementById("responsive");
    if (x.className === "on") {
        x.className = "off";
    } else {
        x.className = "on";
    }
    document.body.scrollTop = 0;
    document.documentElement.scrollTop = 0;
}
window.onscroll = function () {
    var x = document.getElementById("responsive");
    var currentScrollPos = window.pageYOffset;
    if (currentScrollPos > 5) {
        x.className = "off";
    }
}