$(document).ready(function () {
    var routingUrl = 'http://' + location.hostname + ':8000';       // 接口服务地址
    var file_path = 'http://' + location.hostname + ':8080/';

    $(document).on('click', '.get-file-detail', function () {
        // 添加一些相关信息
        FileNodeType = $(this).parents('.vis-tip-div').attr('nodetype');
        var fileImgStr = '';
        $('.file-show-panel').html(fileImgStr);
        $('.file-detail-panel').show();
        /*上传文件插件*/
        $('#input-file').fileinput({
            language: 'zh',
            uploadUrl: 'http://106.12.37.57:80/upload_File'
        });
        /*上传文件插件*/
    });
    // 关闭文件上传界面
    $(document).on('click', '.file-detail-close', function () {
        $('.file-detail-panel').hide();                                 // 关闭详情模态框,

    });

    $(document).on('click', '.vis-Comment-server-submit', function () {
        var server_name = $("#server_name").val();
        var server_name_en = $("#server_name_en").val();
        var server_description = $("#server_description").val();
        var server_url = $("#server_url").val();
        var ServerInfo = {
            server_name: server_name,
            server_name_en: server_name_en,
            server_description:server_description,
            server_url:server_url,
        };
        $.ajax({
            url: routingUrl + '/server_register',
            data: ServerInfo,
            dataType:'json',
            type: 'POST',
            success: function (res) {
                if (res.code == 200){
                    console.log(res.message);
                }
            },
            error: function () {
                console.log("failure");
            }
        })

    });

    getCurrentLoginInfo();
    /**
     * 请求当前登录账户
     */
    function getCurrentLoginInfo() {
        $.ajax({
            url: routingUrl + '/get_current_login_info',
            type: 'POST',
            success: function (res) {
                console.log("请求当前登录账户成功 __url --> /get_current_login_info");
                console.dir(res);
                $('.login-div').find('strong').html(res.username);
            },
            error: function () {
                console.log("请求当前登录账户成功 __url --> /get_current_login_info");
            }
        })
    }
    // 登录账户
    $(document).on('click', '.login-div', function () {
        $('.login-ul').slideToggle(200);
    });
    // 注销
     $(document).on('click', '#logout', function () {
        $('.login-ul').slideUp(200);
        $.ajax({
            url: routingUrl + '/back_user_logout',
            type: 'POST',
            success: function (res) {
                console.log("注销账户");
                window.location.href = routingUrl + '/back_login';
            },
            error: function () {
                console.log("注销失败");
            }
        });
    });

     $(document).on('click', '#index', function () {
        $("#table_user").show();
        $("#form_user").hide();
        $("#form_server").hide();

     });

     $(document).on('click', '#user', function () {
        $("#table_user").hide();
        $("#form_server").hide();
         $("#form_user").show();
     });

     $(document).on('click', '#server', function () {
        $("#table_user").hide();
        $("#form_server").show();
        $("#form_user").hide();
     });


     $(document).on('click', '.vis-news-tip-submit', function () {
        var name = $("#news_name").val();
        var type = $("#news_type").val();
        var source = $("#news_source").val();
        var author = $("#news_author").val();
        var news = $("#news_info").val();

        var image_list = [];
        if (NodeFileList.length>0){
            for (var i=0;i<NodeFileList.length;i++){
                var image_url = NodeFileList[i].imgPath;
                image_list.push(image_url);
            }
        }


        var NewsInfo = {
            name: name,
            type: type,
            source:source,
            image_list:image_list.toString(),
            author:author,
            news:news
        };
        console.log(NewsInfo);
        $.ajax({
            url: routingUrl + '/save_news_info',
            data: NewsInfo,
            dataType:'json',
            type: 'POST',
            success: function (res) {
                if (res.code == 200){
                    console.log(res.message);
                }
            },
            error: function () {
                console.log("failure");
            }
        })
     });

     $(document).on('click', '.vis-Comment-user-submit', function () {
        var username = $("#user_name").val();
        var password = $("#password").val();
        var password_confirmation = $("#password_confirmation").val();
        var UserInfo = {
            username: username,
            password: password,
            password_confirmation:password_confirmation,
        };
        console.log(UserInfo);
        $.ajax({
            url: routingUrl + '/user_register',
            data: UserInfo,
            dataType:'json',
            type: 'POST',
            success: function (res) {
                if (res.code == 200){
                    console.log(res.message);
                }
            },
            error: function () {
                console.log("failure");
            }
        })
     });
});