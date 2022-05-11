function scrollFunction1() {
    let e = document.getElementById("el1");
    e.scrollIntoView({
        block: 'start',
        behavior: 'smooth',
        inline: 'start'
    });
}
function scrollFunction2() {
    let e = document.getElementById("el2");
    e.scrollIntoView({
        block: 'end',
        behavior: 'smooth',
        inline: 'center'
    });
}
