function loadNewLazyImages(t) {
    if ("IntersectionObserver" in window) {
        t = document.querySelectorAll(".lazy");
        var e = new IntersectionObserver(function (t, a) {
            t.forEach(function (t) {
                if (t.isIntersecting) {
                    var a = t.target;
                    (a.src = a.dataset.src), a.classList.remove("lazy"), e.unobserve(a);
                }
            });
        });
        t.forEach(function (t) {
            e.observe(t);
        });
    } else {
        var a;
        function i() {
            a && clearTimeout(a),
                (a = setTimeout(function () {
                    var e = window.pageYOffset;
                    t.forEach(function (t) {
                        t.offsetTop < window.innerHeight + e && ((t.src = t.dataset.src), t.classList.remove("lazy"));
                    }),
                        0 == t.length && (document.removeEventListener("scroll", i), window.removeEventListener("resize", i), window.removeEventListener("orientationChange", i));
                }, 20));
        }
        (t = document.querySelectorAll(".lazy")), document.addEventListener("scroll", i), window.addEventListener("resize", i), window.addEventListener("orientationChange", i);
    }
}

document.addEventListener("DOMContentLoaded", function () {
    loadNewLazyImages(void 0);
});
