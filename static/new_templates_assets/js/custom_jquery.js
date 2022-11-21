
// $("#header").load("header.html");
// $("#inner_header").load("inner_header.html");
// $("#wpooch").load("wpooch.html");
// $("#nswihlh_page").load("nswihlhc.html");
// $("#how_it_works").load("how_it_works.html");
// $("#suggested_plan").load("suggested_plan.html");


// $("#footer").load("footer.html");




$(window).scroll(function () {    
    var scroll = $(window).scrollTop();
    if (scroll >= 1) {        
        $(".header_bx").addClass("top-fixed");
    } else {        
        $(".header_bx").removeClass("top-fixed");
    }
});

$(document).ready(function () {
    
    if ($(window).width() < 990) {        
        $('.prdnewslider').slick({
            infinite: false,
            slidesToShow: 1.5,
            slidesToScroll: 1.5,        
            dots: true,
            arrows: false,
            accessibility: false              
        });
        $('.prdnewslider').slick({
          infinite: false,
          slidesToShow: 1.5,
          slidesToScroll: 1.5,        
          dots: true,
          arrows: false,
          accessibility: false              
      });             
    }    

    $('#cbl_slider').slick({
        autoplay: true,
        autoplaySpeed: 2000,
        /*centerMode: true,*/
        /*centerPadding: '60px',*/
        slidesToShow: 5,
        responsive: [
            {
                breakpoint: 768,
                settings: {
                    arrows: false,
                    centerMode: true,
                    centerPadding: '40px',
                    slidesToShow: 4
                }
            },
            {
                breakpoint: 480,
                settings: {
                    arrows: false,
                    centerMode: true,
                    centerPadding: '0px',
                    slidesToShow: 2,
                    dots: false,
                }
            }
        ]
    });

  $('#tdn_slider').slick({
        infinite: false,
        slidesToShow: 3,
        slidesToScroll: 3,
        responsive: [
            {
              breakpoint: 1024,
              settings: {
                slidesToShow: 2,
                slidesToScroll: 2,
                infinite: true,
                dots: true,
                arrows: false,
              }
            },
            {
              breakpoint: 600,
              settings: {
                slidesToShow: 2,
                slidesToScroll: 2,
                dots: true,
                arrows: false,
              }
            },
            {
              breakpoint: 480,
              settings: {
                slidesToShow: 1,
                slidesToScroll: 1,
                dots: true,
                arrows: false,
              }
            }            
          ]          
      });
  
      $('#wca_owl').slick({
      infinite: false,
      slidesToShow: 2,
      slidesToScroll: 2,
      dots: true,
      arrows: false,
      responsive: [
          {
            breakpoint: 1024,
            settings: {
              slidesToShow: 2,
              slidesToScroll: 2,
              infinite: true,
              dots: true,
              arrows: false,
            }
          },
          {
            breakpoint: 600,
            settings: {
              slidesToShow: 2,
              slidesToScroll: 2,
              dots: true,
              arrows: false,
            }
          },
          {
            breakpoint: 480,
            settings: {
              slidesToShow: 1,
              slidesToScroll: 1,
              dots: true,
              arrows: false,
            }
          }            
        ]  
  });

    $('#wcaoce').owlCarousel({
        loop:false,
        margin:10,
        nav:true,
        dots: true,
        navText : ["<i class='ri-arrow-left-s-line'></i>","<i class='ri-arrow-right-s-line'></i>"],
        responsive:{
            0:{
                items:1
            },
            600:{
                items:2
            },
            1000:{
                items:3
            },
            // 1600:{
            //     items:4.5
            // }
        }
})
    $("#dtl_sldrm").owlCarousel({    
        loop:false,
        items:1,
        margin:0,
        stagePadding: 0,
        dots: true,
        mouseDrag: true,
        touchDrag: true,
        //nav: true,            
        responsive:{
            0:{
                autoplay:true  
            },
            600:{
                autoplay:true  
            },                
        }
    });

    dotcount = 1;

    jQuery('.owl-dot').each(function() {            
        jQuery( this ).addClass( 'dotnumber' + dotcount);
        jQuery( this ).attr('data-info', dotcount);
        dotcount=dotcount+1;
    });

    slidecount = 1;

    jQuery('.owl-item').not('.cloned').each(function() {            
        jQuery( this ).addClass( 'slidenumber' + slidecount);
        slidecount=slidecount+1;
    });

    jQuery('.owl-dot').each(function() {	            
        grab = jQuery(this).data('info');		
        slidegrab = jQuery('.slidenumber'+ grab +' img').attr('src');
        jQuery(this).css("background-image", "url("+slidegrab+")");  	
    });

    amount = $('.owl-dot').length;
    gotowidth = 100/amount;			
    jQuery('.owl-dot').css("height", gotowidth+"%");   
    
 });


 if ($(window).width() < 990) {
  $(function() {
    var slideCount =  $(".slider ul li").length;
    var slideWidth =  $(".slider ul li").width();
    var slideHeight =  $(".slider ul li").height();
    var slideUlWidth =  slideCount * slideWidth;
    
    $(".slider").css({"max-width":slideWidth, "height": slideHeight});
    $(".slider ul").css({"width":slideUlWidth, "margin-left": - slideWidth });
    $(".slider ul li:last-child").prependTo($(".slider ul"));
  
    function moveLeft() {
      $(".slider ul").stop().animate({
        left: + slideWidth
      },700, function() {
        $(".slider ul li:last-child").prependTo($(".slider ul"));
        $(".slider ul").css("left","");
      });
    };
  
    function moveRight() {
      $(".slider ul").stop().animate({
        left: - slideWidth
      },700, function() {
        $(".slider ul li:first-child").appendTo($(".slider ul"));
        $(".slider ul").css("left","");
      });
    };  
  
    $(".next").on("click",function(){
      moveRight();      
    });
    
    $(".prev").on("click",function(){
      moveLeft();      
    });
  });
};




function HideLoader(){
  setTimeout(function() {
    $('.main_loader').hide();
}, 800);
}

function ShowLoader(){
  $('.main_loader').removeClass('d-none');
}