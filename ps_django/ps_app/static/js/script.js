$(()=>{

    /* pae index */
    $('.connecter h6').click(()=>{
        $('.user-options').show()
        $('.user-options').animate({
            top: '9%',
            opacity: '1'
        },1000);
    });
    $('.user-options').mouseleave(()=>{
        $('.user-options').animate({
            top : '15%',
            opacity: '0'
        },1000,()=>{$('.user-options').hide()});
    });
    
    /* page register */
    $('#register').fadeIn(2000);
    $('#register h1').animate({
        'margin-top': '50px',
        'opacity': '1'
    },2000);
    $('#register form').animate({
        'margin-left':'0px',
        'opacity': '1'
    },2000)
    $('#register form .form1').animate({
        'opacity':'1'
    },2000,()=>{
        $('#register form .form2').animate({'opacity':'1'},300,()=> {
            $('#register form .form3').animate({'opacity':'1'},300,()=>{
               $('#register form .form4').animate({'opacity':'1'},300,()=>{
                  $('#register form .form5').animate({'opacity':'1'},300,()=>{
                     $('#register form .form6').animate({'opacity':'1'},300,()=>{
                         $('#register form button[type="submit"]').animate({'opacity':'1'},1000);
                     });
                  });
               });
            });
        });
    });

    $('#register form').submit((e)=>{
        if ($('#register form input[name="ps1"]').val() != $('#register form input[name="ps2"]').val()){
            e.preventDefault();
            $('#register form .error').show()
            $('#register form .error').animate({'opacity':'1'},300);
        }
    });

        /* page login */
    $('#login').fadeIn(2000);
    $('#login h1').animate({
        'margin-top': '50px',
        'opacity': '1'
    },2000);
    $('#login form').animate({
        'margin-left':'0px',
        'opacity': '1'
    },2000)
    $('#login form .form1').animate({
        'opacity':'1'
    },2000,()=>{
        $('#login form .form2').animate({'opacity':'1'},500,()=>{
            $('#login form button[type="submit"]').animate({'opacity':'1'},1000);
        });
    });
});