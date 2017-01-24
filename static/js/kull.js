$(document).ready(function(){
    $('html').niceScroll({
        cursorborder: 'none',
        cursorcolor: '#aaaaaa',
        cursorwidth: '7px'
    });
    var cont =  $('.about-container-in');
   cont.mouseenter(function(){
        $(this).children('.showpara').animate({
            display: 'block',
            top:'-306px',
            height:'270px',
            padding:'5px'
        })
    });
   cont.mouseleave(function(){
        $(this).children('.showpara').animate({
            top:'-1006px',
            height:'270px',
            padding:'5px',
            display: 'none'
        })
    });
    $('.say').click(function(){
        $(this).replaceWith(('<textarea cols="40" id="id_content" name="content" rows="10"></textarea>'));
        $('.submit-comment').css('display','block');
        $('#id_content').focus();
    });


});