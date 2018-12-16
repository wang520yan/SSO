$(document).ready(function () {
    var routingUrl = 'http://' + location.hostname + ':8000';       // 接口服务地址

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
            url: routingUrl + '/user_logout',
            type: 'POST',
            success: function (res) {
                console.log("注销账户");
                window.location.href = routingUrl + '/login';
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

     function getAllServers() {
        $.ajax({
            url: routingUrl + '/get_all_server',
            type: 'POST',
            success: function (res) {
                console.log(res.data);
                $('.login-div').find('strong').html(res.username);
            },
            error: function () {
                console.log("获取服务失败");
            }
        })
    }
    getAllServers();
});