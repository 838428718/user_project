
function userItemShow(page){
    $.ajax({
        type:"GET",
        url:"/app/show_item",
        data:{'page':page},
        success: function(data){
            if(data['status']=='200'){
                userData = data['data'];
                $('#page').text(data['page']);
                $('.userShow').empty();
                for (var i=0;i<userData.length;i++){
                    $('.userShow').prepend("<li></li>");
                    $('.userShow li:first').prepend("<div class=\"item\"></div>");
                    $('.item:first').append($("<img/>").attr({ src: "../static/img/icon.png/", class: "icon" }))
                    $('.item:first').append($("<a href=\"#\" class='userName' ></a>").text(userData[i]['user_name']));
                    $('.item:first').append($("<a href=\"#\" class='group'></a>").text(userData[i]['group']));
                    $('.item:first').append($("<a href=\"#\" class=\"manage\">Edit</a>"));
                    $('.item:first').append($("<a href=\"#\" class= 'manage' id='deleteUser'>Delete</a>"));
                    $('.item:first').append($("<input type='hidden' id='uid'/>").val(userData[i]['uid']));

                }

            }

        }
    });
}
$(function () {
    var page = parseInt($('#page').text());
    userItemShow(page)

    $("#pageUp").click(function() {
        var page = parseInt($('#page').text());
        userItemShow(page-1)
    })


    $("#pageDown").click(function() {
        var page = parseInt($('#page').text());
        userItemShow(page+1)
    })

    $("#pageTo").click(function() {
        var pageNum = parseInt($('.pageNumber').val());
        userItemShow(pageNum)
    })

    $("#logout").click(function() {
        $.ajax({
            type:"GET",
            url:"/app/logout",
            success:function (data) {
                window.location.href="/app/logout";
            }
        });
    })


});
 $(document).on("click", "#deleteUser", function () {
     var item = $(this).parent();
     var uid = item.children('#uid').val();
     var page = parseInt($('#page').text());
     $.ajax({
            type:"GET",
            url:"/app/delete_user",
            data:{'uid': uid},
            success:function (data) {
                if (data['status'] == '200'){
                    alert('deleted successfully')
                    userItemShow(page)
                }

            }
        });
 });

 $(document).on('click', '.userName', function () {
     var item = $(this).parent();
     var uid = item.children('#uid').val();
     $.ajax({
            type:"GET",
            url:"/app/show_user_info",
            data:{'uid': uid},
            success:function (data) {
                if(data['status']=='200'){
                    var msg = 'username:'+data['data']['userName']+'\nage:'+data['data']['age']+'\nphone:'+data['data']['phone']+'\ngroup:'+data['data']['group']
                    alert(msg)
                }

            }
        });
 })