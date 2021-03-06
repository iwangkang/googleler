(function (e) {
    e.fn.modal = function (t) {
        function o() {
            e("." + t.videoClass).attr("src", t.video);
            r.hide();
            if (e(window).width() < i.outerWidth()) var o = e(window).width() - i.outerWidth() / 2 + e(window).scrollLeft();
            else var o = e(window).width() / 2 - i.outerWidth() / 2 + e(window).scrollLeft();
            i.css({
                top: e(window).height() / 2 - i.outerHeight() / 2 + e(window).scrollTop(),
                left: o
            });
            if (s === false) {
                n.css({
                    opacity: t.opacity,
                    backgroundColor: "#" + t.background
                });
                n[t.animationEffect](t.animationSpeed);
                i.delay(t.animationSpeed)[t.animationEffect](t.animationSpeed)
            } else {
                i.show()
            }
            s = true
        }

        function u() {
            if (e(window).width() < r.outerWidth()) {
                var n = e(window).width() - r.outerWidth() / 2 + e(window).scrollLeft()
            } else {
                var n = e(window).width() / 2 - r.outerWidth() / 2 + e(window).scrollLeft()
            }
            r.stop(true).animate({
                top: e(window).height() / 2 - r.outerHeight() / 2 + e(window).scrollTop(),
                left: n
            }, t.moveModalSpeed)
        }

        function a() {
            e("." + t.videoClass).attr("src", "");
            s = false;
            r.fadeOut(100, function () {
                if (t.animationEffect === "slideDown") {
                    n.slideUp()
                } else if (t.animationEffect === "fadeIn") {
                    n.fadeOut()
                }
            });
            return false
        }
        t = e.extend({
            trigger: ".modalLink",
            olay: "div.overlay",
            modals: "div.modal",
            animationEffect: "fadeIn",
            animationSpeed: 400,
            moveModalSpeed: "slow",
            background: "000",
            opacity: .8,
            openOnLoad: false,
            docClose: true,
            closeByEscape: true,
            moveOnScroll: true,
            resizeWindow: true,
            video: "",
            videoClass: "video",
            close: ".closeBtn"
        }, t);
        var n = e(t.olay);
        var r = e(t.modals);
        var i;
        var s = false;
        if (t.animationEffect === "fadein") {
            t.animationEffect = "fadeIn"
        }
        if (t.animationEffect === "slidedown") {
            t.animationEffect = "slideDown"
        }
        n.css({
            opacity: 0
        });
        if (t.openOnLoad) {
            o()
        } else {
            n.hide();
            r.hide()
        }
        e(t.trigger).bind("click", function (t) {
            t.preventDefault();
            if (e(".modalLink").length > 1) {
                getModal = e(this).attr("href");
                i = e(getModal)
            } else {
                i = e(".modal")
            }
            o()
        });
        if (t.docClose) {
            n.bind("click", a)
        }
        e(t.close).bind("click", a);
        if (t.closeByEscape) {
            e(window).bind("keyup", function (e) {
                if (e.which === 27) {
                    a()
                }
            })
        }
        if (t.resizeWindow) {
            e(window).bind("resize", u)
        } else {
            return false
        } if (t.moveOnScroll) {
            e(window).bind("scroll", u)
        } else {
            return false
        }
    }
})(jQuery)