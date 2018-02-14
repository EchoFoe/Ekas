/Скрипт для кнопки "наверх"/
$(function () {

    var scroll_timer;
    var displayed = false;
    var $message = $('#message a');
    var $window = $(window);
    var top = $(document.body).children(0).position().top;

$window.scroll(function () {
    window.clearTimeout(scroll_timer);
scroll_timer = window.setTimeout(function () {
    if($window.scrollTop() <= top) {
        displayed = false;
        $message.fadeOut(500);
    }
    else if(displayed == false) {
        displayed = true;
        $message.stop(true, true).show().click(function () { $message.fadeOut(500); });
    }
}, 100);
});
});
/Скрипт анимационные эффекты/
$(document).ready(function(){

    $("#headerwrap .eco").eq(0).addClass('animated bounceInLeft');
    $("#headerwrap .kotel").eq(0).addClass('animated bounceInRight');
    $("#headerwrap .auto").eq(0).addClass('animated bounceInLeft');
    $("#headerwrap .servis").eq(0).addClass('animated bounceInRight');
    // $("#eks1 .eks1IN1").eq(0).addClass('animated zoomIn');
    // $("#eks1 .eks1IN2").eq(0).addClass('animated bounceInUp');
    // $("#BMK1 .BMKIN1").eq(0).addClass('animated zoomIn');
    // $("#BMK1 .BMKIN2").eq(0).addClass('animated bounceInUp');
    // $("#BMK1 .BMKIN3").addClass('animated bounceInDown');
    var h = $(window).height();
    $(window).scroll(function(){
        // $("#ex1 .eb1").addClass('animated bounceInLeft');
        // $("#ex1 .eb2").addClass('animated bounceInUp');
        // $("#ex1 .eb3").addClass('animated bounceInRight');
        // $("#eks1 .eks1IN3").addClass('animated bounceInRight');
        $("#eks1 .eks1IN4").eq(0).addClass('animated bounceInUp');
        $("#eks1 .eks1IN5").eq(0).addClass('animated bounceInUp');
        // $("#BMK1 .BMKIN4").eq(0).addClass('animated bounceInUp');
        $("#BMK1 .BMKIN5").eq(0).addClass('animated bounceInRight');
        if ( ($(this).scrollTop()+h) >= $("#ex2").offset().top) {
            $("#ex2 .opisanie").css({visibility:"visible"});
            $("#ex2 .lil1").eq(0).addClass('animated bounceInUp');
            $("#ex2 .lil2").eq(1).addClass('animated bounceInRight');
        }
        // if (($(this).scrollTop()+h) >= $("#yo").offset().top) {
        //     $("#yo .container").css({visibility:"visible"});
        //     $("#yo .yoright").eq(0).addClass('animated rotateInDownRight');
        //     $("#yo .container").css({visibility:"visible"});
        //     $("#yo .yoleft").eq(0).addClass('animated rotateInDownLeft');
        // }
        // if ( ($(this).scrollTop()+h) >= $("#dg").offset().top) {
        //     $("#dg .container").css({visibility:"visible"});
        //     $("#dg .proektright").eq(0).addClass('animated zoomInRight');
        //     $("#dg .container").css({visibility:"visible"});
        //     $("#dg .bmkleft").eq(0).addClass('animated zoomInLeft');
        // }
        // if ( ($(this).scrollTop()+h) >= $("#dg1 .kipiaright").offset().top) {
        //     $("#dg1 .container").css({visibility:"visible"});
        //     $("#dg1 .kipiaright").eq(0).addClass('animated bounceInUp');
        //     $("#dg1 .container").css({visibility:"visible"});
        //     $("#dg1 .epbleft").eq(0).addClass('animated bounceInUp');
        // }
        if ( ($(this).scrollTop()+h) >= $("#parneri").offset().top) {
            $("#parneri .container").css({visibility:"visible"});
            $("#parneri .container").eq(0).addClass('animated bounceInUp');
        }
        // if ( $(this).scrollTop() == 0 ) {
        //     $("#ex1 .eb1").each(function(){
        //         if ( $(this).hasClass('.eb1') ) {
        //             $(this).removeClass().addClass('.eb1');
        //         } else {
        //             $(this).removeClass().addClass('.eb1');
        //         }
        //         $(this).css({visibility:"hidden"});
        //     });
        // }
    });
});
/Скрипт для кнопок отзывов ЭПБ/
$(function(){
	var	btn = $(".slider__btn");

	btn.on("click",function(){
		$(".slider__item").first().clone().appendTo(".slider");
		$(".slider__image").first().css({transform: "rotateX(-180deg)", opacity: 0});
		setTimeout(function(){
			$(".slider__item").first().remove();
		},200);
	});
});
$(function () {
    var	btn2 = $(".slider__btn2");

	btn2.on("click",function(){
		$(".slider__item2").first().clone().appendTo(".slider2");
		$(".slider__image2").first().css({transform: "rotateX(-180deg)", opacity: 0});
		setTimeout(function(){
			$(".slider__item2").first().remove();
		},200);
	});
});

