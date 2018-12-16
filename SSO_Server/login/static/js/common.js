/**
 * 显示Loading 加载框
 * @param $panel    显示加载框的位置
 * @param circle_r  加载动画圆的大小
 * @param color 加载动画的颜色 (可选)
 */
function showLoading($panel, circle_r, color) {
    color = color ? color : 'rgba(1, 194, 255, 0.87)';
    var _circle_r = parseInt(circle_r / 3);
    var loadingStr = '                    <div class="loading-card" style="width: ' + circle_r + 'px; height: ' + circle_r + 'px;">\n' +
        '                        <div class="loading-panel panel1">\n' +
        '                            <div class="circle1" style="width: ' + _circle_r + 'px; height: ' + _circle_r + 'px; background-color: ' + color + '"></div>\n' +
        '                            <div class="circle2" style="width: ' + _circle_r + 'px; height: ' + _circle_r + 'px; background-color: ' + color + '"></div>\n' +
        '                            <div class="circle3" style="width: ' + _circle_r + 'px; height: ' + _circle_r + 'px; background-color: ' + color + '"></div>\n' +
        '                            <div class="circle4" style="width: ' + _circle_r + 'px; height: ' + _circle_r + 'px; background-color: ' + color + '"></div>\n' +
        '                        </div>\n' +
        '                        <div class="loading-panel panel2">\n' +
        '                            <div class="circle1" style="width: ' + _circle_r + 'px; height: ' + _circle_r + 'px; background-color: ' + color + '"></div>\n' +
        '                            <div class="circle2" style="width: ' + _circle_r + 'px; height: ' + _circle_r + 'px; background-color: ' + color + '"></div>\n' +
        '                            <div class="circle3" style="width: ' + _circle_r + 'px; height: ' + _circle_r + 'px; background-color: ' + color + '"></div>\n' +
        '                            <div class="circle4" style="width: ' + _circle_r + 'px; height: ' + _circle_r + 'px; background-color: ' + color + '"></div>\n' +
        '                        </div>\n' +
        '                        <div class="loading-panel panel3">\n' +
        '                            <div class="circle1" style="width: ' + _circle_r + 'px; height: ' + _circle_r + 'px; background-color: ' + color + '"></div>\n' +
        '                            <div class="circle2" style="width: ' + _circle_r + 'px; height: ' + _circle_r + 'px; background-color: ' + color + '"></div>\n' +
        '                            <div class="circle3" style="width: ' + _circle_r + 'px; height: ' + _circle_r + 'px; background-color: ' + color + '"></div>\n' +
        '                            <div class="circle4" style="width: ' + _circle_r + 'px; height: ' + _circle_r + 'px; background-color: ' + color + '"></div>\n' +
        '                        </div>\n' +
        '                    </div>\n';
    $panel.html(loadingStr);
}

function showPageNum($this, currentNum, totalNum) {
    var i = parseInt(currentNum) - 2;       // 最前面的页码
    var m = parseInt(currentNum) + 2;        // 最后面的页码
    // if ($this) {
    //     console.log("llllllllllllllllll");
    //     $this.parent().find('li').attr('class', '')
    // }
    $('.pagination').find('.page-num').attr('class', 'page-num');


    if (i <= 0) {
        i = 1;
        m = 5;
    }
    if (m >= parseInt(totalNum)) {
        m = parseInt(totalNum);
    }

    var pageLiStr = '';     // 页码html标签

    var x = 1;
    for (; i <= m; i++) {
        var li = $('.pagination li');
        $(li[x]).find('a').text(i);
        $(li[x]).show();
        if (i == parseInt(currentNum)) {
            $(li[x]).addClass('active');
        }
        x++;
        if (i == m) {
            for (x; x <= 5; x++) {
                $(li[x]).hide();
            }
        }
    }
}

/**
 * 获取当前时间
 * @param timestamp     时间戳
 * @returns {string}    YYYY-MM--DD HH:MM:SS
 */
function showDefaultTime(timestamp) {
    var myDate = new Date(timestamp);
    var year = myDate.getFullYear();
    var month = myDate.getMonth() + 1;
    var day = myDate.getDate();
    var h = myDate.getHours();
    var m = myDate.getMinutes();
    var s = myDate.getSeconds();
    if (month < 10) {
        month = '0' + month;
    }
    if (day < 10) {
        day = '0' + day;
    }
    if (h < 10) {
        h = '0' + h;
    }
    if (m < 10) {
        m = '0' + m;
    }
    if (s < 10) {
        s = '0' + s;
    }
    var time = year + '-' + month + '-' + day + ' ' + h + ':' + m + ':' + s;
    var t_time = year + '-' + month + '-' + day + ' ' + '00' + ':' + '00';

    return time;
}

//设置时间
function showTime(timeTemp) {
    var myDate = new Date(timeTemp);
    var year = myDate.getFullYear();
    var month = myDate.getMonth() + 1;
    var day = myDate.getDate();
    var h = myDate.getHours();
    var m = myDate.getMinutes();
    if (month < 10) {
        month = '0' + month;
    }
    if (day < 10) {
        day = '0' + day;
    }
    if (h < 10) {
        h = '0' + h;
    }
    if (m < 10) {
        m = '0' + m;
    }
    var time = year + '-' + month + '-' + day + 'T' + h + ':' + m;
    var t_time = year + '-' + month + '-' + day + 'T' + '00' + ':' + '00';

    return time;
}

/**
 * 高亮匹配
 * @param str
 * @returns {*}
 */
function hightLlightMatch(str, keywords) {
    var re = new RegExp($.trim(keywords), 'i');     // 匹配高亮
    var result = re.exec(str);
    return result ? str.replace(result[0], '<b style="color:red">' + result[0] + '</b>') : str;
}

/**
 * 数组去重
 * @param {*} arr 
 */
function dedArray(arr) {
    var result = [], i, j, len = arr.length;
    for (i = 0; i < len; i++) {
        for (j = i + 1; j < len; j++) {
            if (arr[i] === arr[j]) {
                j = ++i;
            }
        }
        result.push(arr[i]);
    }
    return result;
}
