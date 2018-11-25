
$(document).ready(function(){
    window.setTimeout( show_popup, 3000 );
    $.ajax({
        url:'/eatm/SBI/',
        type:'get',
        success:function(data) {
            alert(data);
        },

    });
});