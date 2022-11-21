function pad(t) {
    var e = t + "";
    return e.length < 2 ? "0" + e : e;
}
var interval;
!(function (t) {
    t("#reset").on("click", function () {
        t("#register-form").reset();
    });
})(jQuery);
var startTimer = function (t, e) {
    clearInterval(interval);
    var r,
        n,
        a = t;
    interval = setInterval(function () {
        (r = parseInt(a / 60, 10)), (n = parseInt(a % 60, 10));
        var t = (r = r < 10 ? "0" + r : r) + ":" + (n = n < 10 ? "0" + n : n);
        // console.log(t);
        (e.textContent = t), --a < 0 && (clearInterval(interval), (a = 0), $("#resend-otp-btn").show());
    }, 1e3);
};