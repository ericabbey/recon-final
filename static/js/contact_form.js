/**
 * Created by cyberrick on 11/10/2016.
 */

$(document).ready(function(){
    $(document).on('submit',function(e){
        e.preventDefault();

        $.ajax({
            type:'POST',
            url: '/contact/',
            data:{
                name: $('#name').val(),
                email:$('#email').val(),
                message:$('#message').val(),
                csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val()
            },
            success: function(){
                $('#name').text("");
                $('#email').text("");
                $('#message').text("")
                var show = $('.success').show();
                setTimeout(show,3000);
            }
        });
    });
});
