/**
 * Created by Cyberrick on 9/2/2016.
 */
$(window).scroll(function(){
    var wscroll = $(document).scrollTop();
    console.log(wscroll);

    if (wscroll > 570) {
        $('.nav-container ,.navbar-collapse').css('backgroundColor','white');
        $('.nav-container').css('opacity',.9);
        $('.brand ,.nav-ul>li>a ,.nav-ul>i').css('color','black');
        $('.icon-bar').css('backgroundColor','black');
    }else{
        $('.nav-container,.navbar-collapse').css('backgroundColor','transparent');
        $('.nav-container').css('opacity',1);
        $('.brand ,.nav-ul>li>a ,.nav-ul>i').css('color','white');
        $('.icon-bar').css('color','white');
    }





    var toTop = $(".toTop");
    if(wscroll > 670){
        toTop.on("click",function(){
            toTop.css('visibility','visible');
            $('html').animate({scrollTop:'0'},1000);
        });
    }else{
        toTop.css('visibility','hidden');
    }
    var form = $(".form");
    $(".submit").on("click",function(){
        form.addClass("animated fadeOutUp");
        form.one('webkitTransitionEnd otransitionend msTransitionEnd transitionEnd',
            function () {
                form.removeClass("fadeOutUp");

            });
        form.addClass("fadeIn");
    });
});

$('#post_form').submit(function(){
var errors = 0;
    $("#post_form").find(">p:input").map(function(){
        if(!$(this).val()){
            $(this).parents('td').addClass('warning');
        }else if($(this).val()){
            $(this).parents('td').removeClass()('warning');
        }
    });
    if(errors > 0){
        $('#errorwarn').text("All fields are required");
        return false;
    }
});